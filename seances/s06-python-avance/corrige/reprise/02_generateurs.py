"""02 — CORRIGÉ. Générateurs, paresse et itertools."""

from itertools import islice


# TODO 1
def pairs(n):
    """Générateur des nombres pairs de 0 à n inclus."""
    for i in range(0, n + 1, 2):
        yield i


print("pairs(10) :", list(pairs(10)))


# TODO 2
def lignes_non_vides(lignes):
    """Générateur : saute les lignes vides ou faites d'espaces."""
    for ligne in lignes:
        if ligne.strip():
            yield ligne.strip()


brut = ["Loyer", "", "   ", "Courses", "\n", "Bus"]
print("lignes_non_vides :", list(lignes_non_vides(brut)))


# TODO 3
def grosses_depenses(depenses, seuil=100):
    for titre, montant in depenses:
        if montant >= seuil:
            yield titre


carnet = [
    ("Loyer", 850), ("Café", 2.5), ("Courses", 120),
    ("Bus", 1.9), ("Ordinateur", 900), ("Pharmacie", 150),
]
print("3 premières grosses :", list(islice(grosses_depenses(carnet), 3)))


# TODO 4 — le piège
flux = grosses_depenses(carnet)
print("\ncombien (1er comptage) :", sum(1 for _ in flux))
print("combien (2e comptage)  :", sum(1 for _ in flux), "<- 0 : le flux est épuisé")
print("la bonne façon         :", sum(1 for _ in grosses_depenses(carnet)))

# Rappel : sum(1 for _ in gen) CONSOMME le générateur. Si on a besoin du
# contenu ET du compte, on matérialise une fois : resultats = list(gen).
resultats = list(grosses_depenses(carnet))
print("matérialisé une fois   :", len(resultats), resultats)
