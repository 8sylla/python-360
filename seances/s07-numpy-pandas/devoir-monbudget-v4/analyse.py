"""MonBudget v4 — analyses. SQUELETTE À COMPLÉTER.

A lancer APRES nettoyage.py (il a besoin de data/releve_propre.csv).
"""

from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[3] / "data"
pd.set_option("display.float_format", lambda v: f"{v:,.2f}".replace(",", " "))


def charger(chemin: Path = DATA / "releve_propre.csv") -> pd.DataFrame:
    return pd.read_csv(chemin, parse_dates=["date_operation"])


def total_par_categorie(df: pd.DataFrame) -> pd.Series:
    """TODO 1 : groupby("categorie") sur la colonne montant, somme,
    trie du plus grand au plus petit."""
    return pd.Series(dtype=float)


def resume_par_categorie(df: pd.DataFrame) -> pd.DataFrame:
    """TODO 2 : avec .agg(), rends d'un coup nombre / total / moyenne.
    Forme :  .agg(nombre=("montant", "size"), total=("montant", "sum"), ...)"""
    return pd.DataFrame()


def tableau_croise(df: pd.DataFrame) -> pd.DataFrame:
    """TODO 3 : pivot_table, categories en lignes, mois en colonnes,
    somme des montants, fill_value=0, et margins=True pour les totaux."""
    return pd.DataFrame()


def top_depenses(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """TODO 4 : les n plus grosses depenses (indice : .nlargest)."""
    return df.head(0)


if __name__ == "__main__":
    df = charger()
    print(f"{len(df)} depenses\n")
    print("Total par categorie :\n", total_par_categorie(df), "\n")
    print("Resume :\n", resume_par_categorie(df), "\n")
    print("Tableau croise :\n", tableau_croise(df), "\n")
    print("Top 5 :\n", top_depenses(df))
