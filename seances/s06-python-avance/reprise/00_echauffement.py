"""00 — Échauffement séance 6 : prédis l'output AVANT d'exécuter.

Six pièges, tous tirés de vraies erreurs de débutant sur les dunders, les
générateurs et les décorateurs. Écris ta prédiction, PUIS lance (F5 / ▶).
Réponses tout en bas.
"""

print("=== Échauffement séance 6 ===\n")


# ── Piège 1 : l'objet qui ne sait pas se présenter ───────────────────────
class Chien:
    def __init__(self, nom):
        self.nom = nom


rex = Chien("Rex")
print("Piège 1 :", rex)


# ── Piège 2 : __str__ seul ne suffit pas dans une liste ──────────────────
class Chat:
    def __init__(self, nom):
        self.nom = nom

    def __str__(self):
        return f"Chat({self.nom})"


felix = Chat("Félix")
print("Piège 2a :", felix)        # print appelle __str__
print("Piège 2b :", [felix])      # ... et dans une liste ?


# ── Piège 3 : le générateur qu'on parcourt deux fois ─────────────────────
def compter_jusqua(n):
    for i in range(1, n + 1):
        yield i


flux = compter_jusqua(3)
print("Piège 3a :", list(flux))
print("Piège 3b :", list(flux))


# ── Piège 4 : le décorateur qui oublie de rendre ─────────────────────────
def decorateur_bavard(fonction):
    def enveloppe(*args, **kwargs):
        print("  (j'appelle la fonction)")
        fonction(*args, **kwargs)      # oups : pas de return
    return enveloppe


@decorateur_bavard
def additionner(a, b):
    return a + b


print("Piège 4 :", additionner(2, 3))


# ── Piège 5 : le décorateur qui écrase l'identité ────────────────────────
@decorateur_bavard
def saluer(nom):
    """Dit bonjour."""
    return f"Bonjour {nom}"


print("Piège 5 :", saluer.__name__, "/ doc =", saluer.__doc__)


# ── Piège 6 : len() sur un générateur ────────────────────────────────────
# Décommente la ligne suivante et lis la dernière ligne de l'erreur.
# print("Piège 6 :", len(compter_jusqua(3)))


# ═════════════════════════════════════════════════════════════════════════
#  RÉPONSES ATTENDUES
# ═════════════════════════════════════════════════════════════════════════
#  1 : <__main__.Chien object at 0x...> — sans __repr__, l'objet est illisible.
#  2a : Chat(Félix)   2b : [<__main__.Chat object at 0x...>]
#       print() sur une LISTE appelle __repr__ de chaque élément, pas __str__.
#       Morale : si tu n'en écris qu'une, écris __repr__.
#  3a : [1, 2, 3]     3b : []  — un générateur ne se parcourt QU'UNE FOIS.
#  4 : None — l'enveloppe appelle la fonction mais ne rend pas son résultat.
#  5 : 'enveloppe' / doc = None — sans @functools.wraps, l'identité est perdue.
#  6 : TypeError: object of type 'generator' has no len()
#      Un générateur ne connaît pas sa longueur : il ne la découvre qu'en
#      se déroulant. Il faut sum(1 for _ in gen)... qui le consomme.
