# `MonBudget` — v3-avance

**Séance 6 · Sous le capot.**

La v2 marchait, mais elle restait « à côté » de Python : il fallait
`budget.toutes()` pour boucler, une `lambda` pour trier, et
`charger()`/`sauvegarder()` à la main. La v3 **branche les prises** : le
Budget devient une collection native, et le code appelant se lit tout seul.

Ce dossier est la **version de référence** (le corrigé du devoir de la S6).
Le squelette à compléter est dans
[`../../seances/s06-python-avance/devoir-monbudget-v3/`](../../seances/s06-python-avance/devoir-monbudget-v3/).

---

## Les fichiers

| Fichier | Rôle |
|---|---|
| `modeles.py` | `Depense` + ses méthodes spéciales (`__repr__`, `__str__`, `__eq__`, `__hash__`, `__lt__`, `__format__`) |
| `budget.py` | `Budget` : dunders de collection, générateurs, `groupby`, context manager |
| `decorateurs.py` | `@journalise`, `@chronometre`, `@reessayer`, `@cache` |
| `importation.py` | `match/case` **structurel** : un relevé hétérogène → des `Depense` |
| `tracker.py` | le CLI, désormais en `with Budget() as budget:` |
| `tests/` | 27 tests pytest |

## Ce que la v3 débloque

```python
len(budget)            # __len__
for d in budget: ...   # __iter__
budget[0], budget[:3]  # __getitem__ (entier ET tranche)
"Loyer" in budget      # __contains__
sorted(budget)         # __lt__ — plus besoin de lambda
max(budget)            # idem
set(depenses)          # __hash__ — d'où budget.doublons()
print(depense)         # __str__ (et repr() pour le développeur)

with Budget() as budget:      # charge à l'entrée,
    budget.ajouter(depense)   # sauvegarde à la sortie,
                              # MÊME si une erreur survient
```

## Lancer

```bash
cd fil-rouge/v3-avance
python tracker.py
```

Les démos autonomes :

```bash
python decorateurs.py      # @chronometre, @wraps, @cache
python importation.py      # le match structurel sur un relevé hétérogène
```

## Les tests

Depuis la **racine du dépôt** (la configuration pytest est dans `pyproject.toml`) :

```bash
pytest -q
```

> **Le moment qui compte** : passe `SEUIL_GROSSE_DEPENSE` de `100.0` à `1000.0`
> dans `modeles.py`, relance `pytest`. Deux tests deviennent **rouges**, et le
> diff te dit exactement quoi. Le test t'a prévenu avant l'utilisateur.

## Les pièges rencontrés ici

- écrire `__eq__` **annule `__hash__`** → `set()` lève `TypeError` : il faut
  réécrire `__hash__` sur les **mêmes champs**, jamais sur un champ mutable ;
- un **générateur ne se parcourt qu'une fois** (`grosses()` : 2ᵉ tour vide) ;
- `groupby` ne regroupe que les éléments **consécutifs** → trier d'abord ;
- un décorateur sans `functools.wraps` **efface** le nom et la docstring ;
- `__exit__` qui rend `True` **avale** silencieusement les exceptions.

## Ce qui manque encore (et prépare la S7)

`total_par_categorie()` refait à la main, avec une boucle Python, ce qu'un
`groupby` de **pandas** fait en une ligne. Sur 40 000 lignes de relevé, la
boucle plafonne. En **séance 7** : NumPy et pandas — c'est `v4-donnees`.
