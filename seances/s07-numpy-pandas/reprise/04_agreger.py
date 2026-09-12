"""04 — Agréger : sous-totaux et tableau croisé dynamique.

DEUX ANALOGIES :
  - `groupby`, c'est **trier un jeu de cartes en tas**, puis compter chaque
    tas. Excel appelle ça les « sous-totaux ».
  - `pivot_table`, c'est le **tableau croisé dynamique**. Le mot est
    littéralement le même.

Tout ce que MonBudget v3 faisait à la main, avec des boucles et un
defaultdict, tient ici en une ligne — et tourne aussi bien sur 400 lignes
que sur 400 000.
"""

from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[3] / "data"
pd.set_option("display.float_format", lambda v: f"{v:,.2f}".replace(",", " "))

# On repart du relevé DÉJÀ nettoyé (produit par fil-rouge/v4-donnees).
chemin = DATA / "releve_propre.csv"
if not chemin.exists():
    raise SystemExit(
        "releve_propre.csv est absent.\n"
        "Lance d'abord :  python fil-rouge/v4-donnees/nettoyage.py"
    )

df = pd.read_csv(chemin, parse_dates=["date_operation"])
print(f"{len(df)} depenses propres\n")


# ══════════════════════════════════════════════════════════════════════
#  1. groupby : découper, appliquer, combiner
# ══════════════════════════════════════════════════════════════════════
print("--- Total par categorie (le sous-total d'Excel) ---")
totaux = df.groupby("categorie")["montant"].sum().sort_values(ascending=False)
print(totaux, "\n")

print("En v3, c'etait une boucle + un defaultdict + un tri. Ici : une ligne.")


# ══════════════════════════════════════════════════════════════════════
#  2. .agg() : plusieurs statistiques d'un coup
# ══════════════════════════════════════════════════════════════════════
print("\n--- Plusieurs stats a la fois ---")
resume = (
    df.groupby("categorie")
    .agg(nombre=("montant", "size"),
         total=("montant", "sum"),
         moyenne=("montant", "mean"),
         maximum=("montant", "max"))
    .sort_values("total", ascending=False)
)
print(resume)
print("\nLa forme  nom=(\"colonne\", \"fonction\")  nomme les colonnes de sortie.")


# ══════════════════════════════════════════════════════════════════════
#  3. pivot_table : le tableau croisé dynamique
# ══════════════════════════════════════════════════════════════════════
print("\n\n--- Tableau croise : categories x mois ---")
croise = df.pivot_table(
    index="categorie", columns="mois", values="montant",
    aggfunc="sum", fill_value=0, margins=True, margins_name="Total",
)
print(croise)


# ══════════════════════════════════════════════════════════════════════
#  4. Les gestes utiles
# ══════════════════════════════════════════════════════════════════════
print("\n\n--- Gestes utiles ---")
print("Les 3 plus grosses depenses (nlargest) :")
print(df.nlargest(3, "montant")[["date_operation", "libelle", "montant"]].to_string(index=False))

print("\nPart de chaque categorie (%) :")
print((totaux / totaux.sum() * 100).round(1).to_string())


# ══════════════════════════════════════════════════════════════════════
#  5. Exporter — rendre le fichier au collègue
# ══════════════════════════════════════════════════════════════════════
sortie = DATA / "totaux_par_categorie.csv"
resume.to_csv(sortie, encoding="utf-8")
print(f"\nExporte vers {sortie.name}")


# ══════════════════════════════════════════════════════════════════════
#  À toi de jouer
# ══════════════════════════════════════════════════════════════════════
# TODO 1 : quel est le total dépensé par MOIS ? (groupby sur "mois")

# TODO 2 : quel est le montant MOYEN par moyen de paiement ?

# TODO 3 : construis un tableau croisé `moyen_paiement` x `categorie`.

# TODO 4 : quel jour de la semaine dépense-t-on le plus ?
#          (colonne `jour_semaine`, déjà calculée au nettoyage)

# TODO 5 : combien de dépenses dépassent 100 EUR dans chaque catégorie ?
#          Indice : filtre d'abord, groupe ensuite.

# TODO 6 (bonus) : exporte le tableau croisé en Excel avec .to_excel().
#          Ouvre-le : c'est le pont vers tes collègues non techniciens.
