# Sujet 2 — Marché immobilier régional

> Comprendre ce qui fait le **prix** d'un bien pour guider les acheteurs.

[← Retour au cahier des charges](README.md)

## Contexte & problématique

Une agence dispose d'annonces immobilières d'une ville. Certaines saisies sont
**erronées** : prix à `0`, prix négatifs, surfaces manquantes. La question
métier :

> **Quels facteurs influencent le plus le prix des biens immobiliers ?**

## Le jeu de données

Exemple fourni : [`ressources/sujet-2-immobilier-exemple.csv`](ressources/sujet-2-immobilier-exemple.csv)
(18 lignes ; le vrai fichier fera **≥ 1 000 lignes**).

| Colonne | Type | Description |
|---|---|---|
| `Property_ID` | texte | identifiant du bien |
| `City_Quarter` | texte | quartier (Gueliz, Hivernage, Agdal…) |
| `Price_EUR` | entier | prix affiché, en euros |
| `Surface_M2` | entier | surface, en m² |
| `Rooms_Count` | entier | nombre de pièces |
| `Year_Built` | entier | année de construction |
| `Has_Garden` | texte | jardin : Oui / Non |

**Défauts injectés à nettoyer :** **prix aberrants** (`0` ou **négatifs**) et
**surfaces / années manquantes**.

## Les trois livrables, appliqués à ce sujet

### v1 — Fondations & NumPy (25 %)

- Lire le CSV **sans pandas**.
- `Price_EUR`, `Surface_M2` → **tableaux NumPy**.
- **Supprimer les lignes** dont le prix est `≤ 0` (aberrant) ; remplacer les
  **surfaces manquantes** par la **médiane**.
- Stats NumPy : prix **moyen/médian**, **écart-type**, **prix au m²** moyen.

### v2 — Exploration pandas (35 %)

- **DataFrame**, création d'une colonne **`Prix_au_m2 = Price_EUR / Surface_M2`**.
- Segmenter : biens **> 80 m²**, biens **avec jardin**.
- `groupby("City_Quarter")` → **prix moyen et prix/m² par quartier** ;
  `pivot_table` **Quartier × Has_Garden**.
- Export du classement des quartiers par prix/m².

### Finale — Data-viz & appli (40 %)

- **4 graphiques** : histogramme des prix, **nuage de points Surface × Prix**
  (corrélation), **boxplot des prix par quartier** (repérer les extrêmes),
  barres du **prix/m² par quartier**.
- **Appli à menu** : `1. Statistiques prix` · `2. Corrélation surface/prix` ·
  `3. Prix moyen par quartier` · `4. Exporter` · `5. Quitter`.

## Pistes d'analyse

- La **surface** explique-t-elle le prix mieux que le **nombre de pièces** ?
- Quel **quartier** est le plus cher au m² ?
- Le **jardin** ajoute-t-il une vraie prime au prix ?

---

*Critères d'évaluation, format des rendus et soutenance (pitch de 5 min) :
voir le [cahier des charges commun](README.md).*
