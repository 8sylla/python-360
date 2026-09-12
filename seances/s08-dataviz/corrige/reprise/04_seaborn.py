"""CORRIGÉ — 04_seaborn.py

Les cinq questions. La Q3 est celle qui compte : elle apprend à dire non
à une dimension de trop.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

DATA = Path(__file__).resolve().parents[4] / "data"
FIGURES = Path(__file__).parent / "figures"
FIGURES.mkdir(exist_ok=True)

ACCENT, NEUTRE = "#C1121F", "#8B7B78"

df = pd.read_csv(DATA / "releve_propre.csv", parse_dates=["date_operation"])
sns.set_theme(style="whitegrid")


# ── Q1 ─────────────────────────────────────────────────────────────────────
print("Q1. Un boxplot par mois — que dit-il de plus que le lineplot ?")

fig, (haut, bas) = plt.subplots(2, 1, figsize=(11, 8))

par_mois = df.groupby("mois")["montant"].sum().reset_index(name="total")
sns.lineplot(data=par_mois, x="mois", y="total", marker="o", ax=haut,
             color=ACCENT, linewidth=2.5)
haut.set_ylim(0, par_mois["total"].max() * 1.1)
haut.set_title("Le lineplot : six points, six totaux", loc="left",
               weight="bold")
haut.set_ylabel("Total du mois (€)")
haut.set_xlabel("")

sns.boxplot(data=df, x="mois", y="montant", ax=bas, color=NEUTRE)
bas.set_title("Le boxplot : la FORME de chaque mois", loc="left",
              weight="bold")
bas.set_ylabel("Montant d'une dépense (€)")
bas.set_xlabel("")

fig.tight_layout()
fig.savefig(FIGURES / "q1_boxplot_vs_lineplot.png", dpi=150,
            bbox_inches="tight")
plt.close(fig)

medianes = df.groupby("mois")["montant"].median()
print(f"""    -> ecrit : figures/q1_boxplot_vs_lineplot.png

       Le lineplot dit COMBIEN. Le boxplot dit COMMENT.

       Les medianes mensuelles :
{medianes.round(2).to_string()}

       Un mois peut avoir un total eleve pour deux raisons opposees :
       beaucoup de petites depenses, ou quelques grosses. Le total ne
       les distingue pas. Le boxplot, si : la boite montre ou se
       concentrent les depenses, et les points isoles montrent les
       exceptions.

       C'est le meme enseignement que la mediane contre la moyenne :
       un chiffre resume, une forme explique.
""")


# ── Q2 ─────────────────────────────────────────────────────────────────────
print("Q2. errorbar=None puis errorbar=('ci', 95).")

fig, (sans, avec) = plt.subplots(1, 2, figsize=(14, 5), sharex=True)

sns.barplot(data=df, x="montant", y="categorie", ax=sans, color=NEUTRE,
            errorbar=None)
sans.set_title("errorbar=None — une certitude apparente", loc="left",
               weight="bold")
sans.set_xlabel("Montant moyen (€)")
sans.set_ylabel("")

sns.barplot(data=df, x="montant", y="categorie", ax=avec, color=NEUTRE,
            errorbar=("ci", 95))
avec.set_title("errorbar=('ci', 95) — l'incertitude est dite", loc="left",
               weight="bold")
avec.set_xlabel("Montant moyen (€)")
avec.set_ylabel("")

fig.tight_layout()
fig.savefig(FIGURES / "q2_errorbar.png", dpi=150, bbox_inches="tight")
plt.close(fig)

stats = df.groupby("categorie")["montant"].agg(["count", "mean", "std"])
print(f"""    -> ecrit : figures/q2_errorbar.png

{stats.round(2).to_string()}

       Les petits traits sont l'intervalle de confiance a 95 % de la
       MOYENNE. Ce qu'ils disent, en une phrase : « si je refaisais
       six mois de releve, la moyenne tomberait probablement dans
       cette fourchette ».

       Regarde « Autre » : un ecart-type de 199 pour une moyenne de
       141 — l'ecart-type est PLUS GRAND que la moyenne. Sa barre
       d'erreur est de loin la plus large. Le graphique AVOUE que
       cette moyenne ne veut pas dire grand-chose : « Autre » melange
       des depenses de 15 EUR et de 800 EUR.

       Sans errorbar, les six barres ont l'air egalement solides.
       C'est plus joli, et c'est moins honnete.
