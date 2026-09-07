"""Tests des décorateurs — surtout : la preuve que @wraps sert à quelque chose."""

import decorateurs
from decorateurs import chronometre, journalise


def test_wraps_preserve_le_nom_et_la_doc():
    @chronometre
    def additionner(a, b):
        """Additionne deux nombres."""
        return a + b

    assert additionner.__name__ == "additionner"     # sans @wraps : 'enveloppe'
    assert additionner.__doc__ == "Additionne deux nombres."


def test_la_fonction_decoree_rend_toujours_son_resultat():
    @chronometre
    def additionner(a, b):
        return a + b

    assert additionner(2, 3) == 5      # sans `return resultat` : None


def test_le_decorateur_transmet_args_et_kwargs():
    @chronometre
    def concatener(a, b="monde"):
        return f"{a} {b}"

    assert concatener("bonjour") == "bonjour monde"
    assert concatener("bonjour", b="Awa") == "bonjour Awa"


def test_journalise_ecrit_une_ligne(tmp_path, monkeypatch):
    monkeypatch.setattr(decorateurs, "JOURNAL", tmp_path / "journal.log")

    @journalise
    def ajouter(self, valeur):
        return valeur

    ajouter(None, 42)
    contenu = (tmp_path / "journal.log").read_text(encoding="utf-8")
    assert "ajouter" in contenu


def test_cache_evite_le_second_calcul():
    # Le 2e appel avec le même argument ne relance pas le calcul.
    decorateurs.taux_change.cache_clear()
    decorateurs.taux_change("USD")
    decorateurs.taux_change("USD")
    infos = decorateurs.taux_change.cache_info()
    assert infos.hits == 1 and infos.misses == 1
