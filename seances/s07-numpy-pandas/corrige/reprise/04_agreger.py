"""04 — CORRIGÉ. Agrégations."""

from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[4] / "data"
pd.set_option("display.float_format", lambda v: f"{v:,.2f}".replace(",", " "))

df = pd.read_csv(DATA / "releve_propre.csv", parse_dates=["date_operation"])

# TODO 1
print("TODO 1 — total par mois :")
print(df.groupby("mois")["montant"].sum().to_string(), "\n")

# TODO 2
print("TODO 2 — montant moyen par moyen de paiement :")
print(df.groupby("moyen_paiement")["montant"].mean().round(2).to_string(), "\n")

# TODO 3
print("TODO 3 — tableau croise moyen_paiement x categorie :")
print(df.pivot_table(index="moyen_paiement", columns="categorie",
                     values="montant", aggfunc="sum", fill_value=0), "\n")

# TODO 4
par_jour = df.groupby("jour_semaine")["montant"].sum().sort_values(ascending=False)
print("TODO 4 — total par jour de la semaine :")
print(par_jour.to_string())
print(f"-> on depense le plus le {par_jour.index[0]}\n")

# TODO 5 — filtrer D'ABORD, grouper ENSUITE
grosses = df[df["montant"] > 100]
print("TODO 5 — nombre de depenses > 100 EUR par categorie :")
print(grosses.groupby("categorie")["montant"].size().sort_values(ascending=False).to_string())
print("""
L'ordre compte : on filtre d'abord (moins de lignes a grouper), on groupe
ensuite. L'inverse donnerait un resultat faux ou beaucoup plus lent.
""")

# TODO 6 (bonus) — export Excel
# Necessite le paquet openpyxl :  pip install openpyxl
#
# croise = df.pivot_table(index="categorie", columns="mois",
#                         values="montant", aggfunc="sum", fill_value=0)
# croise.to_excel(DATA / "tableau_croise.xlsx")
#
# C'est le pont vers les collegues non techniciens : ils recoivent un
# fichier qu'ils savent ouvrir, produit par un code reproductible.
print("TODO 6 — voir le code commente (necessite openpyxl).")
