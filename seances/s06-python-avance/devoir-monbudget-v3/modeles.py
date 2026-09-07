"""Modèles de MonBudget v3 — SQUELETTE À COMPLÉTER.

Reprend la Depense de la v2 et lui branche ses « prises ».
Fais les TODO dans l'ordre : chacun débloque une syntaxe Python.
"""

from dataclasses import asdict, dataclass, field
from enum import StrEnum
from functools import total_ordering

SEUIL_GROSSE_DEPENSE = 100.0


class Categorie(StrEnum):
    LOGEMENT = "Logement"
    TRANSPORT = "Transport"
    ALIMENTATION = "Alimentation"
    LOISIRS = "Loisirs"
    SANTE = "Santé"
    AUTRE = "Autre"

    @classmethod
    def depuis_texte(cls, texte: str) -> "Categorie":
        cible = texte.strip().casefold()
        for categorie in cls:
            if categorie.casefold() == cible:
                return categorie
        return cls.AUTRE


# TODO 5 : décommente la ligne ci-dessous UNE FOIS que __eq__ et __lt__
#          existent. (Avant, @total_ordering refuse de démarrer : il exige
#          au moins une opération d'ordre — l'erreur est explicite.)
# @total_ordering
@dataclass(eq=False)   # eq=False : c'est TOI qui écris __eq__
class Depense:
    titre: str
    montant: float
    categorie: Categorie = Categorie.AUTRE
    tags: list[str] = field(default_factory=list)

    # ── TODO 1 : __repr__ (pour le développeur) ──────────────────────────
    #   Doit rendre exactement :  Depense('Loyer', 850.0)
    #   Indice : les !r dans une f-string ajoutent les guillemets.
    #
    # def __repr__(self) -> str:
    #     return ...

    # ── TODO 2 : __str__ (pour l'utilisateur) ────────────────────────────
    #   Doit rendre :  Loyer — Logement — 850.00 EUR
    #
    # def __str__(self) -> str:
    #     return ...

    # ── TODO 3 : __eq__ puis __hash__ ────────────────────────────────────
    #   __eq__ : même titre, même montant, même catégorie (PAS les tags).
    #            Renvoie NotImplemented (jamais False) si `autre` n'est
    #            pas une Depense.
    #   __hash__ : OBLIGATOIRE dès qu'on écrit __eq__, sinon set() lève
    #            « TypeError: unhashable type ». Hache les MÊMES champs.
    #
    # def __eq__(self, autre: object) -> bool:
    #     ...
    #
    # def __hash__(self) -> int:
    #     return hash((...))

    # ── TODO 4 : __lt__ (comparer les MONTANTS) ──────────────────────────
    #   Débloque sorted(), min(), max() — et grâce à @total_ordering,
    #   les opérateurs <=, > et >=.
    #
    # def __lt__(self, autre: "Depense") -> bool:
    #     ...

    # ── Déjà fait (hérité de la v2) ──────────────────────────────────────

    @property
    def est_grosse(self) -> bool:
        return self.montant >= SEUIL_GROSSE_DEPENSE

    def en_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def depuis_dict(cls, donnees: dict) -> "Depense":
        return cls(
            titre=donnees["titre"],
            montant=float(donnees["montant"]),
            categorie=Categorie.depuis_texte(donnees.get("categorie", "")),
            tags=list(donnees.get("tags", [])),
        )
