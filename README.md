# python-360

**Formation Python 360° — ASEGUIM**
_Association des Stagiaires, Étudiants et Élèves Guinéens au Maroc_
Commission Scientifique nationale

> Huit séances de 3 h. Un seul projet. Aucun prérequis.
> De « je n'ai jamais codé » à « je fais parler mes données ».

**→ Le portail de la formation : [8sylla.github.io/python-360](https://8sylla.github.io/python-360/)**

[![CI](https://github.com/8sylla/python-360/actions/workflows/ci.yml/badge.svg)](https://github.com/8sylla/python-360/actions)

---

## ⚠️ Ce dépôt se remplit au fil des séances

Les dossiers sont en place, la plupart sont **encore vides**. C'est normal :
chaque semaine y dépose son notebook, son corrigé et sa version du fil rouge.
Le README de chaque dossier dit ce qui va y arriver, et quand.

Rien ne se perd, rien n'arrive en avance.

---

## Je suis…

| | Va directement à |
| --- | --- |
| **un·e apprenant·e** | [`seances/`](seances/) — le `reprise.ipynb` de ta séance |
| **le formateur** | [`docs/`](docs/) — les guides minutés, séance par séance |
| **curieux du projet** | [`fil-rouge/`](fil-rouge/) — OpportuniTrack, version par version |
| **curieux du site** | [`portail/`](portail/) — HTML, CSS et JS, commentés en français |

---

## Démarrage en 30 secondes (séances 1 à 3)

**Rien à installer.** Ouvre le notebook de la séance dans Google Colab :

```
https://colab.research.google.com/github/8sylla/python-360/blob/main/seances/s01-parler-a-la-machine/reprise.ipynb
```

## Installation locale (à partir de la séance 4)

```bash
git clone https://github.com/8sylla/python-360.git
cd python-360
uv sync                      # ou : pip install -r requirements.txt
```

---

## Le parcours

| # | Séance | Ce que tu sais faire après | Fil rouge |
| --- | --- | --- | --- |
| 0 | Kit de démarrage _(async)_ | Pourquoi Python, et où l'on va | — |
| 1 | Parler à la machine | Variables, types, entrées/sorties | v0.1 fiche |
| 2 | Décider et répéter | Conditions, boucles | v0.2 filtre |
| 3 | Ranger l'information | Listes, dictionnaires | v0.3 carnet |
| 4 | Fabriquer ses outils | Fonctions, fichiers, erreurs | **v1 CLI** |
| 5 | Programmation orientée objet | Classes, dataclasses | **v2 objets** |
| 6 | Sous le capot | Dunders, générateurs, décorateurs | **v3 + tests** |
| 7 | NumPy & pandas | Nettoyer un vrai jeu de données | **v4 données** |
| 8 | Faire parler les données | Agréger, visualiser honnêtement | **v5 dashboard** |

**Arc 1 (S1–S4)** : rampe de lancement, aucun jargon, tout dans le navigateur.
**Arc 2 (S5–S8)** : structurer le code, puis faire parler les données.

Le programme détaillé — les titres officiels et l'inventaire complet des
notions couvertes — est dans
[`docs/programme-detaille.md`](docs/programme-detaille.md).

---

## Organisation du dépôt

```
portail/     le site public, déployé sur GitHub Pages
docs/        les guides du formateur, minutés à la minute
seances/     un dossier par séance : notebook de reprise + corrigé
fil-rouge/   OpportuniTrack, une version par étape du parcours
data/        les jeux de données des séances 7 et 8
```

### `seances/` — le notebook « point de reprise »

Chaque séance aura un `reprise.ipynb` dont **le code de départ fonctionne
déjà**. Tu n'as jamais besoin d'avoir réussi l'exercice précédent pour
suivre le suivant. Manqué une séance ? Ouvre-le, tu es à jour en dix minutes.

### `fil-rouge/` — un projet, six versions

`OpportuniTrack` : un tracker de bourses, stages et appels à candidature.
Il commence en séance 4 comme un script qui lit un fichier, devient un objet
en séance 5, et finit en séance 8 comme un tableau de bord tiré de vraies
données. **Chaque version manque de quelque chose** — et ce manque est
exactement ce que la séance suivante vient réparer.

### `portail/` — le site

Une page, sans dépendance ni outil de build. Pour publier une séance, on
change une ligne dans `portail/js/seances.js`. Voir
[`portail/README.md`](portail/README.md).

---

## Vérifier que tout marche

```bash
uv run ruff check .          # analyse statique
uv run ruff format --check . # mise en forme
uv run pytest -q             # les tests, dès qu'il y en aura
```

L'intégration continue rejoue ces commandes à chaque envoi.

---

## ⚠️ Versions — à lire avant de suivre un tutoriel trouvé en ligne

L'écosystème a bougé en profondeur début 2026. **Une grande partie des
contenus encore bien référencés est aujourd'hui périmée.**

| Outil | Version ciblée | Rupture à connaître |
| --- | --- | --- |
| Python | 3.14 (min. **3.12**) | numpy 2.5 ne descend pas en dessous de 3.12 |
| pandas | 3.0+ | Copy-on-Write par défaut ; l'affectation chaînée lève une **erreur** |
| NumPy | 2.5+ | API 2.x |
| Matplotlib | 3.10+ | Toujours l'interface orientée objet (`fig, ax`) |
| seaborn | 0.13+ | `hue=` requis pour colorier par catégorie |

Vérifie toujours la date d'un tutoriel. C'est une leçon de méthode qui vaut
bien au-delà de Python.

---

## Licence

Le contenu pédagogique et le code sont publiés sous la licence du fichier
[`LICENSE`](LICENSE). Reprends, adapte, enseigne — cite simplement la source.
