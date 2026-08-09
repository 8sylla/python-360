# Demo Day — format et grille

**5 minutes de présentation + 2 minutes de questions** par personne ou binôme.
Au-delà de 10 passages, prévoir une séance dédiée.

## Trame imposée (à communiquer dès la fin de la séance 10)

| # | Contenu | Durée |
|---|---|---|
| 1 | Ce que fait mon projet — **sans jargon** | 30 s |
| 2 | Démonstration en direct | 2 min |
| 3 | **La difficulté rencontrée et comment je l'ai résolue** | 1 min 30 |
| 4 | Ce que j'ajouterais avec une semaine de plus | 1 min |

> La partie 3 est le cœur de l'exercice, et celle que les apprenants escamotent
> par pudeur. Insister en amont : **raconter un bug qui a pris trois heures est
> plus utile au groupe qu'une démonstration parfaite.**

## Grille d'appréciation (non notée, restituée par écrit)

| Critère | Ce qu'on regarde | Observation |
|---|---|---|
| Le projet fonctionne | La démo se déroule sans plantage bloquant | |
| Le code est lisible | Noms explicites, fonctions courtes, `ruff` propre | |
| Il est testé | Au moins 3 tests pertinents qui passent | |
| Il est reproductible | Un tiers peut l'installer via le README | |
| La présentation est claire | Un non-développeur comprend l'utilité | |

## Checklist du livrable final

- [ ] Dépôt GitHub public avec README (installation, usage, captures)
- [ ] `pyproject.toml` + `uv.lock`
- [ ] `ruff check` et `ruff format --check` sans erreur
- [ ] Au moins 5 tests qui passent, dont un test d'API
- [ ] `.env.example` versionné, `.env` **jamais** versionné
- [ ] Workflow CI avec badge vert
- [ ] Dockerfile fonctionnel *(bonus : image publiée)*
- [ ] API déployée et joignable *(bonus)*
