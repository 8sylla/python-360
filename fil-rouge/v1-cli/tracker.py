"""OpportuniTrack v1 — carnet d'opportunités en ligne de commande (séance 4)."""

from stockage import charger, sauvegarder


def demander_entier(question: str) -> int:
    """Redemande une saisie tant que l'utilisateur ne donne pas un entier.

    C'est la ceinture de sécurité : sans elle, taper "douze" fait planter tout
    le programme et l'utilisateur perd ce qu'il avait déjà saisi.
    """
    while True:
        reponse = input(question)
        try:
            return int(reponse)
        except ValueError:
            # On NOMME l'erreur attendue : un except nu masquerait tout,
            # y compris un Ctrl+C ou un vrai bug.
            print("  ⚠  Merci de saisir un nombre entier.")


def saisir_opportunite() -> dict:
    """Construit un dictionnaire à partir des saisies de l'utilisateur."""
    return {
        "titre": input("Titre : ").strip(),
        "organisme": input("Organisme : ").strip(),
        "pays": input("Pays : ").strip().title(),
        "jours": demander_entier("Jours restants : "),
    }


def afficher(opportunites: list) -> None:
    """Affiche le carnet trié de la plus urgente à la moins urgente."""
    if not opportunites:  # une liste vide vaut False
        print("\n(Carnet vide)\n")
        return  # return sans valeur = "je m'arrête ici"

    print(f"\n{'TITRE':<30}{'PAYS':<15}{'JOURS':>6}")
    print("-" * 51)
    for opp in sorted(opportunites, key=lambda o: o["jours"]):
        print(f"{opp['titre']:<30}{opp['pays']:<15}{opp['jours']:>6}")
    print()


def filtrer_par_pays(opportunites: list, pays: str) -> list:
    """Renvoie une NOUVELLE liste ne contenant que le pays demandé.

    La fonction ne modifie pas la liste d'origine : bonne habitude qui évitera
    beaucoup de bugs à partir de la séance 5.
    """
    return [opp for opp in opportunites if opp["pays"].lower() == pays.lower()]


MENU = """
=== OpportuniTrack ===
1. Ajouter une opportunité
2. Afficher le carnet
3. Filtrer par pays
4. Quitter
"""


def main() -> None:
    """Boucle principale du programme."""
    opportunites = charger()

    while True:
        print(MENU)
        choix = input("Ton choix : ").strip()

        # match/case (Python 3.10+) : plus lisible qu'une cascade de if/elif
        # quand on compare UNE variable à plusieurs valeurs fixes.
        match choix:
            case "1":
                opportunites.append(saisir_opportunite())
                sauvegarder(opportunites)
                print("Ajoutée et sauvegardée.")
            case "2":
                afficher(opportunites)
            case "3":
                pays = input("Quel pays ? ")
                afficher(filtrer_par_pays(opportunites, pays))
            case "4":
                print("À bientôt !")
                break
            case _:
                print("Choix invalide.")


# Ce bloc ne s'exécute QUE si l'on lance directement `python tracker.py`.
if __name__ == "__main__":
    main()
