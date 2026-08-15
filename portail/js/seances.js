/* ═══════════════════════════════════════════════════════════════════════
   LE SEUL FICHIER À MODIFIER

   Une séance = un objet. Pour publier une ressource, on ajoute son lien.
   Une clé absente ou à `null` n'affiche simplement rien : les ressources
   sont facultatives, et une séance sans vidéo reste une séance normale.

   Les fichiers se déposent dans  portail/fichiers/  et se citent en chemin
   relatif :  "fichiers/00-kit-demarrage.pdf"
   ═══════════════════════════════════════════════════════════════════════ */

const SEANCES = [
  {
    numero: 0,
    titre: "Kit de démarrage",
    sousTitre: "Pourquoi Python, le parcours, et la prise en main de Colab",
    date: "2026-08-15",
    duree: "2 h 30",
    liens: {
      slides: null,        // ex. "fichiers/00-kit-demarrage.pdf"
    },
  },
  {
    numero: 1,
    titre: "Parler à la machine",
    sousTitre: "Variables, types, entrées et sorties",
    date: "2026-08-19",
    duree: "3 h",
    liens: {},
  },
  {
    numero: 2,
    titre: "Décider et répéter",
    sousTitre: "Booléens, conditions, boucles, lecture d'erreurs",
    date: "2026-08-22",
    duree: "3 h",
    liens: {},
  },
  {
    numero: 3,
    titre: "Ranger l'information",
    sousTitre: "Listes, dictionnaires, tuples, ensembles",
    date: "2026-08-26",
    duree: "3 h",
    liens: {},
  },
  {
    numero: 4,
    titre: "Fabriquer ses outils",
    sousTitre: "Fonctions, modules, fichiers, erreurs",
    date: "2026-08-29",
    duree: "3 h",
    liens: {},
  },
  {
    numero: 5,
    titre: "Programmation orientée objet",
    sousTitre: "Classes, objets, dataclasses, composition",
    date: "2026-09-02",
    duree: "3 h",
    liens: {},
  },
  {
    numero: 6,
    titre: "Sous le capot",
    sousTitre: "Méthodes spéciales, générateurs, décorateurs",
    date: "2026-09-05",
    duree: "3 h",
    liens: {},
  },
  {
    numero: 7,
    titre: "NumPy & pandas",
    sousTitre: "Du tableau en mémoire au DataFrame",
    date: "2026-09-09",
    duree: "3 h",
    liens: {},
  },
  {
    numero: 8,
    titre: "Faire parler les données",
    sousTitre: "Agrégation, jointures, Matplotlib, seaborn",
    date: "2026-09-12",
    duree: "3 h",
    liens: {},
  },
];

/* Les ressources possibles, dans l'ordre d'affichage.
   Aucune n'est obligatoire : seules celles qui ont un lien apparaissent. */
const RESSOURCES = [
  { cle: "slides", libelle: "Slides", icone: "doc" },
  { cle: "notebook", libelle: "Notebook", icone: "code" },
  { cle: "corrige", libelle: "Corrigé", icone: "check" },
  { cle: "video", libelle: "Vidéo", icone: "play" },
];

/* Les outils de la formation. Les logos sont dans assets/logos/ :
   rien n'est chargé depuis un service extérieur. */
const OUTILS = [
  { nom: "Python", fichier: "python.svg", detail: "le langage" },
  { nom: "Google Colab", fichier: "colab.svg", detail: "écrire du code sans rien installer" },
  { nom: "Google Classroom", fichier: "classroom.svg", detail: "les supports et les devoirs" },
  { nom: "Google Meet", fichier: "meet.svg", detail: "la séance en direct" },
  { nom: "VS Code", fichier: "vscode.svg", detail: "à partir de la séance 4" },
  { nom: "GitHub", fichier: "github.svg", detail: "le code, versionné" },
];
