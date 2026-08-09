# Formation Python 360° — Guide du formateur
## ARC 2, seconde partie : Séances 9 à 11

**Aller chercher, exposer, livrer.** Les trois séances qui transforment un apprenant en praticien.

---

# Note de version — à lire avant de préparer les séances 10 et 11

| Outil | Version de référence (août 2026) | Point de vigilance |
|---|---|---|
| **FastAPI** | 0.136.x (0.136.1 publiée le 23 avril 2026) | **Le support de Pydantic v1 a été abandonné** ; le minimum est désormais `pydantic >= 2.7`. Les dépendances standard incluent `pydantic-settings` et `pydantic-extra-types`. Starlette est passé en 1.0 |
| **Pydantic** | 2.13.x | Ne jamais enseigner `.dict()`, `.json()`, `parse_obj()`, `@validator` : ce sont les API v1, dépréciées |
| **uv** | dernières versions de juillet 2026 | Remplace pip + virtualenv + pyenv + pipx + poetry |
| **Ruff** | mises à jour continues | Formateur **et** linter : remplace black + flake8 + isort |
| **BeautifulSoup** | bs4 4.13.x | Toujours préciser le parseur : `BeautifulSoup(html, "html.parser")` |
| **Requests / httpx** | requests 2.32.x, httpx 0.28.x | `requests` pour enseigner, `httpx` si l'async est abordé |

⚠️ **Piège de nommage à connaître avant la S10** : « Pydantic v2 » (la bibliothèque de validation, version 2.13) et « Pydantic AI v2 » (un produit distinct, pour les agents LLM) sont deux choses différentes. Un apprenant qui cherche « pydantic v2 » sur le web tombera sur les deux. Le signaler en une phrase évite une confusion coûteuse.

**Décision importante pour la S10** : le fait que FastAPI ait **supprimé** le support de Pydantic v1 simplifie beaucoup l'enseignement — il n'existe plus qu'une seule façon de faire. Mais cela rend **définitivement caducs** tous les tutoriels FastAPI antérieurs à 2024. Slide d'avertissement obligatoire.

---
---

# SÉANCE 9 — Aller chercher la donnée
### *HTTP, APIs publiques, web scraping, et l'éthique qui va avec*

> **Promesse** : « Jusqu'ici, quelqu'un t'a donné un CSV. Aujourd'hui, tu fabriques tes propres données. »

## Objectifs pédagogiques
1. **Expliquer** le cycle requête/réponse HTTP et **lire** un code de statut.
2. **Interroger** une API publique en JSON avec `requests` et exploiter la réponse.
3. **Justifier** la règle « API d'abord, scraping ensuite ».
4. **Extraire** des données d'une page HTML avec BeautifulSoup (sélecteurs CSS).
5. **Gérer** la pagination, les erreurs réseau et la politesse (délais, en-têtes, `robots.txt`).
6. **Énoncer** les limites légales et éthiques : conditions d'utilisation, données personnelles, charge serveur.
7. **Produire** un pipeline complet : scraping → nettoyage pandas → CSV.

## Déroulé minuté (180 min)

| Temps | Bloc | Modalité | Contenu |
|---|---|---|---|
| 0–15 | **Le web vu de l'intérieur** | Plénière + démo navigateur | Ouverture de l'onglet Réseau des outils de développement sur un site réel. Requête, réponse, statut, en-têtes. |
| 15–40 | **Théorie 1** : `requests` et les APIs | Live coding | `get`, `params`, `.status_code`, `.json()`, `raise_for_status()`, en-têtes. Une vraie API publique interrogée en direct. |
| 40–55 | **Pratique 1** | Individuel | Interroger une API ouverte et en tirer un DataFrame. |
| 55–75 | **Théorie 2** : anatomie d'une page HTML | Plénière + inspecteur | Balises, attributs, classes, sélecteurs CSS. Trouver le bon sélecteur avec l'inspecteur. |
| 75–85 | **PAUSE** | — | — |
| 85–110 | **Théorie 3** : BeautifulSoup | Live coding | `select`, `select_one`, `find_all`, extraction de texte et d'attributs, gestion de l'absence. |
| 110–125 | **Bloc éthique et légal** | Plénière — **non négociable** | `robots.txt`, CGU, données personnelles, charge serveur, jurisprudence. Cas pratiques à trancher en groupe. |
| 125–165 | **Pratique 2 — Fil rouge v6** | Binômes | Scraper multi-pages avec délai, robustesse et export. |
| 165–175 | **Ouverture** | Démo | Ce que `requests` ne peut pas faire : les pages générées en JavaScript. Démo Playwright de 5 minutes. |
| 175–180 | **Clôture** | Plénière | Teaser S10. |

## Concepts clés — expliqués simplement

**HTTP = la commande au restaurant.** Tu passes commande (la **requête**), la cuisine te répond (la **réponse**). La réponse contient un **code** qui dit comment ça s'est passé :
- **200** — voilà votre plat.
- **301 / 302** — le restaurant a déménagé, suivez l'adresse.
- **403** — vous n'êtes pas le bienvenu ici.
- **404** — ce plat n'existe pas à la carte.
- **429** — vous commandez trop vite, calmez-vous. *(Le code que tout scraper finit par rencontrer.)*
- **500** — la cuisine a pris feu ; ce n'est pas votre faute.

**La règle d'or, à énoncer avant toute autre chose : l'API d'abord.** Beaucoup de sites offrent une API officielle qui rend des données propres, stables et autorisées. Le scraping consiste à lire la vitrine faute de porte d'entrée : c'est fragile (le HTML change sans préavis), plus lent, et juridiquement plus sensible. **On ne scrape que ce qu'on ne peut pas obtenir autrement.**

**Le HTML = une poupée russe étiquetée.** Des boîtes dans des boîtes, chacune portant une étiquette (`<div>`, `<h2>`, `<a>`) et parfois un badge (`class="prix"`, `id="resultats"`). Le scraping consiste à dire « donne-moi le contenu de toutes les boîtes portant le badge *prix* ».

**Le sélecteur CSS, en cinq motifs qui couvrent 95 % des besoins :**

