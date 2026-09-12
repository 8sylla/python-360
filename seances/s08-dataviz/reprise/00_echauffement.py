"""ÉCHAUFFEMENT — sept prédictions avant de lancer quoi que ce soit.

Règle du jeu : pour chaque bloc, écris ta réponse sur un papier AVANT
d'exécuter. Le but n'est pas d'avoir raison, c'est de savoir où tu hésites.

    python 00_echauffement.py

Les sept blocs sont les sept pièges de la séance. Aucun n'est artificiel :
tous ont fait perdre une soirée à quelqu'un.
"""

import matplotlib
import pandas as pd

matplotlib.use("Agg")  # pas de fenetre : on veut juste que ca tourne
import matplotlib.pyplot as plt  # noqa: E402

print("=" * 70)
print("  ÉCHAUFFEMENT — écris ta réponse avant de lire la sortie")
print("=" * 70)


# ── 1 ──────────────────────────────────────────────────────────────────────
# groupby rend-il un DataFrame ou une Series ?
ventes = pd.DataFrame(
    {
        "categorie": ["A", "A", "B", "B", "C"],
        "montant": [10.0, 20.0, 5.0, 15.0, 30.0],
    }
)

print("\n[1] Que rend df.groupby('categorie')['montant'].sum() ?")
resultat = ventes.groupby("categorie")["montant"].sum()
print(f"    type   : {type(resultat).__name__}")
print(f"    index  : {list(resultat.index)}")
print("    -> une SERIES indexée par la catégorie, pas un DataFrame.")
print("       C'est pour ça que seaborn exige un .reset_index() derrière :")
print("       il dessine des COLONNES, pas des index.")


# ── 2 ──────────────────────────────────────────────────────────────────────
print("\n[2] Combien de lignes après ce merge ?")
gauche = pd.DataFrame({"cle": ["x", "y"], "valeur": [1, 2]})
droite = pd.DataFrame({"cle": ["x", "x", "x", "y"], "info": ["a", "b", "c", "d"]})

fusion = gauche.merge(droite, on="cle")
print(f"    gauche : {len(gauche)} lignes")
print(f"    droite : {len(droite)} lignes")
print(f"    fusion : {len(fusion)} lignes   <-- PLUS que gauche")
print("    -> la clé 'x' apparaît 3 fois à droite : la ligne 'x' de gauche")
print("       est dupliquée 3 fois. Aucun avertissement.")
print("       LE réflexe : compter les lignes avant et après. Toujours.")


# ── 3 ──────────────────────────────────────────────────────────────────────
print("\n[3] inner ou left : quelle différence, concrètement ?")
budget = pd.DataFrame({"cle": ["x"], "prevu": [100]})
print(f"    inner : {len(gauche.merge(budget, on='cle', how='inner'))} ligne(s)")
print(f"    left  : {len(gauche.merge(budget, on='cle', how='left'))} ligne(s)")
print("    -> inner a fait DISPARAÎTRE la ligne 'y', sans le dire.")
print("       Sur un relevé, c'est une dépense perdue. how='left' la garde,")
print("       avec un NaN visible à la place du budget manquant.")


# ── 4 ──────────────────────────────────────────────────────────────────────
print("\n[4] plt.bar() ou ax.bar() : pourquoi ça compte ?")
fig, (a1, a2) = plt.subplots(1, 2)
a1.bar(["A", "B"], [3, 5])
a2.bar(["A", "B"], [5, 3])
print(f"    fig contient {len(fig.axes)} Axes.")
print("    -> avec plt.bar(), sur QUEL des deux aurait-on dessiné ?")
print("       Réponse : sur « le graphique courant », c'est-à-dire le")
print("       dernier créé. Invisible dans le code, donc impraticable.")
plt.close(fig)


# ── 5 ──────────────────────────────────────────────────────────────────────
print("\n[5] Que vaut la moyenne ici, et que vaut la médiane ?")
loyers = pd.Series([40.0, 55.0, 60.0, 45.0, 900.0])
print(f"    moyenne : {loyers.mean():.0f}")
print(f"    mediane : {loyers.median():.0f}")
print("    -> une seule grosse valeur déplace la moyenne de 50 à 220.")
print("       La médiane, elle, ne bouge pas. Quand les deux s'écartent,")
print("       c'est le signal qu'il y a des valeurs extrêmes.")


# ── 6 ──────────────────────────────────────────────────────────────────────
print("\n[6] Un axe qui ne part pas de zéro : de combien mens-tu ?")
valeurs = [98.0, 100.0, 102.0]
etendue_vraie = (max(valeurs) - min(valeurs)) / min(valeurs) * 100
print(f"    écart réel entre la plus petite et la plus grande : {etendue_vraie:.0f} %")
print("    -> mais si l'axe part de 97, la barre de droite paraît 2,5 fois")
print("       plus haute que celle de gauche. L'écart visuel est de 150 %")
print("       pour un écart réel de 4 %. Ce n'est pas une erreur : c'est")
print("       un choix, et il t'engage.")


# ── 7 ──────────────────────────────────────────────────────────────────────
print("\n[7] Trier par ordre alphabétique, ou par valeur ?")
scores = pd.DataFrame(
    {"pays": ["Algerie", "Benin", "Cameroun"], "note": [12.0, 45.0, 8.0]}
)
print("    alphabetique :", list(scores["pays"]))
print("    par valeur   :", list(scores.sort_values("note", ascending=False)["pays"]))
print("    -> l'ordre alphabétique n'apporte AUCUNE information : il oblige")
print("       le lecteur à comparer les longueurs de barres lui-même.")
print("       Exception : les mois, les tranches d'âge — tout ce qui a")
print("       déjà un ordre naturel.")


print("\n" + "=" * 70)
print("  Combien de fois as-tu hésité ? C'est exactement le programme.")
print("=" * 70)
