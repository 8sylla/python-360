"""JOINDRE — deux tables, une clé, et un piège qui ne prévient pas.

« 4 600 € de loisirs », est-ce beaucoup ? Le relevé ne peut pas répondre :
il ne contient pas ce qu'on avait PRÉVU de dépenser. C'est là que `merge`
devient nécessaire.

    python 02_joindre.py
"""

from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[3] / "data"

pd.set_option("display.width", 120)

df = pd.read_csv(DATA / "releve_propre.csv", parse_dates=["date_operation"])
budget = pd.read_csv(DATA / "budget_prevu.csv", sep=";")

print(f"Releve : {len(df)} depenses")
print(f"Budget : {len(budget)} lignes")
print("\nLes cinq premieres lignes du budget :")
print(budget.head(5).to_string(index=False))
print(f"\n-> UNE ligne par (categorie, mois) : {budget['categorie'].nunique()}"
      f" categories x {budget['mois'].nunique()} mois = {len(budget)}")


# ═══════════════════════════════════════════════════════════════════════════
#  1. merge = le RECHERCHEV d'Excel
# ═══════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  1. merge — le RECHERCHEV, en mieux")
print("=" * 70)

reel = df.groupby(["categorie", "mois"])["montant"].sum().reset_index(name="reel")
fusion = reel.merge(budget, on=["categorie", "mois"], how="left")

print(f"\nreel   : {len(reel)} lignes")
print(f"budget : {len(budget)} lignes")
print(f"fusion : {len(fusion)} lignes   <-- identique a reel : c'est bon signe")
print()
print(fusion.head(6).round(2).to_string(index=False))

print("\n-> « En mieux » que RECHERCHEV pour trois raisons : la cle peut")
print("   etre composee de PLUSIEURS colonnes, le type de jointure est")
print("   explicite, et ca ne casse pas quand on insere une colonne.")


# ═══════════════════════════════════════════════════════════════════════════
#  2. LE PIÈGE — l'explosion de lignes
# ═══════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  2. LE PIÈGE — joindre sur une clé qui n'est pas unique")
print("=" * 70)

# On oublie 'mois' dans la cle. Erreur tres facile a faire.
explose = df.merge(budget, on="categorie", how="left")

print(f"\navant : {len(df)} lignes")
print(f"apres : {len(explose)} lignes   <-- x{len(explose) / len(df):.0f}")
print(f"\ntotal juste  : {df['montant'].sum():12,.2f} EUR".replace(",", " "))
print(f"total fausse : {explose['montant'].sum():12,.2f} EUR".replace(",", " "))

print("\n-> Chaque depense a ete dupliquee SIX fois, une par mois du budget.")
print("   Aucune erreur. Aucun avertissement. Juste un total six fois trop")
print("   grand, et parfaitement plausible si on ne le verifie pas.")

print("\nLE REFLEXE, en trois lignes :")
print("""
    avant = len(df)
    df = df.merge(autre, on=[...], how="left")
    assert len(df) == avant, f"explosion : {avant} -> {len(df)}"
""")

# La meme securite, offerte par pandas lui-meme :
print("pandas sait le verifier tout seul avec validate= :")
try:
    df.merge(budget, on="categorie", how="left", validate="many_to_one")
except pd.errors.MergeError as e:
    print(f"    MergeError : {e}")
print("\n-> validate='many_to_one' dit : « la cle doit etre unique a")
print("   droite ». Si elle ne l'est pas, ca PLANTE au lieu de gonfler")
print("   silencieusement. A mettre partout des qu'on y pense.")


# ═══════════════════════════════════════════════════════════════════════════
#  3. Les quatre jointures
# ═══════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  3. Les quatre jointures, sur un exemple minuscule")
print("=" * 70)

depenses = pd.DataFrame(
    {"categorie": ["Logement", "Loisirs", "Voyage"], "reel": [6000, 900, 400]}
)
prevus = pd.DataFrame(
    {"categorie": ["Logement", "Loisirs", "Sante"], "prevu": [6200, 600, 500]}
)

print("\nGAUCHE (le reel)          DROITE (le prevu)")
print("  Logement, Loisirs,        Logement, Loisirs,")
print("  Voyage                    Sante")

for comment in ["inner", "left", "right", "outer"]:
    resultat = depenses.merge(prevus, on="categorie", how=comment)
    presents = ", ".join(resultat["categorie"])
    print(f"\nhow='{comment:5}' -> {len(resultat)} lignes : {presents}")

print("""
-> inner  : seulement ce qui existe des DEUX cotes. Voyage et Sante
            disparaissent, SANS un mot. C'est le defaut de merge, et
            c'est le piege n2.
   left   : tout le reel, complete si possible. Voyage reste, avec un
            NaN visible en face. C'est presque toujours ce qu'on veut.
   right  : l'inverse. Rarement utile : on ecrit plutot le merge dans
            l'autre sens, c'est plus lisible.
   outer  : tout le monde. Utile pour AUDITER : « qu'est-ce qui ne se
            correspond pas ? »
""")

audit = depenses.merge(prevus, on="categorie", how="outer", indicator=True)
print("indicator=True ajoute une colonne qui dit d'ou vient chaque ligne :")
print(audit.to_string(index=False))
print("\n-> 'left_only' = depense sans budget prevu. 'right_only' = budget")
print("   prevu jamais depense. Les deux sont des informations.")


# ═══════════════════════════════════════════════════════════════════════════
#  À TOI
# ═══════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  À TOI")
print("=" * 70)
print("""
  Q1. Ajoute au tableau `fusion` une colonne `ecart` (reel - prevu) et
      une colonne `depassement` (True/False).
  Q2. Combien de couples (categorie, mois) sont en depassement ?
  Q3. Quelle categorie depasse son budget le plus SOUVENT (en nombre de
      mois) ? Est-ce la meme que celle qui depasse le plus en euros ?
  Q4. Fais le merge avec how="inner" et compare le nombre de lignes.
      Que s'est-il passe, et comment l'aurais-tu su ?
  Q5. Cumule reel et prevu par categorie sur les six mois, et calcule
      l'ecart en POURCENTAGE.

Corrections : corrige/reprise/02_joindre.py
""")
