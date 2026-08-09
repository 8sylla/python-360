# Jeu de données de la formation

## `opportunites_brutes.csv`

**Ce fichier est volontairement sale.** C'est le matériau de l'exercice de
nettoyage de la séance 7. Ne le corrige pas à la main.

| Défaut injecté | Étape du corrigé |
|---|---|
| Casse et espaces incohérents (`Maroc` / `maroc` / ` MAROC `) | 3 — textes |
| Trois formats de date mélangés, dates vides ou aberrantes | 4 — dates |
| Montants en texte (`12 000 MAD`, `€1500`, `N/A`, `-`) | 5 — montants |
| Doublons exacts et quasi-doublons | 6 — doublons |
| Titres ou deadlines manquants | 7 — lignes inexploitables |
| Statuts écrits de plusieurs façons | bonus |
| Une colonne entièrement vide | bonus |

## Régénérer le fichier

```bash
python data/generer_donnees_sales.py                      # 300 lignes
python data/generer_donnees_sales.py --lignes 1000        # plus gros
```

Le générateur est **déterministe** (`random.seed(2026)`) : tout le monde obtient
exactement le même fichier, donc le corrigé tombe juste pour tout le groupe.

Les deadlines sont calculées **relativement à la date du jour** : si tu régénères
le fichier le jour de la séance, les colonnes `jours_restants` seront cohérentes.
Régénère-le la veille.

## Aucune donnée personnelle

Organismes, intitulés et URL sont fictifs ou institutionnels. C'est délibéré :
le bloc éthique de la séance 9 pose la règle « on ne collecte aucune donnée
personnelle », et le matériel pédagogique doit la respecter le premier.
