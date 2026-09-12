"""Génère le budget PRÉVU de la séance 8 (fil rouge MonBudget).

La séance 7 a produit un relevé propre : ce qu'on a réellement dépensé.
Pour savoir si c'est beaucoup, il faut une deuxième table : ce qu'on avait
prévu de dépenser. C'est elle qui rend la jointure nécessaire — on ne joint
pas deux tables pour apprendre `merge`, on les joint parce qu'aucune des
deux ne suffit à répondre à la question.

Le fichier produit a UNE LIGNE PAR (catégorie, mois) — six catégories sur
six mois, donc 36 lignes. Ce détail est pédagogique : la clé de jointure
est le COUPLE (catégorie, mois). Qui joint sur la seule catégorie voit son
relevé passer de 333 à 1 998 lignes. C'est le piège de la séance, et il est
naturel : la table est faite comme le serait un vrai budget.

Lancer :  python data/generer_budget_prevu.py
Le tirage est reproductible (graine fixe) : le même fichier à chaque fois.
"""

import csv
import random
from pathlib import Path

GRAINE = 812
SORTIE = Path(__file__).parent / "budget_prevu.csv"

MOIS = ["2026-01", "2026-02", "2026-03", "2026-04", "2026-05", "2026-06"]

# Le budget mensuel de reference, par categorie. Volontairement proche du
# reel pour certaines categories et volontairement trop bas pour d'autres :
# c'est ce qui donne des depassements a montrer sur le tableau de bord.
BUDGETS = {
    "Logement": 6200.0,
    "Transport": 800.0,
    "Alimentation": 900.0,
    "Loisirs": 600.0,
    "Sante": 500.0,
    "Autre": 700.0,
}


def lignes() -> list[dict[str, str]]:
    """Un budget par categorie et par mois, avec une legere variation."""
    random.seed(GRAINE)
    resultat = []
    for mois in MOIS:
        for categorie, base in BUDGETS.items():
            # +/- 8 % d'un mois sur l'autre : un budget se revise, il n'est
            # jamais figé au centime. Arrondi a 10 euros, comme un humain.
            variation = random.uniform(-0.08, 0.08)
            prevu = round(base * (1 + variation) / 10) * 10
            resultat.append(
                {
                    "categorie": categorie,
                    "mois": mois,
                    "budget_prevu": f"{prevu:.2f}",
                }
            )
    return resultat


def ecrire(chemin: Path = SORTIE) -> None:
    donnees = lignes()
    with chemin.open("w", newline="", encoding="utf-8") as f:
        plume = csv.DictWriter(
            f,
            fieldnames=["categorie", "mois", "budget_prevu"],
            delimiter=";",
        )
        plume.writeheader()
        plume.writerows(donnees)
    print(f"{len(donnees)} lignes ecrites dans {chemin.name}")
    print(f"{len(BUDGETS)} categories x {len(MOIS)} mois")


if __name__ == "__main__":
    ecrire()
