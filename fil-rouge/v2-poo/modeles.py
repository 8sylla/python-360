"""Modèles de données de MonBudget : une dépense et ses catégories.

C'est le cœur de la refactorisation de la séance 5 : le dictionnaire
{titre, categorie, montant} de la v1 devient un objet `Depense`, nommé, typé,
et porteur de ses propres méthodes.
"""

from dataclasses import asdict, dataclass, field
from enum import StrEnum

SEUIL_GROSSE_DEPENSE = 100.0  # au-delà, une dépense est signalée


class Categorie(StrEnum):
    """Les catégories de dépense, une bonne fois pour toutes.

    StrEnum (Python 3.11+) : chaque membre EST une chaîne de caractères.
    Deux conséquences directes :
      - il se sérialise seul en JSON (aucune conversion à écrire) ;
      - Categorie.LOGEMENT == "Logement" vaut True.
    C'est ce qui remplace le `categorie = "Logement"` fragile de la v1 :
    une faute de frappe devient une erreur repérable, pas un bug silencieux.
    """

    LOGEMENT = "Logement"
    TRANSPORT = "Transport"
    ALIMENTATION = "Alimentation"
    LOISIRS = "Loisirs"
    SANTE = "Santé"
    AUTRE = "Autre"

    @classmethod
    def depuis_texte(cls, texte: str) -> "Categorie":
        """Convertit une saisie clavier libre en catégorie ; AUTRE si inconnue.

        Remplace le `.title()` de la v1 : robuste (une faute -> AUTRE, jamais
        un plantage) et insensible à la casse (« logement » -> LOGEMENT).
        """
        cible = texte.strip().casefold()
        for categorie in cls:
            if categorie.casefold() == cible:
                return categorie
        return cls.AUTRE


@dataclass
class Depense:
    """Une dépense : ce que portait le dict de la v1, mais nommé et typé.

    Le décorateur @dataclass écrit tout seul __init__, __repr__ et __eq__ :
    six lignes ici remplacent une quinzaine à la main.
    """

    titre: str
    montant: float
    categorie: Categorie = Categorie.AUTRE
    tags: list[str] = field(default_factory=list)
    # ATTENTION : default_factory=list, JAMAIS tags: list = []. Une liste
    # écrite en valeur par défaut serait UNE SEULE liste, partagée par toutes
    # les dépenses. C'est le piège n°1 des dataclasses.

    @property
    def est_grosse(self) -> bool:
        """Vraie si le montant dépasse le seuil.

        Une @property se lit comme un attribut (depense.est_grosse, sans
        parenthèses) mais se recalcule à chaque lecture.
        """
        return self.montant >= SEUIL_GROSSE_DEPENSE

    def en_dict(self) -> dict:
        """Version dictionnaire, prête pour le JSON."""
        return asdict(self)  # le StrEnum devient "Logement" tout seul

    @classmethod
    def depuis_dict(cls, donnees: dict) -> "Depense":
        """Reconstruit une Depense depuis un dict JSON.

        @classmethod : une méthode qui travaille sur la classe (cls), pas sur
        une instance. Usage typique : un constructeur alternatif. Tolère les
        anciens fichiers de la v1 (sans clé "tags", catégorie en texte libre).
        """
        return cls(
            titre=donnees["titre"],
            montant=float(donnees["montant"]),
            categorie=Categorie.depuis_texte(donnees.get("categorie", "")),
            tags=list(donnees.get("tags", [])),
        )
