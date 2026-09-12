"""MonBudget v5 — préparer les données du tableau de bord.

En v4, on a nettoyé un relevé : on sait ce qu'on a dépensé. Mais « 4 600 €
de loisirs », est-ce beaucoup ? La question n'a pas de réponse dans ce
fichier — il faut une deuxième table : le budget qu'on avait prévu.

C'est là que `merge` devient nécessaire. On ne joint pas deux tables pour
apprendre `merge` : on les joint parce qu'aucune des deux ne répond seule à
la question posée.

Ce module ne dessine rien. Il prépare les tables, et rien d'autre : c'est
ce qui permet de le tester et de le relire.
"""

from pathlib import Path

import pandas as pd

DOSSIER_DATA = Path(__file__).resolve().parents[2] / "data"
RELEVE = DOSSIER_DATA / "releve_propre.csv"
BUDGET = DOSSIER_DATA / "budget_prevu.csv"

JOURS_FR = {
    "Monday": "lundi",
    "Tuesday": "mardi",
    "Wednesday": "mercredi",
    "Thursday": "jeudi",
    "Friday": "vendredi",
    "Saturday": "samedi",
    "Sunday": "dimanche",
}
ORDRE_JOURS = list(JOURS_FR.values())


# ═══════════════════════════════════════════════════════════════════════════
#  Charger
# ═══════════════════════════════════════════════════════════════════════════


def charger_releve(chemin: Path = RELEVE) -> pd.DataFrame:
    """Lit le relevé nettoyé de la séance 7.

    `parse_dates` évite le piège de la séance 7 : sans lui, la colonne
    redevient du texte, et `.dt` ne marche plus. Le fichier étant écrit par
    nous, il est au format ISO — donc sans ambiguïté jour/mois.
    """
    df = pd.read_csv(chemin, parse_dates=["date_operation"])
    return df.assign(jour_semaine=df["jour_semaine"].map(JOURS_FR))


def charger_budget(chemin: Path = BUDGET) -> pd.DataFrame:
    """Lit le budget prévu : une ligne par (catégorie, mois). Séparateur ';'."""
    return pd.read_csv(chemin, sep=";")


# ═══════════════════════════════════════════════════════════════════════════
#  Agréger
# ═══════════════════════════════════════════════════════════════════════════


def par_categorie(df: pd.DataFrame) -> pd.DataFrame:
    """Le total par catégorie, TRIÉ par valeur — règle 3 de la dataviz.

    `reset_index()` transforme l'index de groupe en vraie colonne. C'est ce
    que seaborn attend : il travaille sur des colonnes, pas sur des index.
    """
    return (
        df.groupby("categorie")["montant"]
        .sum()
        .sort_values(ascending=False)
        .reset_index(name="total")
    )


def par_mois(df: pd.DataFrame) -> pd.DataFrame:
    """Le total par mois, dans l'ordre CHRONOLOGIQUE.

    Ici on ne trie pas par valeur : les mois ont un ordre naturel, et le
    casser rendrait la courbe illisible. C'est l'exception à la règle 3.
    """
    return df.groupby("mois")["montant"].sum().reset_index(name="total")


def resume_par_categorie(df: pd.DataFrame) -> pd.DataFrame:
    """Plusieurs calculs d'un coup, avec des colonnes NOMMÉES.

    La forme `nom=("colonne", "fonction")` est la seule à retenir : elle
    évite les index à plusieurs niveaux, illisibles pour tout le monde.
    """
    return (
        df.groupby("categorie")
        .agg(
            nombre=("montant", "count"),
            total=("montant", "sum"),
            moyenne=("montant", "mean"),
            maximum=("montant", "max"),
        )
        .sort_values("total", ascending=False)
        .reset_index()
    )


def croise_categorie_mois(df: pd.DataFrame) -> pd.DataFrame:
    """Le tableau croisé catégorie x mois — l'entrée de la heatmap."""
    return df.pivot_table(
        index="categorie",
        columns="mois",
        values="montant",
        aggfunc="sum",
        fill_value=0,
    )


# ═══════════════════════════════════════════════════════════════════════════
#  Joindre — le cœur de la séance
# ═══════════════════════════════════════════════════════════════════════════