| Sélecteur | Signification |
|---|---|
| `h2` | toutes les balises `h2` |
| `.prix` | tous les éléments de classe `prix` |
| `#resultats` | l'élément d'identifiant `resultats` |
| `article .titre` | les éléments de classe `titre` **à l'intérieur** d'un `article` |
| `a[href]` | tous les liens qui **possèdent** un attribut `href` |

Insister sur la méthode plutôt que sur la syntaxe : **clic droit → Inspecter → clic droit sur l'élément → Copier le sélecteur**. Le navigateur écrit le sélecteur à ta place ; il faut ensuite le simplifier.

**La robustesse est le vrai sujet du scraping.** Un scraper qui marche une fois ne vaut rien ; ce qui compte, c'est celui qui survit à une page mal formée. Réflexe à installer :
```python
titre = element.select_one("h3 a")
titre = titre["title"] if titre else None   # jamais d'accès direct sans vérifier
```

### Bloc éthique et légal — le cœur de la séance

Ce bloc n'est pas un supplément moral : c'est une compétence professionnelle. Il se traite en plénière, avec des cas à trancher collectivement.

**Les quatre questions à se poser avant tout scraping :**

1. **Une API existe-t-elle ?** Si oui, la question est réglée.
2. **Que disent les conditions d'utilisation et le `robots.txt` ?** Le `robots.txt` (à l'adresse `site.com/robots.txt`) est une convention indiquant ce que le site souhaite voir automatisé. Il n'a pas force de loi en soi, mais **le violer sciemment aggrave systématiquement la position juridique**. Les CGU, elles, sont contractuelles.
3. **Y a-t-il des données personnelles ?** Noms, adresses, courriels, photos de personnes identifiables : on entre dans le champ du RGPD, et le fait qu'une donnée soit publiquement visible **ne la rend pas librement réutilisable**. Règle simple et sûre pour la formation : *on ne collecte aucune donnée personnelle*.
4. **Quelle charge est-ce que j'impose ?** Un script sans délai peut envoyer des milliers de requêtes par minute. Un scraping poli : un délai entre les requêtes, un `User-Agent` honnête, jamais en parallèle massif, et de préférence hors heures de pointe.

**Les cinq règles à afficher :**
1. API d'abord, scraping ensuite.
2. Lire `robots.txt` et les CGU **avant** d'écrire la première ligne.
3. Un délai entre chaque requête (1 seconde suffit à être respectueux).
4. Aucune donnée personnelle.
5. S'identifier honnêtement dans le `User-Agent` — se faire passer pour un navigateur pour contourner un blocage explicite, c'est franchir une ligne.

**Cas à débattre en groupe** (5 minutes, sans réponse imposée par le formateur) :
- Scraper les offres d'emploi publiques d'un site pour mon usage personnel de recherche d'emploi.
- Le même scraping, mais pour republier les offres sur mon propre site avec de la publicité.
- Scraper les profils publics d'un réseau social pour constituer une base de contacts.
- Collecter des prix de concurrents pour ajuster les miens.

L'objectif n'est pas de produire une doctrine juridique — préciser explicitement que le formateur n'est pas juriste et que le droit varie selon les pays — mais d'installer le **réflexe de se poser la question**.

## Plan des slides — Séance 9 (24 slides)

1. **Couverture** + 2. **Frise**.
2. **D'où viennent les données ?** — les quatre sources : fichier fourni, base de données, API, scraping.
3. **La commande au restaurant** — schéma requête/réponse.
4. **Les codes de statut qui comptent** — tableau avec les 6 codes et leur traduction en français courant.
5. **Démo : l'onglet Réseau** — capture annotée du navigateur.
6. **`requests` en 5 lignes** — le code minimal + `raise_for_status()`.
7. **Une API publique en direct** — la réponse JSON brute, puis le DataFrame obtenu.
8. **⚠️ La règle d'or** — pleine page : *« API d'abord. Scraping seulement si nécessaire. »*
9. **La poupée russe** — le HTML illustré en boîtes imbriquées.
10. **Les 5 sélecteurs CSS** — tableau à imprimer.
11. **Trouver le bon sélecteur** — les 3 clics dans l'inspecteur, capture par capture.
12. **BeautifulSoup en 4 gestes** — `select`, `select_one`, `.text`, `["href"]`.
13. **⚠️ Toujours vérifier l'absence** — le code fragile et le code robuste, côte à côte.
14. **La pagination** — schéma de la boucle sur les pages + le point d'arrêt.
15. **Le scraper poli** — délai, en-tête, session.
16. **`robots.txt`** — capture d'un vrai fichier, commenté.
17. **Les 4 questions avant de scraper** — pleine page.
18. **⚠️ Données personnelles et RGPD** — « public ≠ réutilisable librement ».
19. **Les 5 règles** — la slide à afficher au mur.
20. **Cas pratiques à trancher** — les 4 situations.
21. **Le pipeline complet** — schéma : site → scraper → liste de dicts → pandas → CSV → dashboard S8.
22. **Ce que `requests` ne voit pas** — page vide en HTML brut mais pleine dans le navigateur. Démo Playwright.
23. **Exercice : le fil rouge v6**.
24. **Bilan / teaser S10**.

## Exercice pratique / Fil rouge v6 — Le scraper

**Terrain d'entraînement** : utiliser un site **conçu pour l'apprentissage du scraping**, jamais un site réel en séance. Deux références stables :
- `https://books.toscrape.com` — catalogue paginé, structure propre.
- `https://quotes.toscrape.com` — variantes avec JavaScript, connexion, défilement infini.

C'est aussi une leçon en soi : **on s'entraîne sur un terrain prévu pour ça**.

### Corrigé commenté

