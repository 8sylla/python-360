"""MonBudget v3 — le Budget devient un objet Python à part entière.

En v2, il fallait `budget.toutes()` pour boucler. En v3, le Budget se comporte
comme une collection native : on l'itère, on le mesure, on l'indexe, on teste
l'appartenance — et il se sauvegarde tout seul en sortant d'un bloc `with`.
"""

import json
from collections import defaultdict
from collections.abc import Iterator
from contextlib import contextmanager
from itertools import groupby, islice
from pathlib import Path

from decorateurs import journalise
from modeles import Categorie, Depense

FICHIER = Path(__file__).parent / "depenses.json"


class Budget:
    """Une collection de Depense, persistante et « pythonique »."""

    def __init__(self, fichier: Path = FICHIER) -> None:
        self.fichier = fichier
        self._depenses: list[Depense] = []

    # ══════════════════════════════════════════════════════════════════
    #  Les prises normalisées : ce qui rend l'objet natif
    # ══════════════════════════════════════════════════════════════════

    def __repr__(self) -> str:
        """Pour le développeur."""
        return f"Budget({self.fichier.name!r}, {len(self)} dépenses, {self.total:.2f} EUR)"

    def __str__(self) -> str:
        """Pour l'utilisateur."""
        return f"{len(self)} dépenses pour {self.total:.2f} EUR"

    def __len__(self) -> int:
        """Débloque  len(budget)."""
        return len(self._depenses)

    def __iter__(self) -> Iterator[Depense]:
        """Débloque  for d in budget,  list(budget),  sorted(budget),  max(budget)."""
        return iter(self._depenses)

    def __getitem__(self, index):
        """Débloque  budget[0]  ET la tranche  budget[:3].

        Une liste sait déjà gérer un entier comme une tranche : on délègue.
        """
        return self._depenses[index]

    def __contains__(self, cible: object) -> bool:
        """Débloque  "Loyer" in budget  (par titre)  et  depense in budget."""
        if isinstance(cible, str):
            return any(d.titre == cible for d in self._depenses)
        return cible in self._depenses

    def __bool__(self) -> bool:
        """Un budget vide est « faux ». Sans __bool__, Python utiliserait
        __len__ — même résultat ici, mais le dire évite les surprises."""
        return len(self._depenses) > 0

    # ══════════════════════════════════════════════════════════════════
    #  Le gestionnaire de contexte : charger / sauvegarder tout seul
    # ══════════════════════════════════════════════════════════════════

    def __enter__(self) -> "Budget":
        self.charger()
        return self          # SANS ce return, `as budget` vaudrait None

    def __exit__(self, type_exc, valeur, trace) -> bool:
        self.sauvegarder()   # quoi qu'il arrive, on referme
        return False         # False = on ne masque pas l'exception

    # ══════════════════════════════════════════════════════════════════
    #  Les générateurs : la paresse
    # ══════════════════════════════════════════════════════════════════

    def grosses(self) -> Iterator[Depense]:
        """GÉNÉRATEUR : livre les grosses dépenses une par une.

        `yield` au lieu de `return` : rien n'est calculé tant qu'on ne boucle
        pas, et la liste complète n'est jamais construite en mémoire.
        PIÈGE : un générateur ne se parcourt QU'UNE FOIS.
        """
        for depense in self._depenses:
            if depense.est_grosse:
                yield depense

    def par_categorie(self, categorie: str) -> Iterator[Depense]:
        """Générateur des dépenses d'une catégorie (`yield from` = délégation)."""
        cible = Categorie.depuis_texte(categorie)
        yield from (d for d in self._depenses if d.categorie == cible)

    def top(self, n: int = 3) -> Iterator[Depense]:
        """Les n plus grosses. `islice` coupe un flux sans matérialiser la suite."""
        return islice(sorted(self, reverse=True), n)

    def groupes(self) -> Iterator[tuple[Categorie, list[Depense]]]:
        """Regroupe par catégorie avec itertools.groupby.

        PIÈGE : groupby ne regroupe que les éléments CONSÉCUTIFS — il faut
        trier d'abord sur la même clé, sinon on obtient plusieurs groupes
        pour une même catégorie. Et il faut list(groupe) tout de suite : le
        sous-itérateur meurt dès qu'on passe au groupe suivant.
        """
        def cle(depense: Depense) -> str:
            return depense.categorie

        for categorie, groupe in groupby(sorted(self._depenses, key=cle), key=cle):
            yield categorie, list(groupe)

    # ══════════════════════════════════════════════════════════════════
    #  Lecture
    # ══════════════════════════════════════════════════════════════════

    @property
    def total(self) -> float:
        """Somme des montants — `for d in self` marche grâce à __iter__."""
        return sum(d.montant for d in self)

    def total_par_categorie(self) -> dict[Categorie, float]:
        totaux: dict[Categorie, float] = defaultdict(float)
        for depense in self:
            totaux[depense.categorie] += depense.montant
        return dict(totaux)

    def doublons(self) -> list[Depense]:
        """Les dépenses saisies deux fois.

        Possible uniquement parce que Depense sait dire `==` (__eq__) ET se
        hacher (__hash__) : sans __hash__, ce `set` lèverait une TypeError.
        """
        vues: set[Depense] = set()
        repetees: list[Depense] = []
        for depense in self:
            if depense in vues:
                repetees.append(depense)
            else:
                vues.add(depense)
        return repetees

    # ══════════════════════════════════════════════════════════════════
    #  Écriture (journalisée par le décorateur) et persistance
    # ══════════════════════════════════════════════════════════════════

    @journalise
    def ajouter(self, depense: Depense) -> None:
        self._depenses.append(depense)

    @journalise
    def supprimer(self, index: int) -> Depense:
        return self._depenses.pop(index)

    def charger(self) -> None:
        if not self.fichier.exists():
            return
        with self.fichier.open(encoding="utf-8") as f:
            self._depenses = [Depense.depuis_dict(d) for d in json.load(f)]

    def sauvegarder(self) -> None:
        with self.fichier.open("w", encoding="utf-8") as f:
            json.dump([d.en_dict() for d in self], f, indent=2, ensure_ascii=False)


@contextmanager
def session(fichier: Path = FICHIER):
    """La version courte du même contexte : une fonction, un `yield` au milieu.

    Avant le `yield` = ce que ferait `__enter__`.
    Après (dans le `finally`) = ce que ferait `__exit__`.
    Le `finally` est OBLIGATOIRE : sans lui, une erreur dans le bloc `with`
    sauterait la sauvegarde — exactement ce qu'on voulait éviter.
    """
    budget = Budget(fichier)
    budget.charger()
    try:
        yield budget
    finally:
        budget.sauvegarder()
