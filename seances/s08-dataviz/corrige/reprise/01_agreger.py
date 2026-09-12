"""CORRIGÉ — 01_agreger.py

Les cinq questions métier, résolues. Chacune tient en une expression.
"""

from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[4] / "data"
df = pd.read_csv(DATA / "releve_propre.csv", parse_dates=["date_operation"])

pd.set_option("display.width", 120)


# ── Q1 ─────────────────────────────────────────────────────────────────────
print("Q1. Le mois le plus lourd, et de combien ?")
par_mois = df.groupby("mois")["montant"].sum()
print(par_mois.round(2).to_string())
print(f"\n    -> {par_mois.idxmax()} : {par_mois.max():.2f} EUR")
print(f"       le plus leger est {par_mois.idxmin()} : {par_mois.min():.2f} EUR")
print(f"       ecart : {par_mois.max() - par_mois.min():.2f} EUR "
      f"({(par_mois.max() / par_mois.min() - 1) * 100:.0f} %)")


# ── Q2 ─────────────────────────────────────────────────────────────────────
print("\nQ2. Quelle categorie a la plus grosse depense unique ?")
maxima = df.groupby("categorie")["montant"].max().sort_values(ascending=False)
print(maxima.round(2).to_string())
ligne = df.loc[df["montant"].idxmax()]
print(f"\n    -> {maxima.idxmax()}, avec {maxima.max():.2f} EUR")
print(f"       la ligne : {ligne['libelle']}, le "
      f"{ligne['date_operation'].date()}")
print("       Attention : « Autre » a un maximum de 803 EUR alors que sa")
print("       moyenne est de 141. C'est le signe d'une valeur atypique,")
print("       pas d'un poste couteux.")


# ── Q3 ─────────────────────────────────────────────────────────────────────
print("\nQ3. Combien de depenses par moyen de paiement ?")
print(df["moyen_paiement"].value_counts().to_string())
print("\n    -> value_counts() suffit : c'est un groupby('x').size()")
print("       ecrit plus court, et deja trie par valeur.")


# ── Q4 ─────────────────────────────────────────────────────────────────────
print("\nQ4. Quel jour de la semaine depense-t-on le plus ?")
ordre = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
JOURS = dict(zip(
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    ordre,
))
avec_jour = df.assign(jour=df["jour_semaine"].map(JOURS))

par_jour = avec_jour.groupby("jour")["montant"].agg(
    nombre="count", total="sum", moyenne="mean"
)
print(par_jour.reindex(ordre).round(2).to_string())
print(f"\n    -> en TOTAL : {par_jour['total'].idxmax()}")
print(f"       en MOYENNE : {par_jour['moyenne'].idxmax()}")
print("       Les deux reponses peuvent differer, et c'est le vrai")
print("       enseignement : « depenser le plus » n'est pas une question")
print("       bien posee tant qu'on n'a pas dit total ou moyenne.")
print("\n       Le reindex(ordre) est important : sans lui, les jours")
print("       sortent par ordre ALPHABETIQUE (dimanche, jeudi, lundi...),")
print("       ce qui n'a aucun sens pour une semaine.")


# ── Q5 ─────────────────────────────────────────────────────────────────────
print("\nQ5. La part de chaque categorie, en pourcentage.")
totaux = df.groupby("categorie")["montant"].sum()
parts = (totaux / totaux.sum() * 100).sort_values(ascending=False).round(1)
print(parts.to_string())
brutes = totaux / totaux.sum() * 100
print(f"\n    somme des parts ARRONDIES : {parts.sum():.1f} %")
print(f"    somme des parts EXACTES   : {brutes.sum():.10f} %")
print("""
    -> 99,9 et non 100 : c'est l'arrondi, pas une erreur. Six valeurs
       arrondies au dixieme peuvent perdre jusqu'a 0,3 point au total.
       Ne « corrige » JAMAIS ce genre d'ecart a la main : on affiche
       les parts arrondies, et on garde les valeurs exactes pour les
       calculs.

    -> En revanche, si la somme s'ecarte de plusieurs POINTS, la cause
       est reelle : on a filtre quelque chose sans s'en rendre compte,
       ou on divise par le mauvais total. C'est ce qui arriverait ici
       en oubliant que les 19 remboursements ont ete mis de cote en
       seance 7 : le total de reference ne serait pas le bon.
""")
