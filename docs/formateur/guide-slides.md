# Les diapositives — Formation Python 360° · ASEGUIM

**212 diapositives, 12 decks, une seule identité.**

```
slides/
├── theme.css        ← LA CLASSE. Toute l'identité tient ici.
├── moteur.js        ← navigation, notes, auto-ajustement
├── assets/          ← le logo ASEGUIM
├── modele.html      ← la vitrine des 12 gabarits
├── 00-kit-demarrage.html          8 diapos
├── 01-parler-a-la-machine.html   17
├── 02-decider-et-repeter.html    18
├── 03-ranger-l-information.html  18
├── 04-fabriquer-ses-outils.html  17
├── 05-poo.html                   16
├── 06-python-avance.html         19
├── 07-numpy-pandas.html          20
├── 08-dataviz.html               19
└── 11-production.html            21
```

Ouvre n'importe quel fichier `.html` dans un navigateur. **Garde le dossier
entier** : les decks partagent `theme.css`, `moteur.js` et le logo.

---

## Pendant la présentation

| Touche | Effet |
|---|---|
| `→` `Espace` | Diapo suivante |
| `←` | Diapo précédente |
| `F` | Plein écran |
| `N` | **Notes du présentateur** — bandeau bas, à ne pas projeter |
| `Début` / `Fin` | Première / dernière diapo |
| `Ctrl+P` | Export PDF, une diapo par page |

Un clic à droite avance, à gauche recule. L'adresse se termine par `#7` : tu
peux reprendre exactement où tu en étais, ou envoyer un lien vers une diapo
précise.

**Les notes valent le détour.** Elles contiennent ce que le guide formateur
disait de faire à ce moment précis : quelle erreur provoquer, quelle phrase
dire mot pour mot, quel piège annoncer avant qu'il ne survienne.

---

## L'identité, relevée sur le logo

| Jeton | Valeur | Usage |
|---|---|---|
| `--rouge` | `#D81B27` | L'accent : le mot important, le danger |
| `--or` | `#FDC911` | La progression, les jalons. **Jamais pour du texte** |
| `--vert` | `#185609` | La bonne pratique, le validé, le passage à l'action |
| `--bordeaux` | `#6E0A12` | Profondeur des fonds rouges |
| `--papier` | `#FBF8F7` | Fond des diapos claires |
| `--encre` | `#1A0C0A` | Texte — un noir à sous-ton rouge |

Les trois couleurs de la Guinée, mais chacune avec **un rôle** :
le rouge signale le danger, le vert signale l'action juste, l'or marque
l'avancement. Ce n'est jamais décoratif — c'est ce qui permet de comprendre
une diapo avant même de l'avoir lue.

**Changer une valeur dans `theme.css` la change dans les 12 decks.**

---

## Les 12 gabarits

Ouvre `modele.html` : chaque gabarit y est montré une fois.

| `data-type` | Quand | Texte max |
|---|---|---|
| `couverture` | Ouvrir la séance | titre + 3 métadonnées |
| `section` | Ouvrir une partie | numéro + titre + une ligne |
| `idee` | **Le gabarit par défaut** | **12 mots** |
| `chiffre` | Un nombre qui frappe | le nombre + 8 mots |
| `analogie` | Pictogramme + concept | 2 phrases |
| `duel` | Avant/après, ✗ vs ✓ | 3 lignes par volet |
| `code` | Un extrait | **12 lignes** |
| `etapes` | Un processus | 2 à 4 étapes |
| `alerte` | Le piège | une phrase |
| `formule` | Une formule | formule + traduction |
| `liste` | 3 à 5 points | une ligne chacun |
| `tuiles` | 4 notions parallèles | une ligne chacune |
| `exercice` | À eux de jouer (fond vert) | 4 consignes |
| `regle` | La phrase à retenir | une phrase |
| `fin` | Questions | — |

### Les 16 pictogrammes

`boite` `repertoire` `recette` `aiguillage` `boucle` `machine` `moule`
`prise` `ticket` `cadeau` `tableau` `imbrique` `passeplat` `carton`
`plateau` `ceinture`

Tous au même trait, une seule couleur, aucun aplat.

---

## Modifier une séance

Le contenu n'est pas écrit à la main dans le HTML : il est **généré**.

```
source/
├── moteur_slides.py   ← thème, gabarits, pictogrammes (la classe)
├── contenu.py         ← les 12 decks (les objets)
└── modele.py          ← la vitrine
```

Pour changer une diapo : tu modifies `contenu.py`, tu relances
`python contenu.py`, les 12 fichiers HTML sont réécrits. Pour changer
l'identité : tu modifies le bloc `:root` de `THEME` dans `moteur_slides.py`.

Tu peux aussi éditer directement le HTML si tu préfères — c'est du HTML
lisible, une `<section>` par diapo.

---

## L'auto-ajustement

Le moteur mesure chaque titre au moment de l'affichage. Si une ligne déborde
et se replie toute seule, ou si le bloc dépasse la hauteur disponible, **le
corps est réduit automatiquement** jusqu'à ce que ça tienne. Idem pour les
blocs de code, en largeur comme en hauteur.

Conséquence pratique : tu peux écrire un titre un peu plus long que prévu
sans casser la mise en page. Mais ça reste un filet de sécurité, pas une
autorisation — une diapo dont le texte a rétréci est une diapo qui en dit
trop.

---

## Les 5 règles de fabrication

1. **Une idée par diapo.** Si tu hésites entre deux, fais deux diapos.
2. **12 mots maximum** sur une diapo `idee`. Le reste, tu le **dis**.
3. **Jamais de sous-niveaux.** Ce n'est pas un rapport.
4. **Le rouge signale une seule chose à la fois** : le mot important, ou le danger.
5. **Le code se lit à 8 mètres** : 12 lignes, jamais plus.

---

## Hors connexion

Polices et KaTeX sont chargés depuis un CDN. Sans internet, des polices
système prennent le relais sans casser la mise en page ; seules les formules
mathématiques s'afficheront en texte brut. Si tu présentes sans réseau,
télécharge `katex.min.css` et `katex.min.js` dans `assets/` et remplace les
deux URL dans l'en-tête des fichiers HTML.

**À faire la veille** : ouvre chaque deck une fois, avec le vidéoprojecteur
de la salle, en plein écran.
