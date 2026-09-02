"""La classe Budget : collection de Depense + persistance. SQUELETTE À COMPLÉTER."""

import json
from pathlib import Path

from modeles import Categorie, Depense

FICHIER = Path(__file__).parent / "depenses.json"


class Budget:
    """Un Budget A DES Depense (composition). Il gère leur sauvegarde."""

    def __init__(self, fichier: Path = FICHIER) -> None:
        self.fichier = fichier
        self._depenses: list[Depense] = []

    def __len__(self) -> int:
        return len(self._depenses)

    def ajouter(self, depense: Depense) -> None:
        self._depenses.append(depense)

    @property
    def total(self) -> float:
        """Somme des montants, recalculée à chaque lecture."""
        # TODO : renvoie sum(d.montant for d in self._depenses)
        return 0.0   # <- à compléter

    def par_categorie(self, categorie: str) -> list[Depense]:
        """Rend les dépenses d'une catégorie donnée."""
        # TODO : convertis `categorie` avec Categorie.depuis_texte(...) puis
        #        renvoie une compréhension [d for d in self._depenses if ...].
        return []   # <- à compléter

    def triees_par_montant(self) -> list[Depense]:
        """Du plus gros au plus petit montant."""
        # TODO : sorted(self._depenses, key=lambda d: d.montant, reverse=True)
        return list(self._depenses)   # <- à compléter

    def charger(self) -> None:
        """Lit le fichier JSON s'il existe (sinon ne fait rien)."""
        if not self.fichier.exists():
            return
        with self.fichier.open(encoding="utf-8") as f:
            self._depenses = [Depense.depuis_dict(d) for d in json.load(f)]

    def sauvegarder(self) -> None:
        """Écrit toutes les dépenses dans le fichier JSON."""
        with self.fichier.open("w", encoding="utf-8") as f:
            json.dump([d.en_dict() for d in self._depenses],
                      f, indent=2, ensure_ascii=False)
