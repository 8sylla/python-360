"""00 — Échauffement séance 7 : prédis l'output AVANT d'exécuter.

Sept pièges. Écris ta prédiction, PUIS lance (F5 / ▶). Réponses tout en bas.
"""

import numpy as np
import pandas as pd

print("=== Échauffement séance 7 ===\n")

# ── Piège 1 : la différence qui justifie NumPy ───────────────────────────
liste = [1, 2, 3]
tableau = np.array([1, 2, 3])
print("Piège 1a — liste * 2   :", liste * 2)
print("Piège 1b — tableau * 2 :", tableau * 2)


# ── Piège 2 : un tableau NumPy ne mélange pas les genres ─────────────────
print("\nPiège 2a :", np.array([1, 2, 3.5]).dtype)
print("Piège 2b :", np.array([1, "deux", 3]).dtype)


# ── Piège 3 : le masque booléen ──────────────────────────────────────────
montants = np.array([10, 250, 40, 900])
print("\nPiège 3a — montants > 100  :", montants > 100)
print("Piège 3b — montants[masque]:", montants[montants > 100])


# ── Piège 4 : le « triangle vert d'Excel » ───────────────────────────────
# Une colonne de nombres... stockés en texte.
df = pd.DataFrame({"texte": ["10", "20"], "nombre": [10, 20]})
print("\nPiège 4a — somme de la colonne TEXTE  :", repr(df["texte"].sum()))
print("Piège 4b — somme de la colonne NOMBRE :", df["nombre"].sum())


# ── Piège 5 : dropna() sans subset ───────────────────────────────────────
d = pd.DataFrame({"montant": [10, 20, 30], "note": ["ok", None, None]})
print("\nPiège 5a — dropna() nu         :", len(d.dropna()), "lignes sur", len(d))
print("Piège 5b — dropna(subset=...)  :", len(d.dropna(subset=["montant"])), "lignes")


# ── Piège 6 : l'affectation chaînée (pandas 3.0) ─────────────────────────
budget = pd.DataFrame({"montant": [50.0, 200.0]})
budget[budget["montant"] > 100]["montant"] = 0        # a l'air correct...
print("\nPiège 6 — apres l'affectation :", budget["montant"].tolist())


# ── Piège 7 : NaN n'est égal à rien, pas même à lui-même ─────────────────
s = pd.Series([1, 2, np.nan])
print("\nPiège 7a — s.sum() :", s.sum(), "| s.count() :", s.count(), "| len(s) :", len(s))
print("Piège 7b — s == np.nan trouve :", int((s == np.nan).sum()), "ligne(s)")
print("Piège 7c — s.isna() trouve    :", int(s.isna().sum()), "ligne(s)")


# ═════════════════════════════════════════════════════════════════════════
#  RÉPONSES ATTENDUES
# ═════════════════════════════════════════════════════════════════════════
#  1a : [1, 2, 3, 1, 2, 3]  -> une LISTE se répète
#  1b : [2 4 6]             -> un TABLEAU se multiplie, élément par élément.
#       C'est toute la différence, et toute la raison d'être de NumPy.
#
#  2a : float64  -> l'entier est converti : un tableau est HOMOGÈNE.
#  2b : <U21     -> tout devient du texte. Une seule sorte dans la boîte.
#
#  3a : [False  True False  True]   -> un tableau de booléens : le « masque »
#  3b : [250 900]                   -> le masque sert de filtre
#
#  4a : '1020'  <- LA CATASTROPHE : le texte se CONCATÈNE au lieu de s'additionner.
#  4b : 30
#       C'est le « nombre stocké sous forme de texte » d'Excel. Réflexe :
#       df.info() AVANT tout calcul.
#
#  5a : 1 ligne sur 3   <- dropna() nu supprime toute ligne ayant UN trou,
#                          même dans une colonne facultative comme `note`.
#  5b : 3 lignes        <- avec subset, on ne jette que sur ce qui compte.
#
#  6 : [50.0, 200.0]  -> RIEN N'A CHANGÉ. pandas a émis un avertissement
#      (ChainedAssignmentError) et n'a rien fait. La bonne écriture :
#          budget.loc[budget["montant"] > 100, "montant"] = 0
#
#  7a : 3.0 | 2 | 3   -> sum() et count() IGNORENT les NaN, len() non.
#  7b : 0 ligne(s)    -> NaN n'est égal à rien, pas même à lui-même !
#  7c : 1 ligne(s)    -> il faut TOUJOURS .isna() / .notna()
