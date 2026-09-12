"""03 — CORRIGÉ. Nettoyage."""

from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[4] / "data"
brut = pd.read_csv(DATA / "releve_brut.csv", sep=";", encoding="utf-8")

# On refait vite le nettoyage de base pour partir du bon pied.
texte = brut["date_operation"].str.strip().str.replace("/", "-", regex=False)
dates = (pd.to_datetime(texte, format="%Y-%m-%d", errors="coerce")
         .fillna(pd.to_datetime(texte, format="%d-%m-%Y", errors="coerce")))
montants = pd.to_numeric(
    brut["montant"].str.strip().str.replace("EUR", "", regex=False)
    .str.replace(" ", "", regex=False).str.replace(",", ".", regex=False),
    errors="coerce")

propre = brut.assign(date_operation=dates, montant=montants)

# TODO 1 — harmoniser le moyen de paiement
propre = propre.assign(
    moyen_paiement=propre["moyen_paiement"].str.strip().str.upper()
    .replace({"CARTE": "CB", "VIR": "VIREMENT"})
)
print("TODO 1 — moyens harmonises :", sorted(propre["moyen_paiement"].unique()))

# TODO 2 — separer les remboursements
propre = propre.dropna(subset=["date_operation", "montant"])
depenses = propre[propre["montant"] > 0]
remboursements = propre[propre["montant"] < 0]
print(f"\nTODO 2 — {len(depenses)} depenses, {len(remboursements)} remboursements")
print("Pourquoi separer ? Melanger un remboursement de -80 EUR avec les")
print("depenses fausserait tous les totaux : il les ferait BAISSER.")

# TODO 3 — les aberrants
aberrants = propre[propre["montant"].abs() > 5000]
print(f"\nTODO 3 — {len(aberrants)} montants aberrants :")
print(aberrants[["libelle", "montant"]].to_string(index=False))

# TODO 4 — la colonne mois
depenses = depenses.assign(
    mois=depenses["date_operation"].dt.to_period("M").astype(str)
)
print("\nTODO 4 — mois presents :", sorted(depenses["mois"].unique()))

# TODO 5 — le piege de l'affectation chainee
print("\nTODO 5 — le piege :")
essai = depenses.copy()
essai[essai["montant"] > 100]["categorie"] = "Grosse"     # ne fait RIEN
print("  apres l'affectation chainee, des 'Grosse' ? ",
      (essai["categorie"] == "Grosse").any())
essai.loc[essai["montant"] > 100, "categorie"] = "Grosse"  # correct
print("  apres .loc, des 'Grosse' ?                  ",
      (essai["categorie"] == "Grosse").any())
print("""
pandas a emis un ChainedAssignmentError et n'a rien fait : le filtre
`essai[...]` produit une COPIE, et on a modifie la copie, pas l'original.
La regle : « pandas rend une nouvelle table. Reaffecte. »
Deux ecritures correctes, et deux seulement :
    df.loc[masque, "colonne"] = valeur
    df = df.assign(colonne=...)
""")