```python
"""Scraper d'entraînement — catalogue paginé vers CSV."""

import time

import pandas as pd
import requests
from bs4 import BeautifulSoup

BASE = "https://books.toscrape.com/catalogue/page-{}.html"

# Un User-Agent honnête : je dis qui je suis et pourquoi je passe.
EN_TETES = {
    "User-Agent": "FormationPython/1.0 (exercice pedagogique)"
}

DELAI = 1.0   # secondes entre deux requêtes. Non négociable.


def recuperer_page(numero: int) -> str | None:
    """Télécharge une page et rend son HTML, ou None si elle n'existe pas."""
    reponse = requests.get(BASE.format(numero), headers=EN_TETES, timeout=10)
    # timeout : sans lui, un serveur silencieux fige le script pour toujours.

    if reponse.status_code == 404:
        return None          # fin de la pagination : c'est notre condition d'arrêt
    reponse.raise_for_status()   # lève une exception sur toute autre erreur (403, 500...)

    reponse.encoding = reponse.apparent_encoding   # évite les accents cassés
    return reponse.text


def extraire_livres(html: str) -> list[dict]:
    """Transforme le HTML d'une page en liste de dictionnaires."""
    soup = BeautifulSoup(html, "html.parser")   # toujours préciser le parseur
    livres = []

    # Chaque fiche est un <article class="product_pod">.
    for fiche in soup.select("article.product_pod"):
        lien = fiche.select_one("h3 a")
        prix = fiche.select_one("p.price_color")
        note = fiche.select_one("p.star-rating")

        livres.append({
            # On vérifie SYSTÉMATIQUEMENT l'existence avant d'accéder :
            # une seule fiche mal formée ne doit pas faire tomber tout le scraper.
            "titre": lien["title"] if lien else None,
            "prix": prix.text.strip() if prix else None,
            # Les classes sont ["star-rating", "Three"] : la note est la 2e.
            "note": note["class"][1] if note and len(note["class"]) > 1 else None,
            "url": lien["href"] if lien else None,
        })

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

        time.sleep(DELAI)   # ⚠️ LA ligne qui fait la différence entre
                            # un outil et une nuisance. Ne jamais la retirer.

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
    print(f"\n✅ {len(df)} lignes exportées vers catalogue.csv")
```

**Les quatre points à marteler :**
1. **`time.sleep()` n'est pas optionnel.** Le retirer transforme un exercice en attaque par déni de service involontaire.
2. **`timeout=10`** : sans lui, le script peut se bloquer indéfiniment.
3. **Vérifier avant d'accéder** : `lien["title"] if lien else None`, systématiquement.
4. **Le scraper ne nettoie pas.** Il collecte, point. Le nettoyage est l'affaire de pandas — séparer les responsabilités, exactement comme en S5.

### Palier bonus
1. Réutiliser le décorateur `@reessayer` de la S6 sur `recuperer_page` pour absorber les erreurs réseau passagères.
2. Utiliser une `requests.Session()` : connexion réutilisée, donc plus rapide et plus léger pour le serveur.
3. Suivre les liens de détail de chaque fiche pour enrichir les données (scraping à deux niveaux).
4. Lire et respecter programmatiquement `robots.txt` avec `urllib.robotparser`.
5. Réécrire le scraper en asynchrone avec `httpx` + `asyncio`, avec un `Semaphore` limitant la concurrence — et **discuter** du fait qu'aller plus vite n'est pas toujours souhaitable.

## Ressources — Séance 9
| Ressource | Lien | Note |
|---|---|---|
| Requests — doc officielle | https://requests.readthedocs.io/ | Commencer par « Quickstart » |
| BeautifulSoup — doc officielle | https://www.crummy.com/software/BeautifulSoup/bs4/doc/ | Existe aussi en français sur le même site |
| MDN — Introduction au HTML | https://developer.mozilla.org/fr/docs/Learn/HTML/Introduction_to_HTML | Pour les apprenants sans culture web |
| MDN — Sélecteurs CSS | https://developer.mozilla.org/fr/docs/Web/CSS/CSS_Selectors | La référence |
| MDN — Codes de statut HTTP | https://developer.mozilla.org/fr/docs/Web/HTTP/Status | — |
| Real Python — Web Scraping with BeautifulSoup | https://realpython.com/beautiful-soup-web-scraper-python/ | Utilise un site d'entraînement dédié |
| Terrain d'entraînement — Books to Scrape | https://books.toscrape.com | Conçu pour l'exercice |
| Terrain d'entraînement — Quotes to Scrape | https://quotes.toscrape.com | Variantes JS, connexion, défilement |
| httpx | https://www.python-httpx.org/ | Le successeur async-compatible de requests |
| Playwright for Python | https://playwright.dev/python/ | Pour les pages générées en JavaScript |
| Scrapy | https://docs.scrapy.org/ | À mentionner : le framework pour le scraping à grande échelle |
| `urllib.robotparser` | https://docs.python.org/fr/3/library/urllib.robotparser.html | Lire `robots.txt` par le code |
| Public APIs (annuaire) | https://github.com/public-apis/public-apis | Pour trouver une API plutôt que de scraper |

---
---

# SÉANCE 10 — Exposer : API REST avec FastAPI et Pydantic v2
### *Du script au service*

> **Promesse** : « Ton programme ne servira plus qu'à toi. À la fin de la séance, n'importe qui pourra l'utiliser depuis n'importe où. »

## Objectifs pédagogiques
1. **Expliquer** ce qu'est une API REST et à quoi correspondent GET, POST, PUT, DELETE.
2. **Créer** une application FastAPI et la lancer avec le rechargement automatique.
3. **Définir** des schémas **Pydantic v2** avec `Field`, `field_validator` et `computed_field`.
4. **Distinguer** modèle d'entrée et modèle de sortie, et **justifier** cette séparation.
5. **Gérer** les erreurs avec `HTTPException` et les bons codes de statut.
6. **Utiliser** l'injection de dépendances et organiser le code en `APIRouter`.
7. **Exploiter** la documentation interactive générée automatiquement.
8. **Écrire** un test d'API avec `TestClient`.

## Déroulé minuté (180 min)

