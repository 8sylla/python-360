# `MonBudget` — le fil rouge

Un suivi de dépenses personnelles. Un seul projet, repris et augmenté à
chaque séance : c'est ce qui permet de voir concrètement à quoi sert chaque
notion.

| Version | Séance | Ce qui change |
|---|---|---|
| v0.1 → v0.3 | S1–S3 | Dans les notebooks : une dépense, un filtre, un carnet en mémoire |
| **v1-cli** | S4 | Application en ligne de commande, dépenses écrites en JSON |
| **v2-poo** | S5 | Refactorisation en classes `Depense` et `Budget` |
| **v3-avance** | S6 | Méthodes spéciales, générateurs, décorateurs, premiers tests |
| **v4-donnees** | S7 | Un relevé bancaire de 300 lignes, nettoyé avec pandas |
| **v5-dashboard** | S8 | Le tableau de bord du mois, en quatre graphiques |

## Le principe

**Chaque version manque de quelque chose.** Le carnet de la séance 3 oublie
tout à la fermeture — d'où les fichiers en séance 4. Les fonctions de la
séance 4 se passent toutes la même liste — d'où les objets en séance 5. Ce
manque est le moteur : on ne repart jamais de zéro.

## Pourquoi un budget

Parce que tout le monde en a un. Personne n'a besoin qu'on lui explique ce
qu'est une dépense, une catégorie ou un total — l'attention reste sur le
Python, pas sur le domaine.

Les dossiers se remplissent séance après séance. S'ils sont vides, c'est que
la séance n'a pas encore eu lieu.
