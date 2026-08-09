"""Moteur de fabrication des diapositives — Formation Python 360° · ASEGUIM.

theme.css et moteur.js sont LA CLASSE (écrits une fois, partagés par tous).
Chaque deck de séance est un OBJET produit par `deck()`.
"""

from pathlib import Path

SORTIE = Path("/home/claude/slides-aseguim")

# ═══════════════════════════════════════════════════════════════════════════
#  THÈME — identité ASEGUIM (rouge · or · vert de Guinée, sur papier blanc)
# ═══════════════════════════════════════════════════════════════════════════

THEME = """/* ═══════════════════════════════════════════════════════════════════════
   FORMATION PYTHON 360° — ASEGUIM
   Thème unique partagé par tous les decks. NE PAS MODIFIER par séance :
   changer une valeur ici la change dans les 12 decks à la fois.
   ═══════════════════════════════════════════════════════════════════════ */
:root{
  /* --- Couleurs, relevées sur le logo ASEGUIM ------------------------- */
  --rouge:        #D81B27;   /* accent principal — le mot important, le danger */
  --rouge-vif:    #F0323E;   /* variante lumineuse, uniquement sur fond sombre */
  --bordeaux:     #6E0A12;   /* profondeur : fonds pleins, dégradés */
  --or:           #FDC911;   /* progression, jalons. Jamais pour du texte      */
  --vert:         #185609;   /* la bonne pratique, le validé (vert du sigle)   */
  --vert-clair:   #2C8A1A;

  /* --- Neutres, chauds ------------------------------------------------ */
  --papier:       #FBF8F7;
  --blanc:        #FFFFFF;
  --craie:        #F5EAE9;
  --trait:        #E6D8D6;
  --cendre:       #8B7B78;
  --encre:        #1A0C0A;

  /* --- Typographie ---------------------------------------------------- */
  --display: "Fraunces", "Iowan Old Style", Georgia, serif;
  --texte:   "Inter Tight", -apple-system, "Segoe UI", Helvetica, Arial, sans-serif;
  --mono:    "JetBrains Mono", "SF Mono", Consolas, monospace;

  --t-geant: 128px; --t-titre: 84px; --t-sous: 50px;
  --t-lead: 31px;   --t-corps: 24px; --t-petit: 19px; --t-micro: 15px;

  --marge: 88px;
  --duree: .45s;
}

*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%}
body{background:#0D0605;font-family:var(--texte);color:var(--encre);
     overflow:hidden;-webkit-font-smoothing:antialiased}
.scene{position:fixed;inset:0;display:grid;place-items:center}

/* --- La diapo : toujours 1280x720, mise à l'échelle ------------------- */
.diapo{position:absolute;width:1280px;height:720px;padding:var(--marge);
       background:var(--papier);display:none;flex-direction:column;overflow:hidden;
       transform:scale(var(--k,1));box-shadow:0 40px 120px rgba(0,0,0,.55)}
.diapo.active{display:flex}
.diapo.active > *{animation:entree var(--duree) cubic-bezier(.2,.7,.2,1) both}
.diapo.active > *:nth-child(2){animation-delay:.06s}
.diapo.active > *:nth-child(3){animation-delay:.12s}
.diapo.active > *:nth-child(4){animation-delay:.18s}
@keyframes entree{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){.diapo.active > *{animation:none}}

.diapo[data-fond="rouge"]{
  background:radial-gradient(120% 90% at 78% 6%, #A11420 0%, transparent 58%),
             linear-gradient(155deg, #97121E 0%, #5C070E 100%);
  color:var(--blanc)}
.diapo[data-fond="vert"]{
  background:radial-gradient(120% 90% at 78% 6%, #1F6B0C 0%, transparent 58%),
             linear-gradient(155deg, #185609 0%, #0C2F05 100%);
  color:var(--blanc)}
.diapo[data-fond] .cendre,.diapo[data-fond] .legende{color:rgba(255,255,255,.64)}
.diapo[data-fond] .filet{background:rgba(255,255,255,.22)}

/* --- Signature : le prompt >>> de Python ------------------------------ */
.surtitre{font-family:var(--mono);font-size:var(--t-micro);letter-spacing:.22em;
          text-transform:uppercase;color:var(--rouge);display:flex;align-items:center;
          gap:14px;margin-bottom:30px}
.surtitre::before{content:">>>";opacity:.5;letter-spacing:0}
.diapo[data-fond] .surtitre{color:rgba(255,255,255,.88)}

.filigrane{position:absolute;right:-46px;bottom:-138px;font-family:var(--mono);
           font-size:400px;line-height:1;color:rgba(255,255,255,.07);
           pointer-events:none;user-select:none}
.diapo:not([data-fond]) .filigrane{color:rgba(216,27,39,.055)}

/* --- Typographie ------------------------------------------------------ */
h1,h2,h3{font-family:var(--display);font-weight:600;letter-spacing:-.03em;line-height:1.03}
h1{font-size:var(--t-titre)} h2{font-size:var(--t-sous)} h3{font-size:34px}
.geant{font-family:var(--display);font-weight:700;font-size:var(--t-geant);
       line-height:.95;letter-spacing:-.045em}
.lead{font-size:var(--t-lead);line-height:1.35;color:var(--cendre);max-width:26ch}
.corps{font-size:var(--t-corps);line-height:1.5;max-width:36ch}
.legende{font-size:var(--t-petit);color:var(--cendre);line-height:1.45}
.mono{font-family:var(--mono)}
.centre{margin:auto 0}.pousse{margin-top:auto}
.filet{height:1px;background:var(--trait);margin:26px 0}

.souligne{color:var(--rouge);position:relative;white-space:nowrap}
.souligne::after{content:"";position:absolute;left:0;right:0;bottom:.06em;height:.09em;
                 background:var(--rouge);opacity:.26;border-radius:2px}
.diapo[data-fond] .souligne{color:#FFD7DA}
.diapo[data-fond] .souligne::after{background:#FFD7DA}
.diapo[data-fond="vert"] .souligne{color:var(--or)}
.diapo[data-fond="vert"] .souligne::after{background:var(--or)}

/* --- Gabarits --------------------------------------------------------- */
.marque{display:flex;align-items:center;gap:18px;font-family:var(--mono);
        font-size:var(--t-micro);letter-spacing:.26em;text-transform:uppercase;
        color:rgba(255,255,255,.78)}
.marque img{height:54px;width:auto;background:#fff;border-radius:50%;padding:3px}
.diapo:not([data-fond]) .marque{color:var(--cendre)}

.meta{display:flex;gap:52px;font-family:var(--mono);font-size:var(--t-petit);
      color:rgba(255,255,255,.7)}
.meta b{display:block;color:#fff;font-weight:500;font-size:var(--t-corps)}
.diapo:not([data-fond]) .meta{color:var(--cendre)}
.diapo:not([data-fond]) .meta b{color:var(--encre)}

.numero{font-family:var(--display);font-weight:700;font-size:200px;line-height:.8;
        letter-spacing:-.06em;color:rgba(255,255,255,.17)}
.chiffre{font-family:var(--display);font-weight:700;font-size:230px;line-height:.88;
         letter-spacing:-.05em;color:var(--rouge)}
.diapo[data-fond] .chiffre{color:#fff}

.duo{display:grid;grid-template-columns:360px 1fr;gap:70px;align-items:center;flex:1}
.picto{display:grid;place-items:center}
.picto svg{width:100%;height:auto;max-height:310px}

.duel{display:grid;grid-template-columns:1fr 1fr;gap:46px;flex:1;align-items:stretch}
.volet{background:var(--blanc);border:1px solid var(--trait);border-radius:18px;
       padding:34px 32px;display:flex;flex-direction:column;gap:14px}
.volet[data-signe="non"]{border-color:rgba(216,27,39,.35);background:#FFF5F5}
.volet[data-signe="oui"]{border-color:rgba(24,86,9,.3);background:#F4FAF1}
.volet .marqueur{font-family:var(--mono);font-size:24px;width:48px;height:48px;
                 border-radius:50%;display:grid;place-items:center;color:#fff}
.volet[data-signe="non"] .marqueur{background:var(--rouge)}
.volet[data-signe="oui"] .marqueur{background:var(--vert)}
.diapo[data-fond] .volet{background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.2);
                         color:#fff}

pre.code{font-family:var(--mono);font-size:26px;line-height:1.6;background:var(--encre);
         color:#F6EEED;border-radius:18px;padding:34px 38px;overflow:hidden;
         border-left:5px solid var(--rouge)}
pre.code.petit{font-size:22px;line-height:1.55}
pre.code .k{color:#FF8C93;font-weight:500}
pre.code .f{color:#FFCBCE}
pre.code .s{color:#E7B6B6}
pre.code .n{color:#FFFFFF}
pre.code .c{color:#9B8380;font-style:italic}
pre.code mark{background:rgba(240,50,62,.3);color:#fff;border-radius:4px;padding:1px 4px}
pre.code .ok{color:#8FD97A}

.etapes{display:grid;grid-auto-flow:column;grid-auto-columns:1fr;gap:40px;flex:1;
        align-items:center}
.etape{display:flex;flex-direction:column;gap:16px}
.etape .rang{font-family:var(--mono);font-size:var(--t-micro);letter-spacing:.2em;
             color:var(--rouge)}
.diapo[data-fond] .etape .rang{color:var(--or)}
.etape .barre{height:4px;background:var(--trait);position:relative;border-radius:2px}
.etape .barre::after{content:"";position:absolute;inset:0 auto 0 0;width:38%;
                     background:var(--rouge);border-radius:2px}
.diapo[data-fond] .etape .barre{background:rgba(255,255,255,.22)}
.diapo[data-fond] .etape .barre::after{background:var(--or)}

.signe{font-family:var(--display);font-weight:700;font-size:112px;line-height:1;color:#fff}

.formule{background:var(--blanc);border:1px solid var(--trait);border-radius:20px;
         padding:46px 50px;text-align:center;font-size:38px;
         box-shadow:0 18px 50px rgba(110,10,18,.07)}
.formule .katex{font-size:1.22em}
.diapo[data-fond] .formule{background:rgba(255,255,255,.07);
                           border-color:rgba(255,255,255,.2);color:#fff}

.regle{font-family:var(--display);font-size:60px;font-weight:600;line-height:1.15;
       letter-spacing:-.03em;border-left:6px solid var(--rouge);padding-left:40px;
       max-width:27ch}
.diapo[data-fond] .regle{border-color:var(--or)}

.liste{display:flex;flex-direction:column;gap:22px;font-size:30px;line-height:1.3}
.liste li{list-style:none;display:flex;gap:20px;align-items:baseline}
.liste li::before{content:">";font-family:var(--mono);color:var(--rouge);font-size:24px}
.diapo[data-fond] .liste li::before{color:var(--or)}

.tuiles{display:grid;grid-template-columns:repeat(2,1fr);gap:22px;flex:1;align-content:center}
.tuile{background:var(--blanc);border:1px solid var(--trait);border-radius:16px;
       padding:26px 28px}
.tuile b{font-family:var(--mono);color:var(--rouge);font-size:var(--t-petit);
         display:block;margin-bottom:8px;letter-spacing:.12em;text-transform:uppercase}
.tuile span{font-size:26px;line-height:1.3}
.diapo[data-fond] .tuile{background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.18)}
.diapo[data-fond] .tuile b{color:var(--or)}

/* --- Pied de diapo : le rail des 11 séances --------------------------- */
.pied{position:absolute;left:var(--marge);right:var(--marge);bottom:34px;display:flex;
      align-items:center;justify-content:space-between;font-family:var(--mono);
      font-size:13px;letter-spacing:.15em;text-transform:uppercase;color:var(--cendre)}
.diapo[data-fond] .pied{color:rgba(255,255,255,.55)}
.rail{display:flex;gap:6px;align-items:center}
.rail i{width:20px;height:3px;background:var(--trait);border-radius:2px;display:block}
.rail i.faite{background:var(--or)}
.rail i.ici{background:var(--rouge);width:32px}
.diapo[data-fond] .rail i{background:rgba(255,255,255,.22)}
.diapo[data-fond] .rail i.faite{background:var(--or);opacity:.8}
.diapo[data-fond] .rail i.ici{background:#fff}

/* --- Outils du présentateur (jamais projetés) ------------------------- */
.notes{display:none}
.panneau{position:fixed;left:0;right:0;bottom:0;z-index:20;background:rgba(13,6,5,.96);
         color:#F3E9E8;border-top:1px solid rgba(255,255,255,.12);padding:18px 28px;
         font-size:16px;line-height:1.5;max-height:34vh;overflow:auto;
         transform:translateY(101%);transition:transform .28s ease}
.panneau.ouvert{transform:none}
.panneau b{color:var(--rouge-vif);font-family:var(--mono);font-size:12px;
           letter-spacing:.2em;text-transform:uppercase;display:block;margin-bottom:6px}
.compteur{position:fixed;right:16px;bottom:14px;z-index:15;font-family:var(--mono);
          font-size:12px;color:rgba(255,255,255,.35);letter-spacing:.14em}
.aide{position:fixed;left:16px;bottom:14px;z-index:15;font-family:var(--mono);
      font-size:12px;color:rgba(255,255,255,.3);letter-spacing:.1em}

@media print{
  @page{size:1280px 720px;margin:0}
  body{background:#fff;overflow:visible}
  .scene{position:static;display:block}
  .diapo{display:flex!important;position:relative;transform:none!important;
         box-shadow:none;page-break-after:always;break-after:page}
  .diapo > *{animation:none!important}
  .panneau,.compteur,.aide{display:none}
}
"""

