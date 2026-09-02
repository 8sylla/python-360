# Sujet 5 — Climat & évolution des températures

> À partir des relevés **Berkeley Earth**, visualiser l'évolution des
> **températures** sur plus d'un siècle et comparer les pays.

[← Retour au cahier des charges](README.md)

## Le vrai jeu de données

**[Climate Change: Earth Surface Temperature Data — Kaggle](https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data)**
(relevés de **1743 à 2013**, plusieurs fichiers CSV).

Deux fichiers au choix, selon l'ambition du groupe :

- **`GlobalLandTemperaturesByCountry.csv`** (le plus simple) — température
  moyenne par pays et par mois ;
- **`GlobalLandTemperaturesByCity.csv`** (plus gros) — par ville.

### Colonnes principales

| Colonne | Description |
|---|---|
| `dt` | date du relevé (`AAAA-MM-JJ`, en fait le mois) |
| `AverageTemperature` | température moyenne (°C) — **souvent manquante avant 1850** |
| `AverageTemperatureUncertainty` | incertitude de la mesure |
| `Country` (et `City`) | localisation |

### Les vrais défauts à nettoyer

- **beaucoup de `AverageTemperature` manquantes** sur les décennies anciennes ;
- la colonne `dt` est un **texte** : il faut en **extraire l'année** ;
- des **noms de pays** à harmoniser (entités historiques, doublons) ;
- des séries **incomplètes** selon les villes.

## Les trois livrables, appliqués à ce dataset

### v1 — Fondations & NumPy (25 %)

- Lire le CSV **sans pandas** ; extraire l'**année** de `dt` (`dt[:4]`).
- `AverageTemperature` → **tableau NumPy**, en ignorant les valeurs vides.
- Stats NumPy : température **moyenne/médiane**, **écart-type**, **min/max**.

### v2 — Exploration pandas (35 %)

- **DataFrame**, `to_datetime(dt)`, `dropna(subset="AverageTemperature")`,
  colonne **`Year`**.
- Segmenter : un **pays** (ex. le Maroc) et les **20 dernières années**.
- `groupby("Year")` → **température moyenne annuelle** ;
  `pivot_table` **Country × décennie**.
- Export de la série « température moyenne par année ».

### Finale — Data-viz & appli (40 %)

- **4 graphiques** : **courbe de la température moyenne par année** (la
  tendance !), barres **par pays**, boxplot **par décennie**, courbe comparant
  **2 ou 3 pays**.
- **Appli à menu** : `1. Tendance annuelle` · `2. Comparer des pays` ·
  `3. Statistiques d'un pays` · `4. Exporter` · `5. Quitter`.

## Pistes d'analyse

- La **courbe annuelle** monte-t-elle nettement sur le dernier siècle ?
- Quel **pays** se réchauffe le plus vite ?
- L'**incertitude** des mesures diminue-t-elle avec le temps ?

---

*Critères d'évaluation, format des rendus et soutenance (pitch de 5 min) :
voir le [cahier des charges commun](README.md).*
