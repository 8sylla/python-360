"""Génère le relevé bancaire SALE de la séance 7 (fil rouge MonBudget).

Le fichier produit, `releve_brut.csv`, est volontairement imparfait : c'est
tout son intérêt pédagogique. Chaque défaut injecté ci-dessous correspond à
une étape du nettoyage de la séance.

Le fichier est ecrit avec un separateur POINT-VIRGULE : c'est la realite
des exports bancaires francais, et cela oblige a expliciter `sep=";"`
dans read_csv.

Lancer :  python data/generer_releve.py
Le tirage est reproductible (graine fixe) : le même fichier à chaque fois.
"""

import csv
import random
from pathlib import Path

GRAINE = 360
N_LIGNES = 400
SORTIE = Path(__file__).parent / "releve_brut.csv"

# Un commerçant -> sa catégorie « propre ». On salira l'écriture ensuite.
COMMERCANTS = [
    ("Carrefour Market", "Alimentation"),
    ("Boulangerie Paul", "Alimentation"),
    ("Lidl", "Alimentation"),
    ("Marjane", "Alimentation"),
    ("Pass Navigo", "Transport"),
    ("Total Energies", "Transport"),
    ("Uber", "Transport"),
    ("SNCF Connect", "Transport"),
    ("Loyer Appartement", "Logement"),
    ("EDF", "Logement"),
    ("Assurance Habitation", "Logement"),
    ("Orange Fibre", "Logement"),
    ("Netflix", "Loisirs"),
    ("Spotify", "Loisirs"),
    ("Cinema Pathe", "Loisirs"),
    ("Fnac", "Loisirs"),
    ("Pharmacie Centrale", "Sante"),
    ("Dr Diallo", "Sante"),
    ("Mutuelle", "Sante"),
]

MOYENS = ["CB", "CB", "CB", "carte", "CARTE", "virement", "VIR", "prelevement"]

# Champ libre, vide 8 fois sur 10 : sert a montrer qu'on ne fait JAMAIS
# dropna() sans subset (sinon on jetterait 80 % du releve).
NOTES = ["", "", "", "", "", "", "", "", "a verifier", "cadeau", "pro", "urgent"]


def salir_categorie(cat: str, rng: random.Random) -> str:
    """Défaut 1 : casse et espaces incohérents, parfois vide."""
    tirage = rng.random()
    if tirage < 0.08:
        return ""  # manquante
    if tirage < 0.20:
        return cat.upper()
    if tirage < 0.32:
        return cat.lower()
    if tirage < 0.40:
        return f"  {cat} "  # espaces parasites
    return cat


def salir_date(jour: int, mois: int, rng: random.Random) -> str:
    """Défaut 2 : trois formats de date mélangés, parfois vide."""
    tirage = rng.random()
    if tirage < 0.04:
        return ""  # date manquante
    if tirage < 0.35:
        return f"2026-{mois:02d}-{jour:02d}"  # ISO
    if tirage < 0.70:
        return f"{jour:02d}/{mois:02d}/2026"  # français
    return f"{jour:02d}-{mois:02d}-2026"  # tirets


def salir_montant(valeur: float, rng: random.Random) -> str:
    """Défaut 3 : montants en texte, virgule décimale, espaces, devise, N/A."""
    tirage = rng.random()
    if tirage < 0.03:
        return "N/A"  # illisible
    if tirage < 0.05:
        return ""  # manquant
    if tirage < 0.20:
        return f"{valeur:.2f}".replace(".", ",")  # virgule décimale
    if tirage < 0.30:
        return f"{valeur:,.2f}".replace(",", " ").replace(".", ",") + " EUR"
    return f"{valeur:.2f}"


def main() -> None:
    rng = random.Random(GRAINE)
    lignes = []

    for _ in range(N_LIGNES):
        commercant, categorie = rng.choice(COMMERCANTS)
        mois = rng.randint(1, 6)
        jour = rng.randint(1, 28)

        # Un montant plausible selon la catégorie.
        if categorie == "Logement":
            valeur = rng.uniform(300, 900)
        elif categorie == "Sante":
            valeur = rng.uniform(10, 120)
        else:
            valeur = rng.uniform(2, 150)

        # Défaut 4 : quelques remboursements (montants négatifs).
        if rng.random() < 0.04:
            valeur = -valeur

        # Défaut 5 : de rares valeurs aberrantes (erreur de saisie).
        if rng.random() < 0.015:
            valeur = valeur * 1000

        # Défaut 6 : libellé à la casse/espacement incohérents.
        libelle = commercant
        t = rng.random()
        if t < 0.12:
            libelle = commercant.upper()
        elif t < 0.20:
            libelle = f" {commercant}  "

        lignes.append(
            {
                "date_operation": salir_date(jour, mois, rng),
                "libelle": libelle,
                "categorie": salir_categorie(categorie, rng),
                "montant": salir_montant(valeur, rng),
                "moyen_paiement": rng.choice(MOYENS),
                "note": rng.choice(NOTES),
            }
        )

    # Défaut 7 : des doublons exacts (double saisie bancaire).
    for _ in range(18):
        lignes.append(dict(rng.choice(lignes)))

    rng.shuffle(lignes)

    with SORTIE.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "date_operation",
                "libelle",
                "categorie",
                "montant",
                "moyen_paiement",
                "note",
            ],
            delimiter=";",
        )
        writer.writeheader()
        writer.writerows(lignes)

    print(f"{len(lignes)} lignes ecrites dans {SORTIE.name}")


if __name__ == "__main__":
    main()
