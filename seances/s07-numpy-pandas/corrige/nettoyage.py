"""Corrigé de la séance 7 — pipeline de nettoyage (pandas 3.0).

Lancer depuis la racine du dépôt :
    python seances/s07-numpy-pandas/corrige/nettoyage.py

RÈGLE D'OR pandas 3.0 : une opération rend une NOUVELLE table.
Si tu veux garder le résultat, réaffecte.
"""

from pathlib import Path

import pandas as pd

RACINE = Path(__file__).resolve().parents[3]
ENTREE = RACINE / "data" / "opportunites_brutes.csv"
SORTIE = RACINE / "seances" / "s07-numpy-pandas" / "opportunites_propres.csv"


def nettoyer(df: pd.DataFrame) -> pd.DataFrame:
    depart = len(df)

    # --- 3) TEXTES ---------------------------------------------------------
    # .str applique une méthode de texte à TOUTE la colonne d'un coup :
    # c'est la vectorisation de la séance, appliquée aux chaînes.
    df = df.assign(
        pays=df["pays"].str.strip().str.title(),  # " maroc " -> "Maroc"
        titre=df["titre"].str.strip(),
        organisme=df["organisme"].str.strip(),
    )

    # --- 4) DATES ----------------------------------------------------------
    # format="mixed" : pandas détecte le format ligne par ligne.
    # errors="coerce" : l'irrécupérable devient NaT au lieu de tout faire planter.
    df = df.assign(
        deadline=pd.to_datetime(df["deadline"], format="mixed", dayfirst=True, errors="coerce")
    )
    print(f"{df['deadline'].isna().sum()} dates illisibles")  # on TRACE ce qu'on perd

    # --- 5) MONTANTS -------------------------------------------------------
    montants = (
        df["montant"]
        .astype("string")
        .str.replace(r"[^\d,.]", "", regex=True)  # ne garde que les chiffres
        .str.replace(",", ".", regex=False)  # virgule décimale -> point
        .replace("", None)
    )
    df = df.assign(montant=pd.to_numeric(montants, errors="coerce"))

    # --- 6) DOUBLONS -------------------------------------------------------
    avant = len(df)
    df = df.drop_duplicates(subset=["titre", "organisme"], keep="first")
    print(f"{avant - len(df)} doublons supprimés")

    # --- 7) LIGNES INEXPLOITABLES -----------------------------------------
    # On ne supprime QUE ce qui rend la ligne inutilisable. Supprimer toute ligne
    # ayant une valeur manquante quelque part est presque toujours une erreur.
    avant = len(df)
    df = df.dropna(subset=["titre", "deadline"])
    print(f"{avant - len(df)} lignes inexploitables supprimées")

    # --- 8) COLONNES CALCULÉES --------------------------------------------
    aujourd_hui = pd.Timestamp.today().normalize()
    df = df.assign(jours_restants=(df["deadline"] - aujourd_hui).dt.days)
    df = df.assign(
        # ⚠ & et non "and" : on combine deux COLONNES de booléens.
        # Les parenthèses sont obligatoires (priorité des opérateurs).
        urgente=(df["jours_restants"] >= 0) & (df["jours_restants"] < 7)
    )

    # --- BONUS : normalisation des statuts ---------------------------------
    correspondances = {
        "a faire": "a_faire",
        "à faire": "a_faire",
        "a_faire": "a_faire",
        "en cours": "en_cours",
        "en_cours": "en_cours",
        "envoyee": "envoyee",
        "envoyée": "envoyee",
        "archivee": "archivee",
        "archivée": "archivee",
    }
    df = df.assign(
        statut=df["statut"].str.strip().str.lower().map(correspondances).fillna("a_faire")
    )

    # --- BONUS : colonne parasite entièrement vide -------------------------
    df = df.drop(columns=[c for c in df.columns if df[c].isna().all()])

    print(f"\n{len(df)} lignes propres sur {depart} au départ")
    return df


def main() -> None:
    df = pd.read_csv(ENTREE, encoding="utf-8")

    # LE RITUEL DES 5 COMMANDES devant tout jeu de données inconnu
    print(df.shape)
    print(df.head())
    df.info()
    print(df["pays"].value_counts())

    df = nettoyer(df)
    df.to_csv(SORTIE, index=False, encoding="utf-8")
    print(f"Écrit : {SORTIE}")


if __name__ == "__main__":
    main()
