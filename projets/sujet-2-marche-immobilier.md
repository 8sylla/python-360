# Sujet 2 — Marché immobilier régional

> À partir de vraies annonces immobilières de **Melbourne**, comprendre ce qui
> fait le **prix** d'un bien pour guider les acheteurs.

[← Retour au cahier des charges](README.md)

## Le vrai jeu de données

**[Melbourne Housing Snapshot — Kaggle](https://www.kaggle.com/datasets/dansbecker/melbourne-housing-snapshot)**
(≈ **13 500 biens**, fichier `melb_data.csv`). Version plus complète (34 857
lignes) : *Melbourne Housing Market* du même auteur.

### Colonnes principales

| Colonne | Description |
|---|---|
| `Suburb`, `Address`, `Regionname`, `CouncilArea` | localisation |
| `Rooms`, `Bedroom2`, `Bathroom`, `Car` | composition du bien |
| `Type` | maison / appartement / … |
| `Price` | **prix de vente** (AUD) |
| `Landsize`, `BuildingArea` | surfaces (m²) |
| `YearBuilt` | année de construction |
| `Distance` | distance au centre-ville |

### Les vrais défauts à nettoyer

- **beaucoup de valeurs manquantes** — c'est tout l'intérêt : `BuildingArea`
  (~**60 %** vides), `YearBuilt` (~**55 %**), `Car`, `CouncilArea` ;
- dans la version complète, ~**22 %** de **`Price` manquants** (lignes à écarter
  ou à traiter à part) ;
- des `Landsize` / `BuildingArea` à **0** peu crédibles.

## Les trois livrables, appliqués à ce dataset

### v1 — Fondations & NumPy (25 %)

- Lire le CSV **sans pandas**.
- `Price`, `Landsize`, `BuildingArea` → **tableaux NumPy**.
- **Écarter** les lignes sans `Price` ; remplacer les `BuildingArea` manquantes
  par la **médiane**.
- Stats NumPy : prix **moyen/médian**, **écart-type**, **prix au m²** moyen.

### v2 — Exploration pandas (35 %)

- **DataFrame**, colonne **`Prix_au_m2 = Price / BuildingArea`**.
- Segmenter : biens **> 80 m²**, avec **≥ 3 chambres**.
- `groupby("Regionname")` → **prix moyen et prix/m² par région** ;
  `pivot_table` **Type × Rooms**.
- Export du classement des régions par prix/m².

### Finale — Data-viz & appli (40 %)

- **4 graphiques** : histogramme des prix, **nuage `BuildingArea` × `Price`**
  (corrélation), **boxplot des prix par `Type`** (repérer les extrêmes),
  barres du **prix moyen par région**.
- **Appli à menu** : `1. Statistiques prix` · `2. Corrélation surface/prix` ·
  `3. Prix par région` · `4. Exporter` · `5. Quitter`.

## Pistes d'analyse

- La **surface** explique-t-elle le prix mieux que le nombre de **pièces** ?
- Quelle **région** est la plus chère au m² ?
- La **distance au centre** fait-elle vraiment baisser le prix ?

---

*Critères d'évaluation, format des rendus et soutenance (pitch de 5 min) :
voir le [cahier des charges commun](README.md).*
