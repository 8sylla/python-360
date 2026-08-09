"""OpportuniTrack v2 — même usage qu'en v1, structure orientée objet (séance 5).

Compare ce fichier avec fil-rouge/v1-cli/tracker.py : le comportement visible
est identique. C'est la définition même d'une refactorisation.
"""

from datetime import date

from carnet import Carnet
from modeles import Opportunite

MENU = """
=== OpportuniTrack v2 ===
1. Ajouter une opportunité
2. Afficher le carnet
3. Afficher seulement les urgentes
4. Filtrer par pays
5. Quitter
"""


def saisir() -> Opportunite:
    """Construit une Opportunite à partir des saisies."""
    titre = input("Titre : ").strip()
    organisme = input("Organisme : ").strip()
    pays = input("Pays : ").strip().title()

    while True:
        try:
            deadline = date.fromisoformat(input("Deadline (AAAA-MM-JJ) : ").strip())
            break
        except ValueError:
            print("  ⚠  Format attendu : 2027-01-15")

    return Opportunite(titre=titre, organisme=organisme, pays=pays, deadline=deadline)


def afficher(opportunites: list[Opportunite]) -> None:
    if not opportunites:
        print("\n(Rien à afficher)\n")
        return

    print(f"\n{'TITRE':<32}{'PAYS':<15}{'JOURS':>6}")
    print("-" * 53)
    for opp in opportunites:
        marque = " !" if opp.est_urgente else ""
        print(f"{opp.titre:<32}{opp.pays:<15}{opp.jours_restants:>6}{marque}")
    print()


def main() -> None:
    carnet = Carnet()
    carnet.charger()

    while True:
        print(MENU)
        match input("Ton choix : ").strip():
            case "1":
                carnet.ajouter(saisir())
                carnet.sauvegarder()
                print("Ajoutée et sauvegardée.")
            case "2":
                # Le code principal se lit maintenant comme une phrase.
                afficher(carnet.triees_par_urgence())
            case "3":
                afficher(carnet.urgentes())
            case "4":
                afficher(carnet.par_pays(input("Quel pays ? ")))
            case "5":
                print("À bientôt !")
                break
            case _:
                print("Choix invalide.")


if __name__ == "__main__":
    main()
