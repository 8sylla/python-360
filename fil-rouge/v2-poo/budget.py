"""La collection de dépenses et sa persistance : la classe Budget.

COMPOSITION : un Budget *a des* Depense (il n'en hérite pas). C'est la classe
qui absorbe l'ancien `stockage.py` de la v1 — charger/sauvegarder deviennent
des méthodes, plus des fonctions qui trimballent une liste.
"""

import json
from collections import defaultdict
from pathlib import Path

from modeles import Categorie, Depense

FICHIER = Path(__file__).parent / "depenses.json"


class Budget:
    """Gère une collection de Depense et sa sauvegarde sur disque."""

    def __init__(self, fichier: Path = FICHIER) -> None:
        self.fichier = fichier
        self._depenses: list[Depense] = []
        # Le _ devant _depenses signale : « interne, passe par les méthodes ».
        # C'est un panneau, pas un mur : Python n'a pas de vrai « private ».

    # ---------- Lecture ----------

    def __len__(self) -> int:
        """Permet d'écrire len(budget). Première méthode spéciale de la
        formation ; on approfondit les dunders en séance 6."""
        return len(self._depenses)

    @property
    def total(self) -> float:
        """Somme des montants, recalculée à chaque lecture (budget.total).

        C'est le total qu'affichait la v1 en bas du tableau — sauf qu'ici il
        ne peut jamais être périmé : le stocker dans un attribut le rendrait
        faux dès le prochain ajout.
        """
        return sum(d.montant for d in self._depenses)

    def toutes(self) -> list[Depense]:
        """Renvoie une COPIE : personne ne modifie la liste interne par erreur."""
        return list(self._depenses)

    def par_categorie(self, categorie: str) -> list[Depense]:
        """Remplace filtrer_par_categorie() de la v1, même résultat visible."""
        cible = Categorie.depuis_texte(categorie)
        return [d for d in self._depenses if d.categorie == cible]

    def triees_par_montant(self) -> list[Depense]:
        """Du plus gros au plus petit : l'ordre d'affichage de la v1."""
        return sorted(self._depenses, key=lambda d: d.montant, reverse=True)

    def total_par_categorie(self) -> dict[Categorie, float]:
        """Le total de chaque catégorie. Utile pour le tableau de bord (S8)."""
        totaux: dict[Categorie, float] = defaultdict(float)
        for d in self._depenses:
            totaux[d.categorie] += d.montant
        return dict(totaux)

    # ---------- Écriture ----------

    def ajouter(self, depense: Depense) -> None:
        self._depenses.append(depense)

    def supprimer(self, index: int) -> Depense:
        return self._depenses.pop(index)

    # ---------- Persistance (l'ancien stockage.py, devenu des méthodes) ----------

    def charger(self) -> None:
        """Lit le fichier JSON s'il existe ; sinon, ne fait rien."""
        if not self.fichier.exists():
            return
        with self.fichier.open(encoding="utf-8") as f:
            self._depenses = [Depense.depuis_dict(d) for d in json.load(f)]

    def sauvegarder(self) -> None:
        """Écrit toutes les dépenses dans le fichier JSON."""
        with self.fichier.open("w", encoding="utf-8") as f:
            json.dump(
                [d.en_dict() for d in self._depenses],
                f,
                indent=2,
                ensure_ascii=False,
            )
