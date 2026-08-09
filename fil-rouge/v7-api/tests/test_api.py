"""Tests de l'API (séances 10 et 11).

Lancer : uv run pytest -q
"""

import sys
from pathlib import Path

from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from main import app  # noqa: E402

client = TestClient(app)


def test_liste_repond_200():
    reponse = client.get("/opportunites")
    assert reponse.status_code == 200
    assert isinstance(reponse.json(), list)


def test_creation_refuse_un_titre_trop_court():
    """Ce test passe SANS qu'aucune ligne de validation n'ait été écrite dans
    les routes : c'est Pydantic qui travaille."""
    reponse = client.post(
        "/opportunites",
        json={
            "titre": "ab",  # min_length=3 -> doit être refusé
            "organisme": "Test",
            "pays": "Maroc",
            "deadline": "2027-01-01",
        },
    )
    assert reponse.status_code == 422  # 422 = corps invalide


def test_404_sur_identifiant_inexistant():
    assert client.get("/opportunites/999999").status_code == 404


def test_creation_puis_lecture():
    creation = client.post(
        "/opportunites",
        json={
            "titre": "Bourse de test",
            "organisme": "Organisme de test",
            "pays": "  maroc ",  # sera normalisé par le field_validator
            "deadline": "2027-06-30",
        },
    )
    assert creation.status_code == 201

    cree = creation.json()
    assert cree["pays"] == "Maroc"  # la normalisation a bien eu lieu
    assert "jours_restants" in cree  # le computed_field est présent

    lecture = client.get(f"/opportunites/{cree['id']}")
    assert lecture.status_code == 200
    assert lecture.json()["titre"] == "Bourse de test"

    # Nettoyage : on supprime ce qu'on a créé.
    assert client.delete(f"/opportunites/{cree['id']}").status_code == 204
