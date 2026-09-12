"""MATPLOTLIB — le cadre et la photo.

Une seule architecture à comprendre : la **Figure** est le cadre, l'**Axes**
est la photo à l'intérieur. Un cadre peut contenir plusieurs photos.

    python 03_matplotlib.py

Les images arrivent dans figures/.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

DATA = Path(__file__).resolve().parents[3] / "data"
FIGURES = Path(__file__).parent / "figures"
FIGURES.mkdir(exist_ok=True)

df = pd.read_csv(DATA / "releve_propre.csv", parse_dates=["date_operation"])
table = (
    df.groupby("categorie")["montant"]
    .sum()
    .sort_values(ascending=False)
    .reset_index(name="total")
)


# ═══════════════════════════════════════════════════════════════════════════
#  1. Figure et Axes
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 70)
print("  1. LE CADRE ET LA PHOTO")
print("=" * 70)

fig, ax = plt.subplots(figsize=(9, 5))
print(f"\nfig : {type(fig).__name__}   <- le cadre, la feuille entiere")
print(f"ax  : {type(ax).__name__}   <- la photo, la zone de trace")
print(f"fig contient {len(fig.axes)} Axes")

grille, axes = plt.subplots(2, 2, figsize=(8, 6))
print(f"\nplt.subplots(2, 2) -> {len(grille.axes)} Axes")
print(f"axes est un tableau de forme {axes.shape}")
print("   axes[0, 0] est en haut a gauche, axes[1, 1] en bas a droite.")
plt.close(grille)


# ═══════════════════════════════════════════════════════════════════════════
#  2. Les six lignes à connaître par cœur
# ═══════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  2. LE SQUELETTE — six lignes, et rien d'autre à retenir")
print("=" * 70)

ax.barh(table["categorie"], table["total"], color="#8B7B78")
ax.invert_yaxis()
ax.set_xlabel("Total dépensé sur six mois (€)")
ax.set_title("Dépenses par catégorie", loc="left", weight="bold")
fig.tight_layout()
fig.savefig(FIGURES / "01_squelette.png", dpi=150, bbox_inches="tight")
print("\n  fig, ax = plt.subplots(figsize=(9, 5))")
print("  ax.barh(x, y)")
print("  ax.set_xlabel(...)     <- PAS optionnel")
print("  ax.set_title(...)      <- PAS optionnel")
print("  fig.tight_layout()")
print("  fig.savefig(..., dpi=150, bbox_inches='tight')")
print("\n-> ecrit : figures/01_squelette.png")
print("   Un graphique sans titre d'axe ni unite n'est pas un graphique :")
print("   c'est une decoration.")
plt.close(fig)


# ═══════════════════════════════════════════════════════════════════════════
#  3. Pourquoi jamais plt.bar()
# ═══════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  3. ax.bar() plutôt que plt.bar()")
print("=" * 70)
print("""
  # L'interface d'ETAT : agit sur « le graphique courant »
  plt.bar(x, y)
  plt.title("...")        <- sur QUEL graphique ? Le dernier cree.

  # L'interface ORIENTEE OBJET : on dit sur quoi on dessine
  fig, ax = plt.subplots()
  ax.bar(x, y)
  ax.set_title("...")     <- sur celui-la, et pas un autre.

-> Les deux marchent avec UN graphique. Des qu'on en veut deux, la
   premiere devient impraticable. Autant prendre la bonne habitude
   tout de suite : c'est le meme nombre de caracteres.

-> Le piege de nommage : plt.title() devient ax.set_title(),
   plt.xlabel() devient ax.set_xlabel(). Le prefixe set_ apparait.
   C'est la seule chose a memoriser en passant d'une doc a l'autre.
""")


# ═══════════════════════════════════════════════════════════════════════════
#  4. L'axe qui mente — à voir de ses yeux
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 70)
print("  4. L'AXE QUI MENT")
print("=" * 70)

par_mois = df.groupby("mois")["montant"].sum()
fig, (gauche, droite) = plt.subplots(1, 2, figsize=(13, 4.5))

gauche.bar(par_mois.index, par_mois.values, color="#C1121F")
gauche.set_ylim(par_mois.min() * 0.98, par_mois.max() * 1.02)
gauche.set_title("Axe tronqué", loc="left", weight="bold")

droite.bar(par_mois.index, par_mois.values, color="#8B7B78")
droite.set_ylim(0, par_mois.max() * 1.05)
droite.set_title("Axe honnête", loc="left", weight="bold")

for ax_ in (gauche, droite):
    ax_.set_ylabel("Total du mois (€)")
    ax_.tick_params(axis="x", labelrotation=45)

fig.tight_layout()
fig.savefig(FIGURES / "02_axe_qui_mente.png", dpi=150, bbox_inches="tight")
plt.close(fig)

ecart = (par_mois.max() / par_mois.min() - 1) * 100
print(f"\nEcart REEL entre le mois le plus faible et le plus fort : {ecart:.0f} %")
print("-> ecrit : figures/02_axe_qui_mente.png")
print("   Ouvre l'image. A gauche, mai ressemble a un effondrement.")
print("   Meme jeu de donnees. Seul l'axe change.")
print("\n   REGLE 2 : l'axe des barres part de zero. Toujours.")
print("   (Une COURBE peut se permettre un axe tronque : elle montre une")
print("    variation, pas une quantite. Une barre, non : sa longueur EST")
print("    la quantite.)")


# ═══════════════════════════════════════════════════════════════════════════
#  5. Exporter
# ═══════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  5. EXPORTER — trois arguments qui changent tout")
print("=" * 70)

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(par_mois.index, par_mois.values, marker="o", color="#C1121F")
ax.set_ylim(0, par_mois.max() * 1.1)
ax.set_ylabel("Total du mois (€)")
ax.set_title("Juin est le mois le plus lourd", loc="left", weight="bold")
fig.tight_layout()

fig.savefig(FIGURES / "03_sans_soin.png")
fig.savefig(FIGURES / "03_avec_soin.png", dpi=150, bbox_inches="tight")
fig.savefig(FIGURES / "03_vectoriel.svg", bbox_inches="tight")
plt.close(fig)

tailles = {
    p.name: p.stat().st_size // 1024
    for p in sorted(FIGURES.glob("03_*"))
}
for nom, ko in tailles.items():
    print(f"  {nom:22} {ko:4} ko")

print("""
  dpi=150            net a l'impression et au videoprojecteur.
                     Par defaut c'est 100 : flou des qu'on agrandit.
  bbox_inches="tight"  supprime la marge blanche parasite autour.
  .svg               vectoriel : ne pixelise JAMAIS, quel que soit le
                     zoom. A preferer pour un rapport ou une slide.
                     Le PNG reste utile pour un mail ou une page web.
""")


# ═══════════════════════════════════════════════════════════════════════════
#  À TOI
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 70)
print("  À TOI")
print("=" * 70)
print("""
  Q1. Refais le graphique du squelette avec bar() au lieu de barh().
      Les noms de categories sont-ils lisibles ? Que fais-tu ?
  Q2. Ajoute la valeur en euros au bout de chaque barre (ax.text).
  Q3. Construis une figure 1x2 : les categories a gauche, l'evolution
      mensuelle a droite. Un seul fig.savefig a la fin.
  Q4. Mets un titre general a la figure entiere (cherche suptitle).
  Q5. Colore en rouge la seule categorie qui depasse 10 000 EUR, et en
      gris toutes les autres. (Indice : une liste de couleurs.)

Corrections : corrige/reprise/03_matplotlib.py
""")
