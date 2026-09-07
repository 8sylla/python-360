"""MonBudget v3 — le Budget devient natif. SQUELETTE À COMPLÉTER."""

import json
from collections.abc import Iterator
from pathlib import Path

from decorateurs import journalise
from modeles import Categorie, Depense

FICHIER = Path(__file__).parent / "depenses.json"


class Budget:
    """Une collection de Depense, persistante."""

    def __init__(self, fichier: Path = FICHIER) -> None:
        self.fichier = fichier
        self._depenses: list[Depense] = []

    # ── Déjà fait ────────────────────────────────────────────────────────

    def __len__(self) -> int:
        return len(self._depenses)

    @property
    def total(self) -> float:
        return sum(d.montant for d in self._depenses)

    # ── TODO 1 : __repr__ ────────────────────────────────────────────────
    #   Doit rendre par ex. :  Budget(3 dépenses, 972.50 EUR)
    #
    # def __repr__(self) -> str:
    #     return ...

    # ── TODO 2 : __iter__ ────────────────────────────────────────────────
    #   Débloque  for d in budget,  list(budget),  sorted(budget),  max().
    #   Indice : return iter(self._depenses)
    #
    # def __iter__(self) -> Iterator[Depense]:
    #     ...

    # ── TODO 3 : __getitem__ ─────────────────────────────────────────────
    #   Débloque  budget[0]  ET la tranche  budget[:3].
    #   Indice : la liste interne gère déjà les deux — délègue-lui.
    #
    # def __getitem__(self, index):
    #     ...

    # ── TODO 4 : __contains__ ────────────────────────────────────────────
    #   Débloque  "Loyer" in budget  (comparaison par TITRE).
    #
    # def __contains__(self, cible) -> bool:
    #     ...

    # ── TODO 5 : le générateur grosses() ─────────────────────────────────
    #   Livre une par une les dépenses dont est_grosse est vrai.
    #   Utilise `yield`, PAS `return` d'une liste.
    #
    # def grosses(self) -> Iterator[Depense]:
    #     ...

    # ── TODO 6 : le gestionnaire de contexte ─────────────────────────────
    #   __enter__ : charge, puis RETOURNE self (sinon `as budget` = None).
    #   __exit__  : sauvegarde, puis renvoie False (ne masque pas l'erreur).
    #
    # def __enter__(self) -> "Budget":
    #     ...
    #
    # def __exit__(self, type_exc, valeur, trace) -> bool:
    #     ...

    # ── Écriture (journalisée) et persistance ────────────────────────────

    @journalise            # TODO 7 : rends ce décorateur réellement actif
    def ajouter(self, depense: Depense) -> None:
        self._depenses.append(depense)

    def par_categorie(self, categorie: str) -> list[Depense]:
        cible = Categorie.depuis_texte(categorie)
        return [d for d in self._depenses if d.categorie == cible]

    def charger(self) -> None:
        if not self.fichier.exists():
            return
        with self.fichier.open(encoding="utf-8") as f:
            self._depenses = [Depense.depuis_dict(d) for d in json.load(f)]

    def sauvegarder(self) -> None:
        with self.fichier.open("w", encoding="utf-8") as f:
            json.dump(
                [d.en_dict() for d in self._depenses],
                f, indent=2, ensure_ascii=False,
            )
