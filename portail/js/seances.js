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
      slides: "https://drive.google.com/file/d/1ipO6zWyvxEawBNsulloAz9OIb9WLsrcr/view?usp=sharing",
    },
  },
  {
    numero: 1,
    titre: "Parler à la machine",
    sousTitre: "Variables, types, entrées et sorties",
    date: "2026-08-19",
    duree: "3 h",
    liens: {
      slides: "https://drive.google.com/file/d/1CclXmyYVgAdM7Cs2Q17RXHFiIJwTdpqO/view?usp=sharing",
      notebook: "https://colab.research.google.com/github/8sylla/python-360/blob/main/seances/s01-parler-a-la-machine/gestion_depenses_notebook.ipynb",
      video: "https://www.youtube.com/live/Hp6FCd0wbVc"
    },
  },
  {
    numero: 2,
    titre: "Décider et répéter",
    sousTitre: "Booléens, conditions, boucles, lecture d'erreurs",
    date: "2026-08-22",
    duree: "3 h",
    liens: {
      slides: "https://drive.google.com/file/d/1z5g6gLhQy9_-DNNvQZjniBHWC77k5gtT/view?usp=sharing",
      video: "https://youtube.com/live/WPeqJ79RjiM",
      notebook: "https://colab.research.google.com/github/8sylla/python-360/blob/main/seances/s02-decider-et-repeter/gestion_depenses_notebook.ipynb"
    },
  },
  {
    numero: 3,
    titre: "Ranger l'information",
    sousTitre: "Listes, dictionnaires, tuples, ensembles",
    date: "2026-08-26",
    duree: "3 h",
    liens: {
      video: "https://youtube.com/live/N2xOFDQhMdU",
      slides: "https://drive.google.com/file/d/1mF9KEclVesKVhyajs2FnAemcbp15myEH/view?usp=sharing",
      notebook: "https://colab.research.google.com/github/8sylla/python-360/blob/main/seances/s03-ranger-l-information/gestion_depenses_v3.ipynb",
      
    },
  },
  {
    numero: 4,
    titre: "Fabriquer ses outils",
    sousTitre: "Fonctions, modules, fichiers, erreurs",
    date: "2026-08-29",
    duree: "3 h",
    liens: {
      notebook: "https://github.com/8sylla/python-360/tree/main/seances/s04-fabriquer-ses-outils/devoir-monbudget",
      slides: "https://drive.google.com/file/d/1JxCFiQziDyqxkYYkZwvWw_FoiTZSu5lW/view?usp=sharing",
      video: "https://youtube.com/live/J7tonCKK3Zc",
    },
  },
  {
    numero: 5,
    titre: "Programmation orientée objet",
    sousTitre: "Classes, objets, dataclasses, composition",
    date: "2026-09-02",
    duree: "3 h",
    liens: {
      slides: "https://drive.google.com/file/d/1Uf2OppyoO7N8Vr9m_hRLcmDTZsLhS1V1/view?usp=sharing",
      video: "https://youtube.com/live/PHky5p2Zgmc",
      notebook: "https://github.com/8sylla/python-360/tree/main/seances/s05-poo/devoir-monbudget-v2"
    },
  },
  {
    numero: 6,
    titre: "Sous le capot",
    sousTitre: "Méthodes spéciales, générateurs, décorateurs",
    date: "2026-09-05",
    duree: "3 h",
    liens: {
      slides: "https://drive.google.com/file/d/1HmnLC31Iyg32Xjz8uNjxJEjOi8aIQFjK/view?usp=sharing",
      video: "https://youtube.com/live/2AfaEiM-Wbk",
      notebook: "https://docs.google.com/forms/d/e/1FAIpQLSeY9kMxexqRdsENYH3YkxGve0Bc3XXybgHYbMImLQtSBLHthA/viewform?usp=publish-editor"
    },
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
  { cle: "slides", libelle: "Slides", icone: "file-text" },
  { cle: "notebook", libelle: "Notebook", icone: "notebook" },
  { cle: "corrige", libelle: "Corrigé", icone: "check" },
  { cle: "video", libelle: "Vidéo", icone: "video" },
];

/* ── Le projet fil rouge ───────────────────────────────────────────────
   Tous les détails (sujets, livrables, critères) vivent dans le README du
   dépôt : le portail ne fait que présenter et pointer dessus. Les groupes
   et leurs dépôts ne sont pas encore constitués — ils seront ajoutés au
   README, pas ici. */
const PROJETS_URL =
  "https://github.com/8sylla/python-360/blob/main/projets/README.md";
//  Base des fiches détaillées (une par sujet) dans le dépôt.
const PROJETS_BASE =
  "https://github.com/8sylla/python-360/blob/main/projets/";

/* Les trois livrables progressifs, communs aux cinq sujets. */
const LIVRABLES = [
  { tag: "v1", titre: "Fondations & NumPy", poids: "25 %",
    detail: "Lecture brute du CSV, nettoyage et statistiques avec NumPy." },
  { tag: "v2", titre: "Exploration pandas", poids: "35 %",
    detail: "DataFrame, filtrage, groupby / pivot, export propre." },
  { tag: "finale", titre: "Data-viz & démo", poids: "40 %",
    detail: "4 graphiques, une appli à menu, et un pitch de 5 min par équipe." },
];

/* Les cinq sujets. Un groupe par sujet ; le groupe reste « à constituer »
   tant que les équipes ne sont pas fixées. */
const PROJETS = [
  { numero: 1, titre: "Streaming & audience", domaine: "Spotify · 114k titres",
    problematique: "Ce qui rend un titre populaire, et comparer les genres audio.",
    fichier: "sujet-1-streaming-audience.md" },
  { numero: 2, titre: "Marché immobilier", domaine: "Melbourne · immobilier",
    problematique: "Quels facteurs influencent le plus le prix des biens ?",
    fichier: "sujet-2-marche-immobilier.md" },
  { numero: 3, titre: "Ventes e-commerce", domaine: "UCI · 500k ventes",
    problematique: "Quels pays et quels mois font le chiffre d'affaires ?",
    fichier: "sujet-3-ventes-ecommerce.md" },
  { numero: 4, titre: "Santé & bien-être", domaine: "Fitbit · wearables",
    problematique: "Activité, sommeil et calories brûlées sont-ils corrélés ?",
    fichier: "sujet-4-sante-bien-etre.md" },
  { numero: 5, titre: "Climat & températures", domaine: "Berkeley Earth",
    problematique: "Visualiser l'évolution des températures sur plus d'un siècle.",
    fichier: "sujet-5-climat-temperatures.md" },
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
