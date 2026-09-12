"""AGRÉGER — découper, appliquer, combiner.

Le relevé nettoyé en séance 7 fait 333 lignes. Personne ne lit 333 lignes.
Le travail d'aujourd'hui est de les réduire à six chiffres qui parlent.

    python 01_agreger.py
"""

from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[3] / "data"

pd.set_option("display.width", 120)

df = pd.read_csv(DATA / "releve_propre.csv", parse_dates=["date_operation"])
print(f"Releve charge : {len(df)} depenses, {df['montant'].sum():.2f} EUR au total")


# ═══════════════════════════════════════════════════════════════════════════
#  1. Les trois temps
# ═══════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  1. DÉCOUPER, APPLIQUER, COMBINER")
print("=" * 70)

# DÉCOUPER : groupby ne calcule RIEN. Il prepare des paquets.
paquets = df.groupby("categorie")
print(f"\nObjet rendu par groupby : {type(paquets).__name__}")
print(f"Nombre de paquets       : {paquets.ngroups}")
print("Taille de chaque paquet :")
print(paquets.size().to_string())

# APPLIQUER + COMBINER : c'est l'agregation qui declenche le calcul.
totaux = df.groupby("categorie")["montant"].sum()
print("\nTotal par categorie (une Series, indexee par categorie) :")
print(totaux.sort_values(ascending=False).round(2).to_string())


# ═══════════════════════════════════════════════════════════════════════════
#  2. reset_index : de l'index à la colonne
# ═══════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  2. reset_index() — le geste que seaborn exige")
print("=" * 70)

print("\nSANS reset_index : la categorie est un INDEX")
print(f"  colonnes : {list(pd.DataFrame(totaux).columns)}")
print(f"  index    : {totaux.index.name}")

table = totaux.sort_values(ascending=False).reset_index(name="total")
print("\nAVEC reset_index : la categorie est une COLONNE")
print(f"  colonnes : {list(table.columns)}")
print(table.round(2).to_string(index=False))

print("\n-> seaborn dessine des colonnes. Sans reset_index, il ne trouve")
print("   pas 'categorie' et leve une erreur peu claire. Le reflexe :")
print("   toute agregation destinee a un graphique finit par reset_index().")


# ═══════════════════════════════════════════════════════════════════════════
#  3. Plusieurs calculs d'un coup
# ═══════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  3. .agg() — et des colonnes qui portent leur nom")
print("=" * 70)

resume = (
    df.groupby("categorie")
    .agg(
        nombre=("montant", "count"),
        total=("montant", "sum"),
        moyenne=("montant", "mean"),
        mediane=("montant", "median"),
        maximum=("montant", "max"),
    )
    .sort_values("total", ascending=False)
    .reset_index()
)
print()
print(resume.round(2).to_string(index=False))

print("\n-> Lis la ligne Transport et la ligne Logement a voix haute.")
print("   Transport : le poste le PLUS frequent, et le moins cher.")
print("   Logement  : le moins frequent, et de loin le plus lourd.")
print("   Une moyenne seule mentirait. Un count pose a cote dit la verite.")

# La forme a NE PAS apprendre, montree une fois pour savoir la reconnaitre.
ancienne = df.groupby("categorie")["montant"].agg(["count", "sum"])
print(f"\nL'ancienne forme rend des colonnes nommees {list(ancienne.columns)} :")
print("   illisible des qu'on agrege deux colonnes differentes. On ne")
print("   l'utilise pas, on sait juste la reconnaitre dans un vieux code.")


# ═══════════════════════════════════════════════════════════════════════════
#  4. Deux clés de regroupement
# ═══════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  4. Deux clés — et deux formes pour le même calcul")
print("=" * 70)

long = df.groupby(["categorie", "mois"])["montant"].sum().reset_index(name="total")
print(f"\nFORME LONGUE : {len(long)} lignes, 3 colonnes")
print(long.head(4).round(2).to_string(index=False))
print("   ... (36 lignes en tout)")

croise = df.pivot_table(
    index="categorie", columns="mois", values="montant", aggfunc="sum", fill_value=0
)
print(f"\nFORME CROISÉE : {croise.shape[0]} lignes x {croise.shape[1]} colonnes")
print(croise.round(0).to_string())

print("\n-> MÊMES chiffres. La forme longue part vers un autre calcul ou")
print("   vers seaborn ; la forme croisee part vers un humain ou vers une")
print("   heatmap. Choisir la forme, c'est choisir ce que le lecteur verra.")


# ═══════════════════════════════════════════════════════════════════════════
#  À TOI — cinq questions métier
# ═══════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  À TOI — cinq questions, cinq agrégations")
print("=" * 70)
print("""
Réponds à chacune par UNE expression pandas, et vérifie le résultat.

  Q1. Quel est le mois le plus lourd, et de combien ?
  Q2. Quelle categorie a la plus grosse depense unique ?
  Q3. Combien de depenses par moyen de paiement ?
  Q4. Quel jour de la semaine depense-t-on le plus (en total) ?
  Q5. Quelle est la part de chaque categorie, en pourcentage,
      arrondie a une decimale ?

Les corrections sont dans corrige/reprise/01_agreger.py — a ouvrir APRES
avoir essaye les cinq.
""")
