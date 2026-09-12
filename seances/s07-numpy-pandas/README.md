# Séance 7 — NumPy & pandas

**mercredi 9 septembre 2026 · 3 h**

> La séance où l'on cesse de compter à la main. Une liste de dictionnaires
> plafonne à quelques centaines de lignes ; aujourd'hui on en traite des
> centaines de milliers — et surtout, on apprend à ne pas se faire avoir
> par un fichier sale.

## Au programme

- Pourquoi un `ndarray` est plus rapide qu'une liste
- **Vectorisation**, **masques booléens**, **broadcasting**
- `read_csv` (et le piège du séparateur), puis le **rituel des cinq
  commandes** d'inspection
- `.loc` contre `.iloc` ; combiner des filtres avec `&` et `|`
- **Nettoyer** : dates, montants en texte, casse, doublons, valeurs
  manquantes, aberrantes
- Le **Copy-on-Write** de pandas 3.0 — on réaffecte, on ne modifie pas
- **Agréger** : `groupby`, `.agg`, `pivot_table`, export CSV

## Ce que contient ce dossier

| Fichier ou dossier | Ce que c'est | Quand |
|---|---|---|
| [`reprise.ipynb`](reprise.ipynb) | le **notebook** : tout le TD en un seul fichier, exécutable dans Colab | la veille |
| [`reprise/`](reprise/) | le **même TD** en 5 fichiers `.py`, pour VS Code | la veille |
| [`devoir-monbudget-v4/`](devoir-monbudget-v4/) | le **devoir** : squelette de MonBudget v4 | en séance |
| [`corrige/`](corrige/) | les **corrigés** du TD | après la séance |

Le corrigé de référence du projet est publié dans
[`fil-rouge/v4-donnees/`](../../fil-rouge/v4-donnees/).

## Démarrer

Deux façons de faire le TD, au choix — le contenu est le même.

**Dans le navigateur, sans rien installer** — ouvre
[`reprise.ipynb`](reprise.ipynb) dans Colab, puis
**Fichier ▸ Enregistrer une copie dans Drive**. Le notebook télécharge le
relevé tout seul. Il se lit de haut en bas : chaque cellule suppose que les
précédentes ont été exécutées.

**Dans VS Code** — **Fichier ▸ Ouvrir le dossier…** →
[`reprise/`](reprise/), interpréteur **Python 3.11**, puis :

```bash
python 00_echauffement.py
```

Les cinq fichiers se lisent dans l'ordre : `00_echauffement`, `01_numpy`,
`02_pandas_decouverte`, `03_nettoyage`, `04_agreger`.

Vérifie d'abord que tu es bien sur pandas 3 :

```bash
python -c "import pandas as pd; print(pd.__version__)"
```

Si la réponse commence par `2.`, installe la bonne version — la moitié des
gestes de la séance ne se comportent pas pareil.

## Le jeu de données

[`data/releve_brut.csv`](../../data/releve_brut.csv) — 418 lignes de relevé
bancaire, **délibérément sales**. Séparateur `;`. Six défauts y sont
plantés exprès :

| Le défaut | Ce qu'on en fait |
|---|---|
| trois formats de date, dont des vides | deux formats explicites, puis `fillna` |
| montants en texte (`"40,37 EUR"`, `"N/A"`) | `to_numeric(errors="coerce")` |
| casse et espaces incohérents (20 orthographes pour 5 catégories) | `.str.strip().str.title()` |
| 18 doublons exacts | `.drop_duplicates()` |
| 8 montants multipliés par 1000 | un seuil, et on les écarte |
| 19 remboursements (montants négatifs) | **séparés**, pas supprimés |

À la sortie : **333 dépenses et 19 remboursements**.

## Les quatre pièges à retenir

1. **Le séparateur oublié.** Sans `sep=";"`, pandas lève ici une
   `ParserError` dont le message ne parle pas de séparateur — et sur un
   fichier sans virgules, il ne dirait rien du tout.
2. **`pd.to_datetime(..., format="mixed", dayfirst=True)` corrompt les
   dates ISO en silence** — 53 dates fausses sur 418, sans le moindre
   avertissement. On donne les formats explicitement.
3. **`dropna()` sans `subset`** détruit 418 lignes → 102, à cause d'une
   colonne `note` vide 290 fois — et c'est normal qu'elle soit vide.
4. **`df[filtre]["colonne"] = valeur`** émet un `ChainedAssignmentError`,
   qui est un **avertissement** : rien n'est modifié, et le programme
   continue. Utiliser `df.loc[filtre, "colonne"] = valeur`.

## La règle du jour

> **On trace ce qu'on jette.** Chaque suppression s'accompagne d'un
> comptage affiché. Un nettoyage silencieux est un nettoyage suspect.

## Bloqué ?

Colle **le message d'erreur complet en texte** — jamais une capture — dans
le flux du cours sur Google Classroom. La dernière ligne d'un traceback dit
toujours ce qui ne va pas.
