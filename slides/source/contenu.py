"""Contenu des 12 decks — Formation Python 360° · ASEGUIM.

Chaque deck est un OBJET construit à partir des gabarits de moteur_slides.
Pour modifier une séance : on touche uniquement à ce fichier.
"""

from moteur_slides import (alerte, analogie, chiffre, code, couverture, deck, duel,
                           ecrire_socle, etapes, exercice, fin, formule, idee, liste,
                           regle, section, tuiles)

ecrire_socle()
total = {}

# ═══════════════════════════════════════════════════════════════════════════
# SÉANCE 0 — KIT DE DÉMARRAGE (asynchrone)
# ═══════════════════════════════════════════════════════════════════════════
S = None
total["00"] = deck("00-kit-demarrage.html", "Séance 0 — Kit de démarrage", [
    couverture("Avant de<br>commencer.", "Quinze minutes, une fois. Ensuite, on ne parle plus jamais d'installation.",
               [("Séance", "00"), ("Durée", "45 min"), ("Où", "Chez toi")], S),
    idee("La promesse", 'En 11 séances&nbsp;:<br>de «&nbsp;je n\'ai jamais codé&nbsp;»<br>à «&nbsp;j\'ai <span class="souligne">déployé</span> une API&nbsp;».', S,
         notes="Le kit existe pour une seule raison : la séance 1 doit être une séance de code, pas une séance de dépannage."),
    idee("Ce dont tu as besoin", 'Un navigateur.<br>Un compte Google.<br><span class="souligne">C\'est tout.</span>', S,
         notes="Pour les trois premières séances, rien à installer. L'installation locale n'arrive qu'en séance 4."),
    etapes("Google Colab", "Trois clics, et tu codes.", [
        ("colab.research.google.com", "Nouveau notebook."),
        ('print("Bonjour")', "Tape ça dans la cellule."),
        ("Maj + Entrée", "Si ça s'affiche, tu es prêt·e."),
    ]),
    liste("Pour prendre de l'avance", "L'installation locale (séance 4)", [
        "Python 3.14 &mdash; <span class='mono'>python.org/downloads</span>",
        "<b>Windows&nbsp;: cocher «&nbsp;Add python.exe to PATH&nbsp;»</b>",
        "VS Code + l'extension Python de Microsoft",
        "Un compte GitHub",
    ], notes="Le PATH non coché est la cause n°1 des blocages Windows. Le répéter deux fois."),
    idee("La règle de la maison", 'L\'erreur n\'est pas un échec.<br>C\'est un <span class="souligne">message</span>.', S,
         notes="À poser dès le kit. Tout le dispositif pédagogique repose sur cette phrase."),
    liste("Où demander de l'aide", "Le salon #sos-erreurs", [
        "Colle ton message d'erreur <b>en texte</b>, jamais en photo",
        "La dernière ligne dit toujours ce qui ne va pas",
        "Aucune question n'est bête. Aucune.",
    ]),
    fin("Le questionnaire de positionnement prend 2 minutes. Il sert à composer les binômes.", S,
        bas="À très vite"),
])

# ═══════════════════════════════════════════════════════════════════════════
# SÉANCE 1 — PARLER À LA MACHINE
# ═══════════════════════════════════════════════════════════════════════════
S = 1
BAS = "Séance 01 &middot; Parler à la machine"
total["01"] = deck("01-parler-a-la-machine.html", "Séance 1 — Parler à la machine", [
    couverture("Parler à<br>la machine.", "Dans trois heures, tu auras écrit un programme qui te pose des questions et te répond.",
               [("Séance", "01"), ("Durée", "3 h"), ("Prérequis", "Aucun")], S),
    idee("La règle de la maison", 'L\'erreur n\'est pas un échec.<br>C\'est un <span class="souligne">message</span>.', S, BAS,
         notes="Trois engagements du formateur : je provoquerai des erreurs exprès, je ne dirai jamais « c'est faux », personne ne reste bloqué seul."),
    section(1, "C'est quoi, programmer&nbsp;?", "Une recette, et un exécutant très rapide et très bête.", S),
    analogie("Analogie", "recette", 'Un programme,<br>c\'est une <span class="souligne">recette</span>.',
             "Python la lit ligne par ligne, de haut en bas. Il ne devine jamais, il n'anticipe jamais.",
             S, notes="Atelier débranché : « écris la recette pour qu'un robot prépare un thé ». Le formateur joue le robot et exécute littéralement. L'ambiguïté saute aux yeux."),
    idee("L'ordinateur", 'Il est <span class="souligne">obéissant</span>.<br>Il est <span class="souligne">rapide</span>.<br>Il est bête.', S, BAS,
         notes="Si tu oublies « allumer le four », il sert la pâte crue sans se plaindre. C'est toute la difficulté du métier."),
    section(2, "Les variables", "Ranger une information pour la retrouver.", S),
    analogie("Analogie", "boite", 'Une variable,<br>c\'est une <span class="souligne">boîte</span> étiquetée.',
             "<span class='mono'>age = 25</span> &mdash; prends une boîte, colle l'étiquette «&nbsp;age&nbsp;», mets 25 dedans.",
             S, notes="Faire dire les 3 conséquences par le groupe : le = range, remettre efface, un bon nom est un cadeau qu'on se fait dans deux semaines."),
    alerte("Le premier faux ami", 'Le <span class="souligne">=</span> n\'est pas<br>un égal mathématique.',
           "Il veut dire : «&nbsp;range ceci dans cette boîte&nbsp;».", S,
           notes="D'où x = x + 1, absurde en maths, parfaitement normal ici. Le montrer au tableau."),
    tuiles("Les 4 types de base", "On ne fait pas les mêmes gestes avec du texte et avec un nombre.", [
        ("str", "du texte &mdash; <span class='mono'>\"Awa\"</span>"),
        ("int", "un entier &mdash; <span class='mono'>25</span>"),
        ("float", "un décimal &mdash; <span class='mono'>1.68</span>"),
        ("bool", "vrai ou faux &mdash; <span class='mono'>True</span>"),
    ]),
    duel("Le piège des types", "On n'additionne pas des mots et des nombres.",
         ('"5" + "3"', 'donne "53"', "Deux textes collés bout à bout."),
         ("5 + 3", "donne 8", "Deux nombres additionnés."), S,
         notes="Puis montrer \"5\" + 3 → TypeError. Python refuse de deviner : c'est une qualité, pas un défaut."),
    section(3, "Dialoguer", "Le programme pose une question et écoute la réponse.", S),
    alerte("Le piège n&deg;1 de la formation", '<span class="mono" style="font-size:.82em">input()</span> rend toujours<br>du <span class="souligne">texte</span>.',
           "Même quand on tape 42.", S,
           notes="LE piège de tous les débutants. Le provoquer, obtenir le TypeError, corriger avec int(). Annoncer qu'il reviendra trois fois d'ici la séance 4."),
    code("Les f-strings",
         '<span class="k">prenom</span> = <span class="f">input</span>(<span class="s">"Ton prénom : "</span>)\n'
         '<span class="k">age</span> = <span class="f">int</span>(<span class="f">input</span>(<span class="s">"Ton âge : "</span>))\n\n'
         '<span class="f">print</span>(<span class="s">f"Bonjour <mark>{prenom}</mark>, tu as <mark>{age}</mark> ans."</span>)',
         "Le <span class='mono'>f</span> collé au guillemet ouvrant. L'oublier affiche littéralement <span class='mono'>{prenom}</span>.",
         notes="L'oubli du f est l'erreur la plus fréquente de la séance. Le montrer une fois."),
    exercice("Exercice", "Le calculateur de candidature", [
        "Demande le prénom, les offres repérées, les candidatures envoyées",
        "Affiche les offres restantes",
        "Affiche le taux de candidature en pourcentage",
        "<span class='mono'>{taux:.1f}</span> pour n'avoir qu'une décimale",
    ], notes="Si quelqu'un saisit 0 offre, le programme plante (ZeroDivisionError). NE PAS corriger aujourd'hui : le noter au tableau comme une dette. On la rembourse en séance 2 avec if. C'est l'accroche parfaite."),
    code("Le fil rouge &mdash; OpportuniTrack v0.1",
         '<span class="f">print</span>(<span class="s">"="</span> * <span class="n">40</span>)\n'
         '<span class="f">print</span>(<span class="s">f"  {titre.upper()}"</span>)\n'
         '<span class="f">print</span>(<span class="s">f"  Organisme : {organisme}"</span>)\n'
         '<span class="f">print</span>(<span class="s">f"  Deadline  : {deadline}"</span>)\n'
         '<span class="f">print</span>(<span class="s">"="</span> * <span class="n">40</span>)',
         "La carte d'opportunité. En séance 2, elle décidera toute seule s'il faut candidater."),
    regle("À retenir", 'Un programme, c\'est<br>une <span class="souligne">suite d\'étapes</span><br>que la machine suit bêtement.', S, BAS),
    fin("Devoir : ajoute deux informations à ta fiche d'opportunité et poste une capture.", S, BAS),
])

