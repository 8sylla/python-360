"""MonBudget v4 — nettoyage du relevé. SQUELETTE À COMPLÉTER.

Règle de pandas 3.0, à garder sous les yeux :
    « pandas rend une NOUVELLE table. Réaffecte. »

Chaque fonction prend un DataFrame et en REND un autre. Aucune ne modifie
son entrée. C'est ce qui permet de les enchaîner.
"""

from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[3] / "data"
BRUT = DATA / "releve_brut.csv"
PROPRE = DATA / "releve_propre.csv"

SEUIL_ABERRANT = 5000.0


def charger_brut(chemin: Path = BRUT) -> pd.DataFrame:
    """Lit le relevé brut.

    TODO 1 : le fichier est un export français -> separateur POINT-VIRGULE.
             Sans `sep=";"`, pandas leve ici une ParserError dont le
             message ne parle pas de separateur.
             Precise aussi `encoding="utf-8"`.
    """
    return pd.read_csv(chemin)      # <- incomplet : ajoute sep et encoding


def nettoyer_textes(df: pd.DataFrame) -> pd.DataFrame:
    """Harmonise `libelle`, `categorie` et `moyen_paiement`.

    TODO 2 :
      - libelle   : .str.strip().str.title()
      - categorie : .fillna("") puis .str.strip().str.title(),
                    et remplace la chaine vide par "Autre"
      - moyen_paiement : .str.strip().str.upper(), puis .replace() pour
                    ramener CARTE -> CB et VIR -> VIREMENT
      - note      : .fillna("")   (on ne la jette JAMAIS)
    Utilise df.assign(...) — pas df["x"] = ...
    """
    return df


def nettoyer_dates(df: pd.DataFrame) -> pd.DataFrame:
    """Convertit `date_operation` en vraies dates.

    Trois formats coexistent : 2026-04-09, 09/02/2026, 11-06-2026.

    ATTENTION AU PIEGE : `format="mixed", dayfirst=True` applique dayfirst
    AUSSI aux dates ISO et inverse jour et mois, sans lever d'erreur.

    TODO 3 (methode sure) :
      1. normalise les separateurs : .str.strip().str.replace("/", "-")
      2. essaie le format ISO   : pd.to_datetime(t, format="%Y-%m-%d", errors="coerce")
      3. essaie le format FR    : pd.to_datetime(t, format="%d-%m-%Y", errors="coerce")
      4. combine avec .fillna()
    Verifie ensuite que la date MAXIMALE tombe bien en juin.
    """
    return df


def nettoyer_montants(df: pd.DataFrame) -> pd.DataFrame:
    """Convertit `montant` (du texte) en nombres.

    A traiter : "40,37 EUR", "1 250,00", "894.56", "N/A", "".

    TODO 4 : enchaine les .str.replace() pour retirer "EUR" et les espaces,
             remplacer la virgule par un point, puis pd.to_numeric(...,
             errors="coerce").
             COMPTE ensuite combien de valeurs sont devenues NaN : coerce
             est un CHOIX, on doit savoir ce qu'il a jete.
    """
    return df


def supprimer_doublons(df: pd.DataFrame) -> pd.DataFrame:
    """TODO 5 : une ligne. Mais attention a l'ORDRE dans le pipeline :
    il faut avoir nettoye les textes AVANT, sinon '  EDF ' et 'EDF'
    passent pour deux operations differentes."""
    return df


def retirer_inexploitables(df: pd.DataFrame) -> pd.DataFrame:
    """TODO 6 : dropna, mais avec `subset=["date_operation", "montant"]`.
    Un dropna() nu supprimerait toutes les lignes sans `note`,
    c'est-a-dire 8 sur 10."""
    return df


def retirer_aberrants(df: pd.DataFrame, seuil: float = SEUIL_ABERRANT) -> pd.DataFrame:
    """TODO 7 : garde les lignes dont la valeur ABSOLUE du montant est
    inferieure au seuil (la valeur absolue, pour ne pas confondre un gros
    remboursement avec une aberration)."""
    return df


def separer_remboursements(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """TODO 8 : rends (depenses, remboursements) selon le signe du montant.
    Melanger les deux ferait BAISSER les totaux : ce serait faux."""
    return df, df.head(0)


def enrichir(df: pd.DataFrame) -> pd.DataFrame:
    """Deja fait : les colonnes derivees pour la seance 8."""
    return df.assign(
        mois=df["date_operation"].dt.to_period("M").astype(str),
        jour_semaine=df["date_operation"].dt.day_name(),
    )


def nettoyer(df: pd.DataFrame) -> pd.DataFrame:
    """Le pipeline complet — il TRACE ce qu'il jette."""
    etapes = [
        ("textes harmonises", nettoyer_textes),
        ("dates converties", nettoyer_dates),
        ("montants convertis", nettoyer_montants),
        ("doublons supprimes", supprimer_doublons),
        ("lignes inexploitables retirees", retirer_inexploitables),
        ("montants aberrants retires", retirer_aberrants),
    ]
    for nom, etape in etapes:
        avant = len(df)
        df = etape(df)
        perdu = avant - len(df)
        print(f"  {nom:32}{len(df):>5} lignes" + (f"  (-{perdu})" if perdu else ""))
    return enrichir(df)


if __name__ == "__main__":
    brut = charger_brut()
    print(f"Releve brut : {len(brut)} lignes\n")
    propre = nettoyer(brut)
    depenses, remboursements = separer_remboursements(propre)
    print(f"\n{len(depenses)} depenses, {len(remboursements)} remboursements")
    depenses.to_csv(PROPRE, index=False, encoding="utf-8")
    print(f"Ecrit dans {PROPRE.name}")
