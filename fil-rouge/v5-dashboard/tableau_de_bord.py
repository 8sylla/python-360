"""MonBudget v5 — le tableau de bord.

Une figure, quatre panneaux, quatre questions :

    1. Où part l'argent ?              -> des barres
    2. Mes dépenses sont-elles         -> un histogramme
       nombreuses et petites ?
    3. Ai-je tenu mon budget ?         -> des barres groupées (la jointure)
    4. Est-ce que ça dérape ?          -> une ligne

Lancer :  python tableau_de_bord.py
Les images arrivent dans `figures/`.
"""

from pathlib import Path

import matplotlib.pyplot as plt

import donnees as D
import graphiques as G

FIGURES = Path(__file__).parent / "figures"


def construire() -> plt.Figure:
    """La figure complète. Elle ne s'enregistre pas elle-même : c'est
    l'appelant qui décide quoi en faire."""
    releve, budget = D.tout_charger()
    G.theme()

    # UNE Figure (le cadre), QUATRE Axes (les photos), en 2 x 2.
    fig, axes = plt.subplots(2, 2, figsize=(16, 11))

    G.depenses_par_categorie(releve, axes[0, 0])
    G.repartition_des_montants(releve, axes[0, 1])
    G.reel_contre_prevu(releve, budget, axes[1, 0])
    G.evolution_mensuelle(releve, budget, axes[1, 1])

    total = f"{releve['montant'].sum():,.0f}".replace(",", " ")
    fig.suptitle(
        f"MonBudget — six mois, {len(releve)} dépenses, {total} €",
        fontsize=17,
        weight="bold",
    )
    # tight_layout AVANT savefig : sinon les titres se chevauchent.
    fig.tight_layout(rect=(0, 0, 1, 0.97))
    return fig


def annexes() -> list[tuple[str, plt.Figure]]:
    """Les figures du palier bonus, une par fichier."""
    releve, budget = D.tout_charger()
    G.theme()

    fig_heat, ax = plt.subplots(figsize=(11, 5))
    G.carte_de_chaleur(releve, ax)
    fig_heat.tight_layout()

    fig_nuage, ax = plt.subplots(figsize=(9, 5.5))
    G.montant_contre_jour(releve, ax)
    fig_nuage.tight_layout()

    return [
        ("carte_de_chaleur.png", fig_heat),
        ("montant_contre_jour.png", fig_nuage),
        ("axe_qui_mente.png", G.axe_qui_mente(releve, budget)),
    ]


def main() -> None:
    FIGURES.mkdir(exist_ok=True)

    fig = construire()
    # dpi=150 : net a l'impression. bbox_inches="tight" : pas de marge
    # blanche parasite autour de la figure.
    chemin = FIGURES / "tableau_de_bord.png"
    fig.savefig(chemin, dpi=150, bbox_inches="tight")
    print(f"ecrit : {chemin.relative_to(Path(__file__).parent)}")

    for nom, figure in annexes():
        figure.savefig(FIGURES / nom, dpi=150, bbox_inches="tight")
        print(f"ecrit : figures/{nom}")

    # Le SVG ne pixelise jamais : a preferer des qu'on projette ou imprime.
    fig.savefig(FIGURES / "tableau_de_bord.svg", bbox_inches="tight")
    print("ecrit : figures/tableau_de_bord.svg")

    plt.close("all")


if __name__ == "__main__":
    main()
