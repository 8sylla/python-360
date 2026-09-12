"""02 — CORRIGÉ. Découverte de pandas."""

from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[4] / "data"
brut = pd.read_csv(DATA / "releve_brut.csv", sep=";", encoding="utf-8")

petit = pd.DataFrame({
    "titre": ["Loyer", "Cafe", "Netflix", "Essence"],
    "montant": [850.0, 2.5, 13.49, 68.0],
    "categorie": ["Logement", "Alimentation", "Loisirs", "Transport"],
})

# TODO 1
lignes, colonnes = brut.shape
print(f"{lignes} lignes, {colonnes} colonnes")

# TODO 2
print("\nmoyen_paiement :")
print(brut["moyen_paiement"].value_counts(dropna=False))
print("-> CB, carte, CARTE : TROIS ecritures pour le meme moyen de paiement.")

# TODO 3
masque = petit[(petit["montant"] > 10) & (petit["categorie"] != "Loisirs")]
print("\navec un masque :\n", masque)
print("\navec .query() :\n", petit.query("montant > 10 and categorie != 'Loisirs'"))

# TODO 4 — le piege
print("\n--- TODO 4 : pourquoi `and` ne marche pas ---")
try:
    petit[petit["montant"] > 10 and petit["montant"] < 100]
except ValueError as e:
    print("ValueError :", e)
print("""
`and` attend deux VALEURS vrai/faux, une de chaque cote. Or ici chaque cote
est une COLONNE de 4 booleens. Python ne sait pas si « une colonne » est
vraie ou fausse : il refuse.
`&` travaille element par element : il compare la ligne 1 avec la ligne 1,
la 2 avec la 2... C'est ce qu'on veut.
Et les parentheses sont obligatoires : `&` est prioritaire sur `>`.
""")

# TODO 5
avec_ttc = petit.assign(ttc=petit["montant"] * 1.2)
print(avec_ttc)
print("""
Pourquoi .assign() plutot que petit["ttc"] = ... ?
  1. il REND une nouvelle table -> on peut enchainer .assign().pipe().query()
  2. il ne modifie pas l'original : pas d'effet de bord surprise
  3. dans un .assign(), un lambda voit la table EN COURS de construction,
     ce qui permet de calculer une colonne a partir d'une autre creee juste avant.
""")
