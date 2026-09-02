# Sujet 3 — Campagnes & ventes e-commerce

> Trouver le **canal marketing** le plus rentable et comprendre les acheteurs.

[← Retour au cahier des charges](README.md)

## Contexte & problématique

Un site e-commerce trace ses commandes et le **canal** par lequel le client est
arrivé. Les dates sont saisies dans **plusieurs formats** incohérents. La
question métier :

> **Quel canal marketing génère le meilleur retour sur investissement (ROI),
> et comment se comportent les acheteurs ?**

## Le jeu de données

Exemple fourni : [`ressources/sujet-3-ecommerce-exemple.csv`](ressources/sujet-3-ecommerce-exemple.csv)
(18 lignes ; le vrai fichier fera **≥ 1 000 lignes**).

| Colonne | Type | Description |
|---|---|---|
| `Order_ID` | texte | identifiant de commande |
| `Marketing_Channel` | texte | canal (Instagram, Google, Facebook, Email) |
| `Cart_Value_USD` | décimal | montant du panier, en dollars |
| `Is_Converted` | 0/1 | la visite a-t-elle abouti à un achat |
| `Customer_Age` | entier | âge du client |
| `Purchase_Date` | date | date d'achat, **formats mélangés** |

**Défauts injectés à nettoyer :** **formats de dates incohérents**
(`2026-01-05`, `05/01/2026`, `06-01-2026`, `2026/01/07`), quelques **paniers /
âges manquants**.

## Les trois livrables, appliqués à ce sujet

### v1 — Fondations & NumPy (25 %)

- Lire le CSV **sans pandas**.
- `Cart_Value_USD`, `Customer_Age` → **tableaux NumPy**.
- Remplacer les **paniers manquants** par la **moyenne** ; filtrer les âges
  invalides.
- Stats NumPy : panier **moyen**, **taux de conversion** global
  (`mean(Is_Converted)`), âge **médian**.

### v2 — Exploration pandas (35 %)

- **DataFrame**, **normaliser `Purchase_Date`** avec
  `pd.to_datetime(..., errors="coerce")` → un seul format.
- Segmenter : commandes **converties** (`Is_Converted == 1`).
- `groupby("Marketing_Channel")` → **panier moyen et taux de conversion par
  canal** ; `pivot_table` **Canal × tranche d'âge**.
- Export du classement des canaux par conversion.

### Finale — Data-viz & appli (40 %)

- **4 graphiques** : barres du **taux de conversion par canal**, boxplot des
  **paniers par canal**, histogramme des **âges**, courbe des **ventes dans le
  temps**.
- **Appli à menu** : `1. ROI par canal` · `2. Paniers par canal` ·
  `3. Ventes par mois` · `4. Exporter` · `5. Quitter`.

## Pistes d'analyse

- Le canal qui **convertit** le plus est-il celui au **plus gros panier** ?
- Les **jeunes** achètent-ils plutôt via **Instagram** ?
- Y a-t-il une **saisonnalité** des ventes une fois les dates unifiées ?

---

*Critères d'évaluation, format des rendus et soutenance (pitch de 5 min) :
voir le [cahier des charges commun](README.md).*
