# Devoir séance 6 — MonBudget v3 (sous le capot)

Ta v2 marchait, mais elle restait « à côté » de Python : il fallait
`budget.toutes()` pour boucler, une `lambda` pour trier, et
`charger()` / `sauvegarder()` à la main. Aujourd'hui tu **branches les
prises** : le Budget devient une collection native, et le code appelant se
lit tout seul.

> Séance dense : **l'objectif réaliste, c'est de savoir LIRE ce code**. Si tu
> ne finis pas tous les `# TODO`, ce n'est pas grave — fais-les dans l'ordre.

---

## Ouvrir le projet

**VS Code ▸ Fichier ▸ Ouvrir le dossier…** → ce dossier. Interpréteur
**Python 3.11**.

## Les fichiers

| Fichier | À faire |
|---|---|
| `modeles.py` | les dunders de `Depense` : `__repr__`, `__str__`, `__eq__`, `__hash__`, `__lt__` |
| `budget.py` | les dunders de collection + le générateur + le context manager |
| `decorateurs.py` | écrire `@journalise` et `@chronometre` |
| `tracker.py` | **déjà écrit** — il marchera dès que le reste sera complété |
| `tests/` | un test d'exemple ; ajoute-en **au moins 3** |

## Le cahier des charges

1. **`Depense.__repr__`** → `Depense('Loyer', 850.0)` ; **`__str__`** →
   `Loyer — Logement — 850.00 EUR`.
2. **`__eq__`** (titre + montant + catégorie, **pas** les tags) **et
   `__hash__`** sur les mêmes champs — sinon `set()` lève une `TypeError`.
3. **`__lt__`** sur le montant, avec `@total_ordering` : `sorted(budget)` et
   `max(budget)` doivent marcher **sans lambda**.
4. **`Budget`** : `__iter__`, `__getitem__`, `__contains__` (par titre).
5. Un **générateur** `grosses()` qui livre les dépenses ≥ 100 une par une.
6. Un **décorateur** `@journalise` (avec `functools.wraps`) posé sur
   `ajouter()`.
7. Le **context manager** `__enter__` / `__exit__` : charge à l'entrée,
   sauvegarde à la sortie — **même si une erreur survient**.

**Critères de réussite :**

```python
for d in budget: ...        # marche
sorted(budget)              # marche, sans lambda
"Loyer" in budget           # marche
len({depense_a, depense_b}) # marche (pas de TypeError)
with Budget() as b: ...     # sauvegarde toute seule
```

## Lancer

```bash
python tracker.py
pytest -q          # depuis la racine du dépôt
```

## Palier bonus

1. `@dataclass(order=True, frozen=True)` : compare les champs **dans l'ordre
   de déclaration** — piège à débusquer.
2. `itertools.groupby` pour `groupes_par_categorie()` (attention : trier avant).
3. Un `match` structurel qui importe un relevé hétérogène.
4. `@functools.cache` sur une fonction lente, et mesure la différence.

## Rendu

Dépose ton dossier (ou le lien de ton dépôt) sur **Google Classroom**.

> Le corrigé complet est publié après la séance dans
> [`fil-rouge/v3-avance/`](../../../fil-rouge/v3-avance/). Essaie d'abord.
