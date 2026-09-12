"""01 — NumPy : arrêter d'écrire la boucle.

L'ANALOGIE : une liste Python est un **sac de courses** — on y met n'importe
quoi, et c'est éparpillé en mémoire. Un tableau NumPy est une **boîte à
œufs** : une seule sorte de chose, dans des cases alignées et contiguës.

C'est cette régularité qui permet au processeur d'aller vite.
"""

import time

import numpy as np

# ══════════════════════════════════════════════════════════════════════
#  1. Un tableau est HOMOGÈNE (et c'est sa force)
# ══════════════════════════════════════════════════════════════════════
montants = np.array([12.50, 3.00, 40.00, 7.90])
print("tableau :", montants)
print("dtype   :", montants.dtype, "| shape :", montants.shape, "| taille :", montants.size)

# Mélanger les genres ? NumPy convertit tout pour rester homogène.
print("\nnp.array([1, 2, 3.5]).dtype   ->", np.array([1, 2, 3.5]).dtype)
print("np.array([1, 'deux']).dtype   ->", np.array([1, "deux"]).dtype, "(tout devient texte)")


# ══════════════════════════════════════════════════════════════════════
#  2. La vectorisation : on tire la poignée de recopie
# ══════════════════════════════════════════════════════════════════════
print("\n--- Vectorisation ---")
print("montants        :", montants)
print("montants * 1.2  :", montants * 1.2, "  <- TVA sur toute la colonne, sans boucle")
print("montants + 10   :", montants + 10)
print("montants.sum()  :", montants.sum(), "| .mean() :", montants.mean().round(2))
print("montants.std()  :", montants.std().round(2), "(écart-type)")


# ══════════════════════════════════════════════════════════════════════
#  3. La preuve par le chrono
# ══════════════════════════════════════════════════════════════════════
print("\n--- Le chrono, sur 1 000 000 de montants ---")
N = 1_000_000
liste = [float(i) for i in range(1, N + 1)]
tableau = np.arange(1, N + 1, dtype=np.float64)

debut = time.perf_counter()
ttc_boucle = []
for m in liste:                       # ce que tu écrivais jusqu'ici
    ttc_boucle.append(m * 1.2)
t_boucle = time.perf_counter() - debut

debut = time.perf_counter()
ttc_numpy = tableau * 1.2             # une seule ligne
t_numpy = time.perf_counter() - debut

print(f"  boucle for + append : {t_boucle*1000:7.1f} ms")
print(f"  NumPy  tableau*1.2  : {t_numpy*1000:7.1f} ms")
print(f"  -> {t_boucle/t_numpy:.0f} fois plus rapide, resultat identique :",
      np.allclose(ttc_boucle, ttc_numpy))


# ══════════════════════════════════════════════════════════════════════
#  4. Le broadcasting : l'étirement automatique
# ══════════════════════════════════════════════════════════════════════
# C'est la « référence absolue $B$1 » d'Excel, recopiée sur toute la plage.
print("\n--- Broadcasting ---")
print("montants - moyenne :", (montants - montants.mean()).round(2),
      " <- l'écart de chacun à la moyenne")

# Une matrice : 3 mois x 4 catégories
depenses = np.array([[100, 50, 30, 20],
                     [120, 45, 35, 25],
                     [ 90, 60, 25, 15]])
print("\nmatrice (3 mois x 4 categories) :\n", depenses)
print("total par mois (axis=1)      :", depenses.sum(axis=1))
print("total par categorie (axis=0) :", depenses.sum(axis=0))


# ══════════════════════════════════════════════════════════════════════
#  5. Le masque booléen : la rangée de cases cochées
# ══════════════════════════════════════════════════════════════════════
print("\n--- Masques ---")
grosses = montants > 10
print("montants > 10   :", grosses, " <- un tableau de VRAI/FAUX")
print("montants[masque]:", montants[grosses], " <- il sert de filtre")
print("combien ?       :", grosses.sum(), "(True vaut 1)")

# Combiner : & et | , JAMAIS and / or — et des parenthèses !
entre = (montants > 5) & (montants < 40)
print("entre 5 et 40   :", montants[entre])


# ══════════════════════════════════════════════════════════════════════
#  À toi de jouer
# ══════════════════════════════════════════════════════════════════════
scores = np.array([12, 7, 18, 3, 15, 9, 20, 11])

# TODO 1 : affiche la moyenne, la médiane (np.median) et l'écart-type.

# TODO 2 : affiche les scores STRICTEMENT supérieurs à la moyenne
#          (indice : un masque, puis on l'utilise comme filtre).

# TODO 3 : combien de scores sont entre 10 et 18 inclus ?
#          (indice : (a >= 10) & (a <= 18), puis .sum())

# TODO 4 : normalise les scores sur 20 -> sur 100, sans boucle.

# TODO 5 (broadcasting) : retire la moyenne à chaque score, puis vérifie
#          que la somme des écarts est (presque) nulle. Pourquoi « presque » ?
