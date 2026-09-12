"""MonBudget v5 — les graphiques, un par question.

RÈGLE D'ARCHITECTURE : chaque fonction reçoit son `ax` en argument. Une
fonction qui crée sa propre figure ne peut pas être réutilisée dans un
tableau de bord. Ne la change pas.

Et pour chaque panneau, la vraie question n'est pas « quel tracé ? » mais
« qu'est-ce que ce graphique m'apprend, en une phrase ? ». Cette phrase
est le titre.
"""

import pandas as pd
import seaborn as sns
from matplotlib.axes import Axes

import donnees as D

# Une couleur d'accent, une neutre, une pour « c'est bon ». Trois suffisent.
ACCENT = "#C1121F"
NEUTRE = "#8B7B78"
VERT = "#2C8A1A"


def theme() -> None:
    """Fourni. Un thème lisible, en une ligne."""
    sns.set_theme(style="whitegrid", font_scale=1.05)


def euros(x: float) -> str:
    """Fourni. Formate un montant à la française : 36 251 €."""
    return f"{x:,.0f} €".replace(",", " ")


# ═══════════════════════════════════════════════════════════════════════════
#  TODO 5 — Panneau 1 : où part l'argent ?
# ═══════════════════════════════════════════════════════════════════════════


def depenses_par_categorie(df: pd.DataFrame, ax: Axes) -> Axes:
    """Des barres HORIZONTALES, triées, la première en rouge.

    Pourquoi barh et pas bar ? Parce que les libellés sont des MOTS : à
    l'horizontale ils se lisent sans tourner la tête.

    Les gestes :
      table = D.par_categorie(df)
      ax.barh(table["categorie"], table["total"], color=[...])
      ax.invert_yaxis()          <- la plus grosse en haut, comme on lit
      ax.set_xlabel("Total dépensé sur six mois (€)")
      ax.set_title(...)          <- LE MESSAGE, pas la description

    La liste de couleurs : [ACCENT] + [NEUTRE] * (len(table) - 1)

    Bonus : écris la valeur au bout de chaque barre avec ax.text(), et
    élargis ax.set_xlim() sinon la dernière étiquette est coupée.

    TODO 5
    """
    return ax  # TODO 5


# ═══════════════════════════════════════════════════════════════════════════
#  TODO 6 — Panneau 2 : nombreuses et petites, ou rares et grosses ?
# ═══════════════════════════════════════════════════════════════════════════


def repartition_des_montants(df: pd.DataFrame, ax: Axes) -> Axes:
    """Un histogramme, avec la médiane ET la moyenne tracées.

    L'écart entre les deux EST l'enseignement : quand la moyenne est loin
    au-dessus de la médiane, c'est que quelques très grosses valeurs la
    tirent — ici les loyers.

    Les gestes :
      sns.histplot(data=df, x="montant", bins=30, ax=ax, color=NEUTRE)
      ax.axvline(df["montant"].median(), color=ACCENT, label=...)
      ax.axvline(df["montant"].mean(), color=ACCENT, linestyle="--", label=...)
      ax.legend()

    TODO 6
    """
    return ax  # TODO 6


# ═══════════════════════════════════════════════════════════════════════════
#  TODO 7 — Panneau 3 : ai-je tenu mon budget ?  (le fruit de la jointure)
# ═══════════════════════════════════════════════════════════════════════════


def reel_contre_prevu(df: pd.DataFrame, budget: pd.DataFrame, ax: Axes) -> Axes:
    """Le seul panneau qui a besoin des DEUX tables.

    ATTENTION — la question qui fait ce devoir : faut-il tracer les deux
    montants en EUROS côte à côte, ou l'ÉCART EN POURCENTAGE ?

    Essaie les deux. Le logement pèse 36 000 € et la santé 3 000 : sur une
    échelle en euros, que devient le dépassement des loisirs ?

    Les deux graphiques sont exacts. Un seul répond à la question. Choisis,
    et écris en commentaire POURQUOI tu as choisi celui-là.

    Pour la version en pourcentage :
      bilan = D.bilan_par_categorie(df, budget).sort_values("ecart_pct")
      couleurs = [ACCENT if e > 0 else VERT for e in bilan["ecart_pct"]]
      ax.barh(bilan["categorie"], bilan["ecart_pct"], color=couleurs)
      ax.axvline(0, color="#444")          <- le zéro doit se voir
      ax.set_xlim(-limite, limite)         <- symétrique, sinon ça ment

    TODO 7
    """
    return ax  # TODO 7


# ═══════════════════════════════════════════════════════════════════════════
#  TODO 8 — Panneau 4 : est-ce que ça dérape ?
# ═══════════════════════════════════════════════════════════════════════════


def evolution_mensuelle(df: pd.DataFrame, budget: pd.DataFrame, ax: Axes) -> Axes:
    """Deux lignes : le dépensé, et le prévu en pointillés.

    Les mois ne sont PAS triés par valeur : ils ont un ordre naturel.

    Les gestes :
      reel  = D.par_mois(df)
      prevu = budget.groupby("mois")["budget_prevu"].sum().reset_index()
      suivi = reel.merge(prevu, on="mois", how="left")
      ax.plot(suivi["mois"], suivi["total"], marker="o", color=ACCENT, ...)
      ax.plot(suivi["mois"], suivi["budget_prevu"], linestyle="--", ...)
      ax.set_ylim(0, ...)       <- RÈGLE 2 : l'axe part de ZÉRO
      ax.legend()

    Bonus : ax.fill_between(..., where=reel > prevu) pour teinter les mois
    en dépassement.

    Le titre : combien de mois dépassent ? Compte-les, ne l'écris pas
    en dur.

    TODO 8
    """
    return ax  # TODO 8


# ═══════════════════════════════════════════════════════════════════════════
#  TODO 9 (bonus) — la carte de chaleur
# ═══════════════════════════════════════════════════════════════════════════


def carte_de_chaleur(df: pd.DataFrame, ax: Axes) -> Axes:
    """Facultatif. Le tableau croisé catégorie x mois, en couleurs.

    Une heatmap sert à REPÉRER une anomalie, pas à comparer précisément :
    l'œil compare mal deux nuances. D'où `annot=True`, qui affiche aussi
    les chiffres.

      croise = df.pivot_table(index="categorie", columns="mois",
                              values="montant", aggfunc="sum", fill_value=0)
      sns.heatmap(croise, ax=ax, cmap="Reds", annot=True, fmt=".0f")
      ax.tick_params(axis="y", rotation=0)   <- sinon les noms sont couchés

    TODO 9
    """
    return ax  # TODO 9
