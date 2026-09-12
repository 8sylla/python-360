"""CORRIGÉ — 02_joindre.py

Les cinq questions sur la jointure. La Q4 est la plus importante : c'est
celle qui installe le réflexe de comptage.
"""

from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[4] / "data"
df = pd.read_csv(DATA / "releve_propre.csv", parse_dates=["date_operation"])
budget = pd.read_csv(DATA / "budget_prevu.csv", sep=";")

pd.set_option("display.width", 120)

reel = df.groupby(["categorie", "mois"])["montant"].sum().reset_index(name="reel")
fusion = reel.merge(budget, on=["categorie", "mois"], how="left")


# ── Q1 ─────────────────────────────────────────────────────────────────────
print("Q1. Ajouter ecart et depassement.")
fusion = fusion.assign(
    ecart=fusion["reel"] - fusion["budget_prevu"],
    depassement=fusion["reel"] > fusion["budget_prevu"],
)
print(fusion.head(6).round(2).to_string(index=False))
print("\n    -> .assign() plutot que fusion['ecart'] = ... : les deux sont")
print("       corrects, mais assign rend une nouvelle table, donc il")
print("       s'enchaine. C'est la regle d'or de la seance 7.")


# ── Q2 ─────────────────────────────────────────────────────────────────────
print("\nQ2. Combien de couples (categorie, mois) en depassement ?")
n = int(fusion["depassement"].sum())
print(f"    -> {n} sur {len(fusion)}  ({n / len(fusion) * 100:.0f} %)")
print("\n       .sum() sur une colonne de booleens COMPTE les True :")
print("       True vaut 1, False vaut 0. C'est le raccourci le plus")
print("       utile de pandas.")


# ── Q3 ─────────────────────────────────────────────────────────────────────
print("\nQ3. Qui depasse le plus SOUVENT, et qui depasse le plus en euros ?")
bilan = fusion.groupby("categorie").agg(
    mois_en_depassement=("depassement", "sum"),
    ecart_total=("ecart", "sum"),
)
print(bilan.sort_values("mois_en_depassement", ascending=False).round(2).to_string())

record = bilan["mois_en_depassement"].max()
souvent = list(bilan.index[bilan["mois_en_depassement"] == record])
gros = bilan["ecart_total"].idxmax()

print(f"\n    -> le plus SOUVENT : {', '.join(souvent)} "
      f"({record} mois sur 6, a EGALITE)")
print(f"       le plus en EUROS  : {gros} "
      f"(+{bilan.loc[gros, 'ecart_total']:.0f} EUR)")
print("""
       Attention au piege de idxmax() : en cas d'egalite, il rend la
       PREMIERE valeur et ne dit rien de la seconde. Ici Logement et
       Loisirs depassent tous les deux 4 mois sur 6.

       Et le resultat est plus interessant que la question : Logement
       depasse 4 mois sur 6, et finit pourtant SOUS son budget global
       (-699 EUR sur six mois). Ses depassements sont compenses par
       ses bons mois.

       « Depasser souvent » et « depasser au total » sont donc deux
       questions differentes, et elles n'appellent pas la meme
       decision : le logement n'a pas besoin d'etre revu a la hausse,
       les loisirs si.""")


# ── Q4 ─────────────────────────────────────────────────────────────────────
print("\nQ4. Et avec how='inner' ?")
avec_left = reel.merge(budget, on=["categorie", "mois"], how="left")
avec_inner = reel.merge(budget, on=["categorie", "mois"], how="inner")
print(f"    reel  : {len(reel)} lignes")
print(f"    left  : {len(avec_left)} lignes")
print(f"    inner : {len(avec_inner)} lignes")

if len(avec_inner) == len(avec_left):
    print("""
    -> Ici les deux donnent le meme nombre : le budget couvre TOUS les
       couples (categorie, mois) du releve. C'est une chance, pas une
       garantie.

       Comment l'aurais-tu su sans comparer ? En regardant les NaN :

           fusion["budget_prevu"].isna().sum()

       Zero NaN = aucune ligne du reel n'est orpheline = inner et left
       coincident. Des qu'il y a un seul NaN, inner supprime cette
       ligne SANS RIEN DIRE.
""")
print(f"    NaN dans budget_prevu apres le left : "
      f"{int(avec_left['budget_prevu'].isna().sum())}")

# La demonstration : on retire une ligne du budget et on recompte.
ampute = budget[~((budget["categorie"] == "Loisirs") & (budget["mois"] == "2026-03"))]
print(f"\n    Demonstration — on retire 1 ligne du budget ({len(ampute)} restantes) :")
print(f"      left  : {len(reel.merge(ampute, on=['categorie', 'mois'], how='left'))}"
      " lignes, avec 1 NaN visible")
print(f"      inner : {len(reel.merge(ampute, on=['categorie', 'mois'], how='inner'))}"
      " lignes — une depense reelle a DISPARU")
print("\n    -> C'est exactement la perte silencieuse qu'on refuse depuis")
print("       la seance 7. how='left' rend le trou visible ; how='inner'")
print("       le cache.")


# ── Q5 ─────────────────────────────────────────────────────────────────────
print("\nQ5. Ecart en pourcentage, cumule sur six mois.")
cumul = fusion.groupby("categorie")[["reel", "budget_prevu"]].sum()
cumul = cumul.assign(
    ecart=cumul["reel"] - cumul["budget_prevu"],
    ecart_pct=(cumul["reel"] / cumul["budget_prevu"] - 1) * 100,
).sort_values("ecart_pct", ascending=False)
print(cumul.round(2).to_string())
print("""
    -> Le POURCENTAGE ne change pas seulement l'echelle : il change
       ce qu'on VOIT.

       Regarde les trois ecarts de meme taille, autour de 700 EUR :

           Autre      +729 EUR  ->  +18,0 %   depassement net
           Transport  +725 EUR  ->  +15,1 %   depassement net
           Logement   -699 EUR  ->   -1,9 %   budget tenu

       Le meme montant, 700 EUR, est un probleme sur un budget de
       4 000 et du bruit sur un budget de 37 000. En euros, ces trois
       lignes se ressemblent ; en pourcentage, deux sont a corriger et
       la troisieme est saine.

       C'est pour ca que le panneau 3 du tableau de bord trace des
       pourcentages, et non des euros.
""")
