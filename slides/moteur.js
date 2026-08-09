/* Moteur commun à tous les decks. Rien à modifier par séance. */
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
  panneau.innerHTML = notes ? notes.innerHTML : '<b>Notes</b> \u2014';
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
                   {left:'\\(',right:'\\)',display:false}],
      throwOnError: false});
  }
});
