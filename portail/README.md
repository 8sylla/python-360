# Le portail de la formation

Le site public de la Formation Python 360°, déployé sur **GitHub Pages**.
HTML, CSS et JavaScript à la main — aucune dépendance, aucun outil de build.

```
portail/
├── index.html          la page (une seule)
├── css/style.css       toute l'apparence
├── js/seances.js       ← LE SEUL FICHIER À MODIFIER pour publier
├── js/app.js           les cartes, les filtres, la progression
├── fichiers/           les PDF, notebooks et corrigés à télécharger
└── .nojekyll           dit à GitHub de servir les fichiers tels quels
```

---

## Publier une séance — la seule manœuvre courante

Tout se joue dans **`js/seances.js`**. Chaque séance y est un objet ; il
suffit de remplacer `null` par un chemin.

**1.** Dépose le fichier dans `portail/fichiers/` :

```
portail/fichiers/00-kit-demarrage.pdf
```

**2.** Ouvre `js/seances.js` et remplis la ligne correspondante :

```js
liens: {
  slides:   "fichiers/00-kit-demarrage.pdf",   // ← au lieu de null
  notebook: null,
  corrige:  null,
  replay:   null,
},
```

**3.** Pousse. Le bouton s'allume tout seul, et la séance entre dans le
filtre « Déjà publiées ».

Tant qu'une valeur vaut `null`, le bouton reste grisé avec la mention
« à venir » : le visiteur voit que la ressource existe et qu'elle arrive,
plutôt que de se demander s'il a raté quelque chose.

### Les liens acceptés

| Clé | Ce que c'est | Forme attendue |
|---|---|---|
| `slides` | le PDF de projection | `"fichiers/03-ranger.pdf"` |
| `notebook` | le point de reprise, ouvert dans Colab | une URL `colab.research.google.com/github/...` |
| `corrige` | le corrigé, publié après la séance | un chemin ou une URL |
| `replay` | l'enregistrement | une URL (s'ouvre dans un nouvel onglet) |

Le notebook s'ouvre le mieux directement dans Colab :

```js
notebook: "https://colab.research.google.com/github/8sylla/python-360/blob/main/seances/s03-ranger-l-information/reprise.ipynb",
```

---

## Déployer

Le dépôt contient déjà le workflow `.github/workflows/pages.yml`. Une seule
chose à faire, **une fois** :

> **Settings ▸ Pages ▸ Source** → choisir **GitHub Actions**

À chaque `push` sur `main` qui touche `portail/`, le site se reconstruit.
L'adresse sera :

```
https://8sylla.github.io/python-360/
```

---

## Travailler dessus en local

Ouvrir `index.html` en double-cliquant fonctionne : il n'y a ni `fetch`
ni module, tout est chargé par de simples balises `<script>`.

Pour être au plus près du rendu final, on peut quand même servir le dossier :

```bash
python -m http.server 8765 --directory portail
```

puis ouvrir `http://localhost:8765`.

---

## Changer les couleurs

Toute la palette est déclarée en haut de `css/style.css`, dans `:root`.
Elle reprend celle des slides — rouge `#D81B27`, or `#FDC911`, sur le fond
sombre de la diapo « présentateur ». Modifier une variable la change
partout :

```css
:root {
  --rouge: #F0323E;   /* l'accent */
  --or:    #FDC911;   /* les jalons, l'arc 2 */
  --fond:  #0E0F13;   /* le fond de page */
}
```

---

## Ce que fait `app.js`

Trois choses, et rien d'autre :

1. **Fabriquer les cartes** à partir de `SEANCES`, dans `seances.js`.
2. **Filtrer** — toutes / arc 1 / arc 2 / déjà publiées.
3. **Retenir** ce que le visiteur coche comme « fait », dans le
   `localStorage` de son navigateur. Rien n'est envoyé nulle part : c'est
   une commodité de lecture, pas un suivi.

Le code est commenté en français et tient en 130 lignes. Il est fait pour
être lu par les apprenants qui voudront regarder comment le site marche —
c'est aussi à ça qu'il sert.
