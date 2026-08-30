"""outils_budget — CORRIGÉ. Le module d'outils pour les dépenses."""


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
    """Rend la dépense (le dict) au montant le plus élevé, ou None si vide."""
    if not depenses:
        return None
    return max(depenses, key=lambda d: d["montant"])


if __name__ == "__main__":
    exemple = [
        {"titre": "Courses", "categorie": "Alimentation", "montant": 54.20},
        {"titre": "Cinéma", "categorie": "Loisirs", "montant": 12.00},
    ]
    print("Auto-test du module :")
    print("  total       ->", total(exemple))
    print("  categories  ->", categories(exemple))
    print("  formater    ->", formater_euro(total(exemple)))
    print("  plus_grosse ->", plus_grosse(exemple))
