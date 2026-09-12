# `MonBudget` — v4-donnees

**Séance 7 · Le passage à l'échelle.**

Jusqu'ici, MonBudget gérait un carnet saisi **à la main**, une dépense à la
fois. En v4, on reçoit un **vrai relevé bancaire** exporté par la banque :
418 lignes, dates en trois formats, montants en texte, catégories mal
orthographiées, doublons. C'est la réalité des données.

Ce dossier est la **version de référence** (le corrigé du devoir de la S7).
Le squelette à compléter est dans
[`../../seances/s07-numpy-pandas/devoir-monbudget-v4/`](../../seances/s07-numpy-pandas/devoir-monbudget-v4/).

---

## Les deux modules

| Fichier | Rôle |
|---|---|
| `nettoyage.py` | du relevé **brut** au relevé **propre** : dates, montants, textes, doublons, aberrants |
| `analyse.py` | `groupby`, `pivot_table`, `agg` — les insights métier |

Les données vivent dans [`../../data/`](../../data/) :
`releve_brut.csv` (fourni, sale) → `releve_propre.csv` (produit par toi).

## Lancer

```bash
cd fil-rouge/v4-donnees
python nettoyage.py     # nettoie et écrit data/releve_propre.csv
python analyse.py       # affiche les analyses
```

**Sortie réelle du nettoyage :**

```
Releve brut : 418 lignes

  dates converties                  418 lignes
  montants convertis                418 lignes
  textes harmonises                 418 lignes
  doublons supprimes                400 lignes  (-18 lignes)
  lignes inexploitables retirees    365 lignes  (-35 lignes)
  montants aberrants retires        359 lignes  (-6 lignes)

345 depenses, 14 remboursements
```

## Le piège qui coûte le plus cher

`pd.to_datetime(serie, format="mixed", dayfirst=True)` **a l'air** de gérer
les trois formats de date. En réalité il applique `dayfirst` **aussi aux
dates ISO** et inverse jour et mois : `2026-04-09` (9 avril) devient le
**4 septembre**.

Sur ce relevé, cela corrompt **16 lignes** — sans lever la moindre erreur.
Les totaux mensuels sont faux, et rien ne le signale.

La méthode sûre, celle du corrigé :

```python
texte = serie.str.strip().str.replace("/", "-", regex=False)
iso = pd.to_datetime(texte, format="%Y-%m-%d", errors="coerce")
fr  = pd.to_datetime(texte, format="%d-%m-%Y", errors="coerce")
dates = iso.fillna(fr)          # 0 date corrompue
```

## Ce que pandas remplace, ligne pour ligne

| En v3 (Python pur) | En v4 (pandas) |
|---|---|
| boucle `for` + `defaultdict` pour les totaux | `df.groupby("categorie")["montant"].sum()` |
| boucle + `if` pour filtrer | `df[df["montant"] > 100]` |
| tri avec `key=lambda` | `df.nlargest(5, "montant")` |
| compter à la main | `df.groupby(...).agg(nombre=("montant","size"))` |
| tableau croisé impossible | `df.pivot_table(index=..., columns=...)` |

## Ce qui manque encore (et prépare la S8)

Les chiffres sont justes, mais ils restent des **tableaux de nombres**.
Personne ne « voit » que le Logement pèse 69 % du budget en lisant une
colonne. En **séance 8** : Matplotlib et seaborn — c'est `v5-dashboard`.
