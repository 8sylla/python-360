"""03 — CORRIGÉ. La composition : un Budget qui a des Depense."""

from dataclasses import dataclass
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


class Budget:
    """Contient des Depense (composition) et sait les résumer."""

    def __init__(self):
        self._depenses = []

    def ajouter(self, depense):
        self._depenses.append(depense)

    def __len__(self):
        return len(self._depenses)

    @property
    def total(self):
        return sum(d.montant for d in self._depenses)

    def par_categorie(self, categorie):
        return [d for d in self._depenses if d.categorie == categorie]

    @property
    def la_plus_grosse(self):
        if not self._depenses:
            return None
        return max(self._depenses, key=lambda d: d.montant)


budget = Budget()
budget.ajouter(Depense("Loyer", 850, Categorie.LOGEMENT))
budget.ajouter(Depense("Courses", 54.20, Categorie.ALIMENTATION))
budget.ajouter(Depense("Cinéma", 12.00, Categorie.LOISIRS))

print("Total        :", budget.total)                       # 916.2
print("Nb dépenses  :", len(budget))                        # 3
print("Alimentation :", budget.par_categorie(Categorie.ALIMENTATION))
print("La plus grosse :", budget.la_plus_grosse.titre)      # Loyer
