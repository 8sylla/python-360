"""CORRIGÉ — 03_matplotlib.py

Les cinq questions. Les images arrivent dans figures/.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

DATA = Path(__file__).resolve().parents[4] / "data"
FIGURES = Path(__file__).parent / "figures"
FIGURES.mkdir(exist_ok=True)

ACCENT, NEUTRE = "#C1121F", "#8B7B78"

df = pd.read_csv(DATA / "releve_propre.csv", parse_dates=["date_operation"])
table = (
    df.groupby("categorie")["montant"].sum()
    .sort_values(ascending=False).reset_index(name="total")
)


# ── Q1 ─────────────────────────────────────────────────────────────────────
print("Q1. bar() au lieu de barh() : les noms sont-ils lisibles ?")

fig, (a, b) = plt.subplots(1, 2, figsize=(14, 5))

a.bar(table["categorie"], table["total"], color=NEUTRE)
a.set_title("bar() — les noms se chevauchent", loc="left", weight="bold")
a.set_ylabel("Total (€)")

b.bar(table["categorie"], table["total"], color=NEUTRE)
b.tick_params(axis="x", labelrotation=45)
for etiquette in b.get_xticklabels():
    etiquette.set_ha("right")  # sinon l'etiquette tournee est decalee
b.set_title("bar() + rotation 45° — lisible, mais penible", loc="left",
            weight="bold")
b.set_ylabel("Total (€)")

fig.tight_layout()
fig.savefig(FIGURES / "q1_bar_vs_barh.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("""    -> ecrit : figures/q1_bar_vs_barh.png

       Trois reponses possibles, par ordre de qualite :
         1. barh()          -> les noms se lisent horizontalement. LE choix.
         2. rotation 45     -> lisible, mais la tete penchee.
         3. abreger les noms -> on perd de l'information. Non.

       Regle pratique : des que les libelles sont des MOTS, on prend
       barh(). On garde bar() pour des dates ou des nombres.
""")


# ── Q2 ─────────────────────────────────────────────────────────────────────
print("Q2. La valeur au bout de chaque barre.")


def euros(x: float) -> str:
    return f"{x:,.0f} €".replace(",", " ")


fig, ax = plt.subplots(figsize=(9, 5))
ax.barh(table["categorie"], table["total"], color=NEUTRE)
ax.invert_yaxis()
marge = table["total"].max() * 0.02
for y, valeur in enumerate(table["total"]):
    ax.text(valeur + marge, y, euros(valeur), va="center", fontsize=9)
# Sans cette marge a droite, l'etiquette de la plus grande barre sort
# du cadre et disparait.
ax.set_xlim(0, table["total"].max() * 1.22)
ax.set_xlabel("Total dépensé sur six mois (€)")
ax.set_title("Le logement absorbe 61 % du budget", loc="left", weight="bold")
fig.tight_layout()
fig.savefig(FIGURES / "q2_etiquettes.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("""    -> ecrit : figures/q2_etiquettes.png

       Deux details qui font la difference :
         - le set_xlim() elargi, sinon la derniere etiquette est coupee ;
         - la marge devant le texte, sinon il colle a la barre.

       Une fois les valeurs ecrites, la grille verticale ne sert plus a
       rien : ax.grid(False) allege encore.
""")


# ── Q3 et Q4 ───────────────────────────────────────────────────────────────
print("Q3 + Q4. Une figure 1x2, avec un titre general.")

par_mois = df.groupby("mois")["montant"].sum()

fig, (gauche, droite) = plt.subplots(1, 2, figsize=(15, 5))

gauche.barh(table["categorie"], table["total"], color=NEUTRE)
gauche.invert_yaxis()
gauche.set_xlabel("Total sur six mois (€)")
gauche.set_title("Où part l'argent", loc="left", weight="bold")

droite.plot(par_mois.index, par_mois.values, marker="o", color=ACCENT,
            linewidth=2.5)
droite.set_ylim(0, par_mois.max() * 1.1)
droite.set_ylabel("Total du mois (€)")
droite.set_title("Quand on dépense", loc="left", weight="bold")

# Q4 : suptitle porte sur la FIGURE, pas sur un Axes.
fig.suptitle("MonBudget — six mois de relevé", fontsize=15, weight="bold")
# rect reserve la bande du haut au suptitle, sinon il chevauche les titres.
fig.tight_layout(rect=(0, 0, 1, 0.94))
fig.savefig(FIGURES / "q3_q4_figure_1x2.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("""    -> ecrit : figures/q3_q4_figure_1x2.png

       UN seul fig.savefig() a la fin : c'est tout l'interet de la
       Figure. Deux graphiques, une image, un fichier a envoyer.

       Le piege du suptitle : sans rect=(0, 0, 1, 0.94), tight_layout
       ignore le titre general et les titres de panneaux passent
       dessous.
""")


# ── Q5 ─────────────────────────────────────────────────────────────────────
print("Q5. Colorer la seule catégorie au-dessus de 10 000 €.")

SEUIL = 10_000
couleurs = [ACCENT if v > SEUIL else NEUTRE for v in table["total"]]
combien = sum(v > SEUIL for v in table["total"])

fig, ax = plt.subplots(figsize=(9, 5))
ax.barh(table["categorie"], table["total"], color=couleurs)
ax.invert_yaxis()
ax.axvline(SEUIL, color="#444", linestyle=":", linewidth=1.5)
# get_xaxis_transform() : x en unites de donnees, y en fraction de l'axe.
# C'est la bonne facon d'ancrer une etiquette en bas du cadre — sans lui,
# l'etiquette derive des qu'on change les donnees ou qu'on inverse l'axe.
ax.text(SEUIL, 0.02, f" seuil {euros(SEUIL)}", fontsize=9, color="#444",
        transform=ax.get_xaxis_transform())
ax.set_xlabel("Total sur six mois (€)")
ax.set_title(f"{combien} catégorie sur {len(table)} dépasse 10 000 €",
             loc="left", weight="bold")
fig.tight_layout()
fig.savefig(FIGURES / "q5_couleur_conditionnelle.png", dpi=150,
            bbox_inches="tight")
plt.close(fig)

print(f"""    -> ecrit : figures/q5_couleur_conditionnelle.png
       {combien} categorie depasse le seuil.

       Une liste en comprehension suffit :
           [ACCENT if v > SEUIL else NEUTRE for v in valeurs]

       C'est la meme idee qu'un masque booleen de la seance 7, mais le
       resultat est une liste de couleurs au lieu d'un filtre.

       Et le titre COMPTE les categories au lieu d'ecrire « 1 » en dur :
       il restera juste si les donnees changent.
""")
