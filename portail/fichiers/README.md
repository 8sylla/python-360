# Les fichiers téléchargeables

C'est ici que se déposent les PDF, les corrigés et tout ce que le portail
propose au téléchargement.

## Convention de nommage

```
00-kit-demarrage.pdf
01-parler-a-la-machine.pdf
02-decider-et-repeter.pdf
...
```

Les PDF sont produits par le projet `slides-latex` :

```bash
cd slides-latex
.\compiler.bat tous
```

Ils sortent dans `slides-latex/build/`. On copie ici la version **sans
notes** (`00-kit-demarrage.pdf`), jamais la version formateur
(`00-kit-demarrage-notes.pdf`) : celle-là contient les notes de conduite de
séance, qui ne sont pas destinées aux apprenants.

Une fois le fichier déposé, il reste à citer son chemin dans
`portail/js/seances.js` — voir le README du portail.
