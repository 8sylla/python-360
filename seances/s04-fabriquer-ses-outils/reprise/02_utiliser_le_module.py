"""02 — Importer et utiliser un module.

Ici on n'écrit PAS d'outil : on ouvre le tiroir `outils_budget` et on s'en
sert. C'est tout l'intérêt d'un module — le code utile est écrit une fois,
rangé, puis réutilisé.

⚠️  Ce fichier doit être dans le MÊME dossier que outils_budget.py, et VS Code
    doit être ouvert sur ce dossier (Fichier ▸ Ouvrir le dossier).
"""

# Deux façons d'importer. On garde la seconde, plus lisible ici.
# import outils_budget            # -> il faudrait écrire outils_budget.total(...)
from outils_budget import total, categories, par_categorie, formater_euro

# Un carnet de démonstration (comme celui de fin de séance 3).
budget = [
    {"titre": "Courses Carrefour", "categorie": "Alimentation", "montant": 54.20},
    {"titre": "Pass Navigo", "categorie": "Transport", "montant": 86.40},
    {"titre": "Netflix", "categorie": "Loisirs", "montant": 13.49},
    {"titre": "Boulangerie", "categorie": "Alimentation", "montant": 4.50},
    {"titre": "Loyer", "categorie": "Logement", "montant": 850.00},
]


# ── On regarde ensemble ──────────────────────────────────────────────────
print("Total du mois :", formater_euro(total(budget)))
print("Catégories    :", categories(budget))
print("Alimentation  :", par_categorie(budget, "Alimentation"))


# ── À toi de jouer ───────────────────────────────────────────────────────
# TODO 1 : affiche le total des seules dépenses de "Loisirs".
#          (indice : combine par_categorie(...) puis total(...))
print("Loisirs         :", formater_euro(total(par_categorie(budget, "Loisirs"))))

# TODO 2 : affiche le nombre de catégories différentes.
#          (indice : len(categories(...)))
print("Nombre de catégories :", len(categories(budget)))

# ── Le piège du __main__ (à comprendre) ──────────────────────────────────
# Quand tu as fait `from outils_budget import ...`, Python a exécuté
# outils_budget.py EN ENTIER — mais son bloc de test ne s'est pas affiché.
# Pourquoi ? Parce qu'il est protégé par `if __name__ == "__main__"`.
# À l'import, __name__ vaut "outils_budget", pas "__main__" : le test dort.
# Sans cette garde, chaque import relancerait le programme du module.
print("\nCe fichier s'appelle, lui, :", __name__)