| Temps | Bloc | Modalité | Contenu |
|---|---|---|---|
| 0–15 | **Le problème** | Plénière | « Comment ton collègue utilise-t-il ton tracker ? » Les mauvaises réponses (envoyer le fichier, partager l'écran) mènent à la bonne. |
| 15–35 | **Théorie 1** : REST et JSON | Plénière | Ressource, URL, verbes, codes de retour. Le parallèle avec le CRUD déjà écrit en S5. |
| 35–55 | **Théorie 2** : première API | Live coding | `FastAPI()`, `@app.get`, lancement, `/docs`. **Le moment « waouh » de la formation.** |
| 55–70 | **Pratique 1** | Individuel | Trois routes en lecture sur le carnet existant. |
| 70–80 | **PAUSE** | — | — |
| 80–110 | **Théorie 3** : Pydantic v2 | Live coding | `BaseModel`, types, `Field`, validation automatique, messages d'erreur, `field_validator`, `computed_field`. |
| 110–130 | **Théorie 4** : écrire, gérer les erreurs, structurer | Live coding | POST/PUT/DELETE, `status_code`, `HTTPException`, `response_model`, `APIRouter`, `Depends`. |
| 130–165 | **Pratique 2 — Fil rouge v7** | Binômes | L'API complète d'OpportuniTrack. |
| 165–175 | **Tests d'API** | Guidé | `TestClient` : deux tests qui passent. |
| 175–180 | **Clôture** | Plénière | Teaser S11 + consignes du Demo Day. |

## Concepts clés — expliqués simplement

**L'API = le passe-plat du restaurant.** La cuisine (ta logique) et la salle (l'application qui consomme) ne se voient pas. Le passe-plat définit ce qui peut être demandé et sous quelle forme. Personne n'entre dans la cuisine.

**REST en une phrase** : chaque **chose** (une opportunité) a une **adresse** (`/opportunites/12`), et on agit dessus avec un **verbe** :

| Verbe | Adresse | Sens | Équivalent S5 |
|---|---|---|---|
| GET | `/opportunites` | lister | `carnet.toutes()` |
| GET | `/opportunites/12` | consulter | `carnet[12]` |
| POST | `/opportunites` | créer | `carnet.ajouter(...)` |
| PUT | `/opportunites/12` | remplacer | modification |
| DELETE | `/opportunites/12` | supprimer | `carnet.supprimer(12)` |

**Argument pédagogique décisif** : le tableau de droite existe déjà, écrit en séance 5. **L'API n'ajoute pas de logique, elle ajoute une porte d'entrée.** C'est ce qui rend la séance abordable même pour les profils non techniques.

**Pydantic = le videur à l'entrée.** Il contrôle chaque donnée qui entre : le bon type, les champs obligatoires présents, les valeurs dans les bornes. Si ça ne passe pas, il refuse **avant** que ton code ne s'exécute, avec un message précis indiquant quel champ pose problème. Tu n'écris plus jamais de `if not isinstance(...)`.

**FastAPI = Pydantic + les routes + la documentation, gratuitement.** L'argument qui emporte l'adhésion : **on écrit les types, et on obtient la validation, la sérialisation JSON et une documentation interactive testable.** Ouvrir `/docs` en direct et cliquer sur « Try it out » produit systématiquement une réaction dans la salle. Ne pas rater ce moment : il justifie à lui seul la séance.

**⚠️ Pydantic v2, la syntaxe à enseigner — et celle à bannir.** FastAPI a supprimé le support de Pydantic v1 ; tout tutoriel montrant la colonne de gauche est périmé :

| ❌ Pydantic v1 (obsolète) | ✅ Pydantic v2 |
|---|---|
| `@validator("champ")` | `@field_validator("champ")` |
| `model.dict()` | `model.model_dump()` |
| `model.json()` | `model.model_dump_json()` |
| `Model.parse_obj(d)` | `Model.model_validate(d)` |
| `class Config:` | `model_config = ConfigDict(...)` |
| `Optional[str] = None` | `str | None = None` |

**Modèle d'entrée ≠ modèle de sortie.** Une des rares idées d'architecture à faire passer ici. Ce que le client **envoie** (`OpportuniteCreation`) n'est pas ce que le serveur **rend** (`OpportuniteLecture`) : l'entrée ne contient pas d'identifiant (c'est le serveur qui l'attribue), la sortie contient des champs calculés. Confondre les deux, c'est laisser un client imposer un identifiant ou lire un champ interne.

## Plan des slides — Séance 10 (24 slides)

1. **Couverture** + 2. **Frise**.
2. **Le problème** — « comment ton collègue utilise-t-il ton programme ? », les 3 mauvaises réponses barrées.
3. **Le passe-plat** — schéma cuisine / passe-plat / salle.
4. **Une ressource, une adresse, un verbe** — le tableau REST.
5. **Vous l'avez déjà écrit** — colonne S5 en face de colonne REST. Slide clé.
6. **JSON = le dictionnaire Python, en texte** — les deux côte à côte, quasi identiques.
7. **Les codes de retour à connaître** — 200, 201, 204, 400, 404, 422, 500.
8. **Ma première API en 8 lignes** — code minimal, pleine page.
9. **`uvicorn --reload`** — la commande + capture du terminal.
10. **`/docs`** — capture pleine page de Swagger UI. **La slide la plus convaincante du cursus.**
11. **Le videur à l'entrée** — Pydantic illustré.
12. **Un modèle Pydantic** — code annoté, chaque type expliqué.
13. **Ce que la validation renvoie** — capture d'une erreur 422 avec son message détaillé.
14. **⚠️ v1 contre v2** — le tableau des équivalences, en rouge/vert.
15. **`Field()`** — bornes, longueurs, exemples pour la doc.
16. **Validations sur mesure** — `field_validator` et `model_validator`.
17. **`computed_field`** — le champ calculé (`jours_restants`), écho direct de la `@property` de la S5.
18. **Entrée ≠ sortie** — deux modèles, un schéma de flux.
19. **Créer : POST + 201** — le code + la réponse.
20. **Gérer l'erreur : `HTTPException`** — le 404 propre.
21. **Structurer : `APIRouter` et `Depends`** — l'arborescence du projet.
22. **Tester une API** — `TestClient`, un test, la sortie verte.
23. **Fil rouge v7 : l'API cible** — la liste des 6 routes.
24. **Bilan / Demo Day : les consignes**.

## Exercice pratique / Fil rouge v7 — L'API OpportuniTrack

### Corrigé commenté — `schemas.py`

