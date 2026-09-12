# Devoir séance 7 — MonBudget v4 : nettoyer un vrai relevé

Jusqu'ici, tu saisissais tes dépenses **une par une**. Aujourd'hui, ta banque
t'envoie un export : **418 lignes**, dates en trois formats, montants en
texte, catégories mal orthographiées, doublons. C'est la réalité des données.

Ton travail : transformer `data/releve_brut.csv` en `data/releve_propre.csv`,
**en traçant ce que tu jettes**.

---

## Avant de commencer

```bash
pip install -r requirements.txt          # depuis la racine du dépôt
python -c "import pandas; print(pandas.__version__)"   # doit afficher 3.0.x
```

Ouvre **ce dossier** dans VS Code (Fichier ▸ Ouvrir le dossier).

## Le cahier des charges

Complète `nettoyage.py`, fonction par fonction. **Chaque fonction prend un
DataFrame et en rend un nouveau** — jamais de modification en place.

| # | Fonction | Ce qu'elle doit faire |
|---|---|---|
| 1 | `charger_brut` | lire le CSV — **sans oublier `sep=";"`** |
| 2 | `nettoyer_textes` | `strip`, casse harmonisée, catégorie vide → `Autre` |
| 3 | `nettoyer_dates` | les **trois** formats → de vraies dates |
| 4 | `nettoyer_montants` | `"40,37 EUR"` → `40.37` |
| 5 | `supprimer_doublons` | les 18 doublons exacts |
| 6 | `retirer_inexploitables` | date **ou** montant manquant — **et rien d'autre** |
| 7 | `retirer_aberrants` | les montants hors de toute plausibilité |
| 8 | `separer_remboursements` | les montants négatifs ne sont pas des dépenses |

**Critères de réussite**, à vérifier toi-même :

```python
propre.info()                      # date en datetime64, montant en float64
propre.isna().sum().sum()          # doit valoir 0
propre["categorie"].nunique()      # 6, pas 20
propre["date_operation"].max()     # doit être en JUIN, pas en décembre !
(propre["montant"] < 0).sum()      # 0
```

## La toute première erreur (c'est normal)

Lance `python nettoyage.py` **avant même de commencer** : tu obtiendras

```
pandas.errors.ParserError: Error tokenizing data.
C error: Expected 1 fields in line 3, saw 2
```

C'est l'erreur pandas la plus fréquente au monde, et elle dit exactement
ceci : *« tu m'as dit que les colonnes étaient séparées par des virgules,
mais je trouve autre chose »*. La réponse est dans le TODO 1. Chaque erreur
de ce devoir fonctionne ainsi : elle **désigne** le TODO à faire.

## Les trois pièges de ce devoir

1. **Les dates.** `pd.to_datetime(s, format="mixed", dayfirst=True)` a l'air
   de marcher. Vérifie la date **maximale** de ton résultat : si elle tombe
   après juin, tu as corrompu tes données sans le savoir.
2. **`dropna()`.** La colonne `note` est vide 8 fois sur 10. Un `dropna()`
   sans `subset` te fera passer de 418 lignes à une centaine.
3. **L'affectation chaînée.** `df[masque]["colonne"] = valeur` ne fait
   **rien** en pandas 3.0. Deux écritures correctes seulement :
   `df.loc[masque, "colonne"] = valeur` et `df = df.assign(...)`.

## L'ordre du pipeline n'est pas arbitraire

Nettoie les **textes AVANT** de dédoublonner : sinon `"  EDF "` et `"EDF"`
passent pour deux opérations différentes, et `drop_duplicates()` n'en trouve
aucune.

## Lancer

```bash
python nettoyage.py       # doit écrire data/releve_propre.csv
python analyse.py         # les agrégations
```

## Palier bonus

1. **Récupérer les catégories manquantes** à partir du libellé : « Netflix »
   est forcément un Loisir. Indice : un dictionnaire libellé → catégorie, puis
   `.map()` + `.fillna()`.
2. Enchaîner tout le pipeline avec **`.pipe()`** : une seule expression qui se
   lit comme une phrase.
3. `astype("category")` sur `categorie` et `moyen_paiement`, puis compare
   `df.memory_usage(deep=True).sum()` avant/après.

## Rendu

Dépose ton dossier (ou le lien de ton dépôt) sur **Google Classroom**, avec
le **compte-rendu du nettoyage** : combien de lignes à chaque étape, et
pourquoi.

> Le corrigé complet est publié après la séance dans
> [`fil-rouge/v4-donnees/`](../../../fil-rouge/v4-donnees/).
