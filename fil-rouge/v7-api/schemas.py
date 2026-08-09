"""Schémas Pydantic v2 : le contrat d'entrée et de sortie de l'API (séance 10).

⚠ FastAPI ne supporte plus Pydantic v1. Tout tutoriel montrant @validator,
    .dict() ou "class Config" est périmé.
"""

from datetime import date
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field, computed_field, field_validator


class Statut(StrEnum):
    A_FAIRE = "a_faire"
    EN_COURS = "en_cours"
    ENVOYEE = "envoyee"
    ARCHIVEE = "archivee"


class OpportuniteBase(BaseModel):
    """Champs communs à l'entrée et à la sortie."""

    # Field() ajoute des contraintes ET documente l'API automatiquement.
    titre: str = Field(min_length=3, max_length=200, examples=["Bourse Smarts-Up 2027"])
    organisme: str = Field(min_length=2, max_length=120)
    pays: str = Field(min_length=2, max_length=60)
    deadline: date
    statut: Statut = Statut.A_FAIRE
    tags: list[str] = Field(default_factory=list, max_length=10)

    @field_validator("pays")
    @classmethod
    def normaliser_pays(cls, valeur: str) -> str:
        """Normalise la casse à l'entrée.

        En v2 c'est @field_validator (et non @validator). Cette validation
        s'exécute AVANT que la donnée n'atteigne le code métier : le nettoyage
        de la séance 7 devient inutile pour tout ce qui passe par l'API.
        """
        return valeur.strip().title()

    @field_validator("deadline")
    @classmethod
    def deadline_pas_trop_ancienne(cls, valeur: date) -> date:
        if valeur.year < 2020:
            # Ce ValueError devient automatiquement une réponse HTTP 422
            # avec un message clair indiquant le champ concerné.
            raise ValueError("La deadline semble erronée (année < 2020)")
        return valeur


class OpportuniteCreation(OpportuniteBase):
    """Ce que le CLIENT envoie. Pas d'identifiant : c'est le serveur qui l'attribue."""


class OpportuniteLecture(OpportuniteBase):
    """Ce que le SERVEUR renvoie : identifiant + champs calculés."""

    # from_attributes autorise la construction depuis un objet Python et pas
    # seulement depuis un dictionnaire. En v1, cela s'appelait orm_mode.
    model_config = ConfigDict(from_attributes=True)

    id: int

    @computed_field
    @property
    def jours_restants(self) -> int:
        """Champ calculé, présent dans le JSON mais jamais stocké.
        C'est exactement la @property de la séance 5, exposée dans l'API."""
        return (self.deadline - date.today()).days

    @computed_field
    @property
    def urgente(self) -> bool:
        return 0 <= self.jours_restants < 7 and self.statut != Statut.ENVOYEE
