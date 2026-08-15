# Checklist du formateur

## Une fois pour toutes

- [ ] Dépôt GitHub public, avec un dossier par séance
- [ ] Notebooks « point de reprise » testés dans Colab (pas seulement en local)
- [ ] Environnements testés sur **Windows ET macOS** — les écarts se paient en séance
- [ ] Cours Google Classroom créé, un thème par séance, lien Meet généré
- [ ] Questionnaire de positionnement envoyé (sert à composer les binômes)

## La veille de chaque séance

- [ ] Régénérer `data/opportunites_brutes.csv` (les deadlines sont relatives à la date du jour)
- [ ] Exécuter le notebook de reprise **de bout en bout** dans un noyau neuf
- [ ] Vérifier les versions : `pandas`, `numpy`, `matplotlib`, `seaborn` (l'écosystème bouge vite)
- [ ] Préparer le plan B hors ligne (corrigés distribués en local)

## À imprimer et afficher au mur

- [ ] S3 — l'arbre de décision des structures de données
- [ ] S7 — le rituel des 5 commandes d'inspection
- [ ] S8 — quel graphique pour quelle question

## Les rituels de chaque séance

| Moment | Rituel | Durée |
|---|---|---|
| Ouverture | « L'erreur du jour » : un traceback projeté, décodé ensemble | 5 min |
| Milieu | Pair programming : binômes débutant/technique, un pilote + un copilote | — |
| Clôture | « Une ligne, un mot » : chacun écrit un mot retenu dans le chat | 5 min |

## Les 5 règles d'or de l'Arc 1

1. Jamais de jargon sans son analogie **dans la même phrase**.
2. Jamais plus de 8 minutes de live coding d'affilée.
3. L'erreur est le programme de la séance, pas un accident : en provoquer 2 à 3.
4. Tout exercice doit produire une **sortie visible**.
5. Exercice socle pour tous + palier bonus pour les profils techniques.
