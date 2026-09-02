"""03 — La composition : un Budget qui A DES Depense.

« est un » -> héritage.  « a un » -> composition. Un budget n'EST pas une
dépense : il EN CONTIENT. C'est le cas le plus courant, et le plus sûr.
Ce fichier est le brouillon du devoir : la classe Budget, en petit.
"""

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


# ── On regarde ensemble : une classe qui contient des objets ─────────────
class Budget:
    """Contient des Depense (composition) et sait les résumer."""

    def __init__(self):
        self._depenses = []            # _ = « interne, passe par les méthodes »

    def ajouter(self, depense):
        self._depenses.append(depense)

    @property
    def total(self):
        """Recalculé à chaque lecture : jamais périmé."""
        return sum(d.montant for d in self._depenses)


budget = Budget()
budget.ajouter(Depense("Loyer", 850, Categorie.LOGEMENT))
budget.ajouter(Depense("Courses", 54.20, Categorie.ALIMENTATION))
print("Total :", budget.total)         # 904.2


# ── À toi de jouer ───────────────────────────────────────────────────────
# TODO 1 : ajoute une méthode par_categorie(self, categorie) qui rend la liste
#          des dépenses de cette catégorie (une compréhension de liste).

# TODO 2 : ajoute une méthode __len__(self) qui rend le nombre de dépenses,
#          pour pouvoir écrire len(budget).

# TODO 3 : ajoute une @property la_plus_grosse qui rend la Depense au plus
#          gros montant (indice : max(..., key=lambda d: d.montant)).
#          Attention au cas où le budget est vide (rends None).
