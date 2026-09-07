"""Tests des méthodes spéciales de Depense.

pytest ne ramasse que les fichiers `test_*.py` et les fonctions `test_*`.
Un fichier nommé `tests_modeles.py` ne serait JAMAIS exécuté — et personne
ne s'en apercevrait.
"""

from modeles import Categorie, Depense


def test_repr_est_pour_le_developpeur():
    depense = Depense("Loyer", 850.0, Categorie.LOGEMENT)
    assert repr(depense) == "Depense('Loyer', 850.0, 'Logement')"


def test_str_est_pour_l_utilisateur():
    depense = Depense("Loyer", 850.0, Categorie.LOGEMENT)
    assert str(depense) == "Loyer — Logement — 850.00 EUR"


def test_deux_depenses_identiques_sont_egales_malgre_les_tags():
    a = Depense("Netflix", 13.49, Categorie.LOISIRS)
    b = Depense("Netflix", 13.49, Categorie.LOISIRS, tags=["abonnement"])
    assert a == b          # les tags ne font pas l'identité


def test_comparer_a_autre_chose_ne_plante_pas():
    assert Depense("Loyer", 850.0) != "Loyer"


def test_hash_permet_le_set():
    a = Depense("Netflix", 13.49, Categorie.LOISIRS)
    b = Depense("Netflix", 13.49, Categorie.LOISIRS)
    assert len({a, b}) == 1     # sans __hash__ : TypeError


def test_tri_par_montant():
    petite = Depense("Café", 2.5)
    grosse = Depense("Loyer", 850.0)
    assert sorted([grosse, petite]) == [petite, grosse]


def test_total_ordering_offre_les_autres_operateurs():
    petite = Depense("Café", 2.5)
    grosse = Depense("Loyer", 850.0)
    assert grosse > petite and petite <= grosse


def test_est_grosse_pile_au_seuil():
    # LE test qu'on cassera en direct en passant le seuil à 1000.
    assert Depense("Pile au seuil", 100.0).est_grosse is True


def test_aller_retour_dict():
    depense = Depense("Loyer", 850.0, Categorie.LOGEMENT, tags=["fixe"])
    assert Depense.depuis_dict(depense.en_dict()) == depense


def test_categorie_inconnue_devient_autre():
    assert Categorie.depuis_texte("licorne") is Categorie.AUTRE
