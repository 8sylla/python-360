"""CORRIGÉ — 05_tableau_de_bord.py

La Q1 est le cœur de la séance, et elle ne contient pas de code.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.axes import Axes

DATA = Path(__file__).resolve().parents[4] / "data"
FIGURES = Path(__file__).parent / "figures"
FIGURES.mkdir(exist_ok=True)

ACCENT, NEUTRE, VERT = "#C1121F", "#8B7B78", "#2C8A1A"

df = pd.read_csv(DATA / "releve_propre.csv", parse_dates=["date_operation"])
budget = pd.read_csv(DATA / "budget_prevu.csv", sep=";")
sns.set_theme(style="whitegrid", font_scale=1.05)


def euros(x: float) -> str:
    return f"{x:,.0f} €".replace(",", " ")


# ── Q1 ─────────────────────────────────────────────────────────────────────
print("""Q1. LES QUATRE TITRES

    Descriptif  ->  « Depenses par categorie »
    Le message  ->  « Le logement absorbe 61 % du budget a lui seul »

    Descriptif  ->  « Distribution des montants »
    Le message  ->  « 80 % des depenses sont sous 150 EUR, mais la
                      moyenne est tiree par les loyers »

    Descriptif  ->  « Reel contre prevu »
    Le message  ->  « Les loisirs depassent le budget de 30 % »

    Descriptif  ->  « Evolution mensuelle »
    Le message  ->  « 4 mois sur 6 depassent le budget prevu »

    Ce qui change, concretement : dans la colonne de gauche, le lecteur
    doit faire le travail. Dans celle de droite, il est fait.

    Le test : si tu peux remplacer ton titre par le nom de la colonne
    de l'axe des ordonnees sans rien perdre, ce n'est pas un titre.
""")


# ── Q2 ─────────────────────────────────────────────────────────────────────
print("""Q2. LE TEXTE ECRIT EN DUR

    Les deux coupables etaient des NOMS, pas des nombres :

      1. « Le logement absorbe ... »   -> le nom de la categorie n1
      2. « ... tiree par les loyers »  -> l'interpretation de la queue

    Le premier se calcule ; le second est un jugement qui demande de
    connaitre les donnees. Regle pratique : on calcule ce qui est
    factuel, on assume par ecrit ce qui est interpretatif.
