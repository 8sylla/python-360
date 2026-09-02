# Sujet 4 — Santé & bien-être (objets connectés)

> À partir de vraies données de montres **Fitbit**, relier **activité**,
> **sommeil** et **calories** brûlées.

[← Retour au cahier des charges](README.md)

## Le vrai jeu de données

**[FitBit Fitness Tracker Data — Kaggle](https://www.kaggle.com/datasets/arashnic/fitbit)**
(30 utilisateurs, plusieurs fichiers CSV, données quotidiennes et à la minute).

Deux fichiers suffisent pour le projet :

- **`dailyActivity_merged.csv`** — l'activité par jour et par utilisateur ;
- **`sleepDay_merged.csv`** — le sommeil par jour et par utilisateur.

> Le cœur du projet : **fusionner** ces deux fichiers sur `Id` + la date.

### Colonnes principales

| Fichier | Colonnes utiles |
|---|---|
| `dailyActivity_merged.csv` | `Id`, `ActivityDate`, `TotalSteps`, `TotalDistance`, `VeryActiveMinutes`, `SedentaryMinutes`, `Calories` |
| `sleepDay_merged.csv` | `Id`, `SleepDay`, `TotalMinutesAsleep`, `TotalTimeInBed` |

### Les vrais défauts à nettoyer

- **doublons** dans `sleepDay_merged.csv` (à supprimer) ;
- des jours à **`TotalSteps == 0`** (montre non portée) à filtrer ;
- tous les jours n'ont **pas de ligne de sommeil** → valeurs manquantes après
  la fusion ;
- **formats de date** avec l'heure (`4/12/2016 12:00:00 AM`) à parser.

## Les trois livrables, appliqués à ce dataset

### v1 — Fondations & NumPy (25 %)

- Lire `dailyActivity_merged.csv` **sans pandas**.
- `TotalSteps`, `Calories` → **tableaux NumPy**.
- **Filtrer** les jours à `TotalSteps == 0` (aberrants).
- Stats NumPy : pas **moyens**, calories **médianes**, pas **min/max**.

### v2 — Exploration pandas (35 %)

- **DataFrame** des deux fichiers, `drop_duplicates`, **`merge`** activité +
  sommeil sur `Id` et la date.
- **Matrice de corrélation** (`.corr()`) : pas, minutes actives, calories,
  minutes de sommeil.
- `groupby("Id")` → **moyennes par utilisateur** ; jour de la semaine via la
  date.
- Export du tableau de corrélation.

### Finale — Data-viz & appli (40 %)

- **4 graphiques** : **nuage `TotalSteps` × `Calories`** (corrélation),
  histogramme des **minutes de sommeil**, boxplot des **pas par jour de
  semaine**, barres des **minutes actives vs sédentaires**.
- **Appli à menu** : `1. Corrélations` · `2. Sommeil moyen` ·
  `3. Pas par jour` · `4. Exporter` · `5. Quitter`.

## Pistes d'analyse

- **Plus de pas** = **plus de calories** ? La corrélation est-elle forte ?
- Ceux qui **bougent** plus **dorment-ils** mieux ?
- Le **temps sédentaire** est-il lié à un moins bon sommeil ?

---

*Critères d'évaluation, format des rendus et soutenance (pitch de 5 min) :
voir le [cahier des charges commun](README.md).*