def reel_contre_prevu(df: pd.DataFrame, budget: pd.DataFrame) -> pd.DataFrame:
    """Croise le réel et le prévu, par catégorie ET par mois.

    La clé de jointure est le COUPLE (categorie, mois). C'est le point
    important : la table de budget a une ligne par couple, pas une ligne par
    catégorie. Joindre sur la seule catégorie ferait exploser le nombre de
    lignes — voir `jointure_qui_explose` juste en dessous.

    `how="left"` : on garde toutes les dépenses réelles, même si aucun
    budget n'avait été prévu pour ce couple. L'inverse (`inner`) ferait
    disparaître des dépenses réelles sans le dire, ce qui est exactement le
    genre de perte silencieuse qu'on refuse depuis la séance 7.
    """
    reel = (
        df.groupby(["categorie", "mois"])["montant"].sum().reset_index(name="reel")
    )
    fusion = reel.merge(budget, on=["categorie", "mois"], how="left")
    return fusion.assign(
        ecart=fusion["reel"] - fusion["budget_prevu"],
        depassement=fusion["reel"] > fusion["budget_prevu"],
    )


def bilan_par_categorie(df: pd.DataFrame, budget: pd.DataFrame) -> pd.DataFrame:
    """Réel et prévu cumulés sur les six mois, par catégorie.

    C'est la table du panneau 3 du tableau de bord : deux barres par
    catégorie, l'une pour le réel, l'autre pour le prévu.
    """
    croise = reel_contre_prevu(df, budget)
    bilan = (
        croise.groupby("categorie")[["reel", "budget_prevu"]]
        .sum()
        .sort_values("reel", ascending=False)
        .reset_index()
    )
    return bilan.assign(
        ecart=bilan["reel"] - bilan["budget_prevu"],
        ecart_pct=(bilan["reel"] / bilan["budget_prevu"] - 1) * 100,
    )


def jointure_qui_explose(df: pd.DataFrame, budget: pd.DataFrame) -> pd.DataFrame:
    """LE PIÈGE, sur commande — à exécuter en séance, puis à compter.

    On joint sur la seule colonne `categorie`. Comme le budget a six lignes
    par catégorie (une par mois), chaque dépense se retrouve dupliquée six
    fois. Aucune erreur, aucun avertissement : juste six fois trop de
    lignes, et un total six fois trop grand.

    Le réflexe à installer : compter les lignes AVANT et APRÈS chaque
    merge. Si le nombre a grossi, c'est un bug, pas un succès.
    """
    return df.merge(budget, on="categorie", how="left")


def format_long(bilan: pd.DataFrame) -> pd.DataFrame:
    """Passe de « une ligne, deux colonnes » à « deux lignes, une valeur ».

    seaborn dessine des groupes de barres à partir d'une colonne de
    catégorie (`hue`), pas à partir de deux colonnes côte à côte. Il faut
    donc déplier la table : c'est ce que fait `melt`, l'inverse exact de
    `pivot_table`.
    """
    return bilan.melt(
        id_vars="categorie",
        value_vars=["reel", "budget_prevu"],
        var_name="type",
        value_name="montant",
    ).replace({"reel": "Dépensé", "budget_prevu": "Prévu"})


# ═══════════════════════════════════════════════════════════════════════════
#  Le point d'entrée
# ═══════════════════════════════════════════════════════════════════════════


def tout_charger() -> tuple[pd.DataFrame, pd.DataFrame]:
    """Les deux tables, prêtes à l'emploi."""
    return charger_releve(), charger_budget()


if __name__ == "__main__":
    releve, budget = tout_charger()

    print(f"Releve : {len(releve)} depenses")
    print(f"Budget : {len(budget)} lignes ({budget['categorie'].nunique()} categories")
    print(f"         x {budget['mois'].nunique()} mois)")

    print("\n--- Total par categorie ---")
    print(par_categorie(releve).to_string(index=False))

    print("\n--- Bilan reel / prevu ---")
    bilan = bilan_par_categorie(releve, budget)
    print(bilan.round(2).to_string(index=False))

    print("\n--- Le piege de la jointure ---")
    explose = jointure_qui_explose(releve, budget)
    print(f"avant : {len(releve)} lignes")
    print(f"apres : {len(explose)} lignes   <-- x{len(explose) / len(releve):.0f}")
    print(f"total fausse : {explose['montant'].sum():,.2f} EUR".replace(",", " "))
    print(f"total juste  : {releve['montant'].sum():,.2f} EUR".replace(",", " "))
