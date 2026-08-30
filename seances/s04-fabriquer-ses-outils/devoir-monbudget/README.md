# Devoir séance 4 — Projet MonBudget v1

Ton premier **vrai projet** : plus un notebook, mais un dossier de fichiers
`.py` qu'on ouvre dans VS Code. Objectif — une application de suivi de dépenses
en ligne de commande, dont les données **survivent à la fermeture**.

Tu pars de ce dossier `devoir-monbudget/`, où deux fichiers t'attendent avec
des `# TODO` à compléter. Réinvestis **tout** ce qu'on a vu aujourd'hui :
fonctions, module, `import`, fichiers, JSON, `try/except`, `match/case`.

---

## Ouvrir le projet

**VS Code ▸ Fichier ▸ Ouvrir le dossier…** puis choisis **ce dossier**
(`devoir-monbudget/`). Vérifie l'interpréteur **Python 3.11** en bas à droite.

## Le cahier des charges

| # | À faire | Notion mobilisée |
|---|---|---|
| 1 | `charger()` et `sauvegarder()` dans **`stockage.py`** | fichiers, JSON, `pathlib` |
| 2 | `demander_montant()` qui **ne plante jamais** sur une saisie invalide | `try / except ValueError` |
| 3 | `saisir_depense()` : construit une dépense `{titre, categorie, montant}` | dictionnaire, fonctions |
| 4 | `afficher(depenses)` : liste triée + **total** | boucle, `f-string`, `sorted` |
| 5 | `filtrer_par_categorie(depenses, cat)` : rend une **nouvelle** liste | compréhension de liste |
| 6 | Le menu tourne, **sauvegarde après chaque ajout**, quitte proprement | `match / case`, `while` |

**Critères de réussite** (teste-les toi-même) :

- Je lance `python tracker.py`, j'ajoute deux dépenses, je **quitte**.
- Je **relance** : mes deux dépenses sont **toujours là**. ✅
- Je tape `abc` comme montant : le programme **redemande**, il ne plante pas. ✅
- Un `depenses.json` lisible est apparu dans le dossier. ✅

## Lancer

```bash
python tracker.py
```

## Palier bonus (facultatif)

1. Option **« supprimer une dépense »** par numéro, avec confirmation.
2. **Export CSV** avec `csv.DictWriter` (colonnes `titre,categorie,montant`).
3. Un **troisième module** `affichage.py` qui isole tout ce qui `print`.

## Rendu

Dépose ton dossier (ou le lien de ton dépôt) sur **Google Classroom**.
Bloqué ? Colle **le message d'erreur complet en texte** — jamais une capture.
La dernière ligne du traceback dit toujours ce qui ne va pas.

> Le corrigé complet est publié après la séance dans
> [`fil-rouge/v1-cli/`](../../../fil-rouge/v1-cli/). Essaie d'abord.
