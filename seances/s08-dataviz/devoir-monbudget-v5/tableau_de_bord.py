"""MonBudget v5 — le tableau de bord.

Ce fichier est presque entièrement fourni : il assemble les panneaux que
tu as écrits dans `graphiques.py`. Il reste deux TODO.

    python tableau_de_bord.py

L'image arrive dans figures/.
"""

from pathlib import Path

import matplotlib.pyplot as plt

import donnees as D
import graphiques as G

FIGURES = Path(__file__).parent / "figures"


def construire() -> plt.Figure:
    """Une Figure (le cadre), quatre Axes (les photos), en 2 x 2."""
    releve, budget = D.tout_charger()
    G.theme()

    fig, axes = plt.subplots(2, 2, figsize=(16, 11))

    G.depenses_par_categorie(releve, axes[0, 0])
    G.repartition_des_montants(releve, axes[0, 1])
    G.reel_contre_prevu(releve, budget, axes[1, 0])
    G.evolution_mensuelle(releve, budget, axes[1, 1])

    # ═══════════════════════════════════════════════════════════════════════
    #  TODO 10 — le titre général de la figure
    # ═══════════════════════════════════════════════════════════════════════
    # Un titre qui situe : la période, le nombre de dépenses, le total.
    # Calcule-les, ne les écris pas en dur.
    #
    #   total = f"{releve['montant'].sum():,.0f}".replace(",", " ")
    #   fig.suptitle(f"...", fontsize=17, weight="bold")
    #
    # TODO 10

    # tight_layout AVANT savefig, sinon les titres se chevauchent. Le rect
    # reserve la bande du haut au suptitle.
    fig.tight_layout(rect=(0, 0, 1, 0.97))
    return fig


def main() -> None:
    FIGURES.mkdir(exist_ok=True)
    fig = construire()

    # ═══════════════════════════════════════════════════════════════════════
    #  TODO 11 — exporter proprement
    # ═══════════════════════════════════════════════════════════════════════
    # Trois arguments, trois raisons :
    #   dpi=150             net au videoprojecteur (100 par defaut = flou)
    #   bbox_inches="tight" pas de marge blanche parasite
    #   un .svg en plus     vectoriel : ne pixelise jamais
    #
    #   fig.savefig(FIGURES / "tableau_de_bord.png", ...)
    #   fig.savefig(FIGURES / "tableau_de_bord.svg", ...)
    #
    # TODO 11

    print(f"Fichiers dans {FIGURES.name}/ :")
    for f in sorted(FIGURES.glob("*")):
        print(f"  {f.name}  ({f.stat().st_size // 1024} ko)")
    if not any(FIGURES.glob("*")):
        print("  (aucun — le TODO 11 n'est pas fait)")

    plt.close("all")


if __name__ == "__main__":
    main()
