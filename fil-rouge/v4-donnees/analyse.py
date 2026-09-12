"""MonBudget v4 — analyser le relevé nettoyé avec pandas.

Tout ce que la v3 faisait à la main, avec des boucles Python, tient ici en
une ligne — et tourne sur 400 lignes comme sur 400 000.
"""

from pathlib import Path

import pandas as pd

from nettoyage import PROPRE

pd.set_option("display.width", 100)
pd.set_option("display.float_format", lambda v: f"{v:,.2f}".replace(",", " "))


def charger(chemin: Path = PROPRE) -> pd.DataFrame:
    """Relit le relevé propre en redonnant son type à la colonne de dates."""
    return pd.read_csv(chemin, parse_dates=["date_operation"])


def total_par_categorie(df: pd.DataFrame) -> pd.Series:
    """L'équivalent d'une ligne du tableau croisé d'Excel.

    En v3, c'était une boucle avec un defaultdict. Ici : une ligne.
    """
    return df.groupby("categorie")["montant"].sum().sort_values(ascending=False)


def total_par_mois(df: pd.DataFrame) -> pd.Series:
    return df.groupby("mois")["montant"].sum()


def tableau_croise(df: pd.DataFrame) -> pd.DataFrame:
    """Catégories en lignes, mois en colonnes — le tableau croisé dynamique."""
    return df.pivot_table(
        index="categorie", columns="mois", values="montant",
        aggfunc="sum", fill_value=0, margins=True, margins_name="Total",
    )


def resume_par_categorie(df: pd.DataFrame) -> pd.DataFrame:
    """Plusieurs statistiques d'un coup : c'est tout l'intérêt de .agg()."""
    return (
        df.groupby("categorie")
        .agg(nombre=("montant", "size"),
             total=("montant", "sum"),
             moyenne=("montant", "mean"),
             maximum=("montant", "max"))
        .sort_values("total", ascending=False)
    )


def top_depenses(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    return df.nlargest(n, "montant")[["date_operation", "libelle", "categorie", "montant"]]


def part_du_budget(df: pd.DataFrame) -> pd.Series:
    """Le poids de chaque catégorie, en pourcentage."""
    totaux = total_par_categorie(df)
    return (totaux / totaux.sum() * 100).round(1)


if __name__ == "__main__":
    df = charger()
    print(f"=== MonBudget v4 : {len(df)} depenses analysees ===\n")

    print("Total par categorie :")
    print(total_par_categorie(df).to_string(), "\n")

    print("Part du budget (%) :")
    print(part_du_budget(df).to_string(), "\n")

    print("Resume par categorie :")
    print(resume_par_categorie(df).to_string(), "\n")

    print("Total par mois :")
    print(total_par_mois(df).to_string(), "\n")

    print("Les 5 plus grosses depenses :")
    print(top_depenses(df).to_string(index=False), "\n")

    print("Tableau croise categorie x mois :")
    print(tableau_croise(df).to_string())
