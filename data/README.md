# Les jeux de données

Le matériau des séances 7 et 8 du fil rouge **MonBudget**.

| Fichier | Séance | Rôle |
|---|---|---|
| `releve_brut.csv` | 7 | l'entrée, volontairement sale |
| `releve_propre.csv` | 7 → 8 | la sortie du nettoyage, **et l'entrée du tableau de bord** |
| `budget_prevu.csv` | 8 | la seconde table, celle qui rend la jointure nécessaire |

## `releve_brut.csv` — séance 7

Un relevé bancaire de **418 lignes**, sur six mois (janvier → juin 2026).
**Ce fichier est volontairement sale** — c'est tout son intérêt. Ne le
corrige pas à la main : le nettoyer avec pandas *est* l'exercice.

| Colonne | Contenu |
|---|---|
| `date_operation` | la date de l'opération |
| `libelle` | le commerçant (Carrefour Market, EDF, Netflix…) |
| `categorie` | Alimentation, Transport, Logement, Loisirs, Sante |
| `montant` | le montant de l'opération |
| `moyen_paiement` | CB, virement, prélèvement |

### Les défauts injectés, et l'étape qui les traite

| Défaut | À quoi ça ressemble | Étape du corrigé |
|---|---|---|
| **Trois formats de date** mélangés | `2026-04-09`, `09/02/2026`, `11-06-2026` | `nettoyer_dates` |
| Dates **manquantes** | cellule vide | `retirer_inexploitables` |
| **Montants en texte** | `"57,76"`, `"1 234,56 EUR"`, `"N/A"` | `nettoyer_montants` |
| **Casse et espaces** incohérents | `CARREFOUR MARKET`, `  Netflix  `, `LOISIRS` | `nettoyer_textes` |
| Catégories **manquantes** | cellule vide → `Autre` | `nettoyer_textes` |
| **Doublons exacts** (18) | la même opération saisie deux fois | `supprimer_doublons` |
| **Montants négatifs** (remboursements) | `-76.40` | `separer_remboursements` |
| **Valeurs aberrantes** | un montant × 1000 par erreur de saisie | `retirer_aberrants` |

Aucune donnée personnelle : les noms d'enseignes sont réels et publics, tout
le reste est fabriqué.

### Régénérer le fichier

Le tirage est **reproductible** (graine fixe) — tout le monde a exactement le
même relevé :

```bash
python data/generer_releve.py
```

## `releve_propre.csv` — produit en séance 7

La sortie du pipeline de nettoyage : **333 dépenses** (plus 19 remboursements
mis de côté), zéro valeur manquante sur les colonnes utiles, dates et montants
correctement typés, plus deux colonnes calculées (`mois`, `jour_semaine`).

C'est le fichier d'entrée du **tableau de bord de la séance 8**.

> **Pourquoi celui-là est versionné**, alors qu'il se produit ? Parce qu'il est
> aussi l'*entrée* de la séance 8 : sans lui, un dépôt fraîchement cloné ne
> permettrait de lancer aucun fichier du TD. La graine du générateur étant fixe,
> la version que tu produis est identique à celle du dépôt — la relancer ne crée
> donc aucun conflit.

## `budget_prevu.csv` — séance 8

Ce qu'on avait **prévu** de dépenser : **36 lignes**, soit six catégories ×
six mois. Séparateur `;`.

| Colonne | Contenu |
|---|---|
| `categorie` | Logement, Transport, Alimentation, Loisirs, Sante, Autre |
| `mois` | `2026-01` à `2026-06` |
| `budget_prevu` | le budget de ce couple, en euros |

Cette table existe pour une raison précise : « 4 600 € de loisirs », est-ce
beaucoup ? Le relevé seul ne peut pas répondre. On ne joint pas deux tables
pour apprendre `merge` — on les joint parce qu'aucune des deux ne suffit.

### Le piège est dans la forme de la table

Il y a **une ligne par couple (catégorie, mois)**. La clé de jointure est donc
le couple, pas la seule catégorie. Qui l'oublie voit son relevé passer de 333 à
1 998 lignes, et son total de 59 522 € à 357 130 € — sans le moindre
avertissement. C'est le piège central de la séance 8, et il est naturel : un
vrai budget se révise chaque mois.

### Régénérer le fichier

```bash
python data/generer_budget_prevu.py
```

Graine fixe, comme pour le relevé : tout le monde a le même budget.
