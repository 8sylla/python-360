# Sujet 1 — Streaming & audience

> À partir d'un vrai catalogue **Spotify**, comprendre **ce qui rend un titre
> populaire** et comparer les **genres** par leurs caractéristiques audio.

[← Retour au cahier des charges](README.md)

## Le vrai jeu de données

**[Spotify Tracks Dataset — Kaggle](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset)**
(≈ **114 000 titres**, **125 genres**, un seul fichier `dataset.csv`).

> Kaggle demande un compte gratuit pour télécharger. Sur la page du dataset :
> onglet **Data → Download**.

### Colonnes principales

| Colonne | Description |
|---|---|
| `track_id` | identifiant Spotify du titre |
| `artists`, `album_name`, `track_name` | métadonnées |
| `popularity` | popularité de 0 à 100 |
| `duration_ms` | durée en **millisecondes** |
| `explicit` | contenu explicite (True/False) |
| `danceability`, `energy`, `valence`, `acousticness`, `tempo`, `loudness`… | **caractéristiques audio** (0–1 pour la plupart) |
| `track_genre` | genre |

### Les vrais défauts à nettoyer

- une **colonne d'index parasite** en tête (`Unnamed: 0`) à supprimer ;
- des **doublons** : un même `track_id` apparaît sous plusieurs genres ;
- quelques **valeurs manquantes** (une ligne sans `artists`/`track_name`) ;
- des **durées à 0 ms** et des `popularity` à 0 à questionner.

## Les trois livrables, appliqués à ce dataset

### v1 — Fondations & NumPy (25 %)

- Lire le CSV **sans pandas**, ignorer la colonne d'index parasite.
- `popularity` et `duration_ms` → **tableaux NumPy** ; convertir la durée en
  **minutes** (`/ 60000`).
- Retirer les lignes à `duration_ms == 0` ; gérer la ligne aux champs vides.
- Stats NumPy : popularité **moyenne/médiane**, durée **moyenne**, danceability
  **min/max**.

### v2 — Exploration pandas (35 %)

- **DataFrame**, `drop_duplicates(subset="track_id")`.
- Segmenter : titres **très populaires** (`popularity > 70`).
- `groupby("track_genre")` → **popularité moyenne et énergie moyenne par
  genre** ; `pivot_table` **genre × explicit**.
- Export du **top 15 des genres** par popularité moyenne.

### Finale — Data-viz & appli (40 %)

- **4 graphiques** : histogramme de `popularity`, **nuage de points
  `energy` × `danceability`** (corrélation), boxplot de `popularity` pour les
  10 genres les plus fréquents, barres du **top genres**.
- **Appli à menu** : `1. Statistiques` · `2. Genres les plus populaires` ·
  `3. Corrélation énergie/danceabilité` · `4. Exporter` · `5. Quitter`.

## Pistes d'analyse

- Les titres **dansants** sont-ils plus **populaires** ?
- Quel **genre** a la meilleure popularité moyenne ?
- Les titres **explicites** sont-ils plus populaires que les autres ?

---

*Critères d'évaluation, format des rendus et soutenance (pitch de 5 min) :
voir le [cahier des charges commun](README.md).*