# ═══════════════════════════════════════════════════════════════════════════
# SÉANCE 2 — DÉCIDER ET RÉPÉTER
# ═══════════════════════════════════════════════════════════════════════════
S = 2
BAS = "Séance 02 &middot; Décider et répéter"
total["02"] = deck("02-decider-et-repeter.html", "Séance 2 — Décider et répéter", [
    couverture("Décider,<br>et répéter.", "Aujourd'hui, ton programme arrête d'exécuter bêtement : il choisit.",
               [("Séance", "02"), ("Durée", "3 h"), ("Rappel", "Variables, types")], S),
    idee("L'erreur du jour", 'Notre dette de<br>la semaine dernière&nbsp;:<br><span class="souligne">ZeroDivisionError</span>.', S, BAS,
         notes="On l'avait laissée exprès. À la fin du premier bloc, elle sera réglée en trois lignes."),
    section(1, "Décider", "Vrai ou faux, et rien d'autre.", S),
    idee("Le booléen", 'Il n\'existe que<br><span class="souligne">deux</span> réponses&nbsp;:<br>True. False.', S, BAS,
         notes="12 > 5 n'affiche pas « oui ». Ça VAUT True. Toute condition se ramène à ces deux valeurs."),
    duel("Le deuxième faux ami", "Un égal, ou deux ?",
         ("= (un seul)", "age = 18", "Je range 18 dans la boîte."),
         ("== (deux)", "age == 18", "Est-ce que c'est pareil ?"), S,
         notes="Deuxième erreur la plus fréquente du cursus. L'annoncer explicitement fait gagner une heure de dépannage."),
    analogie("Analogie", "aiguillage", 'Le <span class="mono">if</span>,<br>c\'est un <span class="souligne">aiguillage</span>.',
             "Au panneau, le programme regarde la condition et prend une route. Une seule branche est empruntée. Jamais deux.",
             S),
    alerte("Ce n'est pas de la décoration", 'L\'<span class="souligne">indentation</span><br>fait partie du code.',
           "Quatre espaces disent : «&nbsp;cette ligne est à l'intérieur du if&nbsp;».", S,
           notes="Analogie : les paragraphes en retrait d'un contrat, qui appartiennent à l'article au-dessus. Montrer l'IndentationError."),
    code("if / elif / else",
         '<span class="k">if</span> jours_restants &lt; <span class="n">0</span>:\n'
         '    <span class="f">print</span>(<span class="s">"Deadline dépassée"</span>)\n'
         '<span class="k">elif</span> jours_restants &lt; <span class="n">7</span>:\n'
         '    <span class="f">print</span>(<span class="s">"URGENT"</span>)\n'
         '<span class="k">else</span>:\n'
         '    <span class="f">print</span>(<span class="s">"Tu as le temps"</span>)',
         "Lis-le à voix haute en français. La traduction littérale est la meilleure aide-mémoire."),
    section(2, "Répéter", "Deux façons, deux usages.", S),
    duel("for ou while ?", "La question à se poser : est-ce que je sais combien de fois ?",
         ("for", "je sais combien", "Distribuer 12 tracts : 12 tours."),
         ("while", "je ne sais pas", "Remplir un seau : tant qu'il n'est pas plein.")
         , S, notes="Ne pas présenter while comme « plus avancé ». C'est un usage différent, pas un niveau supérieur."),
    alerte("range(5)", 'Ça commence à <span class="souligne">0</span><br>et ça s\'arrête <span class="souligne">avant</span> 5.',
           "0, 1, 2, 3, 4. Cinq tours.", S,
           notes="Le compter à voix haute avec le groupe, en levant les doigts. Ça évite trois semaines de confusion."),
    analogie("Le motif à connaître par cœur", "boucle", 'L\'<span class="souligne">accumulateur</span>&nbsp;:<br>une boîte qui grossit.',
             "<span class='mono'>total = total + prix</span> &mdash; à chaque tour, on ajoute. On le reverra jusqu'à la séance 11.",
             S),
    alerte("Le danger du while", 'Quelque chose doit<br><span class="souligne">changer</span> à l\'intérieur.',
           "Sinon la boucle tourne pour l'éternité.", S,
           notes="Écrire une boucle infinie en direct, la laisser tourner, demander au groupe de trouver pourquoi. Puis montrer le bouton stop."),
    exercice("Exercice", "Le nombre mystère", [
        "L'ordinateur choisit un nombre entre 1 et 100",
        "Le joueur propose&nbsp;: «&nbsp;trop grand&nbsp;» ou «&nbsp;trop petit&nbsp;»",
        "Compter les essais et féliciter",
        "Bonus&nbsp;: limiter à 7 essais",
    ], notes="Faire lire « while not trouve » à voix haute : « tant que ce n'est pas trouvé ». Demander pourquoi le else final est forcément l'égalité."),
    formule("Palier bonus", "Pourquoi 7 essais suffisent toujours",
            r"\lceil \log_{2}(100) \rceil = 7",
            "Chaque proposition bien choisie divise les possibilités par deux.",
            notes="Faire d'abord jouer le groupe contre la machine. La surprise vient avant l'explication, jamais l'inverse.", fond="rouge"),
    code("Le fil rouge &mdash; OpportuniTrack v0.2",
         '<span class="c"># « Je candidate si le niveau correspond ET s\'il reste 3 jours. »</span>\n'
         '<span class="k">if</span> niveau_requis == mon_niveau <span class="k">and</span> jours &gt;= <span class="n">3</span>:\n'
         '    <span class="f">print</span>(<span class="s">"À CANDIDATER"</span>)\n'
         '<span class="k">elif</span> jours &lt;= <span class="n">0</span>:\n'
         '    <span class="f">print</span>(<span class="s">"Trop tard"</span>)',
         "Écris la règle <b>en français</b> au tableau avant de coder. La traduction est le vrai apprentissage."),
    regle("À retenir", 'Écris la règle en français.<br>Puis <span class="souligne">traduis-la</span>.', S, BAS),
    fin("La semaine prochaine : gérer des centaines d'informations, pas une seule.", S, BAS),
])

