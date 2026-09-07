"""MonBudget v3 — le même programme, mais le code se lit tout seul.

Lancement :  python tracker.py

Ce qui change par rapport à la v2, visible dans main() :
  - plus de charger()/sauvegarder() à la main : `with Budget() as budget:` ;
  - plus de budget.toutes() : on boucle directement sur le budget ;
  - plus de lambda de tri : `sorted(budget)` suffit, Depense sait se comparer.
"""

from budget import Budget
from modeles import Categorie, Depense


def demander_montant(question: str) -> float:
    """Redemande tant que ce n'est pas un nombre valide."""
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


def afficher(depenses) -> None:
    """Affiche n'importe quel itérable de Depense (liste, générateur, budget)."""
    depenses = list(depenses)          # un générateur ne se parcourt qu'une fois
    if not depenses:
        print("\n(Aucune dépense)\n")
        return
    print()
    for i, depense in enumerate(depenses, start=1):
        marque = "  <- grosse" if depense.est_grosse else ""
        print(f"{i:>2}. {depense:court}{marque}")
    print()


MENU = """
=== MonBudget (v3) ===
1. Ajouter une dépense
2. Afficher le carnet (trié)
3. Les 3 plus grosses
4. Par catégorie
5. Doublons détectés
6. Quitter
"""


def main() -> None:
    # Le with charge à l'entrée et sauvegarde à la sortie, quoi qu'il arrive.
    with Budget() as budget:
        while True:
            print(MENU)
            match input("Ton choix : ").strip():
                case "1":
                    budget.ajouter(saisir_depense())
                    print("Ajoutée.")
                case "2":
                    afficher(sorted(budget, reverse=True))   # __iter__ + __lt__
                    print(f"TOTAL : {budget.total:.2f} EUR\n")
                case "3":
                    afficher(budget.top(3))
                case "4":
                    afficher(budget.par_categorie(input("Quelle catégorie ? ")))
                case "5":
                    afficher(budget.doublons())
                case "6":
                    print(f"À bientôt ! ({budget})")
                    break
                case _:
                    print("Choix invalide.")


if __name__ == "__main__":
    main()
