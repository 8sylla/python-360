"""Modèles de MonBudget : une dépense et ses catégories. SQUELETTE À COMPLÉTER."""

from dataclasses import asdict, dataclass, field
from enum import StrEnum

SEUIL_GROSSE_DEPENSE = 100.0


class Categorie(StrEnum):
    """Les catégories de dépense (StrEnum : chaque membre EST une chaîne)."""
    LOGEMENT = "Logement"
    TRANSPORT = "Transport"
    ALIMENTATION = "Alimentation"
    LOISIRS = "Loisirs"
    SANTE = "Santé"
    AUTRE = "Autre"

    @classmethod
    def depuis_texte(cls, texte: str) -> "Categorie":
        """Rend la catégorie correspondant au texte, ou AUTRE si inconnu."""
        # TODO : mets `texte` en minuscules (.strip().casefold()), parcours les
        #        membres (for categorie in cls) et compare categorie.casefold()
        #        au texte. Si rien ne colle -> return cls.AUTRE.
        return cls.AUTRE   # <- à compléter


@dataclass
class Depense:
    """Une dépense : titre, montant, catégorie, et des tags optionnels."""

    titre: str
    montant: float
    categorie: Categorie = Categorie.AUTRE
    # TODO : ajoute un champ  tags: list[str] = field(default_factory=list)
    #        ATTENTION : default_factory=list, JAMAIS = [] (liste partagée !).

    @property
    def est_grosse(self) -> bool:
        """Vraie si le montant dépasse le seuil (se lit sans parenthèses)."""
        # TODO : renvoie True si self.montant >= SEUIL_GROSSE_DEPENSE
        return False   # <- à compléter

    def en_dict(self) -> dict:
        """Version dictionnaire, prête pour le JSON."""
        return asdict(self)

    @classmethod
    def depuis_dict(cls, donnees: dict) -> "Depense":
        """Reconstruit une Depense depuis un dict JSON (tolère le format v1)."""
        return cls(
            titre=donnees["titre"],
            montant=float(donnees["montant"]),
            categorie=Categorie.depuis_texte(donnees.get("categorie", "")),
            # tags=list(donnees.get("tags", [])),   # <- décommente quand tags existe
        )