# ═══════════════════════════════════════════════════════════════════════════
# SÉANCE 3 — RANGER L'INFORMATION
# ═══════════════════════════════════════════════════════════════════════════
S = 3
BAS = "Séance 03 &middot; Ranger l'information"
total["03"] = deck("03-ranger-l-information.html", "Séance 3 — Ranger l'information", [
    couverture("Ranger<br>l'information.", "Jusqu'ici tu manipulais une info à la fois. Aujourd'hui, tu en gères des centaines.",
               [("Séance", "03"), ("Durée", "3 h"), ("Rappel", "Boucles, conditions")], S),
    idee("Le problème", 'pays1, pays2,<br>pays3, pays4&hellip;<br><span class="souligne">Ça ne tient pas.</span>', S, BAS,
         notes="Projeter 40 variables numérotées. Laisser le malaise s'installer trois secondes avant de proposer la liste."),
    section(1, "La liste", "Ordonnée, modifiable, numérotée.", S),
    idee("La liste", 'Une liste de courses.<br>Ordonnée. Modifiable.<br>On peut y répéter.', S, BAS),
    alerte("Ce qui surprend tout le monde", 'On compte à partir<br>de <span class="souligne">zéro</span>.',
           "Le premier élément est à la position 0.", S,
           notes="Analogie de l'ascenseur français : le rez-de-chaussée est l'étage 0. Le « premier » est au-dessus."),
    code("Les gestes de base",
         'pays = [<span class="s">"Maroc"</span>, <span class="s">"Guinée"</span>, <span class="s">"France"</span>]\n\n'
         'pays[<span class="n">0</span>]        <span class="c"># le premier</span>\n'
         'pays[<span class="n">-1</span>]       <span class="c"># le dernier, sans calculer</span>\n'
         'pays[<span class="n">1</span>:<span class="n">3</span>]      <span class="c"># de 1 INCLUS à 3 EXCLU</span>\n'
         '<span class="f">len</span>(pays)     <span class="c"># combien</span>\n'
         '<span class="s">"Maroc"</span> <span class="k">in</span> pays',
         "La tranche, c'est le ticket de train : on monte à la gare 1, on descend avant la gare 4."),
    section(2, "Le dictionnaire", "On cherche par nom, pas par position.", S),
    analogie("Analogie", "repertoire", 'Le dictionnaire,<br>c\'est un <span class="souligne">répertoire</span>.',
             "On n'y cherche pas «&nbsp;la 3<sup>e</sup> personne&nbsp;». On y cherche le numéro de Fatou.",
             S),
    duel("Le réflexe professionnel", "Sur de vraies données, il manque toujours quelque chose.",
         ('dico["ville"]', "plante si absent", "KeyError, et tout s'arrête."),
         ('dico.get("ville")', "rend None", "Ou la valeur par défaut que tu choisis."), S),
    section(3, "La structure reine", "Celle qui portera tout le reste de la formation.", S),
    analogie("Une liste de dictionnaires", "tableau", 'Des lignes.<br>Des colonnes.<br>Un <span class="souligne">tableau</span>.',
             "Chaque dictionnaire est une ligne. Chaque clé est une colonne.",
             S),
    idee("Annonce importante", 'Ce que tu viens d\'écrire,<br>pandas l\'appellera un<br><span class="souligne">DataFrame</span>.', S, BAS,
         notes="Phrase à dire mot pour mot : « vous avez déjà compris la structure ; en séance 7, il ne restera que la syntaxe ». Ça désamorce l'angoisse de l'Arc 2 quatre séances à l'avance."),
    tuiles("Quelle structure choisir ?", "L'arbre de décision, à afficher au mur.", [
        ("dictionnaire", "chaque champ a un nom"),
        ("liste", "l'ordre compte, je modifie"),
        ("tuple", "l'ordre compte, jamais modifié"),
        ("set", "juste savoir qui est là, sans doublon"),
    ], notes="Le set en une ligne utile : list(set(ma_liste)) supprime les doublons. Le montrer, c'est spectaculaire."),
    exercice("Exercice", "Le carnet d'opportunités", [
        "Combien d'opportunités au total&nbsp;?",
        "Lesquelles expirent dans moins de 10 jours&nbsp;?",
        "Quels pays sont représentés, <b>sans doublon</b>&nbsp;?",
        "Laquelle est la plus urgente&nbsp;? Classe-les toutes.",
    ], notes="Pour min() et sorted(), le paramètre key= répond à la question « comparer sur quoi ? ». Le lambda se présente comme une mini-fonction jetable, pas comme un chapitre."),
    code("Bonus &mdash; la compréhension de liste",
         '<span class="c"># Quatre lignes...</span>\n'
         'urgentes = []\n'
         '<span class="k">for</span> opp <span class="k">in</span> opportunites:\n'
         '    <span class="k">if</span> opp[<span class="s">"jours"</span>] &lt; <span class="n">10</span>:\n'
         '        urgentes.<span class="f">append</span>(opp)\n\n'
         '<span class="c"># ...ou une seule.</span>\n'
         '<span class="ok">urgentes = [opp <span class="k">for</span> opp <span class="k">in</span> opportunites <span class="k">if</span> opp[<span class="s">"jours"</span>] &lt; <span class="n">10</span>]</span>',
         "À montrer, pas à imposer. La version en quatre lignes reste parfaitement correcte."),
    liste("PEP 8", "Cinq règles, et on n'en parle plus", [
        "<span class='mono'>snake_case</span> pour les noms",
        "Quatre espaces d'indentation",
        "Des espaces autour du <span class='mono'>=</span>",
        "Des noms explicites plutôt que courts",
        "Une instruction par ligne",
    ]),
    regle("À retenir", 'Une liste de dictionnaires,<br>c\'est déjà un <span class="souligne">tableau</span>.', S, BAS),
    fin("La semaine prochaine : on quitte le navigateur, et tes données survivent à la fermeture.", S, BAS),
])

# ═══════════════════════════════════════════════════════════════════════════
# SÉANCE 4 — FABRIQUER SES OUTILS
# ═══════════════════════════════════════════════════════════════════════════
S = 4
BAS = "Séance 04 &middot; Fabriquer ses outils"
total["04"] = deck("04-fabriquer-ses-outils.html", "Séance 4 — Fabriquer ses outils", [
    couverture("Fabriquer<br>ses outils.", "À la fin de la séance, tu as un vrai programme, dans un vrai fichier, qui garde tes données.",
               [("Séance", "04"), ("Durée", "3 h"), ("Nouveau", "VS Code")], S),
    idee("Aujourd'hui", 'On quitte<br>le navigateur.', S, BAS,
         notes="Vingt minutes de migration guidée. Ne passer à la suite que quand TOUT LE MONDE a vu un « Bonjour » dans le terminal."),
    etapes("Migration", "VS Code en quatre gestes", [
        ("Ouvrir un dossier", "Fichier &rsaquo; Ouvrir le dossier."),
        ("Créer tracker.py", "L'extension .py, jamais .txt."),
        ("Choisir l'interpréteur", "En bas à droite : Python 3.14."),
        ("Exécuter", "La flèche, ou F5."),
    ]),
    section(1, "La fonction", "Ne plus jamais copier-coller.", S),
    idee("Le problème", 'Le même bloc,<br>copié <span class="souligne">trois fois</span>.<br>Un bug à corriger trois fois.', S, BAS),
    analogie("Analogie", "machine", 'Une fonction,<br>c\'est une <span class="souligne">machine à café</span>.',
             "Tu mets quelque chose dedans, elle fait son travail, elle te rend quelque chose. Tu n'as pas besoin de savoir comment elle chauffe l'eau.",
             S),
    alerte("La grande confusion", '<span class="mono" style="font-size:.8em">print</span> parle à l\'humain.<br><span class="mono" style="font-size:.8em">return</span> parle au <span class="souligne">programme</span>.',
           "Une fonction qui print est un cul-de-sac.", S,
           notes="Le faire vivre par l'échec : def double(n): print(n*2), puis resultat = double(5), puis resultat + 1 → TypeError. Trente secondes, effet garanti."),
    code("Anatomie d'une fonction",
         '<span class="k">def</span> <span class="f">saluer</span>(prenom: <span class="k">str</span>) -&gt; <span class="k">str</span>:\n'
         '    <span class="s">"""Rend un message de salutation."""</span>\n'
         '    <span class="k">return</span> <span class="s">f"Bonjour {prenom} !"</span>\n\n'
         'message = <span class="f">saluer</span>(<span class="s">"Awa"</span>)',
         "La docstring documente. Essaie <span class='mono'>help(saluer)</span> : elle s'affiche."),
    section(2, "La mémoire longue", "Ce qui survit à la fermeture.", S),
    tuiles("Trois formats, trois usages", "Lequel choisir ?", [
        ("txt", "du texte brut, pour des notes"),
        ("csv", "un tableau, s'ouvre dans Excel"),
        ("json", "des données imbriquées &mdash; ta liste de dicts"),
        ("&rarr; séance 10", "le JSON est le format du web"),
    ]),
    code("Lire et écrire",
         '<span class="k">with</span> FICHIER.<span class="f">open</span>(<span class="s">"w"</span>, encoding=<span class="s">"utf-8"</span>) <span class="k">as</span> f:\n'
         '    json.<span class="f">dump</span>(donnees, f, indent=<span class="n">2</span>, ensure_ascii=<span class="k">False</span>)',
         "<span class='mono'>with</span> referme le fichier <b>quoi qu'il arrive</b>. <span class='mono'>encoding=\"utf-8\"</span> sauve tes accents."),
    analogie("Analogie", "ceinture", '<span class="mono">try / except</span>,<br>c\'est la <span class="souligne">ceinture</span>.',
             "«&nbsp;Essaie ceci&nbsp;; si ça casse pour telle raison, fais plutôt cela.&nbsp;»",
             S),
    alerte("Règle professionnelle", 'Jamais d\'<span class="mono" style="font-size:.82em">except</span> <span class="souligne">nu</span>.',
           "On nomme l'erreur qu'on attend&nbsp;: <span class='mono'>except ValueError:</span>", S,
           notes="Un except nu masque aussi le Ctrl+C et les vrais bugs. C'est une règle de métier, pas une préférence de style."),
    code("match / case &mdash; Python 3.10+",
         '<span class="k">match</span> choix:\n'
         '    <span class="k">case</span> <span class="s">"1"</span>: <span class="f">ajouter</span>()\n'
         '    <span class="k">case</span> <span class="s">"2"</span>: <span class="f">afficher</span>()\n'
         '    <span class="k">case</span> <span class="s">"3"</span>: <span class="f">quitter</span>()\n'
         '    <span class="k">case</span> _:   <span class="f">print</span>(<span class="s">"Choix invalide"</span>)',
         "Plus lisible qu'une cascade de <span class='mono'>elif</span> quand on compare une variable à des valeurs fixes."),
    exercice("Fil rouge v1", "OpportuniTrack en ligne de commande", [
        "Deux fichiers&nbsp;: <span class='mono'>stockage.py</span> et <span class='mono'>tracker.py</span>",
        "Un menu&nbsp;: ajouter, afficher, filtrer, quitter",
        "Les données survivent à la fermeture",
        "Le corrigé est sur le dépôt &mdash; <b>après</b> avoir essayé",
    ], notes="Revue de code en 3 points : les noms sont-ils compréhensibles ? Vois-tu deux blocs presque identiques ? Cette fonction fait-elle une seule chose ?"),
    regle("Fin de la rampe de lancement", 'Tu as écrit ~250 lignes.<br>Tu as une application<br>qui <span class="souligne">marche</span>.', S, BAS,
          notes="Marquer solennellement la fin de l'Arc 1. Prévenir que le rythme monte : à partir de la S5, le palier bonus devient le socle."),
    fin("À partir de la semaine prochaine : on n'apprend plus des instructions, on apprend à structurer.", S, BAS),
])