```python
"""Schémas Pydantic v2 : le contrat d'entrée et de sortie de l'API."""

from datetime import date

from pydantic import BaseModel, ConfigDict, Field, computed_field, field_validator

from modeles import Statut     # l'Enum écrit en séance 5, réutilisé tel quel


class OpportuniteBase(BaseModel):
    """Champs communs à l'entrée et à la sortie."""

    # Field() ajoute des contraintes ET documente l'API automatiquement.
    titre: str = Field(min_length=3, max_length=200,
                       examples=["Bourse Smarts-Up 2027"])
    organisme: str = Field(min_length=2, max_length=120)
    pays: str = Field(min_length=2, max_length=60)
    deadline: date
    statut: Statut = Statut.A_FAIRE
    tags: list[str] = Field(default_factory=list, max_length=10)

    @field_validator("pays")
    @classmethod
    def normaliser_pays(cls, valeur: str) -> str:
        """Normalise la casse à l'entrée.

        En v2 c'est @field_validator (et non @validator) et le décorateur
        s'applique à une méthode de classe. Cette validation s'exécute
        AVANT que la donnée n'atteigne le code métier : le nettoyage
        de la séance 7 devient inutile pour tout ce qui passe par l'API.
        """
        return valeur.strip().title()

    @field_validator("deadline")
    @classmethod
    def deadline_pas_trop_ancienne(cls, valeur: date) -> date:
        if valeur.year < 2020:
            raise ValueError("La deadline semble erronée (année < 2020)")
            # Ce ValueError devient automatiquement une réponse HTTP 422
            # avec un message clair indiquant le champ concerné.
        return valeur


class OpportuniteCreation(OpportuniteBase):
    """Ce que le CLIENT envoie. Pas d'identifiant : c'est le serveur qui l'attribue."""
    pass


class OpportuniteLecture(OpportuniteBase):
    """Ce que le SERVEUR renvoie : identifiant + champs calculés."""

    model_config = ConfigDict(from_attributes=True)
    # from_attributes : autorise la construction depuis un objet Python
    # (notre dataclass Opportunite) et non seulement depuis un dictionnaire.
    # En v1, cela s'appelait orm_mode.

    id: int

    @computed_field
    @property
    def jours_restants(self) -> int:
        """Champ calculé, présent dans le JSON mais jamais stocké.

        C'est exactement la @property de la séance 5, exposée dans l'API.
        """
        return (self.deadline - date.today()).days

    @computed_field
    @property
    def urgente(self) -> bool:
        return 0 <= self.jours_restants < 7 and self.statut != Statut.ENVOYEE
```

### Corrigé commenté — `main.py`

```python
"""API OpportuniTrack."""

from fastapi import Depends, FastAPI, HTTPException, Query, status

from schemas import OpportuniteCreation, OpportuniteLecture
from stockage import DepotOpportunites

app = FastAPI(
    title="OpportuniTrack API",
    description="Suivi d'opportunités : bourses, stages, appels à candidature.",
    version="1.0.0",
)
# Ces trois champs alimentent directement la page /docs.


def get_depot() -> DepotOpportunites:
    """Dépendance : fournit l'accès aux données.

    L'injection de dépendances permet de REMPLACER cette source par une
    fausse dans les tests, sans toucher au code des routes.
    """
    return DepotOpportunites()


@app.get("/opportunites", response_model=list[OpportuniteLecture], tags=["Lecture"])
def lister(
    pays: str | None = Query(None, description="Filtrer par pays"),
    urgentes_seulement: bool = False,
    depot: DepotOpportunites = Depends(get_depot),
):
    """Liste les opportunités, avec filtres optionnels.

    Cette docstring devient la description de la route dans /docs :
    documenter son code documente son API. Deux effets, un seul effort.
    """
    resultats = depot.toutes()

    if pays:
        resultats = [o for o in resultats if o.pays.casefold() == pays.casefold()]
    if urgentes_seulement:
        resultats = [o for o in resultats if o.est_urgente]

    return resultats
    # On rend des objets Python : response_model les convertit en JSON
    # et FILTRE les champs non déclarés. Rien ne fuit par accident.


@app.get("/opportunites/{opp_id}", response_model=OpportuniteLecture, tags=["Lecture"])
def consulter(opp_id: int, depot: DepotOpportunites = Depends(get_depot)):
    """Consulte une opportunité par son identifiant."""
    opportunite = depot.par_id(opp_id)

    if opportunite is None:
        # Le bon code + un message utile. Ne JAMAIS rendre 200 avec un
        # corps vide pour une ressource absente : c'est mentir au client.
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Aucune opportunité d'identifiant {opp_id}",
        )
    return opportunite


@app.post(
    "/opportunites",
    response_model=OpportuniteLecture,
    status_code=status.HTTP_201_CREATED,   # 201 = créé, pas 200
    tags=["Écriture"],
)
def creer(
    donnees: OpportuniteCreation,          # ← la validation a DÉJÀ eu lieu ici
    depot: DepotOpportunites = Depends(get_depot),
):
    """Crée une opportunité.

    Si le corps de la requête est invalide, cette fonction n'est jamais
    appelée : FastAPI a répondu 422 avec le détail des champs fautifs.
    """
    return depot.ajouter(donnees)


@app.delete("/opportunites/{opp_id}", status_code=status.HTTP_204_NO_CONTENT,
            tags=["Écriture"])
def supprimer(opp_id: int, depot: DepotOpportunites = Depends(get_depot)):
    """Supprime une opportunité. 204 = succès, sans contenu à renvoyer."""
    if not depot.supprimer(opp_id):
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Introuvable")


@app.get("/statistiques", tags=["Analyse"])
def statistiques(depot: DepotOpportunites = Depends(get_depot)):
    """Le groupby de la séance 8, exposé en JSON."""
    toutes = depot.toutes()
    par_pays: dict[str, int] = {}
    for opp in toutes:
        par_pays[opp.pays] = par_pays.get(opp.pays, 0) + 1

    return {
        "total": len(toutes),
        "urgentes": sum(1 for o in toutes if o.est_urgente),
        "par_pays": par_pays,
    }
```