MOTEUR = """/* Moteur commun à tous les decks. Rien à modifier par séance. */
const diapos  = [...document.querySelectorAll('.diapo')];
const panneau = document.getElementById('panneau');
let index = 0;

function echelle(){
  document.documentElement.style.setProperty(
    '--k', Math.min(innerWidth / 1280, innerHeight / 720));
}
addEventListener('resize', echelle); echelle();

function aller(n){
  index = Math.max(0, Math.min(diapos.length - 1, n));
  diapos.forEach((d, i) => d.classList.toggle('active', i === index));
  document.getElementById('ici').textContent = index + 1;
  const notes = diapos[index].querySelector('.notes');
  panneau.innerHTML = notes ? notes.innerHTML : '<b>Notes</b> \\u2014';
  ajuster(diapos[index]);
  location.hash = index + 1;
}

addEventListener('keydown', e => {
  switch(e.key){
    case 'ArrowRight': case ' ': case 'PageDown': aller(index+1); e.preventDefault(); break;
    case 'ArrowLeft':  case 'PageUp':            aller(index-1); e.preventDefault(); break;
    case 'Home': aller(0); break;
    case 'End':  aller(diapos.length - 1); break;
    case 'f': case 'F':
      document.fullscreenElement ? document.exitFullscreen()
                                 : document.documentElement.requestFullscreen(); break;
    case 'n': case 'N': panneau.classList.toggle('ouvert'); break;
  }
});
addEventListener('click', e => {
  if (e.target.closest('.panneau')) return;
  aller(e.clientX > innerWidth / 2 ? index + 1 : index - 1);
});

/* --- Auto-ajustement : aucune diapo ne peut déborder ------------------
   Le texte est écrit avec des <br> volontaires. Si une ligne déborde et
   se replie toute seule, ou si le bloc dépasse la hauteur disponible, on
   réduit le corps jusqu'à ce que ça tienne. Tu peux donc écrire un titre
   un peu long sans casser la mise en page. */
function ajuster(diapo){
  diapo.querySelectorAll('.geant, .regle, h1, h2, .lead').forEach(el => {
    const attendu = el.querySelectorAll('br').length + 1;
    el.style.fontSize = '';
    let taille = parseFloat(getComputedStyle(el).fontSize);
    let garde = 0;
    while (garde++ < 40 && taille > 26) {
      const lh = parseFloat(getComputedStyle(el).lineHeight) || taille * 1.1;
      if (Math.round(el.scrollHeight / lh) <= attendu) break;
      taille -= 3;
      el.style.fontSize = taille + 'px';
    }
  });

  diapo.querySelectorAll('pre.code').forEach(el => {
    el.style.fontSize = '';
    let taille = parseFloat(getComputedStyle(el).fontSize);
    let garde = 0;
    while (garde++ < 30 && taille > 15 &&
           (el.scrollWidth > el.clientWidth + 1 || el.scrollHeight > el.clientHeight + 1)) {
      taille -= 1;
      el.style.fontSize = taille + 'px';
    }
  });

  /* Dernier filet : si la diapo entière déborde, on resserre les titres. */
  let garde = 0;
  while (garde++ < 20 && diapo.scrollHeight > diapo.clientHeight + 1) {
    diapo.querySelectorAll('.geant, .regle, h1, h2, .chiffre, .numero').forEach(el => {
      const t = parseFloat(getComputedStyle(el).fontSize);
      el.style.fontSize = Math.max(24, t - 4) + 'px';
    });
  }
}

document.getElementById('total').textContent = diapos.length;
aller(parseInt(location.hash.slice(1)) - 1 || 0);
addEventListener('beforeprint', () => diapos.forEach(ajuster));

addEventListener('load', () => {
  if (window.renderMathInElement) {
    renderMathInElement(document.body, {
      delimiters: [{left:'$$',right:'$$',display:true},
                   {left:'\\\\(',right:'\\\\)',display:false}],
      throwOnError: false});
  }
});
"""

