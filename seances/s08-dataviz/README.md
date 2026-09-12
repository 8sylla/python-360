# Séance 8 — Faire parler les données

**samedi 12 septembre 2026 · 3 h**

> **Dernière séance du cursus.** Un tableau propre ne convainc personne. Un
> graphique juste, si.

## Au programme

- **Agréger** : `groupby`, `reset_index`, `.agg` avec des colonnes nommées,
  `pivot_table`
- **Joindre** : `merge`, les quatre jointures, et **le piège de
  l'explosion de lignes**
- **Matplotlib** : Figure et Axes, l'interface orientée objet, le squelette
  en six lignes, l'export
- **seaborn** : le catalogue des six tracés, `hue`, les facettes,
  `objects` en ouverture
- **Les cinq règles de la dataviz honnête** — et le non-résultat assumé

## Ce que contient ce dossier

| Dossier | Ce que c'est | Quand |
|---|---|---|
| [`reprise/`](reprise/) | le **TD** : 6 fichiers `.py` à ouvrir dans VS Code | la veille |
| [`devoir-monbudget-v5/`](devoir-monbudget-v5/) | le **devoir** : le tableau de bord | en séance |
| [`corrige/`](corrige/) | les **corrigés** du TD | après la séance |

Le corrigé de référence du projet est publié dans
[`fil-rouge/v5-dashboard/`](../../fil-rouge/v5-dashboard/).

## Démarrer

**VS Code ▸ Fichier ▸ Ouvrir le dossier…** → [`reprise/`](reprise/),
interpréteur **Python 3.11**, puis :

```bash
python 00_echauffement.py
```

Vérifie d'abord que Matplotlib et seaborn sont là :

```bash
python -c "import matplotlib, seaborn; print(matplotlib.__version__, seaborn.__version__)"
```

Il faut au moins `3.10` et `0.13`. Sinon : `pip install -r requirements.txt`.

## Les données

Deux tables, dans `data/` :

| Fichier | Ce que c'est |
|---|---|
| `releve_propre.csv` | les **333 dépenses** nettoyées en séance 7 |
| `budget_prevu.csv` | ce qu'on avait **prévu**, une ligne par (catégorie, mois) — 36 lignes, séparateur `;` |

C'est la seconde table qui rend la jointure nécessaire : « 4 600 € de
loisirs », est-ce beaucoup ? Le relevé seul ne peut pas répondre.

## Les cinq règles de la dataviz honnête

1. Le **titre porte le message**, pas la description.
   « Les loisirs dépassent le budget de 30 % » plutôt que
   « Dépenses par catégorie ».
2. L'axe des **barres part de zéro**. Toujours. Une courbe peut se
   permettre un axe tronqué — elle montre une variation. Une barre, non :
   sa longueur **est** la quantité.
3. **Trier** par valeur, pas par ordre alphabétique — sauf ce qui a déjà un
   ordre naturel (les mois).
4. **Pas de camembert** au-delà de 3 parts. Jamais en 3D.
5. **Une question, un graphique.** Si tu ne peux pas dire en une phrase ce
   que le graphique répond, il n'est pas prêt.

## Les trois pièges à retenir

1. **`merge` peut faire grossir ta table sans rien dire.** La clé est le
   **couple** `(categorie, mois)`. Sur la seule catégorie : 333 lignes
   deviennent **1 998**, et le total passe de 59 522 € à **357 130 €**.
   Compte tes lignes avant et après — ou utilise
   `validate="many_to_one"`, qui plante au lieu de gonfler.
2. **`how="inner"` fait disparaître des lignes en silence.** C'est le
   défaut de `merge`. `how="left"` garde tout, avec un `NaN` visible.
3. **`sns.barplot` trace une MOYENNE, pas une somme** — et les petits
   traits sont un intervalle de confiance à 95 %.

## Le geste du jour

> **Le titre porte le message.** Pour chaque graphique : « qu'est-ce que ça
> m'apprend, en une phrase ? ». Cette phrase **est** le titre.

Et son corollaire, le plus difficile à admettre :

> Un titre honnête peut dire qu'il n'y a **rien** à voir. « Aucun lien
> entre le montant et le jour du mois » est un résultat, pas un échec.

## Et après ?

Quatre chemins, présentés en clôture :

| Direction | Par où commencer |
|---|---|
| **Data / IA** | scikit-learn, puis Kaggle Learn |
| **Collecter** | scraping et APIs publiques — fabriquer ses données |
| **Exposer** | FastAPI — passer du script au service |
| **Automatiser** | *Automate the Boring Stuff with Python* |

Les trois premiers sont exactement ce qu'on n'a pas eu le temps de faire.

## Bloqué ?

Colle **le message d'erreur complet en texte** — jamais une capture — dans
le flux du cours sur Google Classroom.