**Lancement** :
```bash
uvicorn main:app --reload
# puis ouvrir http://127.0.0.1:8000/docs
```

### Le test d'API

```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_liste_repond_200():
    reponse = client.get("/opportunites")
    assert reponse.status_code == 200
    assert isinstance(reponse.json(), list)


def test_creation_refuse_un_titre_trop_court():
    reponse = client.post("/opportunites", json={
        "titre": "ab",                    # min_length=3 -> doit être refusé
        "organisme": "Test",
        "pays": "Maroc",
        "deadline": "2027-01-01",
    })
    assert reponse.status_code == 422     # 422 = corps invalide


def test_404_sur_identifiant_inexistant():
    assert client.get("/opportunites/999999").status_code == 404
```

**Le moment pédagogique** : montrer que `test_creation_refuse_un_titre_trop_court` passe **sans qu'aucune ligne de validation n'ait été écrite dans les routes**. C'est Pydantic qui travaille. Cela répond concrètement à la question « à quoi servent les types ? » posée depuis la séance 4.

### Palier bonus
1. Ajouter la pagination (`limit`, `offset`) et rendre le total dans un en-tête.
2. Remplacer le stockage JSON par SQLite via **SQLModel** (même auteur que FastAPI, fondé sur Pydantic).
3. Ajouter une authentification par clé d'API avec `Depends` et l'en-tête `X-API-Key`.
4. Créer une route `POST /import` qui accepte le CSV produit par le scraper de la S9.
5. Passer les routes en `async def` et **discuter honnêtement** de ce que cela change (et ne change pas) quand le stockage reste synchrone.

## Ressources — Séance 10
| Ressource | Lien | Note |
|---|---|---|
| **FastAPI — Tutoriel officiel** | https://fastapi.tiangolo.com/tutorial/ | Existe en français. **La meilleure documentation de tutoriel de l'écosystème Python** |
| FastAPI — Notes de version | https://fastapi.tiangolo.com/release-notes/ | Pour suivre les ruptures (abandon de Pydantic v1) |
| FastAPI — Bigger Applications | https://fastapi.tiangolo.com/tutorial/bigger-applications/ | `APIRouter`, structure de projet |
| FastAPI — Testing | https://fastapi.tiangolo.com/tutorial/testing/ | `TestClient` |
| **Pydantic — doc officielle** | https://docs.pydantic.dev/latest/ | Bien vérifier « latest » et non une v1 archivée |
| Pydantic — Guide de migration v1 → v2 | https://docs.pydantic.dev/latest/migration/ | **À lire par le formateur** : la table des équivalences |
| Pydantic — Validators | https://docs.pydantic.dev/latest/concepts/validators/ | `field_validator`, `model_validator` |
| SQLModel | https://sqlmodel.tiangolo.com/ | Pour le palier bonus |
| Uvicorn | https://www.uvicorn.org/ | Le serveur ASGI |
| MDN — Vue d'ensemble de HTTP | https://developer.mozilla.org/fr/docs/Web/HTTP/Overview | Pour les apprenants sans culture web |
| Full Stack FastAPI Template | https://github.com/fastapi/full-stack-fastapi-template | Dépôt officiel : à montrer, pas à copier en séance |
| Awesome FastAPI | https://github.com/mjhea0/awesome-fastapi | Curation communautaire |

---
---

# SÉANCE 11 — Qualité, tests, mise en production + Demo Day
### *Rendre le travail livrable, puis le livrer*

> **Promesse** : « Le code qui marche sur ta machine ne vaut rien. Aujourd'hui, il marche partout — et tu le montres. »

## Objectifs pédagogiques
1. **Structurer** un projet Python moderne avec `pyproject.toml`.
2. **Gérer** dépendances et environnement avec **uv** et un fichier de verrouillage.
3. **Formater et analyser** son code avec **Ruff**.
4. **Écrire** des tests `pytest` avec fixtures, paramétrage et couverture.
5. **Externaliser** la configuration avec des variables d'environnement (`pydantic-settings`) et **ne jamais versionner de secret**.
6. **Automatiser** les contrôles avec `pre-commit` et une intégration continue GitHub Actions.
7. **Conteneuriser** et **déployer** l'API.
8. **Présenter** son projet en 5 minutes.

## Déroulé minuté (180 min)

| Temps | Bloc | Modalité | Contenu |
|---|---|---|---|
| 0–20 | **Théorie 1** : structurer et `uv` | Live coding | `uv init`, `uv add`, `uv run`, `uv.lock`, `pyproject.toml`, disposition `src/`. |
| 20–35 | **Théorie 2** : Ruff | Live coding | `ruff format`, `ruff check --fix`, configuration dans `pyproject.toml`. |
| 35–65 | **Théorie 3** : tester pour de vrai | Live coding | Fixtures, `parametrize`, `conftest.py`, couverture, que tester en priorité. |
| 65–75 | **PAUSE** | — | — |
| 75–90 | **Théorie 4** : configuration et secrets | Live coding | `.env`, `pydantic-settings`, `.gitignore`, le secret publié par accident. |
| 90–105 | **Théorie 5** : automatiser | Démo | `pre-commit`, un workflow GitHub Actions, le badge vert. |
| 105–125 | **Théorie 6** : conteneuriser et déployer | Démo commentée | Dockerfile, `docker run`, les options d'hébergement. |
| 125–180 | **DEMO DAY** | Plénière festive | 8 à 10 présentations de 5 min, questions, clôture. |

*Si le groupe dépasse 10 personnes, prévoir une 12e session dédiée au Demo Day, ou des présentations en binômes.*

## Concepts clés — expliqués simplement

**`pyproject.toml` = la carte d'identité du projet.** Un seul fichier déclare le nom, la version, les dépendances et la configuration des outils. Il a remplacé l'empilement `setup.py` + `requirements.txt` + `setup.cfg` + `.flake8`.