# ═══════════════════════════════════════════════════════════════════════════
# SÉANCE 5 — LA POO
# ═══════════════════════════════════════════════════════════════════════════
S = 5
BAS = "Séance 05 &middot; Programmation orientée objet"
total["05"] = deck("05-poo.html", "Séance 5 — Programmation orientée objet", [
    couverture("Structurer<br>avec les objets.", "Ton programme marche. Aujourd'hui, on le rend maintenable par quelqu'un d'autre que toi.",
               [("Séance", "05"), ("Durée", "3 h"), ("Arc", "2 sur 2")], S),
    idee("Le signal", 'La même liste,<br>passée à <span class="souligne">six fonctions</span>.', S, BAS,
         notes="Projeter le tracker de la S4 avec « opportunites » surligné dans les six signatures. Laisser le groupe nommer le problème."),
    idee("La règle", 'Quand les mêmes données<br>circulent partout,<br>un <span class="souligne">objet</span> veut naître.', S, BAS),
    analogie("Analogie", "moule", 'La classe est le <span class="souligne">moule</span>.<br>L\'objet est le gâteau.',
             "Un moule ne se mange pas. Il sert à fabriquer autant de gâteaux qu'on veut, tous de la même forme, avec des parfums différents.",
             S),
    code("Une classe",
         '<span class="k">class</span> <span class="f">Opportunite</span>:\n'
         '    <span class="k">def</span> <span class="f">__init__</span>(<span class="k">self</span>, titre, pays, jours):\n'
         '        <span class="k">self</span>.titre = titre\n'
         '        <span class="k">self</span>.pays  = pays\n\n'
         'bourse = <span class="f">Opportunite</span>(<span class="s">"Smarts-Up"</span>, <span class="s">"France"</span>, <span class="n">12</span>)',
         "<span class='mono'>self</span>, c'est «&nbsp;moi-même&nbsp;». <span class='mono'>self.titre</span> se lit «&nbsp;mon titre&nbsp;»."),
    chiffre("Le raccourci moderne", "15&rarr;6", "lignes, avec @dataclass",
            "Et l'affichage lisible et la comparaison sont offerts.", S,
            notes="Règle simple : si ta classe est surtout des attributs, prends une dataclass. Si elle est surtout du comportement, écris une classe normale."),
    code("@dataclass",
         '<span class="k">from</span> dataclasses <span class="k">import</span> dataclass, field\n\n'
         '<span class="f">@dataclass</span>\n'
         '<span class="k">class</span> <span class="f">Opportunite</span>:\n'
         '    titre: <span class="k">str</span>\n'
         '    pays: <span class="k">str</span>\n'
         '    tags: <span class="k">list</span>[<span class="k">str</span>] = <span class="f">field</span>(default_factory=<span class="k">list</span>)',
         "<mark>default_factory=list</mark> et jamais <span class='mono'>= []</span>&nbsp;: une liste par défaut serait partagée par tous les objets."),
    alerte("Le piège n&deg;1 des dataclasses", 'Jamais <span class="mono" style="font-size:.8em">= []</span><br>comme valeur par défaut.',
           "Toutes les instances partageraient la même liste.", S,
           notes="Le démontrer en direct : créer deux objets, ajouter un tag à l'un, constater qu'il apparaît chez l'autre. Stupéfaction garantie."),
    duel("Les chaînes magiques", "Une faute de frappe doit devenir une erreur, pas un bug silencieux.",
         ('statut = "en cour"', "aucune erreur", "Le filtrage casse en silence."),
         ("Statut.EN_COURS", "erreur immédiate", "Et l'éditeur complète tout seul."), S),
    analogie("@property", "boite", 'L\'attribut qui<br>se <span class="souligne">calcule</span> tout seul.',
             "<span class='mono'>opp.jours_restants</span> &mdash; sans parenthèses, recalculé à chaque lecture. Stocker ce nombre serait faux dès demain.",
             S),
    duel("Héritage ou composition ?", "Une seule question à se poser.",
         ("est un", "StageEtudiant est une Opportunite", "Héritage. Rare, à manier avec prudence."),
         ("a des", "Carnet a des Opportunite", "Composition. C'est le cas dans 80 % des situations."), S,
         notes="Dire honnêtement : l'héritage est enseigné en premier et surutilisé en pratique. On l'apprend pour savoir le lire, pas pour en mettre partout."),
    idee("La vérité sur l'encapsulation", 'Python n\'a pas<br>de <span class="souligne">private</span>.', S, BAS,
         notes="_attribut est un panneau, pas un mur. Le dire franchement évite une confusion durable à ceux qui viennent de Java."),
    exercice("Fil rouge v2", "Refactoriser en deux classes", [
        "<span class='mono'>Opportunite</span> &mdash; une opportunité",
        "<span class='mono'>Carnet</span> &mdash; la collection et la persistance",
        "<b>Le comportement visible ne change pas</b>",
        "C'est ça, refactoriser",
    ]),
    code("La récompense",
         'carnet = <span class="f">Carnet</span>()\n'
         'carnet.<span class="f">charger</span>()\n\n'
         '<span class="k">for</span> opp <span class="k">in</span> carnet.<span class="f">triees_par_urgence</span>():\n'
         '    <span class="f">print</span>(opp.titre, opp.jours_restants)',
         "Le code principal se lit maintenant comme une phrase en français. C'est le seul argument qui convainc vraiment."),
    regle("À retenir", 'Une classe,<br>une <span class="souligne">responsabilité</span>.', S, BAS),
    fin("La semaine prochaine : on regarde ce que Python fait dans notre dos.", S, BAS),
])

