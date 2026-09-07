"""01 — Les méthodes spéciales : brancher son objet sur Python.

L'ANALOGIE : la **prise murale normalisée**. Python ne demande jamais
« quelle est ta longueur ? » — il cherche `__len__`. Ton objet n'a pas besoin
de connaître Python : il lui suffit d'avoir la bonne prise.

Chaque dunder que tu écris débloque une syntaxe native.
"""

from functools import total_ordering


# ══════════════════════════════════════════════════════════════════════
#  On regarde ensemble : une carte à jouer
# ══════════════════════════════════════════════════════════════════════
VALEURS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "V", "D", "R", "As"]


@total_ordering        # écrit <=, >, >= à partir de __eq__ et __lt__
class Carte:
    """Une carte à jouer, comparable et affichable."""

    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __repr__(self):
        """Pour le DÉVELOPPEUR (console, listes, débogueur)."""
        return f"Carte({self.valeur!r}, {self.couleur!r})"

    def __str__(self):
        """Pour l'UTILISATEUR (print)."""
        return f"{self.valeur} de {self.couleur}"

    def __eq__(self, autre):
        """Deux cartes sont égales si même valeur ET même couleur."""
        if not isinstance(autre, Carte):
            return NotImplemented       # jamais False : laisse l'autre répondre
        return (self.valeur, self.couleur) == (autre.valeur, autre.couleur)

    def __hash__(self):
        """OBLIGATOIRE dès qu'on écrit __eq__, sinon set() lève TypeError."""
        return hash((self.valeur, self.couleur))

    def __lt__(self, autre):
        """L'ordre d'une carte, c'est sa position dans VALEURS."""
        if not isinstance(autre, Carte):
            return NotImplemented
        return VALEURS.index(self.valeur) < VALEURS.index(autre.valeur)


as_pique = Carte("As", "pique")
sept_coeur = Carte("7", "coeur")

print("repr      :", repr(as_pique))
print("str       :", as_pique)
print("dans liste:", [as_pique])          # <- __repr__, pas __str__
print("égalité   :", as_pique == Carte("As", "pique"))
print("set       :", len({as_pique, Carte("As", "pique")}))   # 1 : dédoublonné
print("tri       :", sorted([as_pique, sept_coeur]))
print("max       :", max([as_pique, sept_coeur]))
print("total_ordering donne >= :", as_pique >= sept_coeur)


# ══════════════════════════════════════════════════════════════════════
#  On regarde ensemble : une COLLECTION qui se comporte comme une liste
# ══════════════════════════════════════════════════════════════════════
class Main:
    """Une main de cartes. Les 4 dunders qui la rendent « native »."""

    def __init__(self, cartes=None):
        self._cartes = list(cartes or [])

    def __repr__(self):
        return f"Main({self._cartes!r})"

    def __len__(self):
        """Débloque  len(main)."""
        return len(self._cartes)

    def __iter__(self):
        """Débloque  for c in main,  list(main),  sorted(main),  max(main)."""
        return iter(self._cartes)

    def __getitem__(self, index):
        """Débloque  main[0]  et la tranche  main[:2]."""
        return self._cartes[index]

    def __contains__(self, carte):
        """Débloque  carte in main."""
        return carte in self._cartes


main = Main([as_pique, sept_coeur, Carte("R", "trefle")])
print("\nlen        :", len(main))
print("boucle     :", [str(c) for c in main])
print("index      :", main[0])
print("tranche    :", main[:2])
print("in         :", sept_coeur in main)
print("triée      :", sorted(main))


# ══════════════════════════════════════════════════════════════════════
#  À toi de jouer
# ══════════════════════════════════════════════════════════════════════
# On repart du fil rouge : une dépense.

class Depense:
    """Une dépense du carnet."""

    def __init__(self, titre, montant):
        self.titre = titre
        self.montant = montant

    # TODO 1 : écris __repr__ pour obtenir  Depense('Loyer', 850.0)
    # TODO 2 : écris __str__ pour obtenir   Loyer — 850.00 EUR
    # TODO 3 : écris __eq__ (même titre ET même montant) + __hash__
    # TODO 4 : écris __lt__ (comparer les MONTANTS) et ajoute @total_ordering
    #          au-dessus de la classe, puis vérifie que sorted() marche.


loyer = Depense("Loyer", 850.0)
cafe = Depense("Café", 2.5)
print("\n--- à compléter ---")
print("repr :", repr(loyer))
print("str  :", loyer)
# print("tri  :", sorted([loyer, cafe]))     # décommente quand __lt__ existe


# TODO 5 : écris une classe Carnet qui contient des Depense et implémente
#          __len__, __iter__, __getitem__ et __contains__ (par titre).
#          Vérifie ensuite que  sum(d.montant for d in carnet)  fonctionne.
