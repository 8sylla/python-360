"""Génère `opportunites_brutes.csv` — un jeu de données VOLONTAIREMENT sale.

Chaque défaut injecté ici correspond à une étape du corrigé de la séance 7.
Le générateur est déterministe (`random.seed(2026)`) : tout le monde travaille
sur exactement le même fichier, donc les corrigés tombent juste pour tous.

Usage :
    python data/generer_donnees_sales.py            # 300 lignes (défaut)
    python data/generer_donnees_sales.py --lignes 500 --sortie autre.csv

DÉFAUTS INJECTÉS (et l'étape du corrigé qui les traite)
-------------------------------------------------------
1. Casse et espaces incohérents sur `pays`, `titre`, `organisme` .... étape 3
2. Trois formats de date mélangés + dates vides ou aberrantes ........ étape 4
3. Montants en texte : "1 500 €", "12.000 MAD", "N/A", "" ............ étape 5
4. Doublons exacts et quasi-doublons ................................. étape 6
5. Titres ou deadlines manquants (lignes inexploitables) ............. étape 7
6. Statuts écrits de plusieurs façons ................................ bonus
7. Une colonne parasite entièrement vide ............................. bonus

AUCUNE DONNÉE PERSONNELLE : organismes et intitulés sont fictifs ou
institutionnels. C'est volontaire — cf. le bloc éthique de la séance 9.
"""

import argparse
import csv
import random
from datetime import date, timedelta

random.seed(2026)  # déterministe : même fichier pour tout le groupe

PAYS_PROPRES = [
    "Maroc",
    "France",
    "Sénégal",
    "Côte d'Ivoire",
    "Tunisie",
    "Canada",
    "Allemagne",
    "Bénin",
    "Cameroun",
    "Rwanda",
]

# Variantes sales : casse, espaces, accents manquants
VARIANTES_PAYS = {
    "Maroc": ["Maroc", "maroc", "MAROC", " Maroc ", "  maroc"],
    "France": ["France", "france", "FRANCE", " France"],
    "Sénégal": ["Sénégal", "senegal", "SENEGAL", " Sénégal "],
    "Côte d'Ivoire": ["Côte d'Ivoire", "cote d'ivoire", "COTE D IVOIRE"],
    "Tunisie": ["Tunisie", "tunisie", " TUNISIE "],
    "Canada": ["Canada", "canada", "CANADA "],
    "Allemagne": ["Allemagne", "allemagne", " Allemagne"],
    "Bénin": ["Bénin", "benin", "BENIN"],
    "Cameroun": ["Cameroun", "cameroun", " Cameroun "],
    "Rwanda": ["Rwanda", "rwanda", "RWANDA"],
}

TYPES = [
    "Bourse",
    "Stage",
    "Programme",
    "Appel à candidatures",
    "Hackathon",
    "Concours",
    "Résidence",
    "Formation",
    "Fellowship",
    "Subvention",
]

DOMAINES = [
    "Intelligence artificielle",
    "Énergies renouvelables",
    "Santé publique",
    "Agritech",
    "Fintech",
    "Data science",
    "Cybersécurité",
    "Mobilité urbaine",
    "Éducation numérique",
    "Économie circulaire",
    "Génie logiciel",
    "Climat",
    "Entrepreneuriat social",
    "Robotique",
    "Biotechnologies",
]

ORGANISMES = [
    "Université Paris Cité",
    "Fondation Mastercard",
    "Banque Islamique de Développement",
    "Union Africaine",
    "Commission Européenne",
    "Agence Française de Développement",
    "Campus France",
    "OCP Group",
    "Orange Digital Center",
    "GIZ",
    "Banque Mondiale",
    "PNUD",
    "Institut Pasteur",
    "CNRS",
    "Erasmus Mundus",
    "African Development Bank",
    "Mozilla Foundation",
    "UNESCO",
]

NIVEAUX = ["Licence", "Master", "Doctorat", "Post-doc", "Tous niveaux"]

STATUTS_SALES = [
    "a_faire",
    "A_FAIRE",
    "à faire",
    "a faire",
    "en_cours",
    "EN COURS",
    "en cours",
    "envoyee",
    "envoyée",
    "ENVOYEE",
    "archivee",
    "archivée",
    "",
]

MONNAIES = ["€", "EUR", "MAD", "USD", "$"]


