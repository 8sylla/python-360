"""SEABORN — Matplotlib avec les statistiques incluses.

seaborn ne remplace pas Matplotlib : il écrit du Matplotlib pour toi. On
lui passe un `ax`, il dessine dedans, et on garde tous les réglages
Matplotlib qu'on connaît déjà.

    python 04_seaborn.py

Les images arrivent dans figures/.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

DATA = Path(__file__).resolve().parents[3] / "data"
FIGURES = Path(__file__).parent / "figures"
FIGURES.mkdir(exist_ok=True)

df = pd.read_csv(DATA / "releve_propre.csv", parse_dates=["date_operation"])
budget = pd.read_csv(DATA / "budget_prevu.csv", sep=";")

# Un theme lisible, en UNE ligne. C'est deja une raison d'utiliser seaborn.
sns.set_theme(style="whitegrid")


# ═══════════════════════════════════════════════════════════════════════════
#  1. Une ligne au lieu de quinze
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 70)
print("  1. LA MÊME CHOSE, EN UNE LIGNE")
print("=" * 70)
print("""
  # En Matplotlib : il faut agreger d'abord
  table = df.groupby("categorie")["montant"].mean().reset_index()
  fig, ax = plt.subplots()
  ax.bar(table["categorie"], table["montant"])
  ... puis calculer soi-meme les barres d'erreur.

  # En seaborn : l'agregation ET l'intervalle de confiance sont inclus
  sns.barplot(data=df, x="montant", y="categorie", ax=ax)
""")

fig, ax = plt.subplots(figsize=(9, 5))
sns.barplot(data=df, x="montant", y="categorie", ax=ax,
            color="#8B7B78", errorbar=("ci", 95))
ax.set_title("Dépense MOYENNE par catégorie, et son incertitude",
             loc="left", weight="bold")
ax.set_xlabel("Montant moyen d'une dépense (€)")
ax.set_ylabel("")
fig.tight_layout()
fig.savefig(FIGURES / "04_barplot.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("-> ecrit : figures/04_barplot.png")
print("""
   ATTENTION, piege : par defaut sns.barplot trace la MOYENNE, pas la
   somme. Les petits traits au bout des barres sont l'intervalle de
   confiance a 95 %. C'est une aide precieuse — et une source de
   malentendus si on croyait voir des totaux.

   Pour des totaux : agreger d'abord, puis ax.barh() en Matplotlib.
   C'est plus explicite, donc plus honnete.
""")


# ═══════════════════════════════════════════════════════════════════════════
#  2. Le catalogue — quelle question, quel graphique
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 70)
print("  2. LE CATALOGUE — cinq questions, cinq tracés")
print("=" * 70)

fig, axes = plt.subplots(2, 3, figsize=(17, 9))

# comparer -> des barres
totaux = (df.groupby("categorie")["montant"].sum()
            .sort_values(ascending=False).reset_index(name="total"))
sns.barplot(data=totaux, x="total", y="categorie", ax=axes[0, 0], color="#C1121F")
axes[0, 0].set_title("comparer -> barplot", loc="left", weight="bold")

# repartir -> un histogramme
sns.histplot(data=df, x="montant", bins=30, ax=axes[0, 1], color="#8B7B78")
axes[0, 1].set_title("répartir -> histplot", loc="left", weight="bold")

# comparer des distributions -> une boite a moustaches
sns.boxplot(data=df, x="montant", y="categorie", ax=axes[0, 2], color="#8B7B78")
axes[0, 2].set_title("comparer des formes -> boxplot", loc="left", weight="bold")

# correler -> un nuage de points
avec_jour = df.assign(jour=df["date_operation"].dt.day)
sns.scatterplot(data=avec_jour, x="jour", y="montant", ax=axes[1, 0],
                alpha=0.6, color="#C1121F")
axes[1, 0].set_title("corréler -> scatterplot", loc="left", weight="bold")

# evoluer -> une ligne
par_mois = df.groupby("mois")["montant"].sum().reset_index(name="total")
sns.lineplot(data=par_mois, x="mois", y="total", marker="o",
             ax=axes[1, 1], color="#C1121F")
axes[1, 1].set_ylim(0, par_mois["total"].max() * 1.1)
axes[1, 1].set_title("évoluer -> lineplot", loc="left", weight="bold")

# reperer -> une carte de chaleur
croise = df.pivot_table(index="categorie", columns="mois",
                        values="montant", aggfunc="sum", fill_value=0)
sns.heatmap(croise, ax=axes[1, 2], cmap="Reds", cbar=False)
axes[1, 2].set_title("repérer -> heatmap", loc="left", weight="bold")
axes[1, 2].tick_params(axis="y", rotation=0)
axes[1, 2].set_xlabel("")
axes[1, 2].set_ylabel("")

fig.tight_layout()
fig.savefig(FIGURES / "05_catalogue.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("""
-> ecrit : figures/05_catalogue.png   (LA figure a garder sous la main)

   comparer des quantites .... barplot   / ax.barh
   repartir une variable ..... histplot
   comparer des formes ....... boxplot
   correler deux variables ... scatterplot
   suivre dans le temps ...... lineplot
   reperer une anomalie ...... heatmap

   Ce qui n'est PAS dans la liste : le camembert. Au-dela de trois
   parts, l'oeil compare mal des angles. Et jamais en 3D.
