# Séance 6 — Sous le capot

**samedi 5 septembre 2026 · 3 h**

> **La séance la plus dense du cursus.** L'objectif est assumé dès l'ouverture :
> aujourd'hui, il suffit de savoir **lire** ce code. Personne n'est censé tout
> finir.

## Au programme

- Les **méthodes spéciales** (dunders) : `__repr__`/`__str__`,
  `__eq__`/`__hash__`, `__lt__`, et les quatre prises d'une collection
- Les **générateurs** : `yield`, la paresse, et le piège du flux épuisé
- Les **décorateurs** : les quatre marches, `functools.wraps`, `@cache`
- Les **gestionnaires de contexte** : `with`, `__enter__`/`__exit__`,
  `@contextmanager`
- Le **`match` structurel** (PEP 636) — au-delà du menu de la séance 4
- **`itertools`** / **`functools`**, puis **ruff** et **pytest**

## Ce que contient ce dossier

| Dossier | Ce que c'est | Quand |
|---|---|---|
| [`reprise/`](reprise/) | le **TD** : 5 fichiers `.py` à ouvrir dans VS Code | la veille |
| [`devoir-quiz/`](devoir-quiz/) | le **devoir** : un **quiz de compréhension** noté sur 100 | en séance |
| [`devoir-monbudget-v3/`](devoir-monbudget-v3/) | **bonus facultatif** : squelette de MonBudget v3 | en séance |
| [`corrige/`](corrige/) | les **corrigés** du TD | après la séance |

> **Pourquoi un quiz et pas un projet ?** Cette séance porte sur des
> mécanismes, pas sur des gestes. Ce qui compte ici est la
> **compréhension** : savoir *pourquoi* `__hash__` doit accompagner
> `__eq__` vaut plus que savoir le taper. Le projet MonBudget v3 reste
> disponible en bonus pour ceux qui veulent aller au bout.

Le corrigé de référence du projet est publié dans
[`fil-rouge/v3-avance/`](../../fil-rouge/v3-avance/) (5 modules, 27 tests).

## Démarrer

**VS Code ▸ Fichier ▸ Ouvrir le dossier…** → [`reprise/`](reprise/),
interpréteur **Python 3.11**, puis :

```bash
python 00_echauffement.py
```

## Les six analogies de la journée

| Notion | Analogie |
|---|---|
| dunders | la **prise murale normalisée** |
| `__repr__` / `__str__` | la **carte de visite** / la **présentation orale** |
| `__lt__` | la **règle du podium** |
| générateur | le **distributeur de tickets** |
| décorateur | l'**emballage cadeau** |
| context manager | la **ceinture de sécurité** |

## Les trois pièges à retenir

1. Écrire `__eq__` **annule `__hash__`** → `set()` lève une `TypeError`.
2. Un **générateur ne se parcourt qu'une fois**.
3. Un décorateur sans **`functools.wraps`** efface le nom et la docstring.

## Bloqué ?

Colle **le message d'erreur complet en texte** — jamais une capture — dans le
flux du cours sur Google Classroom.