# ═══════════════════════════════════════════════════════════════════════════
# SÉANCE 6 — PYTHON AVANCÉ
# ═══════════════════════════════════════════════════════════════════════════
S = 6
BAS = "Séance 06 &middot; Sous le capot"
total["06"] = deck("06-python-avance.html", "Séance 6 — Sous le capot", [
    couverture("Sous<br>le capot.", "Aujourd'hui, tu arrêtes d'utiliser Python et tu commences à le comprendre.",
               [("Séance", "06"), ("Durée", "3 h"), ("Objectif", "Savoir lire")], S),
    idee("Objectif réaliste", 'Aujourd\'hui, il suffit<br>de savoir <span class="souligne">lire</span> ce code.', S, BAS,
         notes="Le dire explicitement en ouverture. C'est la séance la plus dure du cursus : assumer que les débutants ne finiront pas tous les exercices, et que ce n'est pas grave."),
    idee("L'énigme du jour", '&lt;__main__.Carnet<br>object at 0x7f3a&hellip;&gt;<br><span class="souligne">Pourquoi&nbsp;?</span>', S, BAS),
    section(1, "Les prises normalisées", "Ce que Python cherche dans tes objets.", S),
    analogie("Les dunder methods", "prise", 'Python cherche<br>une <span class="souligne">prise</span>.',
             "Il ne demande pas « quelle est ta longueur ? ». Il cherche <span class='mono'>__len__</span>. Si elle existe, <span class='mono'>len(objet)</span> marche.",
             S),
    tuiles("Le catalogue utile", "Tu écris la prise, Python branche l'appareil.", [
        ("__len__", "<span class='mono'>len(carnet)</span>"),
        ("__iter__", "<span class='mono'>for x in carnet</span>"),
        ("__eq__", "<span class='mono'>a == b</span>"),
        ("__repr__", "ce qui s'affiche dans le débogueur"),
    ], notes="Règle pratique : si tu n'en écris qu'une, écris __repr__. Python l'utilise par défaut pour les deux, et c'est celle qui s'affiche dans les listes."),
    section(2, "La paresse", "Ne calculer que ce qu'on demande.", S),
    analogie("Le générateur", "ticket", 'Un <span class="souligne">distributeur</span><br>de tickets.',
             "Une liste imprime les 10 millions de tickets d'avance. Un générateur en imprime un quand tu appuies.",
             S),
    chiffre("La preuve", "×10⁶", "moins de mémoire",
            "Quelques dizaines d'octets, contre plusieurs centaines de mégaoctets.", S,
            notes="Le mesurer en direct avec sys.getsizeof sur range(10_000_000) puis list(range(10_000_000)). L'écart marque durablement."),
    code("yield",
         '<span class="k">def</span> <span class="f">lignes_du_fichier</span>(chemin):\n'
         '    <span class="k">with</span> <span class="f">open</span>(chemin, encoding=<span class="s">"utf-8"</span>) <span class="k">as</span> f:\n'
         '        <span class="k">for</span> ligne <span class="k">in</span> f:\n'
         '            <span class="k">yield</span> ligne.<span class="f">strip</span>()',
         "<span class='mono'>yield</span> rend une valeur, <b>met en pause</b>, et reprend au tour suivant."),
    section(3, "Le décorateur", "Quatre marches. Aucune à sauter.", S),
    analogie("Analogie", "cadeau", 'Un décorateur,<br>c\'est un <span class="souligne">emballage</span>.',
             "Il enveloppe une fonction pour lui ajouter un comportement, sans toucher à son contenu.",
             S),
    etapes("Les quatre marches", "C'est ce découpage qui fait la différence.", [
        ("Une fonction est une valeur", "<span class='mono'>f = dire_bonjour</span>"),
        ("Elle peut en recevoir une", "<span class='mono'>def deux_fois(f)</span>"),
        ("Elle peut en rendre une", "La marche difficile."),
        ("@ est du sucre", "<span class='mono'>f = deco(f)</span>"),
    ], notes="Ne jamais sauter la marche 3. C'est là que se joue la différence entre « je copie » et « je comprends ». Y consacrer le temps nécessaire."),
    code("@chronometre",
         '<span class="k">def</span> <span class="f">chronometre</span>(fonction):\n'
         '    <span class="f">@functools.wraps</span>(fonction)\n'
         '    <span class="k">def</span> <span class="f">enveloppe</span>(*args, **kwargs):\n'
         '        depart = time.<span class="f">perf_counter</span>()\n'
         '        resultat = <span class="f">fonction</span>(*args, **kwargs)\n'
         '        <span class="f">print</span>(time.<span class="f">perf_counter</span>() - depart)\n'
         '        <mark>return resultat</mark>\n'
         '    <span class="k">return</span> enveloppe',
         "Retire <span class='mono'>return resultat</span>&nbsp;: la fonction décorée rend None et tout casse en aval.", petit=True,
         notes="Provoquer les deux erreurs en direct : sans le return, puis sans functools.wraps (le nom devient « enveloppe »)."),
    code("match structurel",
         '<span class="k">match</span> evenement:\n'
         '    <span class="k">case</span> {<span class="s">"type"</span>: <span class="s">"offre"</span>, <span class="s">"jours"</span>: <span class="k">int</span>(j)} <span class="k">if</span> j &lt; <span class="n">7</span>:\n'
         '        <span class="f">alerter</span>(j)\n'
         '    <span class="k">case</span> [premier, *autres]:\n'
         '        <span class="f">traiter</span>(premier)',
         "Ce n'est pas un <span class='mono'>switch</span>&nbsp;: c'est du <b>filtrage de forme</b>. Parfait pour du JSON &mdash; séances 9 et 10."),
    duel("L'outillage qualité", "Deux commandes, et on ne débat plus.",
         ("Avant", "black + flake8 + isort", "Trois outils, trois configurations."),
         ("Maintenant", "ruff format . / ruff check .", "Un seul outil, en quelques millisecondes."), S,
         notes="Vendre ruff comme un gain de temps SOCIAL : plus aucune revue de code ne porte sur la mise en forme, donc toutes portent sur le fond."),
    exercice("Atelier", "Tes trois premiers tests", [
        "<span class='mono'>assert</span>, c'est «&nbsp;j'affirme que&nbsp;». C'est tout.",
        "Écris trois tests. Lance <span class='mono'>pytest</span>. Trois points verts.",
        "Puis <b>casse volontairement</b> ton code.",
        "Le test rouge est le moment de la séance.",
    ]),
    regle("À retenir", 'Un générateur ne se<br>parcourt qu\'<span class="souligne">une fois</span>.', S, BAS),
    fin("La semaine prochaine : quarante mille lignes de données.", S, BAS),
])

# ═══════════════════════════════════════════════════════════════════════════
# SÉANCE 7 — NUMPY & PANDAS
# ═══════════════════════════════════════════════════════════════════════════
S = 7
BAS = "Séance 07 &middot; NumPy &amp; pandas"
total["07"] = deck("07-numpy-pandas.html", "Séance 7 — NumPy & pandas", [
    couverture("Les<br>données.", "Ta liste de dictionnaires plafonne à quelques centaines de lignes. Aujourd'hui, on en traite cent mille.",
               [("Séance", "07"), ("Durée", "3 h"), ("Version", "pandas 3.0")], S),
    alerte("Avant toute chose", 'Les tutoriels d\'avant 2026<br>vont te faire écrire<br>du code qui <span class="souligne">plante</span>.',
           "pandas 3.0 est sorti en janvier 2026. Vérifie toujours la date.", S,
           notes="Faire exécuter print(pd.__version__) par tout le monde. Si c'est une 2.x, installer et redémarrer le noyau avant de continuer."),
    idee("Le pont", 'Ta liste de dictionnaires<br>de la séance 3&nbsp;:<br>c\'est un <span class="souligne">DataFrame</span>.', S, BAS,
         notes="Afficher les deux côte à côte, mêmes données. « Vous connaissez déjà la structure. Il ne reste que la syntaxe. »"),
    section(1, "NumPy", "Pourquoi c'est rapide.", S),
    duel("Deux façons de ranger", "La vitesse vient du rangement, pas de la magie.",
         ("La liste", "un sac de courses", "N'importe quoi dedans, éparpillé en mémoire."),
         ("Le ndarray", "une boîte à œufs", "Une seule sorte, des cases contiguës.")
         , S),
    chiffre("Mesuré en direct", "×62", "plus rapide que ta boucle",
            "Un million de multiplications. Même machine, même résultat.", S,
            notes="Ne PAS annoncer le chiffre : le produire avec %timeit devant le groupe. La mesure vaut dix explications."),
    code("La vectorisation",
         '<span class="c"># La façon liste : Python fait 1 000 000 de tours</span>\n'
         'resultats = [x * <span class="n">2</span> <span class="k">for</span> x <span class="k">in</span> valeurs]\n\n'
         '<span class="c"># La façon NumPy : la boucle est dans le C</span>\n'
         '<span class="ok">resultats = valeurs * <span class="n">2</span></span>',
         "Programmer avec NumPy, c'est arrêter d'écrire la boucle."),
    idee("Le concept qui débloque tout", 'Le <span class="souligne">masque</span> booléen.', S, BAS,
         notes="Le faire dessiner : une rangée de valeurs, une rangée de cases cochées. C'est exactement le mécanisme de df[df.jours < 7]."),
    section(2, "pandas", "Le tableur programmable.", S),
    liste("Le rituel", "Cinq commandes devant tout jeu de données inconnu", [
        "<span class='mono'>df.shape</span> &mdash; combien de lignes, de colonnes",
        "<span class='mono'>df.head()</span> &mdash; à quoi ça ressemble",
        "<span class='mono'>df.info()</span> &mdash; les types, les manquants",
        "<span class='mono'>df.describe()</span> &mdash; les distributions",
        "<span class='mono'>df[\"pays\"].value_counts()</span> &mdash; <b>ce qu'il y a vraiment dedans</b>",
    ], notes="À imprimer et afficher au mur. C'est value_counts() qui révèle que « Maroc », « maroc » et « MAROC » sont trois pays différents pour la machine."),
    chiffre("Le détecteur de saleté", "3", "pays au lieu d'un",
            "Maroc &middot; maroc &middot; MAROC &mdash; la machine ne pardonne pas.", S),
    duel(".loc ou .iloc ?", "La confusion n°1 de pandas.",
         (".iloc", "des positions", "Le <b>i</b> comme index numérique."),
         (".loc", "des étiquettes", "Des noms de colonnes, des valeurs d'index."), S),
    section(3, "pandas 3.0", "La règle d'or, et la seule à apprendre.", S),
    idee("La règle d'or", 'pandas rend<br>une <span class="souligne">nouvelle table</span>.<br>Réaffecte.', S, BAS,
         notes="Ne jamais mentionner l'ancien monde ni SettingWithCopyWarning. Le nouveau modèle mental est plus simple : chaque étape produit une nouvelle table."),
    duel("Copy-on-Write", "Ce qui change concrètement",
         ('df[df.jours&gt;0]["statut"] = "actif"', "lève une ERREUR", "Ce n'est plus un avertissement."),
         ('df = df.assign(statut="actif")', "la bonne façon", "Chaque étape produit une nouvelle table."), S),
    alerte("Le piège des filtres", 'Utilise <span class="souligne">&amp;</span> et <span class="souligne">|</span>,<br>jamais <span class="mono" style="font-size:.8em">and</span> ni <span class="mono" style="font-size:.8em">or</span>.',
           "Et mets des parenthèses autour de chaque condition.", S,
           notes="L'erreur pandas la plus fréquente au monde. On combine deux COLONNES de booléens, pas deux valeurs."),
    formule("Ce que fait describe()", "L'écart-type, en une ligne",
            r"\sigma=\sqrt{\frac{1}{n}\sum_{i=1}^{n}\bigl(x_i-\bar{x}\bigr)^{2}}",
            "Traduction&nbsp;: à quel point les valeurs s'éloignent de la moyenne. <span class='mono'>df[\"montant\"].std()</span>",
            notes="Ne pas démontrer. Montrer, traduire en une phrase, revenir au code. Un public mixte décroche sur une démonstration, pas sur une définition."),
    exercice("Fil rouge v4", "300 opportunités très sales", [
        "Casse incohérente, trois formats de date, doublons",
        "Montants en texte&nbsp;: «&nbsp;12 000 MAD&nbsp;», «&nbsp;N/A&nbsp;»",
        "<b>Trace ce que tu jettes</b>&nbsp;: compte et affiche",
        "Produis <span class='mono'>opportunites_propres.csv</span>",
    ], notes="Un nettoyage silencieux est un nettoyage suspect. Chaque suppression s'accompagne d'un comptage affiché."),
    regle("À retenir", 'On <span class="souligne">trace</span><br>ce qu\'on jette.', S, BAS),
    fin("La semaine prochaine : un tableau propre ne convainc personne. Un graphique juste, si.", S, BAS),
])

