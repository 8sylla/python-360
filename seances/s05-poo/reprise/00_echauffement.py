"""00 — Échauffement POO : prédis l'output AVANT d'exécuter.

Lis chaque bloc, écris ta prédiction, PUIS lance (F5 / ▶). Les réponses
attendues sont en commentaire tout en bas.
"""

from dataclasses import dataclass, field

print("=== Échauffement séance 5 ===\n")


# ── Piège 1 : deux instances sont deux objets distincts ──────────────────
class Chien:
    def __init__(self, nom):
        self.nom = nom          # « self.nom » = « mon nom »


rex = Chien("Rex")
medor = Chien("Médor")
print("Piège 1 :", rex.nom, "/", medor.nom, "/", rex is medor)


# ── Piège 2 : l'affichage par défaut d'un objet ──────────────────────────
print("Piège 2 :", rex)          # à quoi ressemble un objet « nu » ?


# ── Piège 3 : une dataclass, elle, sait s'afficher ───────────────────────
@dataclass
class Point:
    x: int
    y: int


print("Piège 3 :", Point(2, 3))


# ── Piège 4 : LE piège de la liste par défaut partagée ───────────────────
@dataclass
class Panier:
    articles: list = field(default_factory=list)   # la BONNE façon


p1 = Panier()
p2 = Panier()
p1.articles.append("pain")
print("Piège 4 :", "p1 =", p1.articles, "| p2 =", p2.articles)
# Et si on avait écrit  articles: list = []  au lieu de default_factory ?
# (réponse en bas — c'est LE piège de la journée)


# ═════════════════════════════════════════════════════════════════════════
#  RÉPONSES ATTENDUES
# ═════════════════════════════════════════════════════════════════════════
#  Piège 1 : Rex / Médor / False — deux instances, deux objets séparés.
#  Piège 2 : quelque chose comme <__main__.Chien object at 0x...> : illisible.
#            (Une classe normale ne sait pas s'afficher toute seule.)
#  Piège 3 : Point(x=2, y=3) — @dataclass écrit __repr__ pour toi.
#  Piège 4 : p1 = ['pain'] | p2 = []  (grâce à default_factory).
#            Avec  articles: list = []  les DEUX paniers auraient partagé
#            LA MÊME liste : p2 aurait aussi contenu 'pain'. À ne jamais faire.
