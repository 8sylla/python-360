"""LE TABLEAU DE BORD — cinq règles, et un titre à réécrire.

Le code de ce fichier est déjà correct. Ce n'est pas lui qu'on travaille :
c'est les TITRES. La partie « À toi » est le moment le plus important de la
séance, et il ne demande pas une ligne de Python.

    python 05_tableau_de_bord.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

DATA = Path(__file__).resolve().parents[3] / "data"
FIGURES = Path(__file__).parent / "figures"
FIGURES.mkdir(exist_ok=True)

ACCENT, NEUTRE, VERT = "#C1121F", "#8B7B78", "#2C8A1A"

df = pd.read_csv(DATA / "releve_propre.csv", parse_dates=["date_operation"])
budget = pd.read_csv(DATA / "budget_prevu.csv", sep=";")
sns.set_theme(style="whitegrid", font_scale=1.05)


def euros(x: float) -> str:
    return f"{x:,.0f} €".replace(",", " ")


# ═══════════════════════════════════════════════════════════════════════════
#  Les cinq règles
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 70)
print("  LES CINQ RÈGLES DE LA DATAVIZ HONNÊTE")
print("=" * 70)
print("""
  1. Le TITRE PORTE LE MESSAGE, pas la description.
     « Les loisirs depassent le budget de 30 % »
     et non « Depenses par categorie ».

  2. L'axe des BARRES part de ZERO. Toujours.
     Une courbe peut se permettre un axe tronque : elle montre une
     variation. Une barre, non : sa longueur EST la quantite.

  3. TRIER par valeur, pas par ordre alphabetique.
     Exception : ce qui a deja un ordre naturel (les mois).

  4. PAS DE CAMEMBERT au-dela de 3 parts. Jamais en 3D.
     L'oeil humain compare mal des angles, et tres mal des angles
     vus en perspective.

  5. UNE QUESTION, UN GRAPHIQUE.
     Si tu ne peux pas dire en une phrase ce que le graphique
     repond, il n'est pas pret.