# ═══════════════════════════════════════════════════════════════════════════
# SÉANCE 8 — DATAVIZ
# ═══════════════════════════════════════════════════════════════════════════
S = 8
BAS = "Séance 08 &middot; Faire parler les données"
total["08"] = deck("08-dataviz.html", "Séance 8 — Faire parler les données", [
    couverture("Faire parler<br>les données.", "Un tableau propre ne convainc personne. Un graphique juste, si.",
               [("Séance", "08"), ("Durée", "3 h"), ("Outils", "Matplotlib · seaborn")], S),
    idee("Le graphique du jour", 'Trouve l\'<span class="souligne">entourloupe</span>.', S, BAS,
         notes="Projeter un vrai graphique de presse à axe tronqué. Laisser le groupe chercher 90 secondes avant de révéler."),
    section(1, "Agréger", "Découper, appliquer, combiner.", S),
    etapes("groupby", "Trois temps, à mimer avec des cartes", [
        ("Découper", "Un tas par pays."),
        ("Appliquer", "Compter chaque tas."),
        ("Combiner", "Une seule table de résultats."),
    ], notes="Mimer physiquement avec des cartes de couleur. Le geste reste en mémoire bien plus longtemps que la syntaxe."),
    code("La syntaxe moderne",
         'resume = (df.<span class="f">groupby</span>(<span class="s">"pays"</span>)\n'
         '            .<span class="f">agg</span>(nombre=(<span class="s">"titre"</span>, <span class="s">"count"</span>),\n'
         '                 jours_moyens=(<span class="s">"jours"</span>, <span class="s">"mean"</span>))\n'
         '            .<span class="f">reset_index</span>())',
         "La forme <span class='mono'>nom=(\"colonne\", \"fonction\")</span> nomme les colonnes de sortie. N'enseigne pas l'autre."),
    idee("merge", 'C\'est le<br><span class="souligne">RECHERCHEV</span><br>d\'Excel. En mieux.', S, BAS,
         notes="Pour un public venant d'Excel, cette seule phrase fait passer le concept. Puis les quatre types avec des diagrammes d'ensembles."),
    alerte("Le piège de la jointure", 'Compte tes lignes<br><span class="souligne">avant</span> et <span class="souligne">après</span>.',
           "Si le nombre a grossi, c'est un bug, pas un succès.", S,
           notes="Si la clé n'est pas unique à droite, le nombre de lignes explose. Installer le réflexe : len(df) avant, len(df) après."),
    section(2, "Dessiner", "Le cadre et la photo.", S),
    analogie("Matplotlib", "tableau", 'La <span class="souligne">Figure</span> est le cadre.<br>L\'<span class="souligne">Axes</span> est la photo.',
             "Un cadre peut contenir plusieurs photos. C'est toute l'architecture de Matplotlib.",
             S),
    duel("Deux interfaces", "N'en apprends qu'une.",
         ("plt.bar(...)", "agit sur « le graphique courant »", "Invisible, fragile, impraticable à deux graphiques."),
         ("fig, ax = plt.subplots()", "explicite", "Se compose, fonctionne partout."), S,
         notes="Justification : dès qu'on veut deux graphiques côte à côte, l'interface d'état devient impraticable. Autant prendre la bonne habitude tout de suite."),
    tuiles("Quelle question, quel graphique ?", "La slide à imprimer.", [
        ("comparer", "des barres"),
        ("évoluer", "une ligne"),
        ("répartir", "un histogramme"),
        ("corréler", "un nuage de points"),
    ]),
    chiffre("seaborn", "1", "ligne au lieu de quinze",
            "Les moyennes par groupe et les intervalles de confiance sont inclus.", S),
    section(3, "L'honnêteté", "Cinq règles, non négociables.", S),
    liste("Dataviz honnête", "À afficher au mur", [
        "Le <b>titre porte le message</b>, pas la description",
        "L'axe des barres part de <b>zéro</b>. Toujours.",
        "<b>Trier</b> par valeur, pas par ordre alphabétique",
        "Pas de camembert au-delà de 3 parts. Jamais en 3D.",
        "Une question, un graphique",
    ]),
    duel("La règle n°1, en pratique", "Le même graphique, deux titres.",
         ("Opportunités par pays", "descriptif", "Le lecteur doit chercher lui-même."),
         ("Le Maroc en concentre 60 %", "le message", "Le lecteur sait quoi regarder."), S,
         notes="C'est LE moment pédagogique de la séance. Faire réécrire les quatre titres du tableau de bord. Question : « qu'est-ce que ce graphique t'apprend, en une phrase ? »"),
    formule("Ce que « corrélation » veut dire", "Le r de Pearson",
            r"r=\frac{\sum (x_i-\bar{x})(y_i-\bar{y})}{\sqrt{\sum (x_i-\bar{x})^2}\sqrt{\sum (y_i-\bar{y})^2}}",
            "Entre &minus;1 et 1. Et une corrélation n'est <b>jamais</b> une cause."),
    exercice("Fil rouge v5", "Le tableau de bord", [
        "Une figure, quatre panneaux, quatre questions",
        "Combien par pays&nbsp;? Comment se répartissent les délais&nbsp;?",
        "Où en sont les candidatures&nbsp;? Montant contre délai&nbsp;?",
        "<b>Écris tes titres, puis réécris-les</b>",
    ]),
    regle("À retenir", 'Un titre honnête peut dire<br>qu\'il n\'y a <span class="souligne">rien</span> à voir.', S, BAS,
          notes="Tous les graphiques ne racontent pas une histoire, et c'est une information en soi."),
    fin("La semaine prochaine : les données ne tombent pas du ciel. On va les chercher.", S, BAS),
])

