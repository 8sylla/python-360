/* ═══════════════════════════════════════════════════════════════════════
   LE SEUL FICHIER À MODIFIER POUR PUBLIER UNE SÉANCE
   ═══════════════════════════════════════════════════════════════════════

   Chaque séance est un objet. Pour publier un lien, remplace `null` par
   l'adresse du fichier ; le bouton s'allume tout seul. Laisse `null` tant
   que la ressource n'existe pas : le bouton reste grisé, avec « à venir ».

   Les fichiers se déposent dans  portail/fichiers/  puis se citent en
   chemin relatif :  "fichiers/00-kit-demarrage.pdf"

   `date`  : ce qui s'affiche sur la carte. Format libre.
   `arc`   : 1 ou 2 — sert au filtre.
   ═══════════════════════════════════════════════════════════════════════ */

const SEANCES = [
  {
    numero: 0,
    titre: "Kit de démarrage",
    sousTitre: "Pourquoi Python, où l'on va, et comment on s'outille",
    date: "En autonomie · 45 min",
    arc: 1,
    liens: {
      slides:   null,   // ex. "fichiers/00-kit-demarrage.pdf"
      notebook: null,
      corrige:  null,
      replay:   null,
    },
  },
  {
    numero: 1,
    titre: "Parler à la machine",
    sousTitre: "Variables, types, entrées et sorties",
    date: "Séance 1 · 3 h",
    arc: 1,
    liens: { slides: null, notebook: null, corrige: null, replay: null },
  },
  {
    numero: 2,
    titre: "Décider et répéter",
    sousTitre: "Booléens, conditions, boucles, lecture d'erreurs",
    date: "Séance 2 · 3 h",
    arc: 1,
    liens: { slides: null, notebook: null, corrige: null, replay: null },
  },
  {
    numero: 3,
    titre: "Ranger l'information",
    sousTitre: "Listes, dictionnaires, tuples, ensembles",
    date: "Séance 3 · 3 h",
    arc: 1,
    liens: { slides: null, notebook: null, corrige: null, replay: null },
  },
  {
    numero: 4,
    titre: "Fabriquer ses outils",
    sousTitre: "Fonctions, modules, fichiers — et passage à VS Code",
    date: "Séance 4 · 3 h",
    arc: 1,
    liens: { slides: null, notebook: null, corrige: null, replay: null },
  },
  {
    numero: 5,
    titre: "Programmation orientée objet",
    sousTitre: "Classes, objets, dataclasses, composition",
    date: "Séance 5 · 3 h",
    arc: 2,
    liens: { slides: null, notebook: null, corrige: null, replay: null },
  },
  {
    numero: 6,
    titre: "Sous le capot",
    sousTitre: "Dunders, générateurs, décorateurs, outillage qualité",
    date: "Séance 6 · 3 h",
    arc: 2,
    liens: { slides: null, notebook: null, corrige: null, replay: null },
  },
  {
    numero: 7,
    titre: "NumPy & pandas",
    sousTitre: "Du tableau en mémoire au DataFrame",
    date: "Séance 7 · 3 h",
    arc: 2,
    liens: { slides: null, notebook: null, corrige: null, replay: null },
  },
  {
    numero: 8,
    titre: "Faire parler les données",
    sousTitre: "Agrégation, jointures, Matplotlib, seaborn",
    date: "Séance 8 · 3 h",
    arc: 2,
    liens: { slides: null, notebook: null, corrige: null, replay: null },
  },
];

/* Les quatre types de ressource, dans l'ordre où ils s'affichent. */
const RESSOURCES = [
  { cle: "slides",   libelle: "Slides PDF", icone: "doc" },
  { cle: "notebook", libelle: "Notebook",   icone: "code" },
  { cle: "corrige",  libelle: "Corrigé",    icone: "check" },
  { cle: "replay",   libelle: "Replay",     icone: "play" },
];
