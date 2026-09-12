"""MonBudget v5 — les graphiques, un par question.

Une fonction par graphique, et chaque fonction reçoit son `ax`. C'est LA
règle d'architecture de la séance : une fonction qui crée sa propre figure
ne peut pas être réutilisée dans un tableau de bord. Une fonction qui
dessine dans l'`ax` qu'on lui donne se compose partout.

Chaque titre dit ce qu'on a trouvé, pas ce qu'on a tracé — règle 1 de la
dataviz honnête. Les chiffres cités dans les titres sont calculés depuis
les données : ils resteront justes si les données changent.
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.axes import Axes

import donnees as D

# La palette : une couleur d'accent, une couleur neutre. Deux suffisent.
ACCENT = "#C1121F"
NEUTRE = "#8B7B78"
VERT = "#2C8A1A"


def theme() -> None:
    """Un thème lisible, en une ligne. À appeler une fois, au début."""
    sns.set_theme(style="whitegrid", font_scale=1.05)


def euros(x: float) -> str:
    """Formate un montant à la française : 36 251 €."""
    return f"{x:,.0f} €".replace(",", " ")


# ═══════════════════════════════════════════════════════════════════════════
#  1. Comparer  ->  des barres
# ═══════════════════════════════════════════════════════════════════════════


def depenses_par_categorie(df: pd.DataFrame, ax: Axes) -> Axes:
    """Question : où part l'argent ?

    Barres HORIZONTALES : les noms de catégories se lisent sans être
    tournés à 45°. C'est un détail, et c'est la différence entre lisible et
    pas.
    """
    table = D.par_categorie(df)
    part_max = table["total"].iloc[0] / table["total"].sum() * 100

    couleurs = [ACCENT] + [NEUTRE] * (len(table) - 1)
    ax.barh(table["categorie"], table["total"], color=couleurs)
    ax.invert_yaxis()  # la plus grosse en haut, comme on lit

    ax.set_title(
        f"Le {table['categorie'].iloc[0].lower()} absorbe "
        f"{part_max:.0f} % du budget à lui seul",
        loc="left",
        weight="bold",
    )
    ax.set_xlabel("Total dépensé sur six mois (€)")
    ax.set_ylabel("")

    # La valeur au bout de chaque barre : le lecteur n'a plus a viser l'axe.
    marge = table["total"].max() * 0.02
    for y, valeur in enumerate(table["total"]):
        ax.text(valeur + marge, y, euros(valeur), va="center", fontsize=9)
    ax.set_xlim(0, table["total"].max() * 1.22)
    return ax


# ═══════════════════════════════════════════════════════════════════════════
#  2. Répartir  ->  un histogramme
# ═══════════════════════════════════════════════════════════════════════════


def repartition_des_montants(df: pd.DataFrame, ax: Axes) -> Axes:
    """Question : mes dépenses sont-elles nombreuses et petites, ou rares
    et grosses ?

    On trace la médiane ET la moyenne. L'écart entre les deux est
    l'enseignement : quand la moyenne est loin au-dessus de la médiane,
    c'est que quelques très grosses valeurs la tirent — ici les loyers.
    """
    mediane = df["montant"].median()
    moyenne = df["montant"].mean()
    seuil = 150
    part = (df["montant"] < seuil).mean() * 100

    sns.histplot(data=df, x="montant", bins=30, ax=ax, color=NEUTRE)
    ax.axvline(mediane, color=ACCENT, linestyle="-", linewidth=2,
               label=f"médiane {euros(mediane)}")
    ax.axvline(moyenne, color=ACCENT, linestyle="--", linewidth=2,
               label=f"moyenne {euros(moyenne)}")

    ax.set_title(
        f"{part:.0f} % des dépenses sont sous {seuil} €,\n"
        "mais la moyenne est tirée par les loyers",
        loc="left",
        weight="bold",
    )
    ax.set_xlabel("Montant d'une dépense (€)")
    ax.set_ylabel("Nombre de dépenses")
    ax.legend()
    return ax


# ═══════════════════════════════════════════════════════════════════════════
#  3. Composer  ->  des barres groupées  (le fruit de la jointure)
# ═══════════════════════════════════════════════════════════════════════════


def reel_contre_prevu(df: pd.DataFrame, budget: pd.DataFrame, ax: Axes) -> Axes:
    """Question : ai-je tenu mon budget ?

    Ce graphique est le seul qui a besoin des DEUX tables. C'est lui qui
    justifie `merge` : ni le relevé ni le budget ne répond seul.

    On trace l'ÉCART EN POURCENTAGE, pas les deux montants côte à côte.
    Raison : le logement pèse 36 000 € et la santé 3 000 €. Sur une échelle
    en euros, les cinq petites catégories sont écrasées et le dépassement
    des loisirs — l'information du graphique — devient invisible. Le
    pourcentage met toutes les catégories sur la même échelle.

    Voir `reel_contre_prevu_en_euros` juste en dessous : c'est la version
    qui cache l'histoire, gardée exprès pour la comparaison en séance.
    """
    bilan = D.bilan_par_categorie(df, budget).sort_values("ecart_pct")
    pire = bilan.iloc[-1]

    couleurs = [ACCENT if e > 0 else VERT for e in bilan["ecart_pct"]]
    ax.barh(bilan["categorie"], bilan["ecart_pct"], color=couleurs)
    ax.axvline(0, color="#444", linewidth=1.2)

    ax.set_title(
        f"Les {pire['categorie'].lower()} dépassent le budget "
        f"de {pire['ecart_pct']:.0f} %",
        loc="left",
        weight="bold",
    )
    ax.set_xlabel("Écart au budget prévu (%)   —   négatif = tenu")
    ax.set_ylabel("")

    limite = bilan["ecart_pct"].abs().max() * 1.35
    ax.set_xlim(-limite, limite)
    for y, (pct, euro) in enumerate(zip(bilan["ecart_pct"], bilan["ecart"])):
        decalage = limite * 0.03
        ax.text(
            pct + (decalage if pct > 0 else -decalage),
            y,
            f"{pct:+.0f} %  ({euros(euro)})",
            va="center",
            ha="left" if pct > 0 else "right",
            fontsize=9,
        )
    return ax


def reel_contre_prevu_en_euros(
    df: pd.DataFrame, budget: pd.DataFrame, ax: Axes
) -> Axes:
    """La MÊME question, en euros — le graphique qui cache sa réponse.

    À projeter à côté du précédent. Les deux sont exacts ; un seul est
    lisible. C'est la démonstration que le choix de l'encodage n'est pas
    cosmétique : il décide de ce que le lecteur pourra voir.
    """
    bilan = D.bilan_par_categorie(df, budget)
    long = D.format_long(bilan)

    sns.barplot(
        data=long,
        x="montant",
        y="categorie",
        hue="type",
        ax=ax,
        palette={"Dépensé": ACCENT, "Prévu": NEUTRE},
    )
    ax.set_title(
        "Dépensé contre prévu, en euros : où est le dépassement ?",
        loc="left",
        weight="bold",
    )
    ax.set_xlabel("Sur six mois (€)")
    ax.set_ylabel("")
    ax.legend(title="")
    return ax


# ═══════════════════════════════════════════════════════════════════════════
#  4. Évoluer  ->  une ligne
# ═══════════════════════════════════════════════════════════════════════════


def evolution_mensuelle(df: pd.DataFrame, budget: pd.DataFrame, ax: Axes) -> Axes:
    """Question : est-ce que ça dérape, et depuis quand ?

    Les mois ne sont PAS triés par valeur : ils ont un ordre naturel, et le
    casser rendrait la courbe absurde. C'est l'exception à la règle du tri.
    """
    reel = D.par_mois(df)
    prevu = budget.groupby("mois")["budget_prevu"].sum().reset_index()
    fusion = reel.merge(prevu, on="mois", how="left")
    depassements = int((fusion["total"] > fusion["budget_prevu"]).sum())

    ax.plot(fusion["mois"], fusion["total"], marker="o", color=ACCENT,
            linewidth=2.5, label="Dépensé")
    ax.plot(fusion["mois"], fusion["budget_prevu"], marker="o", color=NEUTRE,
            linestyle="--", linewidth=2, label="Prévu")
    ax.fill_between(
        fusion["mois"], fusion["total"], fusion["budget_prevu"],
        where=fusion["total"] > fusion["budget_prevu"],
        color=ACCENT, alpha=0.15, interpolate=True,
    )

    ax.set_title(
        f"{depassements} mois sur {len(fusion)} dépassent le budget prévu",
        loc="left",
        weight="bold",
    )
    ax.set_xlabel("")
    ax.set_ylabel("Total du mois (€)")
    # RÈGLE 2 : l'axe part de zéro. Sans cela, un écart de 2 % ressemble
    # à un effondrement.
    ax.set_ylim(0, fusion[["total", "budget_prevu"]].to_numpy().max() * 1.15)
    ax.legend()
    return ax


# ═══════════════════════════════════════════════════════════════════════════
#  Bonus — pour le palier facultatif
# ═══════════════════════════════════════════════════════════════════════════


def carte_de_chaleur(df: pd.DataFrame, ax: Axes) -> Axes:
    """Le tableau croisé, en couleurs. Utile quand on cherche une anomalie.

    Une heatmap sert à REPÉRER, pas à comparer précisément : l'œil compare
    mal deux nuances. D'où `annot=True` — on affiche aussi les chiffres.
    """
    croise = D.croise_categorie_mois(df)
    sns.heatmap(croise, ax=ax, cmap="Reds", annot=True, fmt=".0f",
                cbar_kws={"label": "€ dépensés"}, linewidths=0.5)

    # L'anomalie n'est pas codée en dur : on cherche la case la plus
    # éloignée de la médiane de SA LIGNE. Le titre reste juste si les
    # données changent.
    ecart = croise.div(croise.median(axis=1), axis=0)
    categorie, mois = ecart.stack().idxmax()
    ax.set_title(
        f"{mois} « {categorie} » sort du lot : "
        f"{ecart.loc[categorie, mois]:.1f}x son mois médian",
        loc="left",
        weight="bold",
    )
    ax.set_xlabel("")
    ax.set_ylabel("")
    # Les noms de catégories tournés à 90 degres ne se lisent pas.
    ax.tick_params(axis="y", rotation=0)
    return ax


def montant_contre_jour(df: pd.DataFrame, ax: Axes) -> Axes:
    """Question : dépense-t-on plus en début de mois ?

    La réponse est non — et un titre qui annonce l'ABSENCE de relation est
    un titre honnête. Tous les graphiques ne racontent pas une histoire,
    et c'est une information en soi.
    """
    avec_jour = df.assign(jour=df["date_operation"].dt.day)
    r = avec_jour["montant"].corr(avec_jour["jour"])

    sns.scatterplot(data=avec_jour, x="jour", y="montant", hue="categorie",
                    alpha=0.7, ax=ax)
    ax.set_title(
        f"Aucun lien entre le montant et le jour du mois (r = {r:+.2f})",
        loc="left",
        weight="bold",
    )
    ax.set_xlabel("Jour du mois")
    ax.set_ylabel("Montant (€)")
    ax.legend(title="", fontsize=8, ncol=2)
    return ax


# ═══════════════════════════════════════════════════════════════════════════
#  L'axe qui ment — la démonstration à projeter en séance
# ═══════════════════════════════════════════════════════════════════════════


def axe_qui_mente(df: pd.DataFrame, budget: pd.DataFrame) -> plt.Figure:
    """Le MÊME jeu de données, deux fois. Seul l'axe change.

    À projeter côte à côte, et à faire commenter avant d'expliquer. C'est
    la démonstration la plus efficace de la séance : personne ne croit
    qu'un axe puisse mentir autant avant de l'avoir vu.
    """
    reel = D.par_mois(df)
    fig, (gauche, droite) = plt.subplots(1, 2, figsize=(13, 4.5))

    for ax, depart, etiquette in [
        (gauche, reel["total"].min() * 0.98, "Axe tronqué"),
        (droite, 0, "Axe honnête"),
    ]:
        ax.bar(reel["mois"], reel["total"], color=ACCENT if depart else NEUTRE)
        ax.set_ylim(depart, reel["total"].max() * 1.05)
        ax.set_title(etiquette, loc="left", weight="bold")
        ax.set_ylabel("Total du mois (€)")

    ecart = (reel["total"].max() / reel["total"].min() - 1) * 100
    fig.suptitle(
        f"Le même écart de {ecart:.0f} % — à gauche il ressemble à un "
        "effondrement, à droite à une variation",
        weight="bold",
    )
    fig.tight_layout()
    return fig
