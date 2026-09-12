# Devoir — MonBudget v5 : le tableau de bord

**À rendre sur Google Classroom.** Dernier devoir du cursus.

Tu as nettoyé un relevé en séance 7. Aujourd'hui tu le fais **parler** :
une figure, quatre panneaux, quatre questions.

---

## Le principe

Une seule image, qui répond à quatre questions :

| Panneau | La question | Le tracé |
|---|---|---|
| 1 | **Où part l'argent ?** | des barres horizontales, triées |
| 2 | **Mes dépenses sont-elles nombreuses et petites, ou rares et grosses ?** | un histogramme |
| 3 | **Ai-je tenu mon budget ?** | des barres — c'est le panneau qui a besoin de la **jointure** |
| 4 | **Est-ce que ça dérape, et depuis quand ?** | une ligne |

## Les données

Deux fichiers, dans `data/` :

- **`releve_propre.csv`** — les 333 dépenses nettoyées en séance 7
- **`budget_prevu.csv`** — ce qu'on avait **prévu** de dépenser, **une
  ligne par (catégorie, mois)**, séparateur `;`

> La deuxième table est là pour une raison : « 4 600 € de loisirs »,
> est-ce beaucoup ? Le relevé seul ne peut pas répondre.

## Les fichiers à compléter

| Fichier | Ce qu'il contient |
|---|---|
| `donnees.py` | charger, agréger, **joindre** — aucun graphique ici |
| `graphiques.py` | une fonction par panneau, chacune reçoit son `ax` |
| `tableau_de_bord.py` | assemble la figure et l'exporte |

Les `TODO` sont numérotés. Fais-les **dans l'ordre** : chaque fichier
dépend du précédent.

## La toute première erreur (c'est normal)

Au premier lancement :

```
TypeError: object of type 'NoneType' has no len()
```

C'est **voulu**. Les fonctions rendent `None` tant que leur `TODO` n'est
pas fait. L'erreur recule d'un cran à chaque fonction complétée : c'est
ton indicateur d'avancement.

## Démarrer

```bash
python donnees.py
```

Puis, quand `donnees.py` affiche ses tables sans erreur :

```bash
python tableau_de_bord.py
```

L'image arrive dans `figures/`.

## Ce qui est évalué

| Critère | Poids |
|---|---|
| Les quatre panneaux sont présents et corrects | 25 % |
| **La jointure ne fait pas exploser le nombre de lignes** | 20 % |
| **Les quatre titres portent un message, pas une description** | 25 % |
| Axes légendés, unités visibles, tri par valeur | 15 % |
| L'export est propre (`dpi`, `bbox_inches`) | 10 % |
| Le code se lit (une fonction par panneau, `ax` en argument) | 5 % |

**Le critère qui compte le plus est celui des titres**, et il ne demande
pas une ligne de Python. Pour chaque panneau, pose-toi la question :

> « Qu'est-ce que ce graphique m'apprend, en **une** phrase ? »

Cette phrase **est** le titre.

## Les cinq règles

1. Le **titre porte le message**, pas la description.
2. L'axe des **barres part de zéro**. Toujours.
3. **Trier** par valeur — sauf ce qui a un ordre naturel (les mois).
4. **Pas de camembert** au-delà de 3 parts. Jamais en 3D.
5. **Une question, un graphique.**

## Les trois pièges

1. **`merge` peut faire grossir la table sans rien dire.** La clé est le
   **couple** `(categorie, mois)`. Sur la seule catégorie : 333 lignes
   deviennent 1 998, et le total passe de 59 522 € à 357 130 €.
   Compte tes lignes avant et après.
2. **`how="inner"` fait disparaître des lignes en silence.** C'est le
   défaut de `merge`. Utilise `how="left"`.
3. **`sns.barplot` trace une MOYENNE, pas une somme.** Si tu veux des
   totaux, agrège d'abord puis utilise `ax.barh()`.

## Palier bonus (facultatif)

1. Un cinquième panneau : la heatmap catégorie × mois (`pivot_table` +
   `sns.heatmap`).
2. Le panneau 3 en **deux versions** — en euros, puis en pourcentage
   d'écart. Laquelle répond à la question, et pourquoi ?
3. Exporte en SVG **et** en PNG, zoome à 400 % sur les deux.
4. Décore une fonction de tracé avec le `@chronometre` de la séance 6.
5. Refais le panneau 1 avec `seaborn.objects`.

## Le corrigé de référence

`fil-rouge/v5-dashboard/` — à consulter **après** avoir rendu.

## Bloqué ?

Colle **le message d'erreur complet en texte** — jamais une capture — dans
le flux du cours sur Google Classroom.
