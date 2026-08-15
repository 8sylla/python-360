# Le portail de la formation

Le site public de la Formation Python 360°, déployé sur **GitHub Pages**.
HTML, CSS et JavaScript à la main — aucune dépendance, aucun outil de build,
rien chargé depuis un service extérieur au moment de l'affichage.

```
portail/
├── index.html          la page (une seule)
├── css/style.css       toute l'apparence
├── js/seances.js       ← LE SEUL FICHIER À MODIFIER
├── js/app.js           écrit le planning et la rangée d'outils
├── assets/             le logo ASEGUIM, la photo, les logos des outils
├── fichiers/           les PDF et corrigés à télécharger
└── .nojekyll           dit à GitHub de servir les fichiers tels quels
```

---

## Publier une ressource

Tout se joue dans **`js/seances.js`**.

**1.** Déposer le fichier dans `portail/fichiers/` :

```
portail/fichiers/00-kit-demarrage.pdf
```

**2.** Ajouter son lien à la séance :

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

**3.** Pousser. Le lien apparaît.

### Les ressources sont facultatives

Une clé absente n'affiche rien. Une séance dont la vidéo n'a pas été
enregistrée montre simplement ses slides — pas de bouton grisé, pas de
« à venir » qui laisserait croire à un oubli.

| Clé | Ce que c'est |
|---|---|
| `slides` | le PDF de projection |
| `notebook` | le point de reprise — de préférence une URL Colab |
| `corrige` | le corrigé, publié après la séance |
| `video` | l'enregistrement |

Pour le notebook, l'ouverture directe dans Colab est la plus pratique :

```js
notebook: "https://colab.research.google.com/github/8sylla/python-360/blob/main/seances/s03-ranger-l-information/reprise.ipynb",
```

### Les dates

`date` s'écrit au format `AAAA-MM-JJ`. Le jour de la semaine et le mois sont
calculés à l'affichage — rien à écrire en toutes lettres. Une séance dont la
date est passée se marque toute seule.

---

## Déployer

Le workflow `.github/workflows/pages.yml` s'en charge. À chaque `push` sur
`main` qui touche `portail/`, le site se reconstruit.

```
https://8sylla.github.io/python-360/
```

---

## Travailler dessus en local

Ouvrir `index.html` en double-cliquant fonctionne : il n'y a ni `fetch` ni
module. Pour être au plus près du rendu final :

```bash
python -m http.server 8765 --directory portail
```

---

## Les couleurs et les polices

Elles sont celles des slides, à l'identique — c'est voulu : le site et les
supports doivent se ressembler. Tout est déclaré dans `:root`, en haut de
`css/style.css`.

```css
--papier: #FBF8F7;   /* le fond            */
--encre:  #1A0C0A;   /* le texte           */
--gris:   #74655F;   /* le texte secondaire */
--rouge:  #D81B27;   /* l'accent           */
```

Playfair Display pour les titres, Montserrat pour le texte, JetBrains Mono
pour les dates et les numéros. Les mêmes que sur les diapositives.

---

## Les logos

`assets/logos/` contient les six logos des outils, en SVG, servis depuis le
dépôt. Ils viennent de [devicon](https://devicon.dev) et
[simple-icons](https://simpleicons.org), tous deux libres. Aucun appel à un
CDN au chargement de la page : si un service tiers disparaît, le site ne
bouge pas.
