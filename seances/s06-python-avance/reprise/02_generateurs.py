"""02 — Les générateurs : la paresse comme stratégie.

L'ANALOGIE : le **distributeur de tickets**. Une liste imprime les 10 millions
de tickets d'avance et remplit la pièce. Le générateur en imprime **un** quand
tu appuies sur le bouton.

Le mot-clé est `yield`. Un seul `yield` dans une fonction la transforme
ENTIÈREMENT en générateur : son corps ne s'exécute même pas à l'appel.
"""

import sys
from itertools import count, groupby, islice

# ══════════════════════════════════════════════════════════════════════
#  1. La preuve par la mémoire
# ══════════════════════════════════════════════════════════════════════
liste = [x * x for x in range(100_000)]          # tout est construit, tout de suite
generateur = (x * x for x in range(100_000))     # rien n'est construit

print("Mémoire d'une liste de 100 000 carrés :", sys.getsizeof(liste), "octets")
print("Mémoire du générateur équivalent      :", sys.getsizeof(generateur), "octets")
print("-> même contenu, ~", sys.getsizeof(liste) // sys.getsizeof(generateur),
      "fois moins de mémoire\n")


# ══════════════════════════════════════════════════════════════════════
#  2. Le corps ne tourne pas à l'appel
# ══════════════════════════════════════════════════════════════════════
def bavard():
    print("  (je démarre seulement maintenant)")
    yield 1
    print("  (je reprends où je m'étais arrêté)")
    yield 2


print("Création du générateur :")
gen = bavard()                 # rien ne s'affiche !
print("  ... rien ne s'est affiché.")
print("Premier next :", next(gen))
print("Second next  :", next(gen))
print()


# ══════════════════════════════════════════════════════════════════════
#  3. Le piège : un générateur ne se parcourt QU'UNE FOIS
# ══════════════════════════════════════════════════════════════════════
def grosses_depenses(depenses, seuil=100):
    """Générateur : livre les grosses dépenses une par une."""
    for titre, montant in depenses:
        if montant >= seuil:
            yield titre


carnet = [("Loyer", 850), ("Café", 2.5), ("Courses", 120), ("Bus", 1.9)]
flux = grosses_depenses(carnet)
print("1er parcours :", list(flux))
print("2e parcours  :", list(flux), "<- épuisé, c'est un FLUX pas un CONTENANT")
print("Solution     :", list(grosses_depenses(carnet)), "(on en recrée un)\n")


# ══════════════════════════════════════════════════════════════════════
#  4. Un flux INFINI, coupé par islice
# ══════════════════════════════════════════════════════════════════════
# count() compte à l'infini : impossible avec une liste, trivial en paresseux.
premiers_carres = (n * n for n in count(1))
print("Les 5 premiers carrés :", list(islice(premiers_carres, 5)))


# ══════════════════════════════════════════════════════════════════════
#  5. itertools.groupby — le trieur de courrier
# ══════════════════════════════════════════════════════════════════════
depenses = [
    ("Loyer", "Logement"),
    ("Courses", "Alimentation"),
    ("Cinéma", "Loisirs"),
    ("Boulangerie", "Alimentation"),
]

# PIÈGE : groupby ne regroupe que les éléments CONSÉCUTIFS.
print("\nSANS tri préalable :")
for cat, groupe in groupby(depenses, key=lambda d: d[1]):
    print("  ", cat, "->", [t for t, _ in groupe])

print("AVEC tri préalable (la bonne façon) :")
for cat, groupe in groupby(sorted(depenses, key=lambda d: d[1]), key=lambda d: d[1]):
    print("  ", cat, "->", [t for t, _ in groupe])


# ══════════════════════════════════════════════════════════════════════
#  À toi de jouer
# ══════════════════════════════════════════════════════════════════════
# TODO 1 : écris un générateur  pairs(n)  qui livre les nombres pairs de 0 à n.
#          Teste : list(pairs(10)) doit donner [0, 2, 4, 6, 8, 10].

# TODO 2 : écris un générateur  lignes_non_vides(lignes)  qui saute les lignes
#          vides d'une liste de chaînes (utilise `if ligne.strip():`).

# TODO 3 : avec islice, affiche seulement les 3 premières grosses dépenses
#          de `carnet` sans construire la liste complète.

# TODO 4 (piège) : que vaut  sum(1 for _ in grosses_depenses(carnet)) ?
#          Et si tu relances la même expression sur le MÊME générateur ?
