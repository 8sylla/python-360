"""Génère modele.html — la vitrine des 12 gabarits (la « classe »)."""
from moteur_slides import *
from moteur_slides import deck

S = 1
d = [
  couverture("Le gabarit<br>couverture.", "Titre, promesse, trois métadonnées. Rien d'autre.",
             [("Séance","00"),("Durée","3 h"),("Prérequis","Aucun")], S),
  section(1, "Le gabarit section", "Ouvre une partie. Numéro géant, une ligne de contexte.", S),
  idee("Le gabarit idee", 'Une idée.<br>Douze mots <span class="souligne">maximum</span>.', S,
       "Le gabarit le plus utilisé", notes="Les notes du présentateur s'affichent ici, avec la touche N. Elles ne sont jamais projetées."),
  chiffre("Le gabarit chiffre", "×62", "un nombre qui frappe",
          "Et sa légende, en deux lignes au plus.", S),
  analogie("Le gabarit analogie", "boite", 'Un <span class="souligne">pictogramme</span><br>et un concept.',
           "Seize pictogrammes sont fournis : boite, repertoire, recette, aiguillage, boucle, machine, moule, prise, ticket, cadeau, tableau, imbrique, passeplat, carton, plateau, ceinture.", S),
  duel("Le gabarit duel", "Avant / après, ✗ / ✓, deux approches.",
       ("Ce qu'on ne fait pas", "le code fautif", "Et pourquoi."),
       ("Ce qu'on fait", "le bon code", "Et pourquoi."), S),
  code("Le gabarit code",
       '<span class="k">def</span> <span class="f">exemple</span>(x: <span class="k">int</span>) -&gt; <span class="k">int</span>:\n'
       '    <span class="c"># douze lignes maximum, corps 26 px</span>\n'
       '    <span class="k">return</span> <mark>x * <span class="n">2</span></mark>',
       "La légende explique la ligne surlignée. <span class='mono'>mark</span> met en évidence."),
  etapes("Le gabarit etapes", "Deux à quatre temps, jamais plus.", [
      ("Découper", "Trois mots de légende."),
      ("Appliquer", "Trois mots de légende."),
      ("Combiner", "Trois mots de légende."),
  ]),
  alerte("Le gabarit alerte", 'Le <span class="souligne">piège</span><br>à ne pas commettre.',
         "Pleine page rouge. Une phrase. Rien d'autre.", S),
  formule("Le gabarit formule", "KaTeX est déjà branché",
          r"\sigma=\sqrt{\frac{1}{n}\sum_{i=1}^{n}\bigl(x_i-\bar{x}\bigr)^{2}}",
          "Toujours suivie de sa traduction en français."),
  liste("Le gabarit liste", "Trois à cinq points, jamais de sous-niveau", [
      "Un point tient sur une ligne",
      "Le marqueur est le <span class='mono'>&gt;</span> du prompt Python",
      "Au-delà de cinq points, fais deux diapos",
  ]),
  tuiles("Le gabarit tuiles", "Quatre notions parallèles.", [
      ("clé", "et sa valeur"), ("clé", "et sa valeur"),
      ("clé", "et sa valeur"), ("clé", "et sa valeur"),
  ]),
  exercice("Le gabarit exercice", "Fond vert : c'est à eux de jouer", [
      "Une consigne par ligne",
      "Quatre au maximum",
      "Le vert du sigle ASEGUIM signale le passage à l'action",
  ]),
  regle("Le gabarit regle", 'La phrase<br>à <span class="souligne">retenir</span>.', S, "Séance 01 &middot; Exemple"),
  fin("Le gabarit fin. Rail de progression en pied de page.", S),
]
print("modele.html :", deck("modele.html", "Les 12 gabarits", d), "diapos")
