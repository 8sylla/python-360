"""Tests du Budget : dunders, générateurs, gestionnaire de contexte."""

import pytest

import decorateurs
from budget import Budget, session
from modeles import Categorie, Depense


@pytest.fixture
def budget(tmp_path, monkeypatch):
    """Un budget rempli, isolé dans un dossier temporaire.

    `tmp_path` est fourni par pytest : on n'écrit JAMAIS dans le vrai
    depenses.json. On redirige aussi le journal du décorateur.
    """
    monkeypatch.setattr(decorateurs, "JOURNAL", tmp_path / "journal.log")
    carnet = Budget(tmp_path / "depenses.json")
    carnet.ajouter(Depense("Loyer", 850.0, Categorie.LOGEMENT))
    carnet.ajouter(Depense("Café", 2.5, Categorie.ALIMENTATION))
    carnet.ajouter(Depense("Courses", 120.0, Categorie.ALIMENTATION))
    return carnet


def test_budget_est_iterable(budget):
    assert [d.titre for d in budget] == ["Loyer", "Café", "Courses"]


def test_len_et_indexation(budget):
    assert len(budget) == 3
    assert budget[0].titre == "Loyer"
    assert len(budget[:2]) == 2          # __getitem__ gère aussi les tranches


def test_contains_par_titre(budget):
    assert "Loyer" in budget
    assert "Yacht" not in budget


def test_budget_vide_est_falsy(tmp_path):
    assert not Budget(tmp_path / "vide.json")


def test_total_utilise_iter(budget):
    assert budget.total == pytest.approx(972.5)


def test_tri_direct_sans_lambda(budget):
    assert max(budget).titre == "Loyer"   # marche grâce à __lt__


def test_grosses_est_un_generateur_et_s_epuise(budget):
    flux = budget.grosses()
    assert [d.titre for d in flux] == ["Loyer", "Courses"]
    assert list(flux) == []               # LE piège : un générateur ne sert qu'une fois


def test_top_n(budget):
    assert [d.titre for d in budget.top(2)] == ["Loyer", "Courses"]


def test_groupes_regroupe_bien_les_categories(budget):
    groupes = dict(budget.groupes())
    assert len(groupes[Categorie.ALIMENTATION]) == 2
    assert len(groupes[Categorie.LOGEMENT]) == 1


def test_doublons_detectes(budget):
    budget.ajouter(Depense("Loyer", 850.0, Categorie.LOGEMENT))
    assert [d.titre for d in budget.doublons()] == ["Loyer"]


def test_aller_retour_sur_disque(budget):
    budget.sauvegarder()
    relu = Budget(budget.fichier)
    relu.charger()
    assert len(relu) == 3
    assert relu[0] == budget[0]


def test_le_contexte_sauvegarde_meme_en_cas_d_erreur(tmp_path, monkeypatch):
    monkeypatch.setattr(decorateurs, "JOURNAL", tmp_path / "journal.log")
    chemin = tmp_path / "depenses.json"

    with pytest.raises(ValueError):
        with session(chemin) as carnet:
            carnet.ajouter(Depense("Loyer", 850.0))
            raise ValueError("boum")

    assert chemin.exists()                # sauvegardé quand même, grâce au finally