""")


# ═══════════════════════════════════════════════════════════════════════════
#  Les quatre panneaux
# ═══════════════════════════════════════════════════════════════════════════
reel = df.groupby(["categorie", "mois"])["montant"].sum().reset_index(name="reel")
croise = reel.merge(budget, on=["categorie", "mois"], how="left")
assert len(croise) == len(reel), "explosion de lignes !"

bilan = (
    croise.groupby("categorie")[["reel", "budget_prevu"]].sum().reset_index()
)
bilan["ecart_pct"] = (bilan["reel"] / bilan["budget_prevu"] - 1) * 100

fig, axes = plt.subplots(2, 2, figsize=(16, 11))

# ── 1. Où part l'argent ?  ->  des barres ────────────────────────────────
table = (
    df.groupby("categorie")["montant"].sum()
    .sort_values(ascending=False).reset_index(name="total")
)
ax = axes[0, 0]
ax.barh(table["categorie"], table["total"],
        color=[ACCENT] + [NEUTRE] * (len(table) - 1))
ax.invert_yaxis()
part = table["total"].iloc[0] / table["total"].sum() * 100
ax.set_title(f"Le logement absorbe {part:.0f} % du budget à lui seul",
             loc="left", weight="bold")
ax.set_xlabel("Total dépensé sur six mois (€)")
ax.set_xlim(0, table["total"].max() * 1.22)
for y, v in enumerate(table["total"]):
    ax.text(v + table["total"].max() * 0.02, y, euros(v), va="center", fontsize=9)

# ── 2. Nombreuses et petites, ou rares et grosses ?  ->  histogramme ────
ax = axes[0, 1]
sns.histplot(data=df, x="montant", bins=30, ax=ax, color=NEUTRE)
ax.axvline(df["montant"].median(), color=ACCENT, linewidth=2,
           label=f"médiane {euros(df['montant'].median())}")
ax.axvline(df["montant"].mean(), color=ACCENT, linestyle="--", linewidth=2,
           label=f"moyenne {euros(df['montant'].mean())}")
sous = (df["montant"] < 150).mean() * 100
ax.set_title(f"{sous:.0f} % des dépenses sont sous 150 €,\n"
             "mais la moyenne est tirée par les loyers",
             loc="left", weight="bold")
ax.set_xlabel("Montant d'une dépense (€)")
ax.set_ylabel("Nombre de dépenses")
ax.legend()

# ── 3. Ai-je tenu mon budget ?  ->  l'écart en %  (la jointure) ─────────
ax = axes[1, 0]
tri = bilan.sort_values("ecart_pct")
ax.barh(tri["categorie"], tri["ecart_pct"],
        color=[ACCENT if e > 0 else VERT for e in tri["ecart_pct"]])
ax.axvline(0, color="#444", linewidth=1.2)
pire = tri.iloc[-1]
ax.set_title(f"Les {pire['categorie'].lower()} dépassent le budget "
             f"de {pire['ecart_pct']:.0f} %", loc="left", weight="bold")
ax.set_xlabel("Écart au budget prévu (%)   —   négatif = tenu")
limite = tri["ecart_pct"].abs().max() * 1.3
ax.set_xlim(-limite, limite)

# ── 4. Est-ce que ça dérape ?  ->  une ligne ────────────────────────────
ax = axes[1, 1]
par_mois = df.groupby("mois")["montant"].sum().reset_index(name="total")
prevu_mois = budget.groupby("mois")["budget_prevu"].sum().reset_index()
suivi = par_mois.merge(prevu_mois, on="mois", how="left")
ax.plot(suivi["mois"], suivi["total"], marker="o", color=ACCENT,
        linewidth=2.5, label="Dépensé")
ax.plot(suivi["mois"], suivi["budget_prevu"], marker="o", color=NEUTRE,
        linestyle="--", linewidth=2, label="Prévu")
depassements = int((suivi["total"] > suivi["budget_prevu"]).sum())
ax.set_title(f"{depassements} mois sur {len(suivi)} dépassent le budget prévu",
             loc="left", weight="bold")
ax.set_ylabel("Total du mois (€)")
ax.set_ylim(0, suivi[["total", "budget_prevu"]].to_numpy().max() * 1.15)
ax.legend()

total = f"{df['montant'].sum():,.0f}".replace(",", " ")
fig.suptitle(f"MonBudget — six mois, {len(df)} dépenses, {total} €",
             fontsize=17, weight="bold")
fig.tight_layout(rect=(0, 0, 1, 0.97))
fig.savefig(FIGURES / "09_tableau_de_bord.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("=" * 70)
print("  -> ecrit : figures/09_tableau_de_bord.png")
print("=" * 70)


# ═══════════════════════════════════════════════════════════════════════════
#  Pourquoi le panneau 3 trace un POURCENTAGE
# ═══════════════════════════════════════════════════════════════════════════
print("""
Le panneau 3 aurait pu tracer les deux montants cote a cote : depense
et prevu, en euros. C'est ce que fait figures/06_hue.png du fichier
precedent — et c'est illisible, parce que le logement pese 36 000 EUR
et la sante 3 000.

Les deux graphiques sont EXACTS. Un seul repond a la question.

-> Le choix de ce qu'on encode (des euros, ou un pourcentage) n'est pas
   cosmetique : il decide de ce que le lecteur pourra voir.
""")


# ═══════════════════════════════════════════════════════════════════════════
#  À TOI — l'exercice le plus important de la séance
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 70)
print("  À TOI")
print("=" * 70)
print("""
  Q1. LE TITRE. Voici quatre titres descriptifs :

        « Depenses par categorie »
        « Distribution des montants »
        « Reel contre prevu »
        « Evolution mensuelle »

      Pour chacun, regarde le panneau correspondant et reponds a la
      question : « qu'est-ce que ce graphique m'apprend, en UNE
      phrase ? ». Cette phrase EST le titre.

      Compare ensuite avec les titres du code ci-dessus.

  Q2. Les pourcentages des titres sont CALCULES : ils resteront justes
      si les donnees changent. Mais deux titres contiennent encore du
      texte ECRIT EN DUR qui pourrait devenir faux. Trouve-les, et
      rends au moins l'un des deux calcule.
      (Indice : regarde les NOMS, pas les nombres.)

  Q3. Ajoute un cinquieme panneau : la heatmap categorie x mois.
      Il faut passer en 2x3 ou en 3x2 — laquelle est la plus lisible
      sur un videoprojecteur 16/9 ?

  Q4. Fabrique une fonction `panneau_categories(df, ax)` a partir du
      panneau 1, puis appelle-la. Pourquoi passer `ax` en argument
      plutot que de creer la figure dans la fonction ?

  Q5. Exporte en SVG et en PNG. Ouvre les deux et zoome a 400 %.
      Lequel montres-tu a un client ?

Corrections : corrige/reprise/05_tableau_de_bord.py
""")