""")


# ── Q3 ─────────────────────────────────────────────────────────────────────
print("Q3. hue='moyen_paiement' sur le scatterplot — est-ce lisible ?")

avec_jour = df.assign(jour=df["date_operation"].dt.day)

fig, (a, b, c) = plt.subplots(1, 3, figsize=(18, 5))

sns.scatterplot(data=avec_jour, x="jour", y="montant", ax=a, alpha=0.6,
                color=ACCENT)
a.set_title("sans hue — 1 information", loc="left", weight="bold")

sns.scatterplot(data=avec_jour, x="jour", y="montant", hue="moyen_paiement",
                ax=b, alpha=0.7)
b.set_title(f"hue = moyen_paiement ({avec_jour['moyen_paiement'].nunique()} "
            "valeurs)", loc="left", weight="bold")

sns.scatterplot(data=avec_jour, x="jour", y="montant", hue="libelle",
                ax=c, alpha=0.7, legend=False)
c.set_title(f"hue = libelle ({avec_jour['libelle'].nunique()} valeurs) — "
            "illisible", loc="left", weight="bold")

fig.tight_layout()
fig.savefig(FIGURES / "q3_hue.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print(f"""    -> ecrit : figures/q3_hue.png

       moyen_paiement : {avec_jour['moyen_paiement'].nunique()} valeurs -> lisible.
       libelle        : {avec_jour['libelle'].nunique()} valeurs -> une bouillie de couleurs.

       La limite pratique est autour de SEPT couleurs. Au-dela, l'oeil
       ne fait plus la difference entre deux teintes voisines, et la
       legende devient plus grande que le graphique.

       Que faire quand il y a trop de categories ?
         - regrouper les petites dans « Autre » ;
         - garder les 5 principales et griser le reste ;
         - passer aux FACETTES : un petit graphique par categorie,
           au lieu d'une couleur par categorie. C'est la Q4.
""")


# ── Q4 ─────────────────────────────────────────────────────────────────────
print("Q4. Facetter par moyen de paiement avec catplot.")

grille = sns.catplot(
    data=df, x="montant", y="categorie", col="moyen_paiement",
    kind="box", height=4.5, aspect=0.95, color=NEUTRE,
)
grille.set_titles("{col_name}")
grille.set_axis_labels("Montant d'une dépense (€)", "")
grille.figure.suptitle(
    "Les trois moyens de paiement ont la même distribution : "
    "ici, cette variable n'explique rien",
    y=1.04, weight="bold",
)
grille.figure.savefig(FIGURES / "q4_facettes.png", dpi=150,
                      bbox_inches="tight")
plt.close(grille.figure)

croise = pd.crosstab(df["categorie"], df["moyen_paiement"])
print(f"""    -> ecrit : figures/q4_facettes.png

{croise.to_string()}

       catplot cree sa PROPRE figure : pas de ax=. Pour lui donner un
       titre general il faut passer par grille.figure.suptitle(), avec
       un y > 1 pour le placer au-dessus des panneaux.

       ET LE RESULTAT EST UN NON-RESULTAT. Regarde le tableau croise :
       le prelevement se retrouve dans les six categories, la carte
       aussi, le virement aussi. Les trois panneaux se ressemblent.

       C'est le moment le plus utile du corrige. Trois reactions
       possibles :

         - Mauvaise : jeter le graphique et n'en parler a personne.
         - Pire     : tronquer les axes jusqu'a ce qu'une difference
                      apparaisse.
         - Bonne    : garder le graphique, et ECRIRE le non-resultat
                      dans le titre.

       « Cette variable n'explique rien » est une information : elle
       dit a la personne qui lira apres toi de ne pas perdre son temps
       a refaire l'analyse. Un titre honnete peut dire qu'il n'y a
       rien a voir.
""")


# ── Q5 ─────────────────────────────────────────────────────────────────────
print("Q5. Réécrire un titre pour qu'il dise ce qu'on VOIT.")

totaux = (df.groupby("categorie")["montant"].sum()
            .sort_values(ascending=False).reset_index(name="total"))
part = totaux["total"].iloc[0] / totaux["total"].sum() * 100

fig, (avant, apres) = plt.subplots(1, 2, figsize=(15, 5))

sns.barplot(data=totaux, x="total", y="categorie", ax=avant, color=NEUTRE)
avant.set_title("comparer -> barplot", loc="left", weight="bold")
avant.set_xlabel("total")
avant.set_ylabel("categorie")

sns.barplot(data=totaux, x="total", y="categorie", ax=apres,
            color=NEUTRE, hue="categorie", legend=False,
            palette=[ACCENT] + [NEUTRE] * (len(totaux) - 1))
apres.set_title(f"Le logement absorbe {part:.0f} % du budget à lui seul",
                loc="left", weight="bold")
apres.set_xlabel("Total dépensé sur six mois (€)")
apres.set_ylabel("")

fig.tight_layout()
fig.savefig(FIGURES / "q5_titre.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("""    -> ecrit : figures/q5_titre.png

       AVANT : « comparer -> barplot »
         Decrit l'OUTIL. Le lecteur doit trouver l'information seul.
         Les axes s'appellent « total » et « categorie » : les noms
         des colonnes, pas des mots francais.

       APRES : « Le logement absorbe 61 % du budget a lui seul »
         Dit la CONCLUSION. Le lecteur sait quoi regarder, et la barre
         rouge le lui montre.

       La question a se poser, chaque fois : « qu'est-ce que ce
       graphique m'apprend, en une phrase ? ». La reponse EST le titre.

       Et si la reponse est « rien de notable » — alors ecris-le. Un
       titre honnete peut dire qu'il n'y a rien a voir.
""")
