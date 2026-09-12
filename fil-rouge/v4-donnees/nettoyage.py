"""MonBudget v4 — nettoyer un vrai relevé bancaire avec pandas.

En v3, le carnet était saisi à la main, une dépense à la fois. Ici on reçoit
un relevé de 400 lignes exporté par la banque : dates en trois formats,
montants en texte, catégories mal orthographiées, doublons. C'est la réalité.

Chaque étape est une petite fonction : on peut la tester seule, et on voit
combien de lignes elle nettoie.
"""

from pathlib import Path

import pandas as pd

DOSSIER_DATA = Path(__file__).resolve().parents[2] / "data"
BRUT = DOSSIER_DATA / "releve_brut.csv"
PROPRE = DOSSIER_DATA / "releve_propre.csv"

SEUIL_ABERRANT = 5000.0     # au-delà, c'est une erreur de saisie


def charger_brut(chemin: Path = BRUT) -> pd.DataFrame:
    """Lit le CSV tel quel. Tout arrive en texte : c'est normal, et voulu.

    `sep=";"` est OBLIGATOIRE ici : les exports bancaires français utilisent
    le point-virgule. Sans lui, pandas lève ici une `ParserError` dont le
    message ne parle pas de séparateur — et sur un fichier sans virgules,
    il ne dirait rien du tout et rendrait une seule colonne géante. On
    n'écrit jamais `read_csv` sans expliciter au moins le séparateur et
    l'encodage.
    """
    return pd.read_csv(chemin, sep=";", encoding="utf-8")


def nettoyer_dates(df: pd.DataFrame) -> pd.DataFrame:
    """Convertit `date_operation` en vraies dates, malgré trois formats.

    PIÈGE MAJEUR : `pd.to_datetime(s, format="mixed", dayfirst=True)` a l'air
    de marcher, mais il applique `dayfirst` AUSSI aux dates ISO et inverse
    jour et mois : « 2026-04-09 » (9 avril) devient le 4 septembre. Sur ce
    relevé, cela corrompt 16 lignes **sans lever la moindre erreur**.

    La méthode sûre : normaliser les séparateurs, puis essayer les formats
    EXPLICITES l'un après l'autre.
    """
    texte = df["date_operation"].str.strip().str.replace("/", "-", regex=False)
    iso = pd.to_datetime(texte, format="%Y-%m-%d", errors="coerce")
    fr = pd.to_datetime(texte, format="%d-%m-%Y", errors="coerce")
    return df.assign(date_operation=iso.fillna(fr))


def nettoyer_montants(df: pd.DataFrame) -> pd.DataFrame:
    """Convertit `montant` (du texte) en nombres.

    À traiter : « 1 234,56 », « 57,76 », « 121.32 », « 34,10 EUR », « N/A ».
    `errors="coerce"` transforme l'illisible en NaN plutôt que de planter.
    """
    texte = (
        df["montant"].str.strip()
        .str.replace("EUR", "", regex=False)
        .str.replace("\u202f", "", regex=False)   # espace fine insécable
        .str.replace(" ", "", regex=False)        # séparateur de milliers
        .str.replace(",", ".", regex=False)       # virgule décimale -> point
    )
    return df.assign(montant=pd.to_numeric(texte, errors="coerce"))


def nettoyer_textes(df: pd.DataFrame) -> pd.DataFrame:
    """Harmonise libellés et catégories : espaces, casse, valeurs vides."""
    categorie = (
        df["categorie"].fillna("").str.strip().str.title().replace("", "Autre")
    )
    return df.assign(
        libelle=df["libelle"].str.strip().str.title(),
        note=df["note"].fillna(""),
        categorie=categorie,
        moyen_paiement=df["moyen_paiement"].str.strip().str.upper()
                        .replace({"CARTE": "CB", "VIR": "VIREMENT"}),
    )


def supprimer_doublons(df: pd.DataFrame) -> pd.DataFrame:
    """Une même opération saisie deux fois par la banque."""
    return df.drop_duplicates()


def retirer_inexploitables(df: pd.DataFrame) -> pd.DataFrame:
    """Écarte ce qu'on ne peut pas analyser : date ou montant manquant.

    `subset=` est ESSENTIEL. Un `dropna()` nu supprimerait toutes les lignes
    dont la colonne `note` est vide — c'est-à-dire 8 sur 10. On ne jette que
    sur les colonnes qui rendent la ligne réellement inutilisable.
    """
    return df.dropna(subset=["date_operation", "montant"])


def retirer_aberrants(df: pd.DataFrame, seuil: float = SEUIL_ABERRANT) -> pd.DataFrame:
    """Écarte les montants hors de toute plausibilité (erreurs de saisie)."""
    return df[df["montant"].abs() < seuil]


def separer_remboursements(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Un montant négatif est un remboursement : ce n'est pas une dépense.

    On ne le jette pas — on le met de côté. Mélanger les deux fausserait
    tous les totaux.
    """
    depenses = df[df["montant"] > 0]
    remboursements = df[df["montant"] < 0]
    return depenses, remboursements


def enrichir(df: pd.DataFrame) -> pd.DataFrame:
    """Ajoute les colonnes dérivées utiles à l'analyse."""
    return df.assign(
        mois=df["date_operation"].dt.to_period("M").astype(str),
        jour_semaine=df["date_operation"].dt.day_name(),
    )


def nettoyer(df: pd.DataFrame, bavard: bool = True) -> pd.DataFrame:
    """Le pipeline complet. Chaque étape annonce ce qu'elle a retiré."""
    etapes = [
        ("dates converties", nettoyer_dates),
        ("montants convertis", nettoyer_montants),
        ("textes harmonises", nettoyer_textes),
        ("doublons supprimes", supprimer_doublons),
        ("lignes inexploitables retirees", retirer_inexploitables),
        ("montants aberrants retires", retirer_aberrants),
    ]
    for nom, etape in etapes:
        avant = len(df)
        df = etape(df)
        if bavard:
            perdu = avant - len(df)
            detail = f"  (-{perdu} lignes)" if perdu else ""
            print(f"  {nom:32}{len(df):>5} lignes{detail}")
    return enrichir(df)


def sauver_propre(df: pd.DataFrame, chemin: Path = PROPRE) -> None:
    """Écrit le relevé nettoyé : l'entrée du tableau de bord de la séance 8."""
    df.to_csv(chemin, index=False, encoding="utf-8")


if __name__ == "__main__":
    brut = charger_brut()
    print(f"Releve brut : {len(brut)} lignes\n")
    propre = nettoyer(brut)
    depenses, remboursements = separer_remboursements(propre)
    print(f"\n{len(depenses)} depenses, {len(remboursements)} remboursements")
    sauver_propre(depenses)
    print(f"Ecrit dans {PROPRE.name}")
