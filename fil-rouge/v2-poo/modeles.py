"""Modèle de données d'OpportuniTrack (séance 5)."""

from dataclasses import asdict, dataclass, field
from datetime import date
from enum import StrEnum


class Statut(StrEnum):
    """Statuts possibles d'une candidature.

    StrEnum (Python 3.11+) est la forme moderne : chaque membre EST une chaîne,
    donc la sérialisation JSON fonctionne sans conversion et
    Statut.A_FAIRE == "a_faire" est vrai.
    (L'ancienne écriture `class Statut(str, Enum)` reste valide mais est datée.)
    """

    A_FAIRE = "a_faire"
    EN_COURS = "en_cours"
    ENVOYEE = "envoyee"
    ARCHIVEE = "archivee"


@dataclass
class Opportunite:
    """Une opportunité repérée (bourse, stage, appel à candidature)."""

    titre: str
    organisme: str
    pays: str
    deadline: date
    statut: Statut = Statut.A_FAIRE
    tags: list[str] = field(default_factory=list)
    # ⚠ default_factory=list et NON default=[] : une liste par défaut serait
    # PARTAGÉE par toutes les instances. C'est le piège n°1 des dataclasses.

    @property
    def jours_restants(self) -> int:
        """Jours avant la deadline, calculés à la volée.

        Une @property se lit comme un attribut (sans parenthèses) mais se
        recalcule à chaque lecture : stocker ce nombre serait faux dès demain.
        """
        return (self.deadline - date.today()).days

    @property
    def est_urgente(self) -> bool:
        """Urgente = échéance dans moins de 7 jours et pas encore envoyée."""
        return 0 <= self.jours_restants < 7 and self.statut != Statut.ENVOYEE

    def marquer_envoyee(self) -> None:
        """Change le statut. La méthode DIT ce qu'elle fait ; le code appelant
        n'a pas à connaître le nom du champ interne."""
        self.statut = Statut.ENVOYEE

    def en_dict(self) -> dict:
        """Version dictionnaire, prête pour le JSON."""
        donnees = asdict(self)
        donnees["deadline"] = self.deadline.isoformat()
        return donnees

    @classmethod
    def depuis_dict(cls, donnees: dict) -> "Opportunite":
        """Reconstruit une Opportunite depuis un dictionnaire JSON.

        @classmethod : une méthode qui travaille sur la classe et non sur une
        instance. Usage typique : les constructeurs alternatifs. `cls` est à la
        classe ce que `self` est à l'instance.
        """
        donnees = dict(donnees)  # copie : on ne modifie pas l'entrée
        donnees["deadline"] = date.fromisoformat(donnees["deadline"])
        donnees["statut"] = Statut(donnees.get("statut", "a_faire"))
        return cls(**donnees)  # ** déplie le dict en arguments