**uv = un seul outil à la place de cinq.** Il remplace pip, virtualenv, pyenv, pipx et poetry, et il est écrit en Rust — l'ordre de grandeur de gain de vitesse est spectaculaire à montrer en direct.
```bash
uv init opportunitrack     # crée le squelette du projet
uv add fastapi uvicorn     # ajoute une dépendance ET l'installe
uv add --dev pytest ruff   # dépendances de développement
uv run pytest              # exécute dans l'environnement, sans activation manuelle
uv sync                    # reconstruit l'environnement à l'identique
```
**L'argument qui porte** : `uv.lock` fige les versions exactes. « Ça marche chez moi » devient « ça marche partout », et c'est vérifiable. Le montrer en supprimant `.venv` et en le reconstruisant en quelques secondes.

**Ruff = un seul outil à la place de quatre.** Formateur et analyseur en un, il remplace black, flake8, isort et une partie de pylint.
```bash
ruff format .        # met en forme : le débat sur les espaces est clos
ruff check . --fix   # détecte et corrige ce qui peut l'être
```
Le vendre comme un **gain de temps social** : plus aucune revue de code ne porte sur la mise en forme, donc toutes portent sur le fond.

**Que tester en priorité ?** Les débutants veulent tout tester ou rien. Donner un ordre clair :
1. La **logique métier** (les calculs, les règles) — rentabilité maximale.
2. Les **cas limites** (liste vide, valeur nulle, date passée) — c'est là que vivent les bugs.
3. Les **bugs déjà rencontrés** — un bug corrigé sans test reviendra.
4. Les **routes d'API** en surface (statut et forme de la réponse).
Ne pas tester : les bibliothèques des autres, les getters triviaux, la mise en forme.

**La fixture = le décor de théâtre.** Elle prépare l'environnement du test et le range ensuite, sans dupliquer ce code dans chaque test :
```python
import pytest
from datetime import date, timedelta
from modeles import Opportunite


@pytest.fixture
def opportunite_urgente() -> Opportunite:
    """Décor réutilisable par tous les tests qui en ont besoin."""
    return Opportunite("Test", "Org", "Maroc", date.today() + timedelta(days=3))


@pytest.mark.parametrize("jours, attendu", [
    (-1, False),   # déjà passée
    (0, True),     # aujourd'hui
    (6, True),     # limite haute
    (7, False),    # juste au-delà du seuil
    (30, False),
])
def test_seuil_urgence(jours, attendu):
    """Un seul test, cinq cas. parametrize évite cinq copies presque identiques
    et nomme chaque cas dans le rapport d'échec."""
    opp = Opportunite("T", "O", "P", date.today() + timedelta(days=jours))
    assert opp.est_urgente is attendu
```
Faire remarquer que les valeurs choisies sont **les bornes** (6 et 7), jamais des valeurs confortables. C'est le cœur du métier de testeur.

**La couverture est un indicateur, pas un objectif.** `pytest --cov` dit quelles lignes n'ont jamais été exécutées. 100 % de couverture avec des assertions creuses ne prouve rien ; 60 % bien ciblés valent mieux. Le dire explicitement évite une course au chiffre.

**Les secrets ne se versionnent jamais.** Le scénario à raconter : une clé d'API poussée sur un dépôt public est exploitée en quelques minutes par des robots qui scrutent GitHub en continu. Et **supprimer le fichier ne suffit pas** — l'historique Git conserve tout. La bonne pratique :
```python
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    cle_api: str
    debug: bool = False


config = Config()   # lit .env et les variables d'environnement, avec validation
```
Avec `.env` dans `.gitignore` et un `.env.example` versionné, sans valeurs.

**Docker = le carton de déménagement.** On emballe l'application *avec* son environnement : même version de Python, mêmes dépendances, même système. Le carton s'ouvre à l'identique sur n'importe quelle machine.

```dockerfile
FROM python:3.14-slim

# uv est disponible en image officielle : on copie juste le binaire.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app

# On copie D'ABORD les fichiers de dépendances : tant qu'ils ne changent pas,
# Docker réutilise cette couche en cache et la reconstruction est instantanée.
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

COPY . .

EXPOSE 8000
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
# --host 0.0.0.0 : sans lui, le serveur n'écoute que l'intérieur du conteneur
# et reste injoignable depuis l'extérieur. Erreur classique.
```

**L'intégration continue = le collègue qui vérifie à ta place, à chaque envoi.**
```yaml
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]

jobs:
  qualite:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v5
      - run: uv sync
      - run: uv run ruff check .
      - run: uv run ruff format --check .
      - run: uv run pytest
```
Le badge vert sur le dépôt GitHub est un puissant moteur de motivation — le montrer comme tel.

## Plan des slides — Séance 11 (26 slides)

1. **Couverture** + 2. **Frise complète** (les 11 séances, la dernière allumée).
2. **« Ça marche sur ma machine »** — le mème, puis la question sérieuse : pourquoi ça ne suffit pas.
3. **La structure d'un projet moderne** — arborescence commentée.
4. **`pyproject.toml`** — le fichier annoté, section par section.
5. **uv remplace cinq outils** — schéma : pip, virtualenv, pyenv, pipx, poetry → uv.
6. **Les 5 commandes uv** — la slide à imprimer.
7. **`uv.lock`** — « ça marche partout », démonstration de la reconstruction.
8. **Ruff remplace quatre outils** — même traitement visuel.
9. **Avant / après `ruff format`** — un fichier mal mis en forme, puis propre.
10. **Configurer Ruff** — l'extrait de `pyproject.toml`.
11. **Que tester en priorité ?** — la pyramide en 4 niveaux.
12. **La fixture = le décor** — illustration théâtre.
13. **`parametrize`** — 5 copies de test barrées, remplacées par un seul.
14. **Tester les bornes** — la frise 6 / 7 entourée.
15. **⚠️ La couverture n'est pas un objectif** — l'exemple du test creux à 100 %.
16. **⚠️ Le secret publié** — le scénario, chronométré.
17. **`.env` + `pydantic-settings`** — le code + le `.gitignore`.
18. **`pre-commit`** — le contrôle qui s'exécute avant chaque commit.
19. **L'intégration continue** — le fichier YAML + capture du badge vert.
20. **Le carton de déménagement** — Docker illustré.
21. **Le Dockerfile annoté** — chaque ligne expliquée.
22. **Où déployer ?** — tableau : VPS, plateformes gérées, conteneurs, avec le critère de choix.
23. **La checklist de mise en production** — 10 points à cocher.
24. **Le parcours accompli** — les 11 séances, ce que chacun sait faire désormais.
25. **Et après ?** — les 4 chemins de spécialisation.
26. **DEMO DAY** — l'ordre de passage.

