# Sujet 5 — Climat & anomalies de température

> Visualiser concrètement l'évolution des **températures** sur 20 ans.

[← Retour au cahier des charges](README.md)

## Contexte & problématique

Des relevés météo annuels par ville, sur 20 ans. Les saisies textuelles sont
**incohérentes** (`Maroc`, `maroc`, `MAROC`) et certaines **années manquent**.
La question métier :

> **Comment visualiser l'évolution des températures mondiales sur les 20
> dernières années ?**

## Le jeu de données

Exemple fourni : [`ressources/sujet-5-climat-exemple.csv`](ressources/sujet-5-climat-exemple.csv)
(18 lignes ; le vrai fichier fera **≥ 1 000 lignes**).

| Colonne | Type | Description |
|---|---|---|
| `Record_ID` | texte | identifiant du relevé |
| `Country` | texte | pays (saisie **incohérente** à normaliser) |
| `City` | texte | ville |
| `Year` | entier | année du relevé |
| `Month` | entier | mois (1 à 12) |
| `Average_Temperature_C` | décimal | température moyenne, en °C |
| `Anomaly_Indicator` | texte | `Normal` / `Eleve` (casse incohérente) |

**Défauts injectés à nettoyer :** **erreurs de saisie textuelle**
(`maroc`/`MAROC`/`Maroc`, `Eleve`/`eleve`), **années manquantes**, quelques
**températures absentes**.

## Les trois livrables, appliqués à ce sujet

### v1 — Fondations & NumPy (25 %)

- Lire le CSV **sans pandas**.
- `Average_Temperature_C` → **tableau NumPy**.
- Remplacer les **températures manquantes** par la **moyenne** ; écarter les
  lignes sans `Year`.
- Stats NumPy : température **moyenne/médiane**, **écart-type**, **min/max**.

### v2 — Exploration pandas (35 %)

- **DataFrame**, **normaliser `Country`** (`.str.strip().str.title()`) et
  `Anomaly_Indicator` (`.str.capitalize()`).
- Segmenter : relevés d'**été** (mois 6–8).
- `groupby("Year")` → **température moyenne par année** ;
  `pivot_table` **Country × Year**.
- Export de la série « température moyenne par année ».

### Finale — Data-viz & appli (40 %)

- **4 graphiques** : **courbe de la température moyenne par année** (la
  tendance !), barres par **pays**, boxplot par **pays**, histogramme des
  anomalies `Eleve` vs `Normal`.
- **Appli à menu** : `1. Tendance annuelle` · `2. Comparer les pays` ·
  `3. Part d'anomalies` · `4. Exporter` · `5. Quitter`.

## Pistes d'analyse

- La **courbe annuelle** monte-t-elle nettement sur 20 ans ?
- Quel **pays** se réchauffe le plus vite ?
- La part de relevés **`Eleve`** augmente-t-elle avec le temps ?

---

*Critères d'évaluation, format des rendus et soutenance (pitch de 5 min) :
voir le [cahier des charges commun](README.md).*