def date_sale(reference: date) -> str:
    """Rend une date dans l'un des trois formats — ou une valeur inexploitable."""
    tirage = random.random()

    if tirage < 0.04:
        return ""  # date vide
    if tirage < 0.06:
        return random.choice(["à confirmer", "bientôt", "N/A", "31/02/2027"])

    formats = [
        reference.strftime("%d/%m/%Y"),  # français
        reference.strftime("%Y-%m-%d"),  # ISO
        reference.strftime("%d-%m-%Y"),  # tirets
    ]
    return random.choice(formats)


def montant_sale() -> str:
    """Rend un montant sous forme de texte, comme dans la vraie vie."""
    tirage = random.random()

    if tirage < 0.18:
        return random.choice(["", "N/A", "non précisé", "-"])

    valeur = random.choice([500, 1200, 1500, 3000, 5000, 8000, 12000, 25000])
    monnaie = random.choice(MONNAIES)

    style = random.random()
    if style < 0.35:
        return f"{valeur:,} {monnaie}".replace(",", " ")  # "12 000 MAD"
    if style < 0.6:
        return f"{monnaie}{valeur}"  # "€1500"
    if style < 0.8:
        return f"{valeur},00 {monnaie}"  # virgule décimale
    return f"{valeur} {monnaie}"


def salir_texte(texte: str) -> str:
    """Ajoute des espaces parasites ou modifie la casse, parfois."""
    tirage = random.random()
    if tirage < 0.12:
        return f"  {texte} "
    if tirage < 0.18:
        return texte.upper()
    if tirage < 0.22:
        return texte.lower()
    return texte


def generer_ligne(aujourd_hui: date) -> dict:
    pays_propre = random.choice(PAYS_PROPRES)
    decalage = random.randint(-30, 180)  # certaines deadlines sont passées
    deadline = aujourd_hui + timedelta(days=decalage)

    titre = f"{random.choice(TYPES)} {random.choice(DOMAINES)}"

    return {
        "titre": salir_texte(titre),
        "organisme": salir_texte(random.choice(ORGANISMES)),
        "pays": random.choice(VARIANTES_PAYS[pays_propre]),
        "deadline": date_sale(deadline),
        "niveau": random.choice(NIVEAUX),
        "montant": montant_sale(),
        "statut": random.choice(STATUTS_SALES),
        "url": f"https://exemple-formation.test/opportunite/{random.randint(1000, 9999)}",
        "commentaire": "",  # colonne parasite : entièrement vide
    }


def generer(nb_lignes: int) -> list[dict]:
    aujourd_hui = date.today()
    lignes = [generer_ligne(aujourd_hui) for _ in range(int(nb_lignes * 0.88))]

    # --- Doublons exacts (7 %) ---------------------------------------------
    for _ in range(int(nb_lignes * 0.07)):
        lignes.append(dict(random.choice(lignes)))

    # --- Quasi-doublons : même titre + organisme, détails différents (5 %) --
    for _ in range(int(nb_lignes * 0.05)):
        source = dict(random.choice(lignes))
        source["montant"] = montant_sale()
        source["statut"] = random.choice(STATUTS_SALES)
        lignes.append(source)

    # --- Lignes inexploitables : titre ou deadline manquants ----------------
    for _ in range(6):
        ligne = generer_ligne(date.today())
        ligne[random.choice(["titre", "deadline"])] = ""
        lignes.append(ligne)

    random.shuffle(lignes)
    return lignes


def main() -> None:
    parseur = argparse.ArgumentParser(description=__doc__)
    parseur.add_argument("--lignes", type=int, default=300)
    parseur.add_argument("--sortie", default="opportunites_brutes.csv")
    arguments = parseur.parse_args()

    lignes = generer(arguments.lignes)
    colonnes = list(lignes[0].keys())

    with open(arguments.sortie, "w", encoding="utf-8", newline="") as fichier:
        redacteur = csv.DictWriter(fichier, fieldnames=colonnes)
        redacteur.writeheader()
        redacteur.writerows(lignes)

    print(f"✅ {len(lignes)} lignes écrites dans {arguments.sortie}")
    print("   Défauts injectés : casse, 3 formats de date, doublons,")
    print("   montants en texte, lignes inexploitables, colonne vide.")


if __name__ == "__main__":
    main()
