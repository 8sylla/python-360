# Le portail de la formation

Le site public, déployé sur GitHub Pages : <https://8sylla.github.io/python-360/>

HTML, CSS et JavaScript à la main. Aucune dépendance, aucun outil de build,
rien chargé depuis un service extérieur au moment de l'affichage.

```
portail/
├── index.html          la page (une seule)
├── css/style.css       toute l'apparence
├── js/seances.js       ← le seul fichier à modifier au quotidien
├── js/app.js           écrit le planning et la rangée d'outils
├── assets/             logo, photo, logos des outils
├── fichiers/           les PDF et corrigés à télécharger
└── .nojekyll           dit à GitHub de servir les fichiers tels quels
```

---

## 1. Publier une ressource

**Déposer le fichier** dans `portail/fichiers/`, puis **ajouter son lien**
dans `js/seances.js` :

```js
{
  numero: 0,
  titre: "Kit de démarrage",
  date: "2026-08-15",
  duree: "2 h 30",
  liens: {
    slides: "fichiers/00-kit-demarrage.pdf",
  },
},
```

Pousser sur `main`. Le lien apparaît en une minute.

### Les quatre ressources possibles

| Clé | Ce que c'est | Forme |
|---|---|---|
| `slides` | le PDF de projection | `"fichiers/00-kit-demarrage.pdf"` |
| `notebook` | le point de reprise | une URL Colab, de préférence |
| `corrige` | le corrigé, publié après la séance | un chemin ou une URL |
| `video` | l'enregistrement | une URL |

Pour le notebook, l'ouverture directe dans Colab évite un téléchargement :

```js
notebook: "https://colab.research.google.com/github/8sylla/python-360/blob/main/seances/s03-ranger-l-information/reprise.ipynb",
```

### Aucune n'est obligatoire

Une clé absente n'affiche rien. **Une séance dont la vidéo n'a pas été
enregistrée montre simplement ses slides** — pas de bouton grisé, pas de
mention « à venir » qui laisserait croire à un oubli.

Une séance sans aucune ressource affiche une ligne discrète :
« Support en préparation » si la date est passée, « Séance à venir » sinon.

---

## 2. Marquer une séance comme faite — c'est automatique

**Il n'y a rien à valider, rien à cocher.** Une séance est considérée comme
faite dès que **sa date est passée**. Le site compare `date` à la date du
jour, à chaque ouverture de la page.

Une séance passée se distingue de deux façons, discrètement : sa puce
`S0` passe au vert, et sa carte prend le fond papier au lieu du blanc.

```js
date: "2026-08-15",   // ← la seule chose qui décide
```

### Ce que ça implique

| Situation | Ce qu'il faut faire |
|---|---|
| La séance a eu lieu comme prévu | **Rien.** |
| La séance est reportée | Changer `date`. Tout suit. |
| La séance a duré plus longtemps | Changer `duree`. |
| Vous voulez publier les slides | Ajouter le lien (voir §1) — c'est indépendant. |

**Publier une ressource et marquer une séance comme faite sont deux choses
séparées.** Une séance peut être passée sans support publié, et un support
peut être publié à l'avance pour une séance à venir.

### Et la fin de la formation ?

Il n'y a pas d'état « formation terminée » à déclencher. Quand la dernière
date est passée, les neuf cartes sont vertes — c'est tout ce que le site a
besoin de savoir.

---

## 3. Les dates

`date` s'écrit au format **`AAAA-MM-JJ`**, et rien d'autre. Le jour de la
semaine et le mois sont calculés à l'affichage.

```js
date: "2026-09-02",   // s'affiche : « 2 sept. — mercredi »
```

Le rythme de la formation est mercredi / samedi en alternance :

| | | |  | | | |
|---|---|---|---|---|---|---|
| S0 | sam. 15 août | 2 h 30 | | S5 | mer. 2 sept. | 3 h |
| S1 | mer. 19 août | 3 h | | S6 | sam. 5 sept. | 3 h |
| S2 | sam. 22 août | 3 h | | S7 | mer. 9 sept. | 3 h |
| S3 | mer. 26 août | 3 h | | S8 | sam. 12 sept. | 3 h |
| S4 | sam. 29 août | 3 h | | | | |

---

## 4. Déployer

Le workflow `.github/workflows/pages.yml` s'en charge : à chaque `push` sur
`main` qui touche `portail/`, le site se reconstruit. Rien à lancer à la
main.

Pour travailler en local, ouvrir `index.html` en double-cliquant suffit — il
n'y a ni `fetch` ni module. Pour être au plus près du rendu final :

```bash
python -m http.server 8765 --directory portail
```

---

## 5. L'apparence

Les couleurs et les polices sont celles des slides, à l'identique : le site
et les supports doivent se ressembler. Tout est déclaré dans `:root`, en
haut de `css/style.css`.

```css
--papier: #FBF8F7;   /* le fond             */
--encre:  #1A0C0A;   /* le texte            */
--gris:   #74655F;   /* le texte secondaire */
--rouge:  #D81B27;   /* l'accent            */
```

Playfair Display pour les titres, Montserrat pour le texte, JetBrains Mono
pour les dates et les numéros.

Le planning est une **grille** : trois colonnes sur grand écran, deux sur
tablette, une sur téléphone. C'est `auto-fill` qui décide, il n'y a aucune
valeur de rupture à maintenir.

### Les logos

`assets/logos/` contient les six logos des outils, en SVG, servis depuis le
dépôt. Ils viennent de [devicon](https://devicon.dev) et de
[simple-icons](https://simpleicons.org), tous deux libres. Aucun appel à un
service tiers au chargement : si l'un d'eux disparaît, le site ne bouge pas.
