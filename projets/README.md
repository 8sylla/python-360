# Projet fil rouge — Data Science avec Python

**Formation Python 360° · Commission Scientifique nationale — ASEGUIM**

Le projet transversal de la formation : concevoir une **application Python
complète** capable de **charger, nettoyer, analyser et visualiser** des données
brutes pour répondre à une problématique métier réelle. Il se déroule en
**trois livrables progressifs**, qui simulent un vrai flux de travail
professionnel.

- **17 étudiants**, répartis en **5 groupes** de 3 à 4 personnes.
- **1 sujet par groupe** (5 sujets ci-dessous).
- **Stack imposée** : Python (bases) · NumPy · pandas · Matplotlib / seaborn.
- **Jeu de données** : un CSV d'au moins **1 000 lignes** et **5 à 8 colonnes**,
  fourni ou validé par le formateur, contenant **volontairement des données
  sales** (manquantes, doublons, aberrantes) à nettoyer.

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

### Sujet 1 — Streaming & audience (Netflix / Spotify)

**Problématique :** comment optimiser les recommandations et comprendre les
habitudes d'écoute des utilisateurs ?

**Colonnes du CSV :** `User_ID`, `Track_Movie_Name`, `Genre`,
`Duration_Minutes`, `Device_Used`, `Date_Watched`, `User_Rating`.

**Défauts injectés :** valeurs manquantes et doublons.

### Sujet 2 — Marché immobilier régional

**Problématique :** quels facteurs influencent le plus le prix des biens, pour
guider les acheteurs ?

**Colonnes du CSV :** `Property_ID`, `City_Quarter`, `Price_EUR`, `Surface_M2`,
`Rooms_Count`, `Year_Built`, `Has_Garden`.

**Défauts injectés :** prix aberrants (`0` ou négatifs).

### Sujet 3 — Campagnes & ventes e-commerce

**Problématique :** quel canal marketing génère le meilleur ROI, et comment se
comportent les acheteurs ?

**Colonnes du CSV :** `Order_ID`, `Marketing_Channel`, `Cart_Value_USD`,
`Is_Converted` (0/1), `Customer_Age`, `Purchase_Date`.

**Défauts injectés :** formats de dates incohérents.

### Sujet 4 — Santé & bien-être (objets connectés)

**Problématique :** existe-t-il une corrélation entre activité physique,
sommeil et calories brûlées ?

**Colonnes du CSV :** `User_ID`, `Daily_Steps`, `Sleep_Hours`,
`Calories_Burned`, `Average_HeartRate`, `Day_Of_Week`.

**Défauts injectés :** lignes vides et valeurs extrêmes à filtrer.

### Sujet 5 — Climat & anomalies de température

**Problématique :** comment visualiser concrètement l'évolution des températures
mondiales sur 20 ans ?

**Colonnes du CSV :** `Record_ID`, `Country`, `City`, `Year`, `Month`,
`Average_Temperature_C`, `Anomaly_Indicator`.

**Défauts injectés :** erreurs de saisie textuelle et années manquantes.

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
