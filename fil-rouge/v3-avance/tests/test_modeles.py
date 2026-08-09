"""Premiers tests du fil rouge (séance 6).

Lancer : uv run pytest -q   (ou simplement : pytest -q)
"""

import sys
from datetime import date, timedelta
from pathlib import Path

import pytest

# Permet d'importer le code de la v2 depuis ce dossier de tests.
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "v2-poo"))

from modeles import Opportunite, Statut  # noqa: E402


@pytest.fixture
def opportunite_urgente() -> Opportunite:
    """Décor de théâtre : un objet prêt à l'emploi, réutilisable par les tests."""
    return Opportunite(
        titre="Test",
        organisme="Org",
        pays="Maroc",
        deadline=date.today() + timedelta(days=3),
    )


def test_jours_restants():
    demain = date.today() + timedelta(days=1)
    opp = Opportunite("Test", "Org", "Maroc", demain)
    assert opp.jours_restants == 1  # assert : "j'affirme que". C'est tout.


def test_est_urgente(opportunite_urgente):
    assert opportunite_urgente.est_urgente is True


def test_non_urgente_si_deja_envoyee(opportunite_urgente):
    opportunite_urgente.marquer_envoyee()
    assert opportunite_urgente.est_urgente is False


@pytest.mark.parametrize(
    "jours, attendu",
    [
        (-1, False),  # déjà passée
        (0, True),  # aujourd'hui
        (6, True),  # limite haute
        (7, False),  # juste au-delà du seuil
        (30, False),
    ],
)
def test_seuil_urgence(jours, attendu):
    """Un seul test, cinq cas. On teste les BORNES (6 et 7), jamais des
    valeurs confortables : c'est là que vivent les bugs."""
    opp = Opportunite("T", "O", "P", date.today() + timedelta(days=jours))
    assert opp.est_urgente is attendu


def test_aller_retour_json():
    """Un objet transformé en dict puis reconstruit doit être identique.
    @dataclass fournit __eq__ gratuitement : la comparaison fonctionne."""
    original = Opportunite("Titre", "Org", "Maroc", date(2027, 1, 15), Statut.EN_COURS, ["ia"])
    reconstruit = Opportunite.depuis_dict(original.en_dict())
    assert reconstruit == original