## Demo Day — format et grille

**Format** : 5 minutes de présentation + 2 minutes de questions par personne (ou binôme).

**Trame imposée** (à communiquer dès la fin de la S10) :
1. Ce que fait mon projet — 30 secondes, sans jargon.
2. Démonstration en direct — 2 minutes.
3. La difficulté que j'ai rencontrée et comment je l'ai résolue — 1 min 30. **C'est le cœur de l'exercice.**
4. Ce que j'ajouterais avec une semaine de plus — 1 minute.

**Grille d'appréciation** (non notée, restituée par écrit à chacun) :

| Critère | Ce qu'on regarde |
|---|---|
| Le projet fonctionne | La démonstration se déroule sans plantage bloquant |
| Le code est lisible | Noms explicites, fonctions courtes, `ruff` sans avertissement |
| Il est testé | Au moins 3 tests pertinents qui passent |
| Il est reproductible | Un tiers peut l'installer en suivant le README |
| La présentation est claire | Un non-développeur comprend l'utilité |

**Un mot au formateur** : la partie 3 (la difficulté rencontrée) est celle qui produit le plus d'apprentissage collectif, et celle que les apprenants ont le plus tendance à escamoter par pudeur. Insister en amont : *raconter un bug qu'on a mis trois heures à comprendre est plus utile au groupe qu'une démonstration parfaite.*

## Livrable final — la checklist du fil rouge

- [ ] Dépôt GitHub public avec un README (installation, usage, captures)
- [ ] `pyproject.toml` + `uv.lock`
- [ ] `ruff check` et `ruff format --check` sans erreur
- [ ] Au moins 5 tests qui passent, dont un test d'API
- [ ] `.env.example` versionné, `.env` **jamais** versionné
- [ ] Un workflow CI avec badge vert
- [ ] Dockerfile fonctionnel (bonus : image publiée)
- [ ] API déployée et joignable (bonus)

## Ressources — Séance 11
| Ressource | Lien | Note |
|---|---|---|
| **uv — doc officielle** | https://docs.astral.sh/uv/ | Commencer par « Getting started » |
| uv — Working on projects | https://docs.astral.sh/uv/guides/projects/ | Le guide de référence pour la séance |
| **Ruff — doc officielle** | https://docs.astral.sh/ruff/ | Configuration + règles |
| Ruff — Configuration | https://docs.astral.sh/ruff/configuration/ | L'extrait `pyproject.toml` |
| **pytest — doc officielle** | https://docs.pytest.org/ | Fixtures, `parametrize`, `conftest.py` |
| pytest-cov | https://pytest-cov.readthedocs.io/ | Couverture |
| Python Packaging User Guide | https://packaging.python.org/ | La référence officielle sur `pyproject.toml` |
| PEP 621 — métadonnées de projet | https://peps.python.org/pep-0621/ | Le standard derrière `pyproject.toml` |
| pydantic-settings | https://docs.pydantic.dev/latest/concepts/pydantic_settings/ | Configuration validée |
| pre-commit | https://pre-commit.com/ | + le hook officiel Ruff |
| GitHub Actions — Python | https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python | — |
| Docker — doc officielle Python | https://docs.docker.com/language/python/ | — |
| FastAPI — Deployment | https://fastapi.tiangolo.com/deployment/ | Concepts + Docker, par l'auteur du framework |
| *Architecture Patterns with Python* | https://www.cosmicpython.com/ | Gratuit en ligne. Pour ceux qui veulent aller au-delà |
| The Hitchhiker's Guide to Python | https://docs.python-guide.org/ | Bonnes pratiques communautaires |

---
---

# Clôture du cursus

## Ce que chaque participant sait faire au terme des 11 séances

| Domaine | Compétence acquise |
|---|---|
| Fondamentaux | Variables, conditions, boucles, fonctions, fichiers, erreurs |
| Structuration | Classes, dataclasses, modules, séparation des responsabilités |
| Python avancé | Dunders, générateurs, décorateurs, contextes, `match` structurel |
| Données | NumPy, pandas 3.0, nettoyage, agrégation, jointures |
| Visualisation | Matplotlib, seaborn, choix du graphique, dataviz honnête |
| Collecte | HTTP, APIs, BeautifulSoup, éthique du scraping |
| Web | API REST, FastAPI, Pydantic v2, documentation automatique |
| Production | uv, Ruff, pytest, secrets, CI, Docker, déploiement |

## Les quatre chemins d'après-formation

À présenter en dernière slide, avec une ressource d'entrée pour chacun :

1. **Data / IA** — scikit-learn, puis PyTorch. Entrée : le cours *Machine Learning* de Kaggle Learn.
2. **Développement backend** — bases de données, SQLAlchemy, authentification, files de messages. Entrée : la suite du tutoriel FastAPI.
3. **Automatisation métier** — *Automate the Boring Stuff*, chapitres tableurs, PDF et courriel.
4. **Applications de données** — Streamlit ou Gradio pour transformer un notebook en application partageable en une heure.

## Ce que le formateur devrait préparer avant le jour J

- [ ] Le dépôt GitHub complet, avec un dossier par séance (énoncé, corrigé, slides, ressources)
- [ ] Les notebooks « point de reprise » — un par séance, avec le code de départ déjà écrit
- [ ] Le jeu de données sale de la S7, généré et testé
- [ ] Les environnements testés sur Windows **et** macOS (les écarts se paient en séance)
- [ ] Le canal de communication ouvert et le salon `#sos-erreurs` créé
- [ ] Les slides à imprimer et afficher : arbre de décision des structures (S3), rituel des 5 commandes (S7), quel graphique pour quelle question (S8), les 5 règles du scraping (S9)
- [ ] Un plan B pour les coupures d'internet : les corrigés distribués hors ligne
