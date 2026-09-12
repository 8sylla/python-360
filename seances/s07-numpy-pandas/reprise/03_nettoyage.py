"""03 — Nettoyer : la trousse à outils.

LA RÈGLE DE pandas 3.0, à répéter à voix haute :
    « pandas rend une NOUVELLE table. Réaffecte. »

Excel rature ta feuille. pandas, lui, te rend un « Enregistrer sous » : chaque
opération produit une nouvelle table, l'originale n'est jamais touchée.
"""

from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[3] / "data"
brut = pd.read_csv(DATA / "releve_brut.csv", sep=";", encoding="utf-8")
print(f"Releve brut : {len(brut)} lignes\n")


# ══════════════════════════════════════════════════════════════════════
#  1. LES DEUX SEULES FAÇONS CORRECTES D'ÉCRIRE DANS UNE TABLE
# ══════════════════════════════════════════════════════════════════════
demo = pd.DataFrame({"montant": [50.0, 200.0], "grosse": [False, False]})

# FAUX — l'affectation chaînée : pandas avertit et ne fait RIEN.
demo[demo["montant"] > 100]["grosse"] = True
print("apres l'affectation chainee :", demo["grosse"].tolist(), " <- rien n'a change")

# CORRECT n°1 — .loc en une seule étape
demo.loc[demo["montant"] > 100, "grosse"] = True
print("apres .loc                  :", demo["grosse"].tolist())

# CORRECT n°2 — .assign(), qui rend une nouvelle table
demo = demo.assign(ttc=demo["montant"] * 1.2)
print("apres .assign               :", demo["ttc"].tolist())


# ══════════════════════════════════════════════════════════════════════
#  2. LES TEXTES — .str applique une méthode à TOUTE la colonne
# ══════════════════════════════════════════════════════════════════════
print("\n--- Textes ---")
print("avant :", brut["categorie"].nunique(), "categories distinctes (!)")
propre = brut.assign(
    categorie=brut["categorie"].fillna("").str.strip().str.title().replace("", "Autre"),
    libelle=brut["libelle"].str.strip().str.title(),
)
print("apres :", propre["categorie"].nunique(), "categories :",
      sorted(propre["categorie"].unique()))


# ══════════════════════════════════════════════════════════════════════
#  3. LES DATES — et LE piège de la séance
# ══════════════════════════════════════════════════════════════════════
print("\n--- Dates ---")
print("formats presents :", brut["date_operation"].dropna().unique()[:3].tolist())

# LA MÉTHODE QUI SEMBLE MARCHER... ET QUI CORROMPT LES DONNÉES
piege = pd.to_datetime(brut["date_operation"], format="mixed",
                       dayfirst=True, errors="coerce")
print(f"  avec format='mixed', dayfirst=True -> max = {piege.max().date()}")
print(f"  or le releve s'arrete en JUIN. {int((piege.dt.month > 6).sum())} dates sont FAUSSES.")
print("  Pourquoi ? dayfirst=True est applique AUSSI aux dates ISO :")
print("  '2026-04-09' (9 avril) est lu comme le 4 septembre. Sans erreur.")

# LA MÉTHODE SÛRE : normaliser les séparateurs, puis des formats EXPLICITES
texte = brut["date_operation"].str.strip().str.replace("/", "-", regex=False)
iso = pd.to_datetime(texte, format="%Y-%m-%d", errors="coerce")
fr = pd.to_datetime(texte, format="%d-%m-%Y", errors="coerce")
dates = iso.fillna(fr)
print(f"  methode sure -> max = {dates.max().date()}, "
      f"{int((dates.dt.month > 6).sum())} date fausse. Illisibles : {int(dates.isna().sum())}")
propre = propre.assign(date_operation=dates)


# ══════════════════════════════════════════════════════════════════════
#  4. LES MONTANTS — du texte vers des nombres
# ══════════════════════════════════════════════════════════════════════
print("\n--- Montants ---")
print("exemples bruts :", brut["montant"].dropna().unique()[:4].tolist())
nombres = pd.to_numeric(
    brut["montant"].str.strip()
    .str.replace("EUR", "", regex=False)
    .str.replace(" ", "", regex=False)
    .str.replace(",", ".", regex=False),
    errors="coerce",
)
print(f"  convertis : {nombres.notna().sum()} | illisibles -> NaN : {nombres.isna().sum()}")
print("  ATTENTION : errors='coerce' est un CHOIX, pas un reflexe.")
print("  On l'assume, donc ON COMPTE ce qu'il a mis a la poubelle.")
propre = propre.assign(montant=nombres)


# ══════════════════════════════════════════════════════════════════════
#  5. DOUBLONS ET LIGNES INEXPLOITABLES
# ══════════════════════════════════════════════════════════════════════
print("\n--- Doublons et trous ---")
avant = len(propre)
propre = propre.drop_duplicates()
print(f"  doublons supprimes : {avant - len(propre)}")
print("  (on nettoie les TEXTES AVANT de dedoublonner : sinon '  EDF ' et")
print("   'EDF' passent pour deux operations differentes)")

print(f"\n  dropna() NU garderait      : {len(propre.dropna())} lignes  <- catastrophe")
print(f"  dropna(subset=[...]) garde : {len(propre.dropna(subset=['date_operation','montant']))} lignes")
print("  Pourquoi ? La colonne `note` est vide 8 fois sur 10 : un dropna nu")
print("  jetterait 80 % du releve. On ne jette QUE sur ce qui rend la ligne")
print("  inutilisable.")
propre = propre.dropna(subset=["date_operation", "montant"])

print(f"\nBilan : {len(brut)} lignes brutes -> {len(propre)} lignes propres")


# ══════════════════════════════════════════════════════════════════════
#  À toi de jouer
# ══════════════════════════════════════════════════════════════════════
# TODO 1 : harmonise la colonne `moyen_paiement` (CB / carte / CARTE / VIR /
#          virement / prelevement) pour n'avoir plus que 3 valeurs propres.
#          Indice : .str.strip().str.upper() puis .replace({...}).

# TODO 2 : combien de montants sont NÉGATIFS ? Ce sont des remboursements :
#          sépare-les des dépenses en deux tables.

# TODO 3 : trouve les montants aberrants (> 5000 EUR) et affiche-les.
#          Combien y en a-t-il ?

# TODO 4 : ajoute une colonne `mois` au format "2026-03".
#          Indice : propre["date_operation"].dt.to_period("M").astype(str)

# TODO 5 (piège) : essaie  propre[propre["montant"] > 100]["categorie"] = "Grosse"
#          Que se passe-t-il ? Réécris-le correctement avec .loc.
