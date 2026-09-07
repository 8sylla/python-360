"""01 — CORRIGÉ. Les méthodes spéciales appliquées au fil rouge."""

from functools import total_ordering


@total_ordering
class Depense:
    """Une dépense : affichable, comparable, hachable."""

    def __init__(self, titre, montant):
        self.titre = titre
        self.montant = montant

    # TODO 1
    def __repr__(self):
        return f"Depense({self.titre!r}, {self.montant!r})"

    # TODO 2
    def __str__(self):
        return f"{self.titre} — {self.montant:.2f} EUR"

    # TODO 3
    def __eq__(self, autre):
        if not isinstance(autre, Depense):
            return NotImplemented
        return (self.titre, self.montant) == (autre.titre, autre.montant)

    def __hash__(self):
        return hash((self.titre, self.montant))

    # TODO 4
    def __lt__(self, autre):
        if not isinstance(autre, Depense):
            return NotImplemented
        return self.montant < autre.montant


# TODO 5
class Carnet:
    """Une collection de Depense qui se comporte comme une liste."""

    def __init__(self, depenses=None):
        self._depenses = list(depenses or [])

    def __repr__(self):
        return f"Carnet({self._depenses!r})"

    def __len__(self):
        return len(self._depenses)

    def __iter__(self):
        return iter(self._depenses)

    def __getitem__(self, index):
        return self._depenses[index]

    def __contains__(self, cible):
        """Par titre si on donne une chaîne, par objet sinon."""
        if isinstance(cible, str):
            return any(d.titre == cible for d in self._depenses)
        return cible in self._depenses


loyer = Depense("Loyer", 850.0)
cafe = Depense("Café", 2.5)

print("repr  :", repr(loyer))
print("str   :", loyer)
print("égal  :", loyer == Depense("Loyer", 850.0))
print("set   :", len({loyer, Depense("Loyer", 850.0)}))
print("tri   :", sorted([loyer, cafe]))
print("total_ordering :", loyer > cafe)

carnet = Carnet([loyer, cafe, Depense("Courses", 120.0)])
print("\nlen      :", len(carnet))
print("boucle   :", [str(d) for d in carnet])
print("index    :", carnet[0])
print("tranche  :", carnet[:2])
print("in titre :", "Loyer" in carnet)
print("somme    :", sum(d.montant for d in carnet))   # marche grâce à __iter__
print("max      :", max(carnet))                       # marche grâce à __lt__