GABARIT_PAGE = """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titre_page} — Formation Python 360° · ASEGUIM</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=Inter+Tight:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>
<link rel="stylesheet" href="theme.css">
</head>
<body>
<div class="scene">
{diapos}
</div>
<div class="aide">&#8592; &#8594; naviguer &middot; F plein &eacute;cran &middot; N notes</div>
<div class="compteur"><span id="ici">1</span> / <span id="total">0</span></div>
<div class="panneau" id="panneau"></div>
<script src="moteur.js"></script>
</body>
</html>
"""

# ═══════════════════════════════════════════════════════════════════════════
#  PICTOGRAMMES — trait unique, une seule couleur, aucun aplat
# ═══════════════════════════════════════════════════════════════════════════

def _svg(corps: str, couleur: str = "var(--rouge)") -> str:
    return (f'<svg viewBox="0 0 240 240" fill="none" stroke="{couleur}" stroke-width="3.5" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{corps}</svg>')


PICTOS = {
    # une boîte étiquetée — la variable
    "boite": _svg('<path d="M40 88 L120 52 L200 88 L120 124 Z"/><path d="M40 88 V172 L120 208 V124"/>'
                  '<path d="M200 88 V172 L120 208"/>'
                  '<rect x="86" y="128" width="68" height="30" rx="6" opacity=".35"/>'
                  '<path d="M96 143 h48" stroke-dasharray="4 7"/>'),
    # un carnet à onglets — le dictionnaire
    "repertoire": _svg('<rect x="52" y="44" width="136" height="152" rx="10"/>'
                       '<path d="M52 82 h136 M52 120 h136 M52 158 h136"/>'
                       '<path d="M188 60 h22 M188 100 h22 M188 140 h22"/>'
                       '<circle cx="80" cy="63" r="5"/><circle cx="80" cy="101" r="5"/>'),
    # une recette / liste ordonnée — l'algorithme
    "recette": _svg('<rect x="58" y="36" width="124" height="168" rx="12"/>'
                    '<path d="M84 78 h72 M84 110 h72 M84 142 h48"/>'
                    '<circle cx="72" cy="78" r="4"/><circle cx="72" cy="110" r="4"/>'
                    '<circle cx="72" cy="142" r="4"/>'),
    # un aiguillage — la condition
    "aiguillage": _svg('<path d="M120 200 V132"/><path d="M120 132 L64 76"/><path d="M120 132 L176 76"/>'
                       '<circle cx="120" cy="132" r="12"/><circle cx="60" cy="60" r="18"/>'
                       '<circle cx="180" cy="60" r="18"/>'),
    # une boucle
    "boucle": _svg('<path d="M74 96 a52 52 0 1 1 -14 44"/><path d="M60 96 h28 M60 96 V68"/>'
                   '<circle cx="150" cy="120" r="8"/>'),
    # une machine à café — la fonction
    "machine": _svg('<rect x="56" y="52" width="128" height="96" rx="10"/>'
                    '<path d="M84 148 v20 a36 36 0 0 0 72 0 v-20"/>'
                    '<path d="M100 88 h40"/><path d="M120 108 v18"/>'
                    '<path d="M92 200 h96"/>'),
    # un moule et son gâteau — la classe
    "moule": _svg('<path d="M48 92 h84 l-10 96 a12 12 0 0 1 -12 10 h-40 a12 12 0 0 1 -12 -10 Z"/>'
                  '<path d="M156 108 h44 l-6 80 h-32 Z"/><path d="M44 92 h92" />'
                  '<path d="M152 108 h52"/>'),
    # une prise électrique — les dunder methods
    "prise": _svg('<rect x="60" y="56" width="120" height="128" rx="16"/>'
                  '<circle cx="100" cy="108" r="9"/><circle cx="140" cy="108" r="9"/>'
                  '<path d="M100 146 h40"/>'),
    # un distributeur de tickets — le générateur
    "ticket": _svg('<rect x="52" y="60" width="136" height="120" rx="12"/>'
                   '<path d="M52 108 h136" stroke-dasharray="6 8"/>'
                   '<path d="M96 180 v34 h48 v-34"/><path d="M96 200 h48" stroke-dasharray="4 6"/>'),
    # un cadeau — le décorateur
    "cadeau": _svg('<rect x="52" y="96" width="136" height="104" rx="10"/>'
                   '<path d="M40 68 h160 v28 H40 Z"/><path d="M120 68 v132"/>'
                   '<path d="M120 68 c-30 -44 -66 -8 -30 0"/><path d="M120 68 c30 -44 66 -8 30 0"/>'),
    # un tableau — le DataFrame
    "tableau": _svg('<rect x="40" y="60" width="160" height="128" rx="10"/>'
                    '<path d="M40 96 h160 M40 132 h160 M40 164 h160 M92 60 v128 M146 60 v128"/>'),
    # une poupée russe — le HTML imbriqué
    "imbrique": _svg('<rect x="40" y="46" width="160" height="148" rx="10"/>'
                     '<rect x="66" y="72" width="108" height="96" rx="8"/>'
                     '<rect x="92" y="98" width="56" height="44" rx="6"/>'),
    # un passe-plat — l'API
    "passeplat": _svg('<path d="M36 60 v132 M204 60 v132"/><rect x="36" y="104" width="168" height="44" rx="8"/>'
                      '<path d="M96 126 h72"/><path d="M150 112 l18 14 -18 14"/>'),
    # un carton de déménagement — Docker
    "carton": _svg('<path d="M44 92 h152 v104 a10 10 0 0 1 -10 10 H54 a10 10 0 0 1 -10 -10 Z"/>'
                   '<path d="M36 60 h168 v32 H36 Z"/><path d="M104 60 v32 M136 60 v32"/>'
                   '<path d="M104 130 h32"/>'),
    # une commande au restaurant — HTTP
    "plateau": _svg('<path d="M40 160 h160"/><path d="M62 160 a58 58 0 0 1 116 0"/>'
                    '<circle cx="120" cy="82" r="10"/><path d="M76 196 h88"/>'),
    # une ceinture de sécurité — try/except
    "ceinture": _svg('<path d="M60 48 C 96 120 128 156 188 176"/>'
                     '<rect x="86" y="140" width="56" height="34" rx="8" transform="rotate(-14 114 157)"/>'
                     '<path d="M60 196 h120"/>'),
}


