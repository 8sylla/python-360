"""MonBudget v5 — préparer les données du tableau de bord.

Ce module ne dessine RIEN. Il charge, agrège, joint. C'est ce qui permet
de le tester : une fonction qui rend une table se vérifie, une fonction
qui affiche un graphique ne se vérifie pas.

Fais les TODO dans l'ordre. Lance `python donnees.py` après chacun :
l'erreur recule d'un cran à chaque fois.
"""

from pathlib import Path

import pandas as pd

DOSSIER_DATA = Path(__file__).resolve().parents[3] / "data"
RELEVE = DOSSIER_DATA / "releve_propre.csv"
BUDGET = DOSSIER_DATA / "budget_prevu.csv"


# ═══════════════════════════════════════════════════════════════════════════
#  TODO 1 — charger les deux tables
# ═══════════════════════════════════════════════════════════════════════════


def charger_releve(chemin: Path = RELEVE) -> pd.DataFrame:
    """Lit le relevé nettoyé de la séance 7.

    Attention : sans `parse_dates`, la colonne `date_operation` revient en
    TEXTE et `.dt` ne marchera plus. Le fichier est au format ISO.

    TODO 1a : rends pd.read_csv(chemin, parse_dates=["date_operation"])
    """
    return None  # TODO 1a


def charger_budget(chemin: Path = BUDGET) -> pd.DataFrame:
    """Lit le budget prévu : une ligne par (catégorie, mois).

    Attention au SÉPARATEUR : ce fichier utilise `;`. Sans `sep=";"`,
    pandas lit une seule colonne — et `df.shape` te le dira.

    TODO 1b : rends pd.read_csv(chemin, sep=";")
    """
    return None  # TODO 1b


# ═══════════════════════════════════════════════════════════════════════════
#  TODO 2 — agréger
# ═══════════════════════════════════════════════════════════════════════════


def par_categorie(df: pd.DataFrame) -> pd.DataFrame:
    """Le total par catégorie, TRIÉ par valeur décroissante.

    Trois gestes enchaînés :
      - groupby("categorie")["montant"].sum()
      - .sort_values(ascending=False)       <- RÈGLE 3 de la dataviz
      - .reset_index(name="total")          <- pour que seaborn s'y retrouve

    Résultat attendu : 6 lignes, colonnes ["categorie", "total"],
    Logement en tête avec 36 251.24.

    TODO 2a
    """
    return None  # TODO 2a


def par_mois(df: pd.DataFrame) -> pd.DataFrame:
    """Le total par mois, dans l'ordre CHRONOLOGIQUE.

    Ici on ne trie PAS par valeur : les mois ont un ordre naturel, et le
    casser rendrait la courbe illisible. C'est l'exception à la règle 3.

    Résultat attendu : 6 lignes, colonnes ["mois", "total"].

    TODO 2b
    """
    return None  # TODO 2b


# ═══════════════════════════════════════════════════════════════════════════
#  TODO 3 — joindre  (le cœur du devoir)
# ═══════════════════════════════════════════════════════════════════════════


def reel_contre_prevu(df: pd.DataFrame, budget: pd.DataFrame) -> pd.DataFrame:
    """Croise le réel et le prévu, par catégorie ET par mois.

    Trois étapes :

      1. agréger le réel par (categorie, mois) :
             df.groupby(["categorie", "mois"])["montant"].sum()
               .reset_index(name="reel")

      2. joindre au budget. LA CLÉ EST LE COUPLE :
             .merge(budget, on=["categorie", "mois"], how="left")

         Pourquoi `on=[...]` et pas `on="categorie"` ? Parce que le budget
         a SIX lignes par catégorie, une par mois. Joindre sur la seule
         catégorie duplique chaque dépense six fois — sans un mot.

         Pourquoi `how="left"` et pas le défaut (`inner`) ? Parce que
         `inner` supprimerait en silence toute dépense sans budget prévu.
         On préfère un NaN visible à une ligne disparue.

      3. ajouter deux colonnes avec .assign() :
             ecart       = reel - budget_prevu
             depassement = reel > budget_prevu

    Résultat attendu : 36 lignes. **Exactement autant que l'étape 1.**

    TODO 3
    """
    return None  # TODO 3


def bilan_par_categorie(df: pd.DataFrame, budget: pd.DataFrame) -> pd.DataFrame:
    """Réel et prévu CUMULÉS sur les six mois, par catégorie.

    C'est la table du panneau 3. À partir de reel_contre_prevu() :

      - groupby("categorie")[["reel", "budget_prevu"]].sum()
      - .reset_index()
      - puis .assign() pour ajouter :
            ecart     = reel - budget_prevu
            ecart_pct = (reel / budget_prevu - 1) * 100

    Résultat attendu : 6 lignes. Loisirs à +29.57 %, Sante à -2.50 %.

    TODO 4
    """
    return None  # TODO 4


# ═══════════════════════════════════════════════════════════════════════════
#  Fourni — le contrôle anti-explosion. Ne le supprime pas.
# ═══════════════════════════════════════════════════════════════════════════


def verifier_jointure(avant: int, apres: int) -> None:
    """Le réflexe de la séance, en une fonction.

    Si le nombre de lignes a grossi après un merge, c'est un bug — pas un
    succès. Cette fonction plante fort et tôt, ce qui est exactement ce
    qu'on veut : mieux vaut une erreur qu'un total six fois trop grand.
    """
    if apres != avant:
        raise ValueError(
            f"La jointure a change le nombre de lignes : {avant} -> {apres}. "
            f"La cle est-elle bien le COUPLE (categorie, mois) ?"
        )


def tout_charger() -> tuple[pd.DataFrame, pd.DataFrame]:
    return charger_releve(), charger_budget()


if __name__ == "__main__":
    releve, budget = tout_charger()
    print(f"Releve : {len(releve)} depenses")
    print(f"Budget : {len(budget)} lignes")

    print("\n--- Total par categorie ---")
    print(par_categorie(releve).to_string(index=False))

    print("\n--- Total par mois ---")
    print(par_mois(releve).to_string(index=False))

    print("\n--- Reel contre prevu ---")
    croise = reel_contre_prevu(releve, budget)
    attendu = len(releve.groupby(["categorie", "mois"]))
    verifier_jointure(attendu, len(croise))
    print(croise.head(6).round(2).to_string(index=False))

    print("\n--- Bilan par categorie ---")
    print(bilan_par_categorie(releve, budget).round(2).to_string(index=False))
