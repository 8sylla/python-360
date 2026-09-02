# Devoir séance 5 — MonBudget v2 (en objets)

Ta v1 marchait. Mais **toutes** tes fonctions se passaient la même liste
`depenses`. Aujourd'hui, tu **refactorises** : une dépense devient un objet
`Depense`, le carnet devient un `Budget`. Objectif : **le programme se comporte
exactement pareil à l'écran**, mais le code devient net et se lit comme une
phrase.

> Refactoriser = changer la structure **sans** changer le comportement visible.
> C'est la définition à retenir de la journée.

---

## Ouvrir le projet

**VS Code ▸ Fichier ▸ Ouvrir le dossier…** → ce dossier `devoir-monbudget-v2/`.
Interpréteur **Python 3.11** (StrEnum en a besoin).

## Les trois fichiers

| Fichier | À faire |
|---|---|
| `modeles.py` | compléter l'énum `Categorie` (StrEnum) et la dataclass `Depense` |
| `budget.py` | compléter la classe `Budget` (total, filtre, tri, charger/sauvegarder) |
| `tracker.py` | **déjà écrit** — il marchera dès que tes classes seront finies |

## Le cahier des charges

1. **`Categorie`** : une `StrEnum` avec au moins 5 catégories, plus une méthode
   `depuis_texte(texte)` qui rend `AUTRE` si le texte est inconnu.
2. **`Depense`** : une `@dataclass` avec `titre`, `montant`, `categorie`, et
   `tags` (avec `field(default_factory=list)` — **jamais** `= []`).
3. Une **`@property est_grosse`** sur `Depense` (vraie si le montant ≥ 100).
4. **`Budget`** : une classe qui **contient** des `Depense` (composition), avec
   `ajouter`, `total` (une `@property`), `par_categorie`, `triees_par_montant`,
   `charger` et `sauvegarder` (JSON, comme la v1).
5. Le menu de `tracker.py` tourne, **sauvegarde après chaque ajout**, et affiche
   le total.

**Critères de réussite :**
- `python tracker.py` : j'ajoute deux dépenses, je quitte, je relance → elles
  sont toujours là ;
- une dépense ≥ 100 est repérée à l'affichage ;
- taper une catégorie inconnue ne plante pas (→ `Autre`) ;
- un `depenses.json` **de la v1** reste lisible par la v2.

## Palier bonus

1. `@dataclass(frozen=True)` sur `Depense` → immuable et **hashable** (utilisable
   dans un `set` pour détecter les doublons). Discute le prix à payer.
2. `total_par_categorie()` → un `dict[Categorie, float]` (utile pour la S8).
3. `DepenseRecurrente(Depense)` avec un champ `frequence` — puis **débats** :
   vrai besoin d'héritage, ou simple champ de plus ?

## Rendu

Dépose ton dossier (ou le lien du dépôt) sur **Google Classroom**.

> Le corrigé complet est publié après la séance dans
> [`fil-rouge/v2-poo/`](../../../fil-rouge/v2-poo/). Essaie d'abord.
