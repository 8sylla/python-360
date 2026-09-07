"""MonBudget v3 — le CLI. DÉJÀ ÉCRIT : ne le modifie pas.

Il utilise volontairement les prises que tu dois brancher :
  - `with Budget() as budget:`   -> TODO 6 (__enter__ / __exit__)
  - `for d in budget`            -> TODO 2 (__iter__)
  - `sorted(budget)`             -> TODO 4 de modeles.py (__lt__)
  - `budget.grosses()`           -> TODO 5 (le générateur)

Tant que ces TODO ne sont pas faits, il plante — et le message d'erreur te
dit exactement lequel il manque. C'est un guide, pas une punition.
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


def saisir_depense() -> Depense:
    titre = input("Titre : ").strip()
    montant = demander_montant("Montant : ")
    choix = " / ".join(c.value for c in Categorie)
    categorie = Categorie.depuis_texte(input(f"Catégorie ({choix}) : "))
    return Depense(titre=titre, montant=montant, categorie=categorie)


def afficher(depenses) -> None:
    depenses = list(depenses)          # un générateur ne se parcourt qu'une fois
    if not depenses:
        print("\n(Aucune dépense)\n")
        return
    print()
    for i, depense in enumerate(depenses, start=1):
        print(f"{i:>2}. {depense}")
    print()


MENU = """
=== MonBudget (v3) ===
1. Ajouter une dépense
2. Afficher le carnet (trié par montant)
3. Les grosses dépenses
4. Quitter
"""


def main() -> None:
    with Budget() as budget:               # TODO 6
        while True:
            print(MENU)
            match input("Ton choix : ").strip():
                case "1":
                    budget.ajouter(saisir_depense())
                    print("Ajoutée.")
                case "2":
                    afficher(sorted(budget, reverse=True))    # TODO 2 + __lt__
                    print(f"TOTAL : {budget.total:.2f} EUR\n")
                case "3":
                    afficher(budget.grosses())                # TODO 5
                case "4":
                    print("À bientôt !")
                    break
                case _:
                    print("Choix invalide.")


if __name__ == "__main__":
    main()
