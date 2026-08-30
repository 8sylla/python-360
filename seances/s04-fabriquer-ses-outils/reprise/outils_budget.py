"""outils_budget — un MODULE : une boîte à outils pour les dépenses.

Un module est un fichier .py qu'on IMPORTE depuis un autre fichier. Celui-ci
ne contient que des fonctions « pures » : elles reçoivent des données, rendent
un résultat, et n'affichent rien elles-mêmes. On les réutilise partout.

On ne lance pas ce fichier directement : on l'ouvre depuis 02_utiliser_le_module.py
avec `import`. (Voir la garde `if __name__ == "__main__"` tout en bas.)
"""


def total(depenses):
    """Rend la somme des montants du carnet."""
    return sum(d["montant"] for d in depenses)


def categories(depenses):
    """Rend l'ensemble (set) des catégories présentes, sans doublon."""
    return {d["categorie"] for d in depenses}


def par_categorie(depenses, categorie):
    """Rend une NOUVELLE liste : seulement les dépenses de cette catégorie."""
    return [d for d in depenses if d["categorie"] == categorie]


def formater_euro(montant):
    """Rend un montant formaté en euros. Ex : 54.2 -> '54.20 €'."""
    return f"{montant:.2f} €"


def plus_grosse(depenses):
    """Rend la dépense (le dict) au montant le plus élevé.

    TODO (bonus) : utilise max(...) avec key=lambda d: d["montant"].
    Pour l'instant, renvoie None pour que le module reste importable.
    """
    return None  # <- à compléter en bonus


# Cette partie ne s'exécute QUE si on lance directement `python outils_budget.py`.
# Elle sert d'auto-test rapide du module, sans polluer ceux qui l'importent.
if __name__ == "__main__":
    exemple = [
        {"titre": "Courses", "categorie": "Alimentation", "montant": 54.20},
        {"titre": "Cinéma", "categorie": "Loisirs", "montant": 12.00},
    ]
    print("Auto-test du module :")
    print("  total       ->", total(exemple))
    print("  categories  ->", categories(exemple))
    print("  formater    ->", formater_euro(total(exemple)))
