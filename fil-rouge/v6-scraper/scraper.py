"""OpportuniTrack v6 — scraper d'entraînement (séance 9).

⚠ LES 5 RÈGLES
    1. API d'abord, scraping seulement si nécessaire.
    2. Lire robots.txt et les CGU AVANT d'écrire la première ligne.
    3. Un délai entre chaque requête.
    4. Aucune donnée personnelle.
    5. S'identifier honnêtement dans le User-Agent.

On s'entraîne sur books.toscrape.com, un site CONÇU pour ça.
Jamais sur un site réel en séance.
"""

import time

import pandas as pd
import requests
from bs4 import BeautifulSoup

BASE = "https://books.toscrape.com/catalogue/page-{}.html"

# Un User-Agent honnête : je dis qui je suis et pourquoi je passe.
EN_TETES = {"User-Agent": "FormationPython/1.0 (exercice pedagogique)"}

DELAI = 1.0  # secondes entre deux requêtes. Non négociable.


def recuperer_page(numero: int) -> str | None:
    """Télécharge une page et rend son HTML, ou None si elle n'existe pas."""
    reponse = requests.get(BASE.format(numero), headers=EN_TETES, timeout=10)
    # timeout : sans lui, un serveur silencieux fige le script pour toujours.

    if reponse.status_code == 404:
        return None  # fin de la pagination : notre condition d'arrêt
    reponse.raise_for_status()  # lève une exception sur 403, 500, etc.

    reponse.encoding = reponse.apparent_encoding  # évite les accents cassés
    return reponse.text


def extraire_livres(html: str) -> list[dict]:
    """Transforme le HTML d'une page en liste de dictionnaires."""
    soup = BeautifulSoup(html, "html.parser")  # toujours préciser le parseur
    livres = []

    for fiche in soup.select("article.product_pod"):
        lien = fiche.select_one("h3 a")
        prix = fiche.select_one("p.price_color")
        note = fiche.select_one("p.star-rating")

        livres.append(
            {
                # On vérifie SYSTÉMATIQUEMENT l'existence avant d'accéder : une seule
                # fiche mal formée ne doit pas faire tomber tout le scraper.
                "titre": lien["title"] if lien else None,
                "prix": prix.text.strip() if prix else None,
                # Les classes sont ["star-rating", "Three"] : la note est la 2e.
                "note": note["class"][1] if note and len(note["class"]) > 1 else None,
                "url": lien["href"] if lien else None,
            }
        )

    return livres


def scraper(max_pages: int = 5) -> pd.DataFrame:
    """Parcourt les pages jusqu'à la limite ou jusqu'à la fin du catalogue."""
    tout = []

    for numero in range(1, max_pages + 1):
        print(f"Page {numero}...", end=" ")
        html = recuperer_page(numero)

        if html is None:
            print("(fin du catalogue)")
            break

        lot = extraire_livres(html)
        tout.extend(lot)
        print(f"{len(lot)} éléments")

        time.sleep(DELAI)  # ⚠ LA ligne qui fait la différence entre un outil
        # et une nuisance. Ne jamais la retirer.

    return pd.DataFrame(tout)


if __name__ == "__main__":
    df = scraper(max_pages=5)

    # Nettoyage avec les outils de la séance 7 : la boucle est bouclée.
    df = df.assign(
        prix_num=pd.to_numeric(
            df["prix"].str.replace(r"[^\d.]", "", regex=True),
            errors="coerce",
        )
    )

    df.to_csv("catalogue.csv", index=False, encoding="utf-8")
    print(f"\n{len(df)} lignes exportées vers catalogue.csv")
