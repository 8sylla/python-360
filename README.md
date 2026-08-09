# python-360

**Formation Python 360° — ASEGUIM**
_Association des Stagiaires, Étudiants et Élèves Guinéens au Maroc_

> Onze séances de 3 h. Un seul projet. Aucun prérequis.
> De « je n'ai jamais codé » à « j'ai déployé une API ».

[![CI](https://github.com/ORGANISATION/python-360/actions/workflows/ci.yml/badge.svg)](https://github.com/ORGANISATION/python-360/actions)

---

## Je suis…

|                           | Va directement à                                                 |
| ------------------------- | ---------------------------------------------------------------- |
| **un·e apprenant·e**      | [`seances/`](seances/) — ouvre le `reprise.ipynb` de ta séance   |
| **le formateur**          | [`docs/`](docs/) — les guides minutés, séance par séance         |
| **en train de présenter** | [`slides/`](slides/) — ouvre le `.html` de la séance, touche `F` |
| **curieux du projet**     | [`fil-rouge/`](fil-rouge/) — OpportuniTrack, version par version |

---

## Démarrage en 30 secondes (séances 1 à 3)

**Rien à installer.** Ouvre le notebook de la séance dans Google Colab :

```
https://colab.research.google.com/github/ORGANISATION/python-360/blob/main/seances/s01-parler-a-la-machine/reprise.ipynb
```

## Installation locale (à partir de la séance 4)

```bash
git clone https://github.com/ORGANISATION/python-360.git
cd python-360
uv sync                      # ou : pip install -r requirements.txt
uv run python fil-rouge/v1-cli/tracker.py
```

---

## Le parcours

| #   | Séance                       | Ce que tu sais faire après        | Fil rouge        |
| --- | ---------------------------- | --------------------------------- | ---------------- |
| 0   | Kit de démarrage _(async)_   | Exécuter du code                  | —                |
| 1   | Parler à la machine          | Variables, types, entrées/sorties | v0.1 fiche       |
| 2   | Décider et répéter           | Conditions, boucles               | v0.2 filtre      |
| 3   | Ranger l'information         | Listes, dictionnaires             | v0.3 carnet      |
| 4   | Fabriquer ses outils         | Fonctions, fichiers, erreurs      | **v1 CLI**       |
| 5   | Programmation orientée objet | Classes, dataclasses              | **v2 objets**    |
| 6   | Sous le capot                | Dunders, générateurs, décorateurs | **v3 + tests**   |
| 7   | NumPy & pandas               | Nettoyer un vrai jeu de données   | **v4 données**   |
| 8   | Faire parler les données     | Agréger, visualiser honnêtement   | **v5 dashboard** |
| 9   | Aller chercher la donnée     | Collecter, éthiquement            | **v6 scraper**   |
| 10  | API REST avec FastAPI        | Exposer son travail               | **v7 API**       |
| 11  | Qualité et production        | Tester, verrouiller, déployer     | **v8 livrable**  |

**Arc 1 (S1–S4)** : rampe de lancement, aucun jargon, tout dans le navigateur.
**Arc 2 (S5–S11)** : structurer, analyser, livrer.

---

## Organisation du dépôt

```
docs/        les guides du formateur, minutés à la minute
slides/      212 diapositives, 12 decks, une identité partagée
seances/     un notebook « point de reprise » par séance
fil-rouge/   OpportuniTrack, en 6 versions de code réel
data/        le jeu de données sale de la séance 7 + son générateur
```

### `seances/` — le notebook « point de reprise »

Chaque séance a un `reprise.ipynb` dont **le code de départ fonctionne déjà**.
Tu n'as jamais besoin d'avoir réussi l'exercice précédent pour suivre le
suivant. Manqué une séance ? Ouvre-le, tu es à jour en dix minutes.

### `slides/` — la classe et les objets

`theme.css` porte toute l'identité visuelle ; les 12 decks l'instancient.
Changer une valeur dans le bloc `:root` la change dans les 212 diapositives.
Touche `N` pendant la présentation : les notes du formateur s'affichent.

### `fil-rouge/` — un projet, huit versions

`OpportuniTrack` : un tracker de bourses, stages et appels à candidature.
Il commence en séance 4 comme un script qui lit un fichier et finit en
séance 11 comme une API testée, conteneurisée et déployée.

---

## Vérifier que tout marche

```bash
uv run ruff check .          # analyse statique
uv run ruff format --check . # mise en forme
uv run pytest -q             # 13 tests
python data/generer_donnees_sales.py   # régénère le jeu de données
```

L'intégration continue rejoue ces trois commandes à chaque envoi.

---

## ⚠️ Versions — à lire avant de suivre un tutoriel trouvé en ligne

L'écosystème a bougé en profondeur début 2026. **Une grande partie des
contenus encore bien référencés est aujourd'hui périmée.**

| Outil    | Version ciblée   | Rupture à connaître                                                  |
| -------- | ---------------- | -------------------------------------------------------------------- |
| Python   | 3.14 (min. 3.11) | —                                                                    |
| pandas   | 3.0+             | Copy-on-Write par défaut ; l'affectation chaînée lève une **erreur** |
| NumPy    | 2.5+             | API 2.x                                                              |
| FastAPI  | 0.136+           | **Pydantic v1 n'est plus supporté**                                  |
| Pydantic | 2.13+            | `model_dump()`, `field_validator`, `ConfigDict`                      |

Vérifie toujours la date d'un tutoriel. C'est une leçon de méthode qui vaut
bien au-delà de Python.

---

## Contribuer

Les corrigés sont publiés après chaque séance. Une coquille, un lien mort,
une explication qui n'a pas fonctionné en salle ? Ouvre une _issue_ — les
retours des apprenants sont ce qui améliore le cursus.

## Licence

Code sous **MIT**, contenu pédagogique sous **CC BY-SA 4.0**.
Le logo ASEGUIM reste la propriété de l'association. Voir [`LICENSE`](LICENSE).

---

<sub>ASEGUIM · Association des Stagiaires, Étudiants et Élèves Guinéens au Maroc</sub>