# ═══════════════════════════════════════════════════════════════════════════
#  GABARITS — chaque fonction rend une <section class="diapo">
# ═══════════════════════════════════════════════════════════════════════════

def _notes(txt: str | None) -> str:
    return f'\n  <div class="notes"><b>Notes</b> {txt}</div>' if txt else ""


def _rail(seance: int | None) -> str:
    if seance is None:
        return ""
    points = []
    for n in range(1, 12):
        classe = "faite" if n < seance else ("ici" if n == seance else "")
        points.append(f'<i class="{classe}"></i>')
    return "".join(points)


def _pied(seance: int | None, gauche: str) -> str:
    if seance is None:
        return ""
    return (f'\n  <div class="pied"><span>{gauche}</span>'
            f'<span class="rail">{_rail(seance)}</span></div>')


def couverture(titre, promesse, meta, seance):
    cases = "".join(f"<div>{k}<b>{v}</b></div>" for k, v in meta)
    return f'''<section class="diapo active" data-type="couverture" data-fond="rouge">
  <div class="filigrane">&gt;&gt;&gt;</div>
  <div class="marque"><img src="assets/logo-aseguim.jpg" alt="ASEGUIM">
    <span>ASEGUIM &middot; Formation Python 360&deg;</span></div>
  <div class="centre">
    <h1 style="font-size:112px;color:#fff">{titre}</h1>
    <p class="lead" style="color:rgba(255,255,255,.74);margin-top:26px;max-width:32ch">{promesse}</p>
  </div>
  <div class="meta pousse">{cases}</div>
</section>'''