# ═══════════════════════════════════════════════════════════════════════════
# SÉANCE 9 — SCRAPING
# ═══════════════════════════════════════════════════════════════════════════
S = 9
BAS = "Séance 09 &middot; Aller chercher la donnée"
total["09"] = deck("09-scraping.html", "Séance 9 — Aller chercher la donnée", [
    couverture("Aller chercher<br>la donnée.", "Jusqu'ici, quelqu'un t'a donné un CSV. Aujourd'hui, tu fabriques tes propres données.",
               [("Séance", "09"), ("Durée", "3 h"), ("Terrain", "Site d'entraînement")], S),
    liste("Avant la première ligne de code", "Les cinq règles", [
        "<b>API d'abord</b>, scraping seulement si nécessaire",
        "Lire <span class='mono'>robots.txt</span> et les CGU <b>avant</b>",
        "Un <b>délai</b> entre chaque requête",
        "<b>Aucune donnée personnelle</b>",
        "S'identifier honnêtement dans le User-Agent",
    ], fond="rouge", notes="Ce bloc n'est pas un supplément moral, c'est une compétence professionnelle. Il ouvre la séance, il ne la conclut pas."),
    section(1, "Le web vu de l'intérieur", "Requête, réponse, code de statut.", S),
    analogie("HTTP", "plateau", 'Tu passes commande.<br>La cuisine <span class="souligne">répond</span>.',
             "Et la réponse porte un code qui dit comment ça s'est passé.",
             S),
    tuiles("Les codes qui comptent", "À reconnaître du premier coup d'œil.", [
        ("200", "voilà votre plat"),
        ("404", "ce plat n'existe pas"),
        ("403", "vous n'êtes pas le bienvenu"),
        ("429", "vous commandez trop vite"),
    ], notes="429, c'est le code que tout scraper finit par rencontrer. C'est le serveur qui demande de ralentir : on ralentit."),
    idee("La règle d'or", 'Une API&nbsp;?<br>Alors la question<br>est <span class="souligne">réglée</span>.', S, BAS,
         notes="Le scraping, c'est lire la vitrine faute de porte d'entrée : fragile, lent, juridiquement plus sensible."),
    section(2, "Extraire", "Du HTML aux données.", S),
    analogie("Le HTML", "imbrique", 'Des boîtes<br>dans des boîtes,<br>toutes <span class="souligne">étiquetées</span>.',
             "Scraper, c'est dire&nbsp;: «&nbsp;donne-moi le contenu de toutes les boîtes portant le badge <i>prix</i>&nbsp;».",
             S),
    tuiles("Cinq sélecteurs CSS", "Ils couvrent 95 % des besoins.", [
        ("h2", "toutes les balises h2"),
        (".prix", "les éléments de classe prix"),
        ("article .titre", "les .titre <b>à l'intérieur</b> d'un article"),
        ("a[href]", "les liens qui ont un href"),
    ]),
    etapes("Trouver le bon sélecteur", "Le navigateur l'écrit à ta place.", [
        ("Clic droit", "Inspecter."),
        ("Clic droit sur l'élément", "Copier le sélecteur."),
        ("Simplifier", "Garder le minimum qui fonctionne."),
    ]),
    code("BeautifulSoup",
         'soup = <span class="f">BeautifulSoup</span>(html, <span class="s">"html.parser"</span>)\n\n'
         '<span class="k">for</span> fiche <span class="k">in</span> soup.<span class="f">select</span>(<span class="s">"article.product_pod"</span>):\n'
         '    lien = fiche.<span class="f">select_one</span>(<span class="s">"h3 a"</span>)\n'
         '    titre = <mark>lien["title"] if lien else None</mark>',
         "Toujours vérifier l'existence avant d'accéder. Une fiche mal formée ne doit pas faire tomber tout le scraper."),
    section(3, "L'éthique", "Quatre questions, à chaque fois.", S),
    liste("Avant de scraper", "Les quatre questions", [
        "Une <b>API</b> existe-t-elle&nbsp;?",
        "Que disent le <span class='mono'>robots.txt</span> et les <b>CGU</b>&nbsp;?",
        "Y a-t-il des <b>données personnelles</b>&nbsp;?",
        "Quelle <b>charge</b> est-ce que j'impose au serveur&nbsp;?",
    ], fond="vert"),
    alerte("Public n'est pas libre", 'Une donnée <span class="souligne">visible</span><br>n\'est pas une donnée<br>librement réutilisable.',
           "Noms, courriels, photos&nbsp;: on entre dans le RGPD.", S,
           notes="Préciser explicitement que tu n'es pas juriste et que le droit varie selon les pays. L'objectif est le réflexe, pas la doctrine."),
    idee("La ligne à ne pas franchir", 'Se faire passer pour<br>un navigateur pour<br>contourner un <span class="souligne">blocage</span>.', S, BAS,
         notes="Cas à débattre en groupe, sans réponse imposée : scraper des offres pour ma recherche d'emploi ; les republier avec de la pub ; collecter des profils de réseau social ; relever les prix d'un concurrent."),
    alerte("La ligne qui change tout", '<span class="mono" style="font-size:.78em">time.sleep(1)</span>',
           "C'est ce qui sépare un outil d'une nuisance.", S),
    exercice("Fil rouge v6", "Le scraper paginé", [
        "Terrain&nbsp;: <span class='mono'>books.toscrape.com</span>, conçu pour ça",
        "Parcourir les pages jusqu'au 404",
        "Un délai entre chaque requête, un <span class='mono'>timeout</span>",
        "Le scraper <b>collecte</b>. pandas <b>nettoie</b>.",
    ], notes="On s'entraîne sur un terrain prévu pour ça, jamais sur un site réel en séance. C'est une leçon en soi."),
    idee("Ce que requests ne voit pas", 'Les pages construites<br>en <span class="souligne">JavaScript</span>.', S, BAS,
         notes="Démo Playwright de 5 minutes : la page est vide en HTML brut, pleine dans le navigateur. Puis mentionner Scrapy pour la grande échelle."),
    regle("À retenir", 'Le scraper collecte.<br>pandas <span class="souligne">nettoie</span>.', S, BAS),
    fin("La semaine prochaine : ton programme cesse de ne servir qu'à toi.", S, BAS),
])

# ═══════════════════════════════════════════════════════════════════════════
# SÉANCE 10 — FASTAPI
# ═══════════════════════════════════════════════════════════════════════════
S = 10
BAS = "Séance 10 &middot; Exposer avec FastAPI"
total["10"] = deck("10-fastapi.html", "Séance 10 — API REST avec FastAPI", [
    couverture("Du script<br>au service.", "Ton programme ne servira plus qu'à toi. À la fin, n'importe qui pourra l'utiliser depuis n'importe où.",
               [("Séance", "10"), ("Durée", "3 h"), ("Pile", "FastAPI · Pydantic v2")], S),
    idee("La question de départ", 'Comment ton collègue<br>utilise-t-il<br>ton <span class="souligne">programme</span>&nbsp;?', S, BAS,
         notes="Laisser venir les mauvaises réponses : lui envoyer le fichier, partager l'écran, lui installer Python. Elles mènent toutes seules à la bonne."),
    analogie("Analogie", "passeplat", 'Une API,<br>c\'est un <span class="souligne">passe-plat</span>.',
             "La cuisine et la salle ne se voient pas. Le passe-plat définit ce qui peut être demandé, et sous quelle forme.",
             S),
    section(1, "REST", "Une ressource, une adresse, un verbe.", S),
    tuiles("Tu l'as déjà écrit en séance 5", "L'API n'ajoute pas de logique. Elle ajoute une porte.", [
        ("GET /opportunites", "<span class='mono'>carnet.toutes()</span>"),
        ("GET /opportunites/12", "<span class='mono'>carnet[12]</span>"),
        ("POST /opportunites", "<span class='mono'>carnet.ajouter(...)</span>"),
        ("DELETE /opportunites/12", "<span class='mono'>carnet.supprimer(12)</span>"),
    ], notes="C'est l'argument qui rend la séance abordable même pour les profils non techniques. Insister : rien de nouveau côté logique."),
    idee("Le JSON", 'C\'est ton dictionnaire<br>Python, écrit en <span class="souligne">texte</span>.', S, BAS),
    section(2, "Pydantic v2", "Le videur à l'entrée.", S),
    idee("Pydantic", 'Il refuse les données<br><span class="souligne">avant</span> que ton code<br>ne s\'exécute.', S, BAS,
         notes="Conséquence directe : tu n'écris plus jamais de if not isinstance(...). Et le message d'erreur indique précisément quel champ pose problème."),
    code("Un modèle",
         '<span class="k">class</span> <span class="f">Opportunite</span>(BaseModel):\n'
         '    titre: <span class="k">str</span> = <span class="f">Field</span>(min_length=<span class="n">3</span>, max_length=<span class="n">200</span>)\n'
         '    pays: <span class="k">str</span>\n'
         '    deadline: date\n\n'
         '    <span class="f">@field_validator</span>(<span class="s">"pays"</span>)\n'
         '    <span class="f">@classmethod</span>\n'
         '    <span class="k">def</span> <span class="f">normaliser</span>(cls, v): <span class="k">return</span> v.<span class="f">strip</span>().<span class="f">title</span>()',
         "La validation s'exécute avant le code métier. Le nettoyage de la séance 7 devient inutile pour tout ce qui passe par l'API.", petit=True),
    alerte("Attention aux tutoriels", 'FastAPI ne supporte<br><span class="souligne">plus</span> Pydantic&nbsp;v1.',
           "Tout contenu antérieur à 2024 est périmé.", S),
    tuiles("v1 &rarr; v2 : la table à connaître", "À gauche, ce qui n'existe plus.", [
        ("@validator", "&rarr; <span class='mono'>@field_validator</span>"),
        (".dict()", "&rarr; <span class='mono'>.model_dump()</span>"),
        ("parse_obj()", "&rarr; <span class='mono'>model_validate()</span>"),
        ("class Config", "&rarr; <span class='mono'>model_config = ConfigDict()</span>"),
    ]),
    duel("Entrée et sortie", "Deux modèles, jamais un seul.",
         ("OpportuniteCreation", "ce que le client envoie", "Pas d'identifiant : le serveur l'attribue."),
         ("OpportuniteLecture", "ce que le serveur rend", "Identifiant + champs calculés."), S,
         notes="Confondre les deux, c'est laisser un client imposer un identifiant ou lire un champ interne."),
    section(3, "Le moment waouh", "La documentation, gratuitement.", S),
    idee("Tu écris les types", 'Tu obtiens la validation,<br>le JSON, et une doc<br><span class="souligne">testable</span>.', S, BAS,
         notes="Ouvrir /docs en direct et cliquer sur « Try it out ». Ne pas rater ce moment : il justifie à lui seul la séance."),
    code("Gérer l'absence",
         '<span class="k">if</span> opportunite <span class="k">is</span> <span class="k">None</span>:\n'
         '    <span class="k">raise</span> <span class="f">HTTPException</span>(\n'
         '        status_code=status.HTTP_404_NOT_FOUND,\n'
         '        detail=<span class="s">f"Aucune opportunité d\'identifiant {opp_id}"</span>)',
         "Ne jamais rendre 200 avec un corps vide pour une ressource absente&nbsp;: c'est mentir au client."),
    exercice("Fil rouge v7", "L'API OpportuniTrack", [
        "<span class='mono'>GET /opportunites</span> avec filtres",
        "<span class='mono'>POST</span> qui rend <b>201</b>, <span class='mono'>DELETE</span> qui rend <b>204</b>",
        "<span class='mono'>GET /statistiques</span> &mdash; le groupby de la S8, en JSON",
        "Puis ouvre <span class='mono'>/docs</span> et clique sur «&nbsp;Try it out&nbsp;»",
    ]),
    idee("Le test qui prouve tout", 'Un titre de deux lettres<br>est refusé. Et tu n\'as écrit<br><span class="souligne">aucune</span> validation.', S, BAS,
         notes="C'est Pydantic qui travaille. Ça répond concrètement à la question « à quoi servent les types ? » posée depuis la séance 4."),
    regle("À retenir", 'Documenter son code,<br>c\'est documenter<br>son <span class="souligne">API</span>.', S, BAS),
    fin("La semaine prochaine : on verrouille, on teste, on livre. Et vous présentez.", S, BAS),
])

