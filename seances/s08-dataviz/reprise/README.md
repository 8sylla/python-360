# Séance 8 — le TD

**Six fichiers, dans l'ordre.** Aucun ne dépend de ton code : ils tournent
tous tels quels. Le travail consiste à les lire, les exécuter, puis
répondre aux questions « À toi » à la fin de chacun.

## Démarrer

**VS Code ▸ Fichier ▸ Ouvrir le dossier…** → ce dossier, interpréteur
**Python 3.11**, puis :

```bash
python 00_echauffement.py
```

## L'ordre

| Fichier | Ce qu'on y fait |
|---|---|
| `00_echauffement.py` | 7 prédictions à écrire **avant** d'exécuter |
| `01_agreger.py` | `groupby`, `reset_index`, `.agg`, `pivot_table` |
| `02_joindre.py` | `merge`, les 4 jointures, **le piège de l'explosion** |
| `03_matplotlib.py` | Figure et Axes, le squelette, l'axe qui mente, exporter |
| `04_seaborn.py` | le catalogue des 6 tracés, `hue`, les facettes, `objects` |
| `05_tableau_de_bord.py` | les 5 règles, et **les titres à réécrire** |

Les images produites arrivent dans `figures/`. **Ouvre-les** : la moitié de
la séance ne se lit pas dans le terminal.

## Ce dont tu as besoin

```bash
python -c "import matplotlib, seaborn; print(matplotlib.__version__, seaborn.__version__)"
```

Il faut au moins `3.10` et `0.13`. Sinon :

```bash
pip install -r requirements.txt
```

Les données viennent de `data/` :

- `releve_propre.csv` — les 333 dépenses nettoyées en séance 7
- `budget_prevu.csv` — ce qu'on avait **prévu** de dépenser, par catégorie
  et par mois (36 lignes)

C'est la seconde table qui rend la jointure nécessaire : « 4 600 € de
loisirs », est-ce beaucoup ? Le relevé seul ne peut pas répondre.

## Les trois pièges de la journée

1. **`merge` peut faire grossir ta table sans rien dire.** La clé de
   jointure ici est le **couple** `(categorie, mois)`. Joindre sur la seule
   catégorie fait passer 333 lignes à 1 998, et le total de 59 522 € à
   357 130 €. Compte tes lignes avant et après. Toujours.
2. **`inner` fait disparaître des lignes en silence.** C'est le défaut de
   `merge`. `how="left"` garde tout, avec un `NaN` visible.
3. **`sns.barplot` trace une MOYENNE, pas une somme.** Si tu voulais des
   totaux, agrège d'abord.

## La règle du jour

> **Le titre porte le message, pas la description.** « Les loisirs
> dépassent le budget de 30 % » plutôt que « Dépenses par catégorie ».

Et son corollaire, qui est le plus difficile à admettre :

> Un titre honnête peut dire qu'il n'y a **rien** à voir. « Aucun lien
> entre le montant et le jour du mois » est un résultat, pas un échec.

## Bloqué ?

Colle **le message d'erreur complet en texte** — jamais une capture — dans
le flux du cours sur Google Classroom.
