# Les jeux de données

> Ce dossier se remplit **à la séance 7**. Il est vide d'ici là.

## `opportunites_brutes.csv` — séance 7

Le matériau de l'exercice de nettoyage. **Ce fichier sera volontairement
sale** — c'est tout son intérêt. Ne le corrige pas à la main.

| Défaut injecté | Étape du corrigé |
|---|---|
| Casse et espaces incohérents (`Maroc` / `maroc` / ` MAROC `) | textes |
| Trois formats de date mélangés, dates vides ou aberrantes | dates |
| Montants en texte (`12 000 MAD`, `€1500`, `N/A`, `-`) | montants |
| Doublons exacts et quasi-doublons | doublons |
| Titres ou deadlines manquants | lignes inexploitables |

Aucune donnée personnelle : les noms d'organismes sont réels et
institutionnels, tout le reste est fabriqué.

## `opportunites_propres.csv` — produit en séance 7

La sortie du pipeline de nettoyage. Il sert d'entrée au tableau de bord de
la séance 8.
