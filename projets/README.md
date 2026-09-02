# Projet fil rouge — Data Science avec Python

**Formation Python 360° · Commission Scientifique nationale — ASEGUIM**

Le projet transversal de la formation : concevoir une **application Python
complète** capable de **charger, nettoyer, analyser et visualiser** des données
brutes pour répondre à une problématique métier réelle. Il se déroule en
**trois livrables progressifs**, qui simulent un vrai flux de travail
professionnel.

- **5 groupes**, **un sujet par groupe** (5 sujets ci-dessous).
- **Stack imposée** : Python (bases) · NumPy · pandas · Matplotlib / seaborn.
- **Jeu de données** : un **vrai jeu open-source** (Kaggle / UCI), avec ses
  **vrais défauts** à nettoyer (valeurs manquantes, doublons, valeurs
  aberrantes, formats incohérents). Chaque sujet indique le sien.

> Les groupes et les dépôts de chaque équipe seront ajoutés ici une fois les
> équipes constituées.

---

## Les trois livrables

| Version | Livrable | Poids | Ce qu'on démontre |
|---|---|---|---|
| **v1** | Fondations Python & nettoyage **NumPy** | 25 % | la syntaxe de base et la manipulation de tableaux |
| **v2** | Exploration & agrégation **pandas** | 35 % | le filtrage, le `groupby`, l'extraction d'insights |
| **Finale** | **Data-viz + démo de l'appli** | 40 % | rendre les données parlantes ; un **pitch de 5 min** par équipe |

### v1 — Fondations Python & NumPy (25 %)

Valider la maîtrise de la syntaxe de base et des tableaux NumPy.

1. Lire le CSV **sans pandas**, avec les structures natives (`open()`, listes,
   dictionnaires).
2. Convertir les colonnes numériques en **tableaux NumPy**.
3. Écrire des fonctions NumPy pour **repérer et corriger les anomalies**
   (valeurs manquantes → moyenne ; retirer les valeurs négatives / aberrantes).
4. Calculer les premières **statistiques descriptives** (moyenne, médiane,
   écart-type, min, max) **uniquement avec NumPy**.

*Rendu : un script `.py` (ou notebook `.ipynb`) documenté et fonctionnel.*

### v2 — Exploration & agrégation pandas (35 %)

Passer à la vitesse supérieure avec la puissance de pandas.

1. Charger les données nettoyées dans un **DataFrame**.
2. **Segmenter** finement (ex. biens > 80 m², utilisateurs écoutant > 2 h…).
3. Croiser les variables avec **`.groupby()`** et **`.pivot_table()`** pour en
   tirer des insights métier (prix moyen par quartier, ROI par canal…).
4. Une fonction d'**export** des tableaux d'agrégation en CSV/Excel propre.

*Rendu : le code mis à jour + un court rapport des **5 découvertes majeures**.*

### Finale — Data-viz & démo de l'application (40 %)

Rendre les données parlantes et présenter un outil d'analyse.

1. Au moins **4 graphiques** pertinents et soignés (Matplotlib / seaborn) :
   histogramme de distribution, nuage de points (corrélations), boxplot
   (anomalies), courbe temporelle (tendances).
2. **L'application finale** : un script principal interactif — au minimum une
   boucle `while` dans le terminal avec un **menu** (« 1. Statistiques »,
   « 2. Graphique des corrélations », « 3. Exporter »…), Streamlit /
   CustomTkinter si le niveau le permet.

*Rendu & soutenance : code final propre et commenté (dépôt GitHub ou archive),
puis **démo live + pitch de 5 minutes par équipe** devant la classe.*

---

## Les 5 sujets

Chaque sujet a sa **fiche détaillée** (dataset réel, livrables déclinés, pistes
d'analyse) et pointe vers un **vrai jeu de données open-source**.

| # | Sujet | Fiche | Vrai dataset |
|---|---|---|---|
| 1 | Streaming & audience | [fiche →](sujet-1-streaming-audience.md) | [Spotify Tracks (Kaggle)](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset) |
| 2 | Marché immobilier | [fiche →](sujet-2-marche-immobilier.md) | [Melbourne Housing (Kaggle)](https://www.kaggle.com/datasets/dansbecker/melbourne-housing-snapshot) |
| 3 | Ventes e-commerce | [fiche →](sujet-3-ventes-ecommerce.md) | [Online Retail (UCI)](https://archive.ics.uci.edu/dataset/352/online+retail) |
| 4 | Santé & bien-être | [fiche →](sujet-4-sante-bien-etre.md) | [FitBit Fitness Tracker (Kaggle)](https://www.kaggle.com/datasets/arashnic/fitbit) |
| 5 | Climat & températures | [fiche →](sujet-5-climat-temperatures.md) | [Earth Surface Temperature (Kaggle)](https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data) |

### Sujet 1 — Streaming & audience

**Problématique :** comprendre les habitudes d'écoute et optimiser les
recommandations.
**Dataset :** [Spotify Tracks — 114 000 titres, 125 genres](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset)
· [fiche détaillée](sujet-1-streaming-audience.md)

### Sujet 2 — Marché immobilier régional

**Problématique :** quels facteurs influencent le plus le prix des biens ?
**Dataset :** [Melbourne Housing](https://www.kaggle.com/datasets/dansbecker/melbourne-housing-snapshot)
· [fiche détaillée](sujet-2-marche-immobilier.md)

### Sujet 3 — Campagnes & ventes e-commerce

**Problématique :** quel canal génère le meilleur ROI, et comment achètent les
clients ?
**Dataset :** [Online Retail — UCI, 500 000+ transactions](https://archive.ics.uci.edu/dataset/352/online+retail)
· [fiche détaillée](sujet-3-ventes-ecommerce.md)

### Sujet 4 — Santé & bien-être (objets connectés)

**Problématique :** activité physique, sommeil et calories sont-ils corrélés ?
**Dataset :** [FitBit Fitness Tracker](https://www.kaggle.com/datasets/arashnic/fitbit)
· [fiche détaillée](sujet-4-sante-bien-etre.md)

### Sujet 5 — Climat & anomalies de température

**Problématique :** visualiser l'évolution des températures sur plus d'un siècle.
**Dataset :** [Earth Surface Temperature — Berkeley Earth](https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data)
· [fiche détaillée](sujet-5-climat-temperatures.md)

---

## Critères d'évaluation

| Critère | Poids | Ce qu'on regarde |
|---|---|---|
| **Qualité du code** | 25 % | conventions PEP 8, commentaires clairs, pas de code mort, bonnes fonctions |
| **Maîtrise technique** | 35 % | NumPy & pandas utilisés à bon escient (éviter les boucles `for` quand pandas fait mieux en une ligne) |
| **Pertinence visuelle** | 20 % | graphiques lisibles, titres clairs, axes légendés, bon type de graphique |
| **Qualité de la démo** | 20 % | fluidité de l'appli en direct, réponses aux questions, interprétation des résultats |

---

## Conseils

- Commencez **petit et qui marche**, puis enrichissez : la v1 doit tourner avant
  d'écrire la v2.
- **Nettoyez d'abord, analysez ensuite** : un graphique sur des données sales
  ment.
- Le code de la démo doit être **relançable devant la classe** sans stress :
  testez-le sur une autre machine avant le jour J.
