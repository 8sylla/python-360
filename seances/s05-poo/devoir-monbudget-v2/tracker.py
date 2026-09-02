"""MonBudget v2 — le menu CLI. DÉJÀ ÉCRIT : il marchera dès que tes classes
(modeles.py, budget.py) seront complétées. Regarde comme main() se lit
maintenant comme une phrase en français.

Lancement :  python tracker.py
"""

from budget import Budget
from modeles import Categorie, Depense


def demander_montant(question: str) -> float:
    while True:
        reponse = input(question)
        try:
            return float(reponse.replace(",", "."))
        except ValueError:
            print("  Attention : saisis un montant (ex : 12.50).")


def choisir_categorie() -> Categorie:
    choix = " / ".join(c.value for c in Categorie)
    return Categorie.depuis_texte(input(f"Catégorie ({choix}) : "))


def saisir_depense() -> Depense:
    titre = input("Titre : ").strip()
    montant = demander_montant("Montant : ")
    return Depense(titre=titre, montant=montant, categorie=choisir_categorie())


def afficher_liste(depenses: list[Depense]) -> None:
    if not depenses:
        print("\n(Aucune dépense)\n")
        return
    print(f"\n{'TITRE':<30}{'CATÉGORIE':<15}{'MONTANT':>10}")
    print("-" * 55)
    for d in depenses:
        marque = "  <- grosse" if d.est_grosse else ""
        print(f"{d.titre:<30}{d.categorie:<15}{d.montant:>10.2f}{marque}")
    print("-" * 55)


MENU = """
=== MonBudget (v2) ===
1. Ajouter une dépense
2. Afficher le carnet
3. Filtrer par catégorie
4. Quitter
"""


def main() -> None:
    budget = Budget()
    budget.charger()
    while True:
        print(MENU)
        match input("Ton choix : ").strip():
            case "1":
                budget.ajouter(saisir_depense())
                budget.sauvegarder()
                print("Ajoutée et sauvegardée.")
            case "2":
                afficher_liste(budget.triees_par_montant())
                print(f"{'TOTAL':<45}{budget.total:>10.2f}\n")
            case "3":
                afficher_liste(budget.par_categorie(input("Quelle catégorie ? ")))
            case "4":
                print(f"À bientôt ! ({len(budget)} dépenses)")
                break
            case _:
                print("Choix invalide.")


if __name__ == "__main__":
    main()