def section(numero, titre, ligne, seance, fond="rouge", notes=None):
    return f'''<section class="diapo" data-type="section" data-fond="{fond}">
  <div class="filigrane">&gt;&gt;&gt;</div>
  <div class="surtitre">Partie {numero}</div>
  <div class="centre">
    <div class="numero">{numero:02d}</div>
    <h1 style="color:#fff;margin-top:-8px">{titre}</h1>
    <p class="lead" style="color:rgba(255,255,255,.74);margin-top:20px">{ligne}</p>
  </div>{_pied(seance, "Formation Python 360&deg; &middot; ASEGUIM")}{_notes(notes)}
</section>'''


def idee(surtitre, texte, seance, bas=None, notes=None, fond=None):
    attr = f' data-fond="{fond}"' if fond else ""
    fil = '<div class="filigrane">&gt;&gt;&gt;</div>' if fond else ""
    return f'''<section class="diapo" data-type="idee"{attr}>
  {fil}<div class="surtitre">{surtitre}</div>
  <div class="centre"><p class="geant">{texte}</p></div>{_pied(seance, bas or "")}{_notes(notes)}
</section>'''


def chiffre(surtitre, valeur, titre, legende, seance, notes=None, fond=None):
    attr = f' data-fond="{fond}"' if fond else ""
    return f'''<section class="diapo" data-type="chiffre"{attr}>
  <div class="surtitre">{surtitre}</div>
  <div class="centre" style="display:flex;align-items:baseline;gap:40px">
    <div class="chiffre">{valeur}</div>
    <div><h2 style="max-width:13ch">{titre}</h2>
      <p class="legende" style="margin-top:16px">{legende}</p></div>
  </div>{_pied(seance, "")}{_notes(notes)}
</section>'''


