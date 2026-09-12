"""01 — CORRIGÉ. NumPy."""

import numpy as np

scores = np.array([12, 7, 18, 3, 15, 9, 20, 11])

# TODO 1
print("moyenne :", scores.mean(), "| mediane :", np.median(scores),
      "| ecart-type :", scores.std().round(2))

# TODO 2 — un masque, puis on s'en sert comme filtre
au_dessus = scores[scores > scores.mean()]
print("au-dessus de la moyenne :", au_dessus)

# TODO 3 — & et non `and`, avec des parentheses
entre = (scores >= 10) & (scores <= 18)
print("entre 10 et 18 :", int(entre.sum()), "scores ->", scores[entre])

# TODO 4 — vectorise : aucune boucle
print("sur 100 :", (scores / 20 * 100).round(1))

# TODO 5 — broadcasting
ecarts = scores - scores.mean()
print("ecarts :", ecarts)
print("somme des ecarts :", ecarts.sum())
print("""
Pourquoi « presque » ? Avec ces valeurs-ci, la somme tombe pile sur 0.0.
Mais ce n'est pas garanti : les nombres a virgule sont stockes en binaire
avec une precision finie (0.1 + 0.2 != 0.3 en Python !). Selon les donnees,
on peut obtenir 1e-16 au lieu de 0.
Conclusion : on ne compare JAMAIS deux flottants avec == ; on utilise
np.isclose() (ou math.isclose).
""")
print("np.isclose(somme, 0) :", np.isclose(ecarts.sum(), 0))
