# OpportuniTrack — le fil rouge

Un seul projet, du début à la fin. Chaque séance ajoute une couche visible au
même artefact : c'est ce qui permet de voir concrètement à quoi sert chaque
notion.

> Les dossiers se remplissent séance après séance. S'ils sont vides, c'est
> que la séance n'a pas encore eu lieu.

| Version | Séance | Ce qui change |
|---|---|---|
| v0.1 → v0.3 | S1–S3 | Dans les notebooks : la fiche, le filtre, le carnet en mémoire |
| **v1-cli** | S4 | Application en ligne de commande, données persistées en JSON |
| **v2-poo** | S5 | Refactorisation en classes `Opportunite` et `Carnet` |
| **v3-avance** | S6 | Dunders, générateurs, décorateurs, premiers tests |
| **v4-donnees** | S7 | 300 vraies lignes, nettoyées avec pandas |
| **v5-dashboard** | S8 | Le tableau de bord à quatre graphiques |

## Le principe

**Chaque version manque de quelque chose.** Le carnet de la séance 3 oublie
tout à la fermeture — d'où les fichiers en séance 4. Les six fonctions de la
séance 4 se passent toutes la même liste — d'où les objets en séance 5. Ce
manque est le moteur : on ne repart jamais de zéro.

## La règle de la refactorisation (séance 5)

Le comportement visible **ne change pas**. Une fois les deux versions
publiées, compare `v1-cli/tracker.py` et `v2-poo/tracker.py` : même usage,
structure différente. C'est la définition même du mot.