def analogie(surtitre, picto, titre, corps, seance, notes=None):
    return f'''<section class="diapo" data-type="analogie">
  <div class="surtitre">{surtitre}</div>
  <div class="duo">
    <div class="picto">{PICTOS[picto]}</div>
    <div><h2>{titre}</h2><p class="corps" style="margin-top:22px">{corps}</p></div>
  </div>{_notes(notes)}
</section>'''


def duel(surtitre, titre, gauche, droite, seance, notes=None, fond=None):
    attr = f' data-fond="{fond}"' if fond else ""

    def volet(v, signe):
        marque = "&#10007;" if signe == "non" else "&#10003;"
        bas = f'<p class="legende pousse">{v[2]}</p>' if len(v) > 2 else ""
        return (f'<div class="volet" data-signe="{signe}"><span class="marqueur">{marque}</span>'
                f'<h3>{v[0]}</h3><p class="legende mono" style="font-size:20px">{v[1]}</p>{bas}</div>')

    return f'''<section class="diapo" data-type="duel"{attr}>
  <div class="surtitre">{surtitre}</div>
  <h2 style="margin-bottom:28px">{titre}</h2>
  <div class="duel">{volet(gauche, "non")}{volet(droite, "oui")}</div>{_notes(notes)}
</section>'''


