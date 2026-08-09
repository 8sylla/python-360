# OpportuniTrack — le fil rouge

Un seul projet, huit versions. Chaque séance ajoute une couche visible au même
artefact : c'est ce qui permet de voir concrètement à quoi sert chaque notion.

| Version | Séance | Ce qui change |
|---|---|---|
| v0.1 → v0.3 | S1-S3 | Dans les notebooks (fiche, filtre, carnet en mémoire) |
| **v1-cli** | S4 | Application en ligne de commande, données persistées en JSON |
| **v2-poo** | S5 | Refactorisation en classes `Opportunite` et `Carnet` |
| **v3-avance** | S6 | Dunders, décorateur `@journalise`, premiers tests |
| v4-v5 | S7-S8 | Notebooks : nettoyage pandas et tableau de bord |
| **v6-scraper** | S9 | Alimentation automatique depuis le web |
| **v7-api** | S10 | API REST FastAPI + Pydantic v2 |
| v8 | S11 | Le tout : verrouillé, testé, conteneurisé, déployé |

**Règle de la refactorisation (S5)** : le comportement visible ne change pas.
Compare `v1-cli/tracker.py` et `v2-poo/tracker.py` — même usage, structure différente.
