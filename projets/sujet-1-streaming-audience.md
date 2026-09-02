# Sujet 1 — Streaming & audience

> Comprendre les habitudes d'écoute d'une plateforme type **Netflix / Spotify**
> et améliorer les recommandations.

[← Retour au cahier des charges](README.md)

## Contexte & problématique

Une plateforme de streaming enregistre chaque lecture (film ou morceau). Ces
journaux sont riches mais **sales** : notes manquantes, sessions dupliquées,
appareils non renseignés. La question métier :

> **Comment optimiser les recommandations et comprendre les habitudes d'écoute
> des utilisateurs ?**

## Le jeu de données

Exemple fourni : [`ressources/sujet-1-streaming-exemple.csv`](ressources/sujet-1-streaming-exemple.csv)
(18 lignes pour voir la forme ; le vrai fichier fera **≥ 1 000 lignes**).

| Colonne | Type | Description |
|---|---|---|
| `User_ID` | texte | identifiant de l'utilisateur |
| `Track_Movie_Name` | texte | titre du contenu écouté / regardé |
| `Genre` | texte | genre (Pop, Drame, Science-fiction…) |
| `Duration_Minutes` | entier | durée de la session, en minutes |
| `Device_Used` | texte | appareil (Mobile, TV, Web, Tablette) |
| `Date_Watched` | date | date de visionnage (AAAA-MM-JJ) |
| `User_Rating` | décimal | note laissée (1 à 5), souvent absente |

**Défauts injectés à nettoyer :** notes (`User_Rating`) et titres/appareils
**manquants**, et **sessions dupliquées** (mêmes lignes répétées).

## Les trois livrables, appliqués à ce sujet

### v1 — Fondations & NumPy (25 %)

- Lire le CSV **sans pandas** (`open()`, `split(",")`) en gérant les cellules
  vides.
- `Duration_Minutes` et `User_Rating` → **tableaux NumPy**.
- Remplacer les **notes manquantes** par la **moyenne** des notes.
- Stats NumPy : durée **moyenne/médiane** d'écoute, note **moyenne**, durée
  **min/max**.

### v2 — Exploration pandas (35 %)

- Charger dans un **DataFrame**, **supprimer les doublons** (`drop_duplicates`).
- Segmenter : les utilisateurs qui écoutent **plus de 2 h au total**.
- `groupby("Genre")` → **durée moyenne et note moyenne par genre** ;
  `pivot_table` **Genre × Device_Used**.
- Export du tableau « note moyenne par genre » en CSV propre.

### Finale — Data-viz & appli (40 %)

- **4 graphiques** : histogramme des durées, barres de la **note moyenne par
  genre**, camembert de la **répartition par appareil**, courbe du **nombre de
  vues par jour**.
- **Appli à menu** : `1. Top genres` · `2. Graphique par appareil` ·
  `3. Exporter les notes moyennes` · `4. Quitter`.

## Pistes d'analyse

- Quel **genre** retient le plus longtemps ? Est-il aussi le mieux noté ?
- L'appareil (**TV vs Mobile**) change-t-il la durée d'écoute ?
- Y a-t-il des **pics** certains jours de la semaine ?

---

*Critères d'évaluation, format des rendus et soutenance (pitch de 5 min) :
voir le [cahier des charges commun](README.md).*
