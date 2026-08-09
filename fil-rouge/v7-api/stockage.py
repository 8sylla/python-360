"""Dépôt de données de l'API (séance 10).

Volontairement simple : un fichier JSON. Le remplacer par SQLite via SQLModel
est le palier bonus de la séance.
"""

import json
from pathlib import Path

from schemas import OpportuniteCreation, OpportuniteLecture

FICHIER = Path("api_donnees.json")


class DepotOpportunites:
    """Accès aux données. Fourni aux routes par injection de dépendances,
    ce qui permet de le REMPLACER par un faux dans les tests."""

    def __init__(self, fichier: Path = FICHIER) -> None:
        self.fichier = fichier
        self._items: list[dict] = []
        self._charger()

    def _charger(self) -> None:
        if self.fichier.exists():
            with self.fichier.open(encoding="utf-8") as f:
                self._items = json.load(f)

    def _sauvegarder(self) -> None:
        with self.fichier.open("w", encoding="utf-8") as f:
            json.dump(self._items, f, indent=2, ensure_ascii=False, default=str)

    def toutes(self) -> list[OpportuniteLecture]:
        return [OpportuniteLecture(**item) for item in self._items]

    def par_id(self, opp_id: int) -> OpportuniteLecture | None:
        for item in self._items:
            if item["id"] == opp_id:
                return OpportuniteLecture(**item)
        return None

    def ajouter(self, donnees: OpportuniteCreation) -> OpportuniteLecture:
        nouvel_id = max((item["id"] for item in self._items), default=0) + 1
        # model_dump(mode="json") sérialise les dates en texte : ⚠ v2,
        # l'ancien .dict() n'existe plus.
        item = donnees.model_dump(mode="json") | {"id": nouvel_id}
        self._items.append(item)
        self._sauvegarder()
        return OpportuniteLecture(**item)

    def supprimer(self, opp_id: int) -> bool:
        avant = len(self._items)
        self._items = [item for item in self._items if item["id"] != opp_id]
        if len(self._items) < avant:
            self._sauvegarder()
            return True
        return False
