"""02 — CORRIGÉ. Importer et utiliser un module."""

from outils_budget import total, categories, par_categorie, formater_euro

budget = [
    {"titre": "Courses Carrefour", "categorie": "Alimentation", "montant": 54.20},
    {"titre": "Pass Navigo", "categorie": "Transport", "montant": 86.40},
    {"titre": "Netflix", "categorie": "Loisirs", "montant": 13.49},
    {"titre": "Boulangerie", "categorie": "Alimentation", "montant": 4.50},
    {"titre": "Loyer", "categorie": "Logement", "montant": 850.00},
]

print("Total du mois :", formater_euro(total(budget)))
print("Catégories    :", categories(budget))
print("Alimentation  :", par_categorie(budget, "Alimentation"))

# TODO 1 : total des dépenses de "Loisirs".
loisirs = par_categorie(budget, "Loisirs")
print("Total Loisirs :", formater_euro(total(loisirs)))

# TODO 2 : nombre de catégories différentes.
print("Nombre de catégories :", len(categories(budget)))

print("\nCe fichier s'appelle, lui, :", __name__)