""")


# ═══════════════════════════════════════════════════════════════════════════
#  3. hue : la troisième dimension
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 70)
print("  3. hue — une troisième variable, sans effort")
print("=" * 70)

reel = df.groupby(["categorie", "mois"])["montant"].sum().reset_index(name="reel")
bilan = (reel.merge(budget, on=["categorie", "mois"], how="left")
             .groupby("categorie")[["reel", "budget_prevu"]].sum()
             .reset_index())
long = bilan.melt(id_vars="categorie", var_name="type", value_name="montant")
long = long.replace({"reel": "Dépensé", "budget_prevu": "Prévu"})

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=long, x="montant", y="categorie", hue="type", ax=ax,
            palette={"Dépensé": "#C1121F", "Prévu": "#8B7B78"})
ax.set_title("Dépensé contre prévu — mais le logement écrase l'échelle",
             loc="left", weight="bold")
ax.set_xlabel("Sur six mois (€)")
ax.set_ylabel("")
fig.tight_layout()
fig.savefig(FIGURES / "06_hue.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("\n-> ecrit : figures/06_hue.png")
print("""
   `hue` a besoin de la forme LONGUE : une colonne qui dit de quel
   groupe il s'agit. C'est ce que fait melt() — l'inverse exact de
   pivot_table.

   Ouvre l'image : le graphique est EXACT, et il ne repond pas a la
   question. Le logement pese 36 000 EUR, la sante 3 000 : les cinq
   petites categories sont ecrasees, et le depassement des loisirs
   est invisible.

   -> La solution n'est pas cosmetique : on change ce qu'on ENCODE.
      Tracer l'ECART EN POURCENTAGE met toutes les categories sur la
      meme echelle. C'est le panneau 3 du tableau de bord (fichier 05).
""")


# ═══════════════════════════════════════════════════════════════════════════
#  4. Les facettes — un graphique par groupe, automatiquement
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 70)
print("  4. LES FACETTES — et pourquoi relplot ne prend pas d'ax")
print("=" * 70)

grille = sns.relplot(
    data=reel, x="mois", y="reel", col="categorie", col_wrap=3,
    kind="line", marker="o", height=2.8, aspect=1.3, color="#C1121F",
)
grille.set_titles("{col_name}")
grille.set_axis_labels("", "Total du mois (€)")
for ax_ in grille.axes.flat:
    ax_.tick_params(axis="x", labelrotation=45)
grille.figure.savefig(FIGURES / "07_facettes.png", dpi=150, bbox_inches="tight")
plt.close(grille.figure)

print("\n-> ecrit : figures/07_facettes.png")
print("""
   Six graphiques, une ligne de code. Chaque categorie a son panneau,
   et TOUS partagent la meme echelle : c'est ce qui rend la comparaison
   possible.

   Piege de vocabulaire : relplot, catplot et displot creent leur PROPRE
   figure — on ne peut pas leur passer ax=. Ce sont des fonctions
   « figure-level ». Les autres (barplot, histplot, lineplot...) sont
   « axes-level » et acceptent ax=.

   Retenir : si le nom finit par -plot tout court, ca prend un ax.
   S'il finit par -plot avec un prefixe (rel/cat/dis/lm), non.
""")


# ═══════════════════════════════════════════════════════════════════════════
#  5. seaborn.objects — une ouverture, pas le programme
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 70)
print("  5. seaborn.objects — la grammaire des graphiques")
print("=" * 70)

import seaborn.objects as so  # noqa: E402

figure = (
    so.Plot(totaux, x="total", y="categorie")
    .add(so.Bar(color="#C1121F"))
    .label(x="Total sur six mois (€)", y="",
           title="Le même graphique, écrit autrement")
    .layout(size=(9, 4.5))
    .plot()
)
figure.save(FIGURES / "08_objects.png", dpi=150, bbox_inches="tight")

print("\n-> ecrit : figures/08_objects.png")
print("""
   so.Plot(donnees, x=..., y=...).add(so.Bar()).label(...)

   On DECRIT le graphique par couches, au lieu d'appeler une fonction
   par type. C'est la meme idee que ggplot2 en R.

   Position a tenir : l'API classique reste le socle — c'est elle qui
   est partout dans la documentation et dans les reponses en ligne.
   `objects` est une ouverture : a connaitre, pas a apprendre ce soir.
""")


# ═══════════════════════════════════════════════════════════════════════════
#  À TOI
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 70)
print("  À TOI")
print("=" * 70)
print("""
  Q1. Trace un boxplot des montants par MOIS. Que raconte-t-il que
      le lineplot des totaux ne raconte pas ?
  Q2. Refais le barplot du 1 avec errorbar=None, puis avec
      errorbar=("ci", 95). Qu'est-ce qui apparait, et qu'est-ce que
      ces petits traits disent exactement ?
  Q3. Ajoute hue="moyen_paiement" au scatterplot. Est-ce lisible ?
      A partir de combien de categories un hue devient-il inutile ?
  Q4. Facette le catalogue par moyen de paiement avec catplot.
  Q5. Prends un graphique du catalogue et reecris son titre pour qu'il
      dise ce qu'on y VOIT, pas ce qu'on y trace.

Corrections : corrige/reprise/04_seaborn.py
""")
