# Séance 6 — Reprise (TD) : sous le capot

**Méthodes spéciales · générateurs · décorateurs · contextes · `match` · tests.**

C'est la séance la plus dense de la formation. On reste dans **VS Code**, et on
avance **par petits pas** : chaque fichier commence par une démonstration
commentée, puis te fait écrire la même chose sur un autre exemple.

---

## Ouvrir et exécuter

1. **VS Code ▸ Fichier ▸ Ouvrir le dossier…** → **ce dossier** `reprise/`.
2. Interpréteur **Python 3.11**.
3. `python 00_echauffement.py` (ou le ▶ / **F5**).

Corrigés dans [`../corrige/reprise/`](../corrige/reprise/) — **après** avoir essayé.

## L'ordre des fichiers

| Fichier | Ce qu'on y travaille |
|---|---|
| `00_echauffement.py` | prédis l'output : `repr` vs `str`, générateur épuisé, décorateur nu |
| `01_dunders.py` | `__repr__`, `__str__`, `__eq__`, `__hash__`, `__lt__`, `__len__`, `__iter__` |
| `02_generateurs.py` | `yield`, paresse, mémoire, `itertools` |
| `03_decorateurs.py` | construire un décorateur en 4 marches, `functools.wraps`, `@cache` |
| `04_contexte_et_match.py` | `with`, `__enter__`/`__exit__`, `@contextmanager`, `match` structurel |

## Les 6 analogies de la journée

| Notion | Analogie |
|---|---|
| **dunders** | la **prise murale normalisée** — Python ne demande pas, il branche |
| **`__repr__` / `__str__`** | la **carte de visite** (pour un pair) / la **présentation orale** (pour le public) |
| **`__lt__`** | la **règle du podium** — une règle, et tout le stade sait classer |
| **générateur** | le **distributeur de tickets** — un ticket quand tu appuies, pas 10 M d'avance |
| **décorateur** | l'**emballage cadeau** — le contenu ne change pas, la couche autour si |
| **context manager** | la **ceinture de sécurité** — « quoi qu'il arrive, on referme » |

## Le réflexe du jour

> Quand quelque chose « marche tout seul » en Python (`len()`, `for`, `in`,
> `sorted()`, `with`, `print()`), c'est qu'une **méthode spéciale** est
> branchée derrière. Il n'y a pas de magie : il y a un protocole.

## Bloqué ?

Colle **le message d'erreur complet en texte** dans Google Classroom. La
dernière ligne du traceback dit ce qui ne va pas.