def code(surtitre, extrait, legende=None, seance=None, notes=None, petit=False):
    cl = "code petit" if petit else "code"
    bas = f'<p class="legende" style="margin-top:22px">{legende}</p>' if legende else ""
    return f'''<section class="diapo" data-type="code">
  <div class="surtitre">{surtitre}</div>
  <pre class="{cl}">{extrait}</pre>
  {bas}{_notes(notes)}
</section>'''


def etapes(surtitre, titre, items, seance=None, notes=None, fond=None):
    attr = f' data-fond="{fond}"' if fond else ""
    blocs = "".join(
        f'<div class="etape"><span class="rang">{i:02d}</span><div class="barre"></div>'
        f'<h3>{t}</h3><p class="legende">{d}</p></div>'
        for i, (t, d) in enumerate(items, 1))
    return f'''<section class="diapo" data-type="etapes"{attr}>
  <div class="surtitre">{surtitre}</div>
  <h2 style="margin-bottom:18px">{titre}</h2>
  <div class="etapes">{blocs}</div>{_notes(notes)}
</section>'''


def alerte(surtitre, titre, ligne, seance=None, notes=None):
    return f'''<section class="diapo" data-type="alerte" data-fond="rouge">
  <div class="filigrane">&gt;&gt;&gt;</div>
  <div class="surtitre">{surtitre}</div>
  <div class="centre">
    <div class="signe">!</div>
    <h1 style="color:#fff;margin-top:14px;max-width:22ch">{titre}</h1>
    <p class="lead" style="color:rgba(255,255,255,.76);margin-top:22px">{ligne}</p>
  </div>{_notes(notes)}
</section>'''


