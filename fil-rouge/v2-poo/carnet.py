"""Collection d'opportunités et persistance (séance 5)."""

import json
from pathlib import Path

from modeles import Opportunite


class Carnet:
    """Gère une collection d'Opportunite et sa sauvegarde sur disque.

    COMPOSITION : un Carnet *a des* Opportunite. Il n'en hérite pas.
    """

    def __init__(self, fichier: Path = Path("donnees.json")) -> None:
        self.fichier = fichier
        self._opportunites: list[Opportunite] = []
        # Le _ signale "interne, passe par les méthodes". Convention, pas verrou.

    # ---------- Lecture ----------

    def __len__(self) -> int:
        """Permet d'écrire len(carnet). Première dunder method : on approfondit en S6."""
        return len(self._opportunites)

    def __iter__(self):
        """Permet d'écrire "for opp in carnet" (séance 6)."""
        return iter(self._opportunites)

    def toutes(self) -> list[Opportunite]:
        """Renvoie une COPIE : personne ne modifie la liste interne par accident."""
        return list(self._opportunites)

    def urgentes(self) -> list[Opportunite]:
        return [o for o in self._opportunites if o.est_urgente]

    def par_pays(self, pays: str) -> list[Opportunite]:
        # casefold() est la version robuste de lower() pour comparer
        # des textes internationaux.
        return [o for o in self._opportunites if o.pays.casefold() == pays.casefold()]

    def triees_par_urgence(self) -> list[Opportunite]:
        return sorted(self._opportunites, key=lambda o: o.deadline)

    # ---------- Écriture ----------

    def ajouter(self, opportunite: Opportunite) -> None:
        self._opportunites.append(opportunite)

    def supprimer(self, index: int) -> Opportunite:
        return self._opportunites.pop(index)

    # ---------- Persistance ----------

    def charger(self) -> None:
        if not self.fichier.exists():
            return
        with self.fichier.open(encoding="utf-8") as f:
            self._opportunites = [Opportunite.depuis_dict(d) for d in json.load(f)]

    def sauvegarder(self) -> None:
        with self.fichier.open("w", encoding="utf-8") as f:
            json.dump([o.en_dict() for o in self._opportunites], f, indent=2, ensure_ascii=False)
