# Sujet 3 — Campagnes & ventes e-commerce

> À partir des vraies transactions d'un **site de vente en ligne britannique**,
> comprendre les ventes, les clients et les pays qui rapportent.

[← Retour au cahier des charges](README.md)

## Le vrai jeu de données

**[Online Retail — UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/352/online+retail)**
(≈ **541 909 lignes**, ventes d'un e-commerce UK, déc. 2010 – déc. 2011).
Miroirs pratiques sur Kaggle :
[Online Retail (UCI)](https://www.kaggle.com/datasets/jihyeseo/online-retail-data-set-from-uci-ml-repo).

> Fichier Excel/CSV. Sur UCI : bouton **Download**.

### Colonnes principales

| Colonne | Description |
|---|---|
| `InvoiceNo` | n° de facture (préfixe **`C`** = annulation) |
| `StockCode`, `Description` | produit |
| `Quantity` | quantité (peut être **négative** sur annulation) |
| `InvoiceDate` | date et heure |
| `UnitPrice` | prix unitaire |
| `CustomerID` | client (souvent **manquant**) |
| `Country` | pays du client |

### Les vrais défauts à nettoyer

- ~**25 %** de **`CustomerID` manquants** (achats invités) ;
- des **annulations** : `InvoiceNo` commençant par **`C`**, avec `Quantity < 0` ;
- des `UnitPrice` à **0**, quelques `Description` manquantes ;
- des doublons de lignes.

## Les trois livrables, appliqués à ce dataset

### v1 — Fondations & NumPy (25 %)

- Lire le fichier (convertir en CSV au besoin) **sans pandas**.
- `Quantity`, `UnitPrice` → **tableaux NumPy** ; créer
  **`Montant = Quantity * UnitPrice`**.
- **Filtrer** les annulations (`Quantity < 0`) et les prix ≤ 0.
- Stats NumPy : panier **moyen**, quantité **médiane**, montant **total**.

### v2 — Exploration pandas (35 %)

- **DataFrame**, `to_datetime(InvoiceDate)`, retirer les lignes sans
  `CustomerID`.
- Segmenter : commandes d'un **pays** donné, montants **> 100**.
- `groupby("Country")` → **chiffre d'affaires par pays** ;
  `pivot_table` **Country × mois**.
- Export du **top 10 des pays** par CA.

### Finale — Data-viz & appli (40 %)

- **4 graphiques** : barres du **CA par pays** (top 10), courbe du **CA par
  mois**, histogramme des **montants de commande**, boxplot des paniers par
  pays.
- **Appli à menu** : `1. CA par pays` · `2. Ventes par mois` ·
  `3. Top produits` · `4. Exporter` · `5. Quitter`.

## Pistes d'analyse

- Quel **pays** (hors UK) pèse le plus dans le chiffre d'affaires ?
- Y a-t-il une **saisonnalité** (pic avant Noël) ?
- Quels **produits** reviennent le plus souvent ?

---

*Critères d'évaluation, format des rendus et soutenance (pitch de 5 min) :
voir le [cahier des charges commun](README.md).*
