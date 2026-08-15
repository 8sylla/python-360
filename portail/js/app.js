/* ═══════════════════════════════════════════════════════════════════════
   Formation Python 360° — le vivant du portail

   Trois choses, pas une de plus :
     1. fabriquer les cartes à partir de js/seances.js
     2. filtrer (arc 1 / arc 2 / déjà publiées)
     3. retenir ce que le visiteur a coché comme « fait » (localStorage)

   Aucune dépendance, aucun réseau : la page marche même en double-cliquant
   sur index.html depuis le disque.
   ═══════════════════════════════════════════════════════════════════════ */

(function () {
  "use strict";

  const CLE_STOCKAGE = "python360.seances-faites";

  const grille    = document.getElementById("grille");
  const vide      = document.getElementById("vide");
  const filtres   = document.querySelectorAll(".filtre");
  const avanceBoi = document.querySelector(".avancement");
  const avanceBar = document.querySelector(".avancement__barre i");
  const avanceTxt = document.querySelector(".avancement__txt");

  /* ── les petites icônes, en SVG inline ─────────────────────────────── */
  const ICONES = {
    doc:   '<path d="M4 1.5h5l3 3v9a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1v-11a1 1 0 0 1 1-1Z"/><path d="M9 1.5v3h3"/>',
    code:  '<path d="M5.5 4.5 2 8l3.5 3.5"/><path d="M10.5 4.5 14 8l-3.5 3.5"/>',
    check: '<path d="M2.5 8.5l3.5 3.5 7.5-8"/>',
    play:  '<path d="M4 2.5v11l9-5.5-9-5.5Z"/>',
  };

  const svg = (nom) =>
    `<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"
      stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${ICONES[nom] || ""}</svg>`;

  /* ── mémoire locale ─────────────────────────────────────────────────── */
  function lireFaites() {
    try {
      const brut = localStorage.getItem(CLE_STOCKAGE);
      return brut ? new Set(JSON.parse(brut)) : new Set();
    } catch (e) {
      return new Set();          // navigation privée, stockage bloqué : tant pis
    }
  }

  function ecrireFaites(ensemble) {
    try {
      localStorage.setItem(CLE_STOCKAGE, JSON.stringify([...ensemble]));
    } catch (e) { /* sans conséquence */ }
  }

  let faites = lireFaites();

  /* ── une carte ──────────────────────────────────────────────────────── */
  function fabriqueCarte(s) {
    const carte = document.createElement("article");
    carte.className = "carte";
    carte.dataset.arc = String(s.arc);
    carte.dataset.numero = String(s.numero);
    carte.dataset.publiee = Object.values(s.liens).some(Boolean) ? "oui" : "non";
    if (faites.has(s.numero)) carte.classList.add("est-faite");

    const liens = RESSOURCES.map((r) => {
      const url = s.liens[r.cle];
      if (url) {
        return `<a class="lien" href="${url}"${r.cle === "replay" ? ' target="_blank" rel="noopener"' : ""}>
                  ${svg(r.icone)}${r.libelle}</a>`;
      }
      return `<span class="lien lien--absent" title="Pas encore publié">
                ${svg(r.icone)}${r.libelle} · à venir</span>`;
    }).join("");

    carte.innerHTML = `
      <div class="carte__tete">
        <div class="pastille" aria-hidden="true">${s.numero}</div>
        <div>
          <h3 class="carte__titre">${s.titre}</h3>
          <p class="carte__sous">${s.sousTitre}</p>
        </div>
      </div>
      <p class="carte__date">${s.date}</p>
      <div class="carte__liens">
        ${liens}
        <button class="carte__fait" type="button">
          ${faites.has(s.numero) ? "annuler" : "marquer comme fait"}
        </button>
      </div>`;

    carte.querySelector(".carte__fait").addEventListener("click", (ev) => {
      if (faites.has(s.numero)) faites.delete(s.numero);
      else faites.add(s.numero);
      ecrireFaites(faites);
      carte.classList.toggle("est-faite");
      ev.currentTarget.textContent = faites.has(s.numero) ? "annuler" : "marquer comme fait";
      majAvancement();
    });

    return carte;
  }

  /* ── avancement ─────────────────────────────────────────────────────── */
  function majAvancement() {
    const total = SEANCES.length;
    const n = SEANCES.filter((s) => faites.has(s.numero)).length;
    avanceBoi.hidden = n === 0;
    avanceBar.style.width = (n / total) * 100 + "%";
    avanceTxt.textContent = `${n} / ${total} séance${n > 1 ? "s" : ""} suivie${n > 1 ? "s" : ""}`;
  }

  /* ── filtres ────────────────────────────────────────────────────────── */
  function applique(nom) {
    let visibles = 0;
    grille.querySelectorAll(".carte").forEach((c) => {
      const ok =
        nom === "tous" ? true :
        nom === "arc1" ? c.dataset.arc === "1" :
        nom === "arc2" ? c.dataset.arc === "2" :
        nom === "publiees" ? c.dataset.publiee === "oui" : true;
      c.hidden = !ok;
      if (ok) visibles += 1;
    });
    vide.hidden = visibles > 0;
  }

  filtres.forEach((b) => {
    b.addEventListener("click", () => {
      filtres.forEach((x) => x.classList.remove("est-actif"));
      b.classList.add("est-actif");
      applique(b.dataset.filtre);
    });
  });

  /* ── menu mobile ────────────────────────────────────────────────────── */
  const burger = document.querySelector(".burger");
  const nav = document.getElementById("nav");
  burger.addEventListener("click", () => {
    const ouvert = nav.classList.toggle("est-ouvert");
    burger.setAttribute("aria-expanded", String(ouvert));
  });
  nav.addEventListener("click", (e) => {
    if (e.target.tagName === "A") {
      nav.classList.remove("est-ouvert");
      burger.setAttribute("aria-expanded", "false");
    }
  });

  /* ── rendu ──────────────────────────────────────────────────────────── */
  const fragment = document.createDocumentFragment();
  SEANCES.forEach((s) => fragment.appendChild(fabriqueCarte(s)));
  grille.appendChild(fragment);
  majAvancement();
})();