def formule(surtitre, titre, tex, legende, seance=None, notes=None, fond=None):
    attr = f' data-fond="{fond}"' if fond else ""
    fil = '<div class="filigrane">&gt;&gt;&gt;</div>' if fond else ""
    return f'''<section class="diapo" data-type="formule"{attr}>
  {fil}<div class="surtitre">{surtitre}</div>
  <h2 style="margin-bottom:26px">{titre}</h2>
  <div class="formule">$${tex}$$</div>
  <p class="legende" style="margin-top:24px;text-align:center">{legende}</p>{_notes(notes)}
</section>'''


def regle(surtitre, texte, seance=None, bas=None, notes=None, fond=None):
    attr = f' data-fond="{fond}"' if fond else ""
    fil = '<div class="filigrane">&gt;&gt;&gt;</div>' if fond else ""
    return f'''<section class="diapo" data-type="regle"{attr}>
  {fil}<div class="surtitre">{surtitre}</div>
  <div class="centre"><p class="regle">{texte}</p></div>{_pied(seance, bas or "")}{_notes(notes)}
</section>'''


def liste(surtitre, titre, points, seance=None, notes=None, fond=None):
    attr = f' data-fond="{fond}"' if fond else ""
    fil = '<div class="filigrane">&gt;&gt;&gt;</div>' if fond else ""
    lis = "".join(f"<li>{p}</li>" for p in points)
    return f'''<section class="diapo" data-type="liste"{attr}>
  {fil}<div class="surtitre">{surtitre}</div>
  <h2 style="margin-bottom:30px">{titre}</h2>
  <ul class="liste centre">{lis}</ul>{_notes(notes)}
</section>'''


def tuiles(surtitre, titre, items, seance=None, notes=None, fond=None):
    attr = f' data-fond="{fond}"' if fond else ""
    blocs = "".join(f'<div class="tuile"><b>{k}</b><span>{v}</span></div>' for k, v in items)
    return f'''<section class="diapo" data-type="tuiles"{attr}>
  <div class="surtitre">{surtitre}</div>
  <h2 style="margin-bottom:24px">{titre}</h2>
  <div class="tuiles">{blocs}</div>{_notes(notes)}
</section>'''


def exercice(surtitre, titre, consignes, seance=None, notes=None):
    lis = "".join(f"<li>{c}</li>" for c in consignes)
    return f'''<section class="diapo" data-type="exercice" data-fond="vert">
  <div class="filigrane">&gt;&gt;&gt;</div>
  <div class="surtitre">{surtitre}</div>
  <h1 style="color:#fff;font-size:66px;margin-bottom:26px">{titre}</h1>
  <ul class="liste" style="color:rgba(255,255,255,.9)">{lis}</ul>{_notes(notes)}
</section>'''


def fin(ligne, seance, bas=None, notes=None):
    return f'''<section class="diapo" data-type="fin" data-fond="rouge">
  <div class="filigrane">&gt;&gt;&gt;</div>
  <div class="surtitre">Fin de s&eacute;ance</div>
  <div class="centre">
    <h1 style="color:#fff;font-size:98px">Des questions&nbsp;?</h1>
    <p class="lead" style="color:rgba(255,255,255,.74);margin-top:22px;max-width:34ch">{ligne}</p>
  </div>{_pied(seance, bas or "#sos-erreurs &middot; colle ton erreur en texte")}{_notes(notes)}
</section>'''


# ═══════════════════════════════════════════════════════════════════════════
#  ÉCRITURE
# ═══════════════════════════════════════════════════════════════════════════

def deck(nom_fichier: str, titre_page: str, diapos: list[str]) -> int:
    SORTIE.mkdir(parents=True, exist_ok=True)
    html = GABARIT_PAGE.format(titre_page=titre_page, diapos="\n\n".join(diapos))
    (SORTIE / nom_fichier).write_text(html, encoding="utf-8")
    return len(diapos)


def ecrire_socle() -> None:
    SORTIE.mkdir(parents=True, exist_ok=True)
    (SORTIE / "theme.css").write_text(THEME, encoding="utf-8")
    (SORTIE / "moteur.js").write_text(MOTEUR, encoding="utf-8")
