"""02 — CORRIGÉ. @dataclass, StrEnum, @property."""

from dataclasses import dataclass, field
from enum import StrEnum


class Categorie(StrEnum):
    LOGEMENT = "Logement"
    TRANSPORT = "Transport"
    ALIMENTATION = "Alimentation"
    LOISIRS = "Loisirs"
    AUTRE = "Autre"


@dataclass
class Depense:
    titre: str
    montant: float
    categorie: Categorie = Categorie.AUTRE
    tags: list[str] = field(default_factory=list)

    @property
    def est_grosse(self):
        return self.montant >= 100

    @property
    def resume(self):
        return f"{self.titre} — {self.categorie} — {self.montant:.2f} EUR"


loyer = Depense("Loyer", 850, Categorie.LOGEMENT)
print(loyer.resume)                       # Loyer — Logement — 850.00 EUR

# TODO 1
cafe = Depense("Café", 2.50, Categorie.ALIMENTATION)
print(cafe)
print("est_grosse :", cafe.est_grosse)    # False

# TODO 3 — le piège évité par default_factory
a = Depense("A", 10)
b = Depense("B", 20)
a.tags.append("perso")
print("tags a :", a.tags, "| tags b :", b.tags)   # ['perso'] | []
