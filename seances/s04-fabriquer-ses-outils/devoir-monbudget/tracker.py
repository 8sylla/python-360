"""MonBudget — carnet de dépenses en ligne de commande (v1).

SQUELETTE À COMPLÉTER. Le menu (main) est déjà écrit : il appelle des
fonctions que TU dois écrire au-dessus. Complète les `# TODO`, puis lance :

    python tracker.py
"""

from stockage import charger, sauvegarder   # tes outils du fichier voisin


def demander_montant(question: str) -> float:
    """Redemande tant que la saisie n'est pas un nombre valide (ne plante jamais)."""
    # TODO : une boucle `while True`, un `input`, un `try / except ValueError`.
    #   - dans le try : return float(reponse.replace(",", "."))
    #   - dans l'except : affiche un message et la boucle recommence.
    return 0.0  # <- remplace


def saisir_depense() -> dict:
    """Demande titre, catégorie, montant et rend un dictionnaire dépense."""
    # TODO : renvoie {"titre": ..., "categorie": ..., "montant": ...}
    #   Utilise input(...).strip() pour le texte et demander_montant(...) pour
    #   le montant. Astuce : .title() met "loyer" -> "Loyer".
    return {}  # <- remplace


def afficher(depenses: list) -> None:
    """Affiche le carnet trié par montant décroissant, avec le total."""
    # TODO :
    #   - si la liste est vide, dis-le et return.
    #   - sinon, boucle sur sorted(depenses, key=..., reverse=True) et print
    #     chaque dépense, puis le total (sum des montants).
    pass  # <- remplace


def filtrer_par_categorie(depenses: list, categorie: str) -> list:
    """Rend une NOUVELLE liste : seulement les dépenses de cette catégorie."""
    # TODO : une compréhension de liste. Compare en minuscules (.lower())
    #   pour que "loisirs" et "Loisirs" marchent pareil.
    return []  # <- remplace


MENU = """
=== MonBudget ===
1. Ajouter une dépense
2. Afficher le carnet
3. Filtrer par catégorie
4. Quitter
"""


def main() -> None:
    """Boucle principale — déjà écrite. Elle appelle TES fonctions."""
    depenses = charger()

    while True:
        print(MENU)
        choix = input("Ton choix : ").strip()

        match choix:
            case "1":
                depenses.append(saisir_depense())
                sauvegarder(depenses)
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


if __name__ == "__main__":
    main()