""")

table = (
    df.groupby("categorie")["montant"].sum()
    .sort_values(ascending=False).reset_index(name="total")
)
tete = table["categorie"].iloc[0]
part = table["total"].iloc[0] / table["total"].sum() * 100
print(f"    Version calculee : « Le {tete.lower()} absorbe "
      f"{part:.0f} % du budget a lui seul »\n")


# ── Q4 (la fonction) ───────────────────────────────────────────────────────
def panneau_categories(donnees: pd.DataFrame, ax: Axes) -> Axes:
    """Panneau 1, en fonction. `ax` est un ARGUMENT, pas une creation."""
    t = (
        donnees.groupby("categorie")["montant"].sum()
        .sort_values(ascending=False).reset_index(name="total")
    )
    p = t["total"].iloc[0] / t["total"].sum() * 100
    ax.barh(t["categorie"], t["total"],
            color=[ACCENT] + [NEUTRE] * (len(t) - 1))
    ax.invert_yaxis()
    ax.set_title(f"Le {t['categorie'].iloc[0].lower()} absorbe {p:.0f} % "
                 "du budget à lui seul", loc="left", weight="bold")
    ax.set_xlabel("Total dépensé sur six mois (€)")
    ax.set_xlim(0, t["total"].max() * 1.22)
    for y, v in enumerate(t["total"]):
        ax.text(v + t["total"].max() * 0.02, y, euros(v), va="center",
                fontsize=9)
    return ax


def panneau_repartition(donnees: pd.DataFrame, ax: Axes) -> Axes:
    mediane, moyenne = donnees["montant"].median(), donnees["montant"].mean()
    sous = (donnees["montant"] < 150).mean() * 100
    sns.histplot(data=donnees, x="montant", bins=30, ax=ax, color=NEUTRE)
    ax.axvline(mediane, color=ACCENT, linewidth=2,
               label=f"médiane {euros(mediane)}")
    ax.axvline(moyenne, color=ACCENT, linestyle="--", linewidth=2,
               label=f"moyenne {euros(moyenne)}")
    ax.set_title(f"{sous:.0f} % des dépenses sont sous 150 €,\n"
                 "mais la moyenne est tirée par les loyers",
                 loc="left", weight="bold")
    ax.set_xlabel("Montant d'une dépense (€)")
    ax.set_ylabel("Nombre de dépenses")
    ax.legend()
    return ax


def panneau_ecart(donnees: pd.DataFrame, prevu: pd.DataFrame, ax: Axes) -> Axes:
    reel = donnees.groupby(["categorie", "mois"])["montant"].sum()
    reel = reel.reset_index(name="reel")
    croise = reel.merge(prevu, on=["categorie", "mois"], how="left")
    assert len(croise) == len(reel), "explosion de lignes !"
    bilan = croise.groupby("categorie")[["reel", "budget_prevu"]].sum()
    bilan["pct"] = (bilan["reel"] / bilan["budget_prevu"] - 1) * 100
    bilan = bilan.sort_values("pct")

    ax.barh(bilan.index, bilan["pct"],
            color=[ACCENT if e > 0 else VERT for e in bilan["pct"]])
    ax.axvline(0, color="#444", linewidth=1.2)
    pire = bilan.iloc[-1]
    ax.set_title(f"Les {bilan.index[-1].lower()} dépassent le budget "
                 f"de {pire['pct']:.0f} %", loc="left", weight="bold")
    ax.set_xlabel("Écart au budget prévu (%)   —   négatif = tenu")
    limite = bilan["pct"].abs().max() * 1.3
    ax.set_xlim(-limite, limite)
    return ax


def panneau_evolution(donnees: pd.DataFrame, prevu: pd.DataFrame,
                      ax: Axes) -> Axes:
    reel = donnees.groupby("mois")["montant"].sum().reset_index(name="total")
    cible = prevu.groupby("mois")["budget_prevu"].sum().reset_index()
    suivi = reel.merge(cible, on="mois", how="left")
    ax.plot(suivi["mois"], suivi["total"], marker="o", color=ACCENT,
            linewidth=2.5, label="Dépensé")
    ax.plot(suivi["mois"], suivi["budget_prevu"], marker="o", color=NEUTRE,
            linestyle="--", linewidth=2, label="Prévu")
    n = int((suivi["total"] > suivi["budget_prevu"]).sum())
    ax.set_title(f"{n} mois sur {len(suivi)} dépassent le budget prévu",
                 loc="left", weight="bold")
    ax.set_ylabel("Total du mois (€)")
    ax.set_ylim(0, suivi[["total", "budget_prevu"]].to_numpy().max() * 1.15)
    ax.legend()
    return ax


def panneau_heatmap(donnees: pd.DataFrame, ax: Axes) -> Axes:
    croise = donnees.pivot_table(index="categorie", columns="mois",
                                 values="montant", aggfunc="sum",
                                 fill_value=0)
    sns.heatmap(croise, ax=ax, cmap="Reds", annot=True, fmt=".0f",
                cbar=False, linewidths=0.5, annot_kws={"fontsize": 8})
    ecart = croise.div(croise.median(axis=1), axis=0)
    cat, mois = ecart.stack().idxmax()
    ax.set_title(f"{mois} « {cat} » : {ecart.loc[cat, mois]:.1f}x "
                 "son mois médian", loc="left", weight="bold")
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.tick_params(axis="y", rotation=0)
    return ax


# ── Q3 : le cinquième panneau, en 3x2 ──────────────────────────────────────
print("Q3 + Q4. Cinq panneaux, en 3x2, avec des fonctions.")

fig, axes = plt.subplots(3, 2, figsize=(16, 16))
panneau_categories(df, axes[0, 0])
panneau_repartition(df, axes[0, 1])
panneau_ecart(df, budget, axes[1, 0])
panneau_evolution(df, budget, axes[1, 1])
panneau_heatmap(df, axes[2, 0])
axes[2, 1].axis("off")  # une case vide vaut mieux qu'un panneau de remplissage

total = f"{df['montant'].sum():,.0f}".replace(",", " ")
fig.suptitle(f"MonBudget — six mois, {len(df)} dépenses, {total} €",
             fontsize=17, weight="bold")
fig.tight_layout(rect=(0, 0, 1, 0.98))
fig.savefig(FIGURES / "q3_cinq_panneaux.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("""    -> ecrit : figures/q3_cinq_panneaux.png

       3x2 ou 2x3 ? Sur un videoprojecteur 16/9, c'est 2x3 qui gagne
       (large et peu haut). Mais pour un document A4 ou un ecran qu'on
       fait defiler, 3x2 est meilleur. Le format cible decide, pas le
       gout.

       Et la case vide : `axes[2, 1].axis("off")`. Une case vide est
       plus honnete qu'un panneau ajoute pour remplir. La regle 5 dit
       « une question, un graphique » — elle interdit aussi le
       graphique sans question.

       Q4 : pourquoi passer `ax` en argument ?

         def panneau(donnees, ax):       # se compose partout
         def panneau(donnees):           # cree sa figure -> inutilisable
             fig, ax = plt.subplots()      dans un tableau de bord

       Une fonction qui cree sa propre figure ne peut pas etre
       reutilisee. Une fonction qui recoit son `ax` marche seule ET
       dans une grille. C'est la meme idee que « une fonction rend une
       valeur, elle n'affiche pas » de la seance 4.
""")


# ── Q5 ─────────────────────────────────────────────────────────────────────
print("Q5. SVG contre PNG.")

fig, ax = plt.subplots(figsize=(9, 5))
panneau_categories(df, ax)
fig.tight_layout()
fig.savefig(FIGURES / "q5_export.png", dpi=150, bbox_inches="tight")
fig.savefig(FIGURES / "q5_export.svg", bbox_inches="tight")
plt.close(fig)

png = (FIGURES / "q5_export.png").stat().st_size // 1024
svg = (FIGURES / "q5_export.svg").stat().st_size // 1024
print(f"""    q5_export.png : {png} ko
    q5_export.svg : {svg} ko

    -> Zoome a 400 % : le PNG pixelise, le SVG reste net. Le SVG
       contient les FORMES (« un rectangle de tant sur tant »), le PNG
       contient des pixels.

       Que montrer a un client ?
         - dans un rapport imprime ou une slide  -> SVG (ou PDF)
         - dans un mail, un site, Slack          -> PNG (partout lisible)
         - dans les deux cas                     -> exporte les deux,
                                                    ca coute une ligne.

       Le piege du SVG : sur un nuage de 300 000 points, il devient
       enorme et lent a ouvrir. Au-dela de quelques milliers de
       formes, le PNG a dpi eleve est le bon choix.
""")
