"""MonBudget — carnet de dépenses en ligne de commande (v1).

Lancement :  python tracker.py

Le programme lit ses dépenses au démarrage, propose un menu, et sauvegarde
sur le disque après chaque ajout. Les données survivent à la fermeture.
"""

from stockage import charger, sauvegarder   # on importe NOS outils


def demander_montant(question: str) -> float:
    """Redemande une saisie tant que ce n'est pas un nombre valide.

    La ceinture de sécurité : sans elle, taper "douze" ferait planter tout
    le programme et l'utilisateur perdrait sa saisie.
    """
    while True:
        reponse = input(question)
        try:
            return float(reponse.replace(",", "."))   # accepte "12,50"
        except ValueError:
            print("  Attention : saisis un montant (ex : 12.50).")


def saisir_depense() -> dict:
    """Construit un dictionnaire dépense à partir des saisies clavier."""
    return {
        "titre": input("Titre : ").strip(),
        "categorie": input("Catégorie : ").strip().title(),  # "loyer" -> "Loyer"
        "montant": demander_montant("Montant : "),
    }


def afficher(depenses: list) -> None:
    """Affiche le carnet, trié du plus gros au plus petit montant."""
    if not depenses:                    # une liste vide vaut False
        print("\n(Carnet vide)\n")
        return                          # return sans valeur = « je m'arrête ici »

    print(f"\n{'TITRE':<30}{'CATÉGORIE':<15}{'MONTANT':>10}")
    print("-" * 55)
    for d in sorted(depenses, key=lambda x: x["montant"], reverse=True):
        print(f"{d['titre']:<30}{d['categorie']:<15}{d['montant']:>10.2f}")
    print("-" * 55)
    total = sum(d["montant"] for d in depenses)
    print(f"{'TOTAL':<45}{total:>10.2f}\n")


def filtrer_par_categorie(depenses: list, categorie: str) -> list:
    """Renvoie une NOUVELLE liste : seulement la catégorie demandée.

    Ne modifie pas la liste d'origine — bonne habitude qui évitera des bugs
    dès la séance 5.
    """
    cible = categorie.strip().lower()
    return [d for d in depenses if d["categorie"].lower() == cible]


MENU = """
=== MonBudget ===
1. Ajouter une dépense
2. Afficher le carnet
3. Filtrer par catégorie
4. Quitter
"""


def main() -> None:
    """Boucle principale : elle orchestre, sans logique métier dedans."""
    depenses = charger()                # on récupère ce qui a été sauvegardé

    while True:
        print(MENU)
        choix = input("Ton choix : ").strip()

        match choix:                    # 3.10+, plus lisible qu'une cascade d'elif
            case "1":
                depenses.append(saisir_depense())
                sauvegarder(depenses)   # sauvegarde immédiate
                print("Ajoutée et sauvegardée.")
            case "2":
                afficher(depenses)
            case "3":
                cat = input("Quelle catégorie ? ")
                afficher(filtrer_par_categorie(depenses, cat))
            case "4":
                print("À bientôt !")
                break
            case _:
                print("Choix invalide.")


# Ne s'exécute QUE si l'on lance directement `python tracker.py`
# (et pas si un autre fichier fait `import tracker`).
if __name__ == "__main__":
    main()
