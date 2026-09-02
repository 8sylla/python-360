# Sujet 4 — Santé & bien-être (objets connectés)

> Relier **activité physique**, **sommeil** et **calories** à partir de données
> de montres connectées.

[← Retour au cahier des charges](README.md)

## Contexte & problématique

Des montres connectées remontent chaque jour le nombre de pas, les heures de
sommeil, les calories brûlées et le rythme cardiaque. Les capteurs produisent
des **lignes vides** et des **valeurs extrêmes** (bugs). La question métier :

> **Existe-t-il une corrélation entre l'activité physique, le sommeil et les
> calories brûlées ?**

## Le jeu de données

Exemple fourni : [`ressources/sujet-4-sante-exemple.csv`](ressources/sujet-4-sante-exemple.csv)
(18 lignes ; le vrai fichier fera **≥ 1 000 lignes**).

| Colonne | Type | Description |
|---|---|---|
| `User_ID` | texte | identifiant de l'utilisateur |
| `Daily_Steps` | entier | pas effectués dans la journée |
| `Sleep_Hours` | décimal | heures de sommeil |
| `Calories_Burned` | entier | calories brûlées |
| `Average_HeartRate` | entier | fréquence cardiaque moyenne (bpm) |
| `Day_Of_Week` | texte | jour de la semaine |

**Défauts injectés à nettoyer :** **lignes entièrement vides** et **valeurs
extrêmes** à filtrer (ex. `150000` pas, `300` bpm, `0` pas).

## Les trois livrables, appliqués à ce sujet

### v1 — Fondations & NumPy (25 %)

- Lire le CSV **sans pandas**, en **ignorant les lignes vides**.
- Colonnes numériques → **tableaux NumPy**.
- **Filtrer les valeurs extrêmes** (ex. garder `0 < Daily_Steps < 40000`,
  `40 < HeartRate < 200`).
- Stats NumPy : pas **moyens**, sommeil **médian**, calories **min/max**.

### v2 — Exploration pandas (35 %)

- **DataFrame**, `dropna()` sur les lignes vides.
- **Matrice de corrélation** (`.corr()`) entre pas, sommeil, calories, rythme.
- `groupby("Day_Of_Week")` → **pas moyens et sommeil moyen par jour**.
- Export du tableau de corrélation.

### Finale — Data-viz & appli (40 %)

- **4 graphiques** : **nuage de points Pas × Calories** (corrélation),
  histogramme des heures de **sommeil**, boxplot du **rythme cardiaque**
  (repérer les extrêmes), barres des **pas moyens par jour**.
- **Appli à menu** : `1. Corrélations` · `2. Sommeil moyen` ·
  `3. Pas par jour` · `4. Exporter` · `5. Quitter`.

## Pistes d'analyse

- **Plus de pas** = **plus de calories** ? La corrélation est-elle forte ?
- Le **week-end**, dort-on plus mais bouge-t-on moins ?
- Un rythme cardiaque élevé va-t-il avec une forte activité ?

---

*Critères d'évaluation, format des rendus et soutenance (pitch de 5 min) :
voir le [cahier des charges commun](README.md).*
