"""MonBudget v2 — le même programme que la v1, mais bâti sur des objets.

Lancement :  python tracker.py

Le comportement à l'écran est identique à la v1. Ce qui change est sous le
capot : une dépense est un objet Depense, le carnet est un objet Budget. Le
code de main() se lit maintenant comme une phrase en français.
"""

from budget import Budget
from modeles import Categorie, Depense


def demander_montant(question: str) -> float:
    """Redemande tant que ce n'est pas un nombre valide (ne plante jamais)."""
    while True:
        reponse = input(question)
        try:
            return float(reponse.replace(",", "."))   # accepte "12,50"
        except ValueError:
            print("  Attention : saisis un montant (ex : 12.50).")


def choisir_categorie() -> Categorie:
    """Affiche les catégories disponibles et rend celle choisie."""
    choix = " / ".join(c.value for c in Categorie)
    texte = input(f"Catégorie ({choix}) : ")
    return Categorie.depuis_texte(texte)   # une faute -> AUTRE, jamais un crash


def saisir_depense() -> Depense:
    """Construit une Depense à partir des saisies clavier."""
    titre = input("Titre : ").strip()
    montant = demander_montant("Montant : ")
    categorie = choisir_categorie()
    return Depense(titre=titre, montant=montant, categorie=categorie)


def afficher_liste(depenses: list[Depense]) -> None:
    """Affiche une liste de dépenses, avec un repère pour les grosses."""
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
    """Boucle principale : elle se lit comme une phrase, grâce aux objets."""
    budget = Budget()
    budget.charger()

    while True:
        print(MENU)
        choix = input("Ton choix : ").strip()

        match choix:
            case "1":
                budget.ajouter(saisir_depense())
                budget.sauvegarder()
                print("Ajoutée et sauvegardée.")
            case "2":
                afficher_liste(budget.triees_par_montant())
                print(f"{'TOTAL':<45}{budget.total:>10.2f}\n")
            case "3":
                cat = input("Quelle catégorie ? ")
                afficher_liste(budget.par_categorie(cat))
            case "4":
                print(f"À bientôt ! ({len(budget)} dépenses enregistrées)")
                break
            case _:
                print("Choix invalide.")


if __name__ == "__main__":
    main()
