# `MonBudget` — v2-poo

**Séance 5 · La même application, en objets.**

La v1 marchait, mais **toutes** ses fonctions se passaient la même liste
`depenses` en argument. Dès qu'une donnée circule partout comme ça, un objet
veut naître. On refactorise : une `Depense` devient un objet, le carnet devient
un `Budget`. **Le comportement à l'écran ne change pas** — c'est la définition
même d'une refactorisation.

Ce dossier est la **version de référence** (le corrigé du devoir de la séance 5).
Le squelette à compléter est dans
[`../../seances/s05-poo/devoir-monbudget-v2/`](../../seances/s05-poo/devoir-monbudget-v2/).

---

## Les trois modules

| Fichier | Rôle | Ce qu'il remplace (v1) |
|---|---|---|
| `modeles.py` | la classe `Depense` (dataclass) + l'énum `Categorie` (StrEnum) | le dict `{titre, categorie, montant}` |
| `budget.py` | la classe `Budget` : collection + persistance JSON | `stockage.py` + les fonctions qui trimballaient la liste |
| `tracker.py` | le menu CLI, désormais mince | `tracker.py` |

## Les notions de la séance, et où elles vivent

- **`@dataclass`** → `Depense` : `__init__`, `__repr__`, `__eq__` écrits pour toi.
- **`field(default_factory=list)`** → `Depense.tags` : le piège n°1 (une liste
  `= []` serait partagée par toutes les instances).
- **`StrEnum`** (3.11+) → `Categorie` : plus de chaînes magiques ; se sérialise
  seule en JSON.
- **`@property`** → `Budget.total` et `Depense.est_grosse` : un attribut qui se
  **calcule** à chaque lecture, donc jamais périmé.
- **Composition** : un `Budget` *a des* `Depense` (il n'en hérite pas).

## Lancer

```bash
cd fil-rouge/v2-poo
python tracker.py
```

> Un carnet de départ ? `cp depenses.example.json depenses.json`. Les fichiers
> `depenses.json` de la **v1 restent lisibles** : `Depense.depuis_dict` tolère
> l'absence de `tags` et la catégorie en texte libre.

## Ce qui manque encore (et prépare la S6)

Écrire `budget.total` marche, mais `for depense in budget:` ne marche pas encore,
et deux dépenses identiques ne sont pas reconnues comme égales de façon fine. En
**séance 6**, on ajoute les **méthodes spéciales** (`__iter__`, `__eq__`,
`__lt__`), les **générateurs** et les **décorateurs** — c'est `v3-avance`.