# ═══════════════════════════════════════════════════════════════════════════
# SÉANCE 11 — PRODUCTION + DEMO DAY
# ═══════════════════════════════════════════════════════════════════════════
S = 11
BAS = "Séance 11 &middot; Qualité et production"
total["11"] = deck("11-production.html", "Séance 11 — Qualité, tests, production", [
    couverture("Rendre<br>livrable.", "Le code qui marche sur ta machine ne vaut rien. Aujourd'hui, il marche partout.",
               [("Séance", "11"), ("Durée", "3 h"), ("Final", "Demo Day")], S),
    idee("La phrase interdite", '«&nbsp;Ça marche<br>sur <span class="souligne">ma</span> machine.&nbsp;»', S, BAS),
    section(1, "L'environnement", "Un seul outil à la place de cinq.", S),
    chiffre("uv", "5&rarr;1", "outils remplacés",
            "pip, virtualenv, pyenv, pipx, poetry.", S,
            notes="Le montrer : supprimer .venv, lancer uv sync, l'environnement se reconstruit en quelques secondes. L'effet est plus convaincant que le discours."),
    code("Les cinq commandes",
         '<span class="f">uv</span> init opportunitrack    <span class="c"># le squelette</span>\n'
         '<span class="f">uv</span> add fastapi uvicorn    <span class="c"># ajoute ET installe</span>\n'
         '<span class="f">uv</span> add --dev pytest ruff  <span class="c"># outils de dev</span>\n'
         '<span class="f">uv</span> run pytest             <span class="c"># sans activer quoi que ce soit</span>\n'
         '<span class="f">uv</span> sync                   <span class="c"># reconstruit à l\'identique</span>',
         "<span class='mono'>uv.lock</span> fige les versions exactes. «&nbsp;Ça marche partout&nbsp;», et c'est vérifiable."),
    duel("Ruff", "Un seul outil, en quelques millisecondes.",
         ("Avant", "black + flake8 + isort + pylint", "Quatre outils, quatre configurations."),
         ("ruff", "format . / check . --fix", "Le débat sur les espaces est clos."), S),
    section(2, "Tester", "Ce qui rapporte, et ce qui ne rapporte rien.", S),
    liste("Que tester en priorité ?", "Dans cet ordre, pas un autre", [
        "La <b>logique métier</b> &mdash; rentabilité maximale",
        "Les <b>cas limites</b> &mdash; liste vide, valeur nulle, date passée",
        "Les <b>bugs déjà rencontrés</b> &mdash; sinon ils reviendront",
        "Les <b>routes d'API</b> en surface",
    ], notes="Ne pas tester : les bibliothèques des autres, les getters triviaux, la mise en forme. Les débutants veulent tout tester ou rien."),
    analogie("La fixture", "moule", 'C\'est le<br><span class="souligne">décor</span> de théâtre.',
             "Elle prépare l'environnement du test et le range ensuite, sans dupliquer ce code partout.",
             S),
    code("parametrize",
         '<span class="f">@pytest.mark.parametrize</span>(<span class="s">"jours, attendu"</span>, [\n'
         '    (<span class="n">-1</span>, <span class="k">False</span>),  <span class="c"># déjà passée</span>\n'
         '    (<span class="n">0</span>,  <span class="k">True</span>),\n'
         '    (<span class="n">6</span>,  <span class="k">True</span>),   <span class="c"># limite haute</span>\n'
         '    (<span class="n">7</span>,  <span class="k">False</span>),  <span class="c"># juste au-delà</span>\n'
         '])',
         "Un seul test, cinq cas. Et on teste les <b>bornes</b> (6 et 7), jamais des valeurs confortables."),
    formule("La couverture", "Un indicateur, pas un objectif",
            r"\text{couverture}=\frac{\text{lignes exécutées}}{\text{lignes totales}}",
            "60&nbsp;% bien ciblés valent mieux que 100&nbsp;% d'assertions creuses.",
            notes="Le dire explicitement évite une course au chiffre, qui produit des tests inutiles et un faux sentiment de sécurité."),
    section(3, "Livrer", "Secrets, conteneur, automatisation.", S),
    alerte("En quelques minutes", 'Une clé publiée sur GitHub<br>est <span class="souligne">exploitée</span>.',
           "Et supprimer le fichier ne suffit pas&nbsp;: l'historique conserve tout.", S,
           notes="Des robots scrutent GitHub en continu. La bonne pratique : .env dans .gitignore, .env.example versionné sans valeurs."),
    analogie("Docker", "carton", 'C\'est un <span class="souligne">carton</span><br>de déménagement.',
             "On emballe l'application <i>avec</i> son environnement. Le carton s'ouvre à l'identique sur n'importe quelle machine.",
             S),
    idee("L'intégration continue", 'Le collègue qui vérifie<br>à ta place, à chaque<br><span class="souligne">envoi</span>.', S, BAS,
         notes="Le badge vert sur le dépôt est un moteur de motivation puissant. Le montrer comme tel."),
    liste("La checklist du livrable", "À cocher avant le Demo Day", [
        "README avec installation et captures",
        "<span class='mono'>ruff check</span> et <span class='mono'>ruff format --check</span> sans erreur",
        "Au moins 5 tests qui passent, dont un test d'API",
        "<span class='mono'>.env</span> jamais versionné",
        "CI au vert &middot; Dockerfile fonctionnel",
    ], fond="vert"),
    section(12, "Demo Day", "Cinq minutes chacun.", S, fond="vert"),
    liste("La trame imposée", "Dans cet ordre", [
        "Ce que fait mon projet &mdash; 30 s, <b>sans jargon</b>",
        "Démonstration en direct &mdash; 2 min",
        "<b>La difficulté rencontrée, et comment je l'ai résolue &mdash; 1 min 30</b>",
        "Ce que j'ajouterais avec une semaine de plus &mdash; 1 min",
    ], notes="La partie 3 est le cœur de l'exercice et celle qu'on escamote par pudeur. Insister : raconter un bug qui a pris trois heures est plus utile au groupe qu'une démo parfaite."),
    idee("Onze séances plus tard", 'De «&nbsp;je n\'ai jamais codé&nbsp;»<br>à «&nbsp;j\'ai <span class="souligne">déployé</span><br>une API&nbsp;».', S, BAS),
    tuiles("Et après ?", "Quatre chemins, une porte d'entrée chacun.", [
        ("Data / IA", "scikit-learn, puis Kaggle Learn"),
        ("Backend", "bases de données, la suite du tuto FastAPI"),
        ("Automatisation", "Automate the Boring Stuff"),
        ("Applications", "Streamlit : un notebook devient une appli"),
    ]),
    fin("Merci. Le dépôt reste ouvert, et le salon aussi.", S, bas="ASEGUIM &middot; Formation Python 360&deg;"),
])

print("Decks générés :")
for k in sorted(total):
    print(f"  {k} → {total[k]:>2} diapos")
print("TOTAL :", sum(total.values()), "diapositives")
