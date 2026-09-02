"""02 — La boîte à outils POO : @dataclass, StrEnum, @property.

Trois raccourcis qui font 90 % de la POO moderne en Python. On les applique
directement au domaine du fil rouge : la dépense.
"""

from dataclasses import dataclass, field
from enum import StrEnum


# ── On regarde ensemble : une énum de catégories ─────────────────────────
# StrEnum (3.11+) : chaque membre EST une chaîne. Fini les "Logment" qui
# cassent le filtrage en silence : une catégorie inconnue devient visible.
class Categorie(StrEnum):
    LOGEMENT = "Logement"
    TRANSPORT = "Transport"
    ALIMENTATION = "Alimentation"
    LOISIRS = "Loisirs"
    AUTRE = "Autre"


print("Categorie.LOGEMENT vaut :", Categorie.LOGEMENT)
print('Comparable à du texte  :', Categorie.LOGEMENT == "Logement")   # True


# ── On regarde ensemble : une dépense en dataclass ───────────────────────
@dataclass
class Depense:
    titre: str
    montant: float
    categorie: Categorie = Categorie.AUTRE
    tags: list[str] = field(default_factory=list)   # jamais = []

    @property
    def est_grosse(self):
        """Un attribut qui se CALCULE : depense.est_grosse (sans parenthèses)."""
        return self.montant >= 100


loyer = Depense("Loyer", 850, Categorie.LOGEMENT)
print(loyer)                       # __repr__ offert par @dataclass
print("est_grosse :", loyer.est_grosse)


# ── À toi de jouer ───────────────────────────────────────────────────────
# TODO 1 : crée une Depense "Café" de 2.50 en catégorie ALIMENTATION.
#          Affiche-la, puis affiche son est_grosse (doit être False).

# TODO 2 : ajoute à la dataclass Depense une @property `resume` qui rend une
#          phrase comme "Loyer — Logement — 850.00 EUR". Teste sur loyer.

# TODO 3 (le piège) : crée deux Depense sans préciser tags. Ajoute un tag à la
#          première (depense_a.tags.append("perso")) et vérifie que la seconde
#          a TOUJOURS une liste vide. C'est grâce à default_factory.
