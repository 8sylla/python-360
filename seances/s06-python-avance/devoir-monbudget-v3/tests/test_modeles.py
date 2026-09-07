"""Un test d'exemple — ajoute-en au moins trois autres.

Lancer depuis CE dossier :   pytest -q
(pytest ne ramasse que les fichiers `test_*.py` et les fonctions `test_*`.)
"""

from modeles import Categorie, Depense


def test_est_grosse_au_seuil():
    """Le test qu'on cassera en direct en changeant SEUIL_GROSSE_DEPENSE."""
    assert Depense("Pile au seuil", 100.0).est_grosse is True


def test_categorie_inconnue_devient_autre():
    assert Categorie.depuis_texte("licorne") is Categorie.AUTRE


# ── À toi d'écrire ────────────────────────────────────────────────────────
# TODO A : test_repr_est_pour_le_developpeur
#     assert repr(Depense("Loyer", 850.0)) == "Depense('Loyer', 850.0)"
#
# TODO B : test_deux_depenses_identiques_sont_egales
#     Deux Depense de mêmes titre/montant/catégorie doivent être ==,
#     même si leurs tags diffèrent.
#
# TODO C : test_hash_permet_le_set
#     len({a, b}) doit valoir 1 pour deux dépenses identiques.
#     (Sans __hash__ : TypeError.)
#
# TODO D : test_tri_par_montant
#     sorted([grosse, petite]) doit rendre [petite, grosse].
