"""02 — pandas : l'onglet Excel piloté par du code.

DEUX ANALOGIES :
  - une **Series**, c'est UNE COLONNE ; un **DataFrame**, c'est UN ONGLET.
  - `.loc`, c'est l'**adresse** (« rue des Loisirs ») ;
    `.iloc`, c'est la **place de parking n°3**.
"""

from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[3] / "data"

# ══════════════════════════════════════════════════════════════════════
#  1. LE PONT : ta liste de dictionnaires de la séance 3 EST un tableau
# ══════════════════════════════════════════════════════════════════════
budget_v3 = [
    {"titre": "Loyer", "montant": 850.0, "categorie": "Logement"},
    {"titre": "Courses", "montant": 54.2, "categorie": "Alimentation"},
    {"titre": "Netflix", "montant": 13.49, "categorie": "Loisirs"},
]
df = pd.DataFrame(budget_v3)      # une ligne, et c'est un tableau
print("--- Le pont S3 -> S7 ---")
print(df)
print("\nUne colonne = une Series :")
print(df["montant"], "\n")
print("type d'une colonne :", type(df["montant"]).__name__)


# ══════════════════════════════════════════════════════════════════════
#  2. read_csv : ne JAMAIS laisser pandas deviner
# ══════════════════════════════════════════════════════════════════════
# Le relevé de la banque est en point-virgule (export français).
# Sans sep=";", pandas lit UNE seule colonne géante.
brut = pd.read_csv(DATA / "releve_brut.csv", sep=";", encoding="utf-8")

print("\n\n--- Le rituel des 5 commandes (le check-up avant de conduire) ---")
print("1. shape   :", brut.shape, "(lignes, colonnes)")
print("\n2. head(3) :")
print(brut.head(3))
print("\n3. info() — LE plus important : regarde les dtypes")
brut.info()
print("\n4. describe() sur les colonnes numériques :")
print(brut.describe())
print("\n5. value_counts() — le détecteur de saleté :")
print(brut["categorie"].value_counts(dropna=False))


# ══════════════════════════════════════════════════════════════════════
#  3. Ce que value_counts vient de révéler
# ══════════════════════════════════════════════════════════════════════
print("\n--> Regarde bien : 'Logement', 'logement', 'LOGEMENT' et '  Logement '")
print("    sont QUATRE catégories différentes pour la machine.")
print("    Nombre de catégories distinctes :", brut["categorie"].nunique())
print("    Alors qu'il n'y en a que 5 en vrai. C'est ça, une donnée sale.")


# ══════════════════════════════════════════════════════════════════════
#  4. .loc (l'adresse) contre .iloc (la place de parking)
# ══════════════════════════════════════════════════════════════════════
print("\n\n--- .loc contre .iloc ---")
print("iloc[0, 1]  (ligne 0, colonne 1) :", brut.iloc[0, 1])
print("loc[0, 'libelle'] (par son nom)  :", brut.loc[0, "libelle"])
print("\niloc[0:3, 0:2] — par positions :")
print(brut.iloc[0:3, 0:2])


# ══════════════════════════════════════════════════════════════════════
#  5. Filtrer : & et |, JAMAIS and / or — et des parenthèses
# ══════════════════════════════════════════════════════════════════════
petit = pd.DataFrame({
    "titre": ["Loyer", "Cafe", "Netflix", "Essence"],
    "montant": [850.0, 2.5, 13.49, 68.0],
    "categorie": ["Logement", "Alimentation", "Loisirs", "Transport"],
})
print("\n\n--- Filtrer ---")
print("masque montant > 50 :\n", petit["montant"] > 50, "\n")
print("les grosses :\n", petit[petit["montant"] > 50], "\n")

# Deux conditions : chaque condition entre parenthèses !
deux = petit[(petit["montant"] > 10) & (petit["categorie"] != "Logement")]
print("montant > 10 ET pas Logement :\n", deux)

# .query() : le SEUL endroit où `and` est correct
print("\nla meme chose avec .query() :")
print(petit.query("montant > 10 and categorie != 'Logement'"))


# ══════════════════════════════════════════════════════════════════════
#  À toi de jouer
# ══════════════════════════════════════════════════════════════════════
# TODO 1 : combien de lignes et de colonnes fait `brut` ? Affiche-le en une
#          phrase du type "418 lignes, 6 colonnes".

# TODO 2 : affiche le value_counts() de la colonne `moyen_paiement`.
#          Combien de façons différentes d'écrire "CB" trouves-tu ?

# TODO 3 : dans `petit`, affiche les dépenses de plus de 10 EUR qui ne sont
#          PAS des Loisirs. Fais-le une fois avec un masque, une fois avec
#          .query().

# TODO 4 (piège) : essaie  petit[petit["montant"] > 10 and petit["montant"] < 100]
#          Lis l'erreur. Pourquoi `and` ne marche-t-il pas sur des colonnes ?

# TODO 5 : ajoute une colonne `ttc` (montant * 1.2) avec .assign(), puis
#          affiche le tableau. Pourquoi .assign() plutôt que petit["ttc"] = ... ?
