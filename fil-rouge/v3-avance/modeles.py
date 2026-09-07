"""Modèles de MonBudget v3 — la Depense branche ses « prises ».

En v2, la dataclass écrivait tout pour nous. En v3, on reprend la main sur les
méthodes spéciales pour décider NOUS-MÊMES ce que veulent dire « afficher »,
« être égal » et « être plus petit ».
"""

from dataclasses import asdict, dataclass, field
from enum import StrEnum
from functools import total_ordering

SEUIL_GROSSE_DEPENSE = 100.0


class Categorie(StrEnum):
    """Les catégories de dépense (StrEnum : le membre EST une chaîne)."""

    LOGEMENT = "Logement"
    TRANSPORT = "Transport"
    ALIMENTATION = "Alimentation"
    LOISIRS = "Loisirs"
    SANTE = "Santé"
    AUTRE = "Autre"

    @classmethod
    def depuis_texte(cls, texte: str) -> "Categorie":
        """Convertit une saisie libre en catégorie ; AUTRE si inconnue."""
        cible = texte.strip().casefold()
        for categorie in cls:
            if categorie.casefold() == cible:
                return categorie
        return cls.AUTRE


# @total_ordering : on écrit UNE comparaison (__lt__) et Python en déduit
# <=, >, >=. Une méthode écrite, trois offertes.
@total_ordering
@dataclass(eq=False)   # eq=False : c'est NOUS qui disons ce que « pareil » veut dire
class Depense:
    """Une dépense : affichable, comparable, triable, hachable."""

    titre: str
    montant: float
    categorie: Categorie = Categorie.AUTRE
    tags: list[str] = field(default_factory=list)   # jamais = []

    # ══════════════════════════════════════════════════════════════════
    #  Afficher : deux publics, deux méthodes
    # ══════════════════════════════════════════════════════════════════

    def __repr__(self) -> str:
        """Pour le DÉVELOPPEUR (console, débogueur, listes)."""
        return f"Depense({self.titre!r}, {self.montant!r}, {self.categorie.value!r})"

    def __str__(self) -> str:
        """Pour l'UTILISATEUR : ce que voit print(depense)."""
        return f"{self.titre} — {self.categorie} — {self.montant:.2f} EUR"

    def __format__(self, spec: str) -> str:
        """Permet f"{depense:court}". Sans spec, on retombe sur __str__."""
        if spec == "court":
            return f"{self.titre[:12]:<12}{self.montant:>9.2f}"
        return str(self)

    # ══════════════════════════════════════════════════════════════════
    #  Comparer : égalité, tri, et le hachage qui va avec
    # ══════════════════════════════════════════════════════════════════

    def __eq__(self, autre: object) -> bool:
        """« La même dépense » = même titre, même montant, même catégorie.

        Les `tags` ne comptent pas : ce sont des annotations, pas l'identité.
        On rend NotImplemented (jamais False) face à un type inconnu, pour
        laisser l'autre objet donner sa réponse.
        """
        if not isinstance(autre, Depense):
            return NotImplemented
        return (self.titre, self.montant, self.categorie) == (
            autre.titre,
            autre.montant,
            autre.categorie,
        )

    def __hash__(self) -> int:
        """OBLIGATOIRE dès qu'on écrit __eq__.

        Écrire __eq__ met __hash__ à None : sans cette méthode,
        `set(depenses)` lèverait « TypeError: unhashable type ».
        On hache EXACTEMENT les champs comparés — et jamais un champ mutable
        (surtout pas `tags`, qui est une liste).
        """
        return hash((self.titre, self.montant, self.categorie))

    def __lt__(self, autre: "Depense") -> bool:
        """L'ordre naturel d'une dépense, c'est son MONTANT.

        Débloque d'un coup : sorted(), min(), max(), et grâce à
        @total_ordering les opérateurs <=, > et >=.
        """
        if not isinstance(autre, Depense):
            return NotImplemented
        return self.montant < autre.montant

    # ══════════════════════════════════════════════════════════════════
    #  Le reste, hérité de la v2
    # ══════════════════════════════════════════════════════════════════

    @property
    def est_grosse(self) -> bool:
        """Un attribut qui se calcule à chaque lecture."""
        return self.montant >= SEUIL_GROSSE_DEPENSE

    def en_dict(self) -> dict:
        """Version dictionnaire, prête pour le JSON."""
        return asdict(self)

    @classmethod
    def depuis_dict(cls, donnees: dict) -> "Depense":
        """Reconstruit une Depense depuis un dict JSON (tolère v1 et v2)."""
        return cls(
            titre=donnees["titre"],
            montant=float(donnees["montant"]),
            categorie=Categorie.depuis_texte(donnees.get("categorie", "")),
            tags=list(donnees.get("tags", [])),
        )
