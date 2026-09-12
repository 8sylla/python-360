# Séance 7 — Reprise (TD) : NumPy & pandas

**Du tableau en mémoire au relevé bancaire de 418 lignes.**

Aujourd'hui, MonBudget change d'échelle. Jusqu'ici tu saisissais tes dépenses
une par une. Maintenant tu reçois un **vrai relevé exporté par la banque** :
dates en trois formats, montants en texte, doublons. On va le nettoyer.

---

## Avant de commencer : installer pandas

Depuis la **racine du dépôt** :

```bash
pip install -r requirements.txt
```

Puis vérifie — c'est le rituel d'ouverture de la séance :

```bash
python -c "import pandas as pd, numpy as np; print(pd.__version__, np.__version__)"
```

Tu dois voir **3.0.x** et **2.4.x**. Si tu vois `2.x` pour pandas, tes
tutoriels en ligne ne correspondront pas à ce cours.

> **Avertissement de méthode.** pandas 3.0 est sorti en janvier 2026 et a
> changé une règle centrale (le *Copy-on-Write*). **Beaucoup de tutoriels
> encore bien référencés montrent du code qui ne marche plus.** Vérifie
> toujours la date d'un article avant de le suivre.

## Ouvrir et exécuter

**VS Code ▸ Fichier ▸ Ouvrir le dossier…** → **ce dossier** `reprise/`,
interpréteur **Python 3.11**, puis :

```bash
python 00_echauffement.py
```

## L'ordre des fichiers

| Fichier | Ce qu'on y travaille |
|---|---|
| `00_echauffement.py` | prédis l'output : liste vs tableau, dtype, masques, NaN |
| `01_numpy.py` | `ndarray`, vectorisation, broadcasting, masques — **et le chrono** |
| `02_pandas_decouverte.py` | Series/DataFrame, `read_csv`, le rituel des 5 commandes, `.loc`/`.iloc` |
| `03_nettoyage.py` | la trousse à outils : textes, dates, montants, doublons |
| `04_agreger.py` | `groupby`, `pivot_table`, export |

Corrigés dans [`../corrige/reprise/`](../corrige/reprise/) — **après** avoir
essayé.

## Les analogies du jour

| Notion | Analogie |
|---|---|
| `ndarray` vs `list` | la **boîte à œufs** (une seule sorte, cases alignées) contre le **sac de courses** |
| vectorisation | on **tire la poignée de recopie**, on ne remplit pas les cellules une par une |
| masque booléen | la **rangée de cases cochées** posée sur les valeurs — le *filtre automatique* |
| DataFrame | un **onglet Excel**, mais piloté par du code |
| `.loc` / `.iloc` | l'**adresse** (« rue des Loisirs ») / la **place de parking n°3** |
| Copy-on-Write | Excel rature ta feuille ; **pandas te rend un « Enregistrer sous »** |
| `groupby` | **trier un jeu de cartes en tas**, puis compter chaque tas |
| `pivot_table` | le **tableau croisé dynamique**, littéralement |

## Les trois phrases à retenir

1. **« pandas rend une nouvelle table. Réaffecte. »**
2. **« `&` et `|`, jamais `and` ni `or` — et des parenthèses. »**
3. **« On trace ce qu'on jette. »**

## Bloqué ?

Colle **le message d'erreur complet en texte** dans Google Classroom.
