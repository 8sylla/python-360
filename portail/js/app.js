/* ═══════════════════════════════════════════════════════════════════════
   Formation Python 360° — le peu de JavaScript qu'il faut

     1. écrire le planning à partir de js/seances.js
     2. écrire la rangée d'outils
     3. ouvrir le menu sur petit écran

   Aucune dépendance, aucun réseau, rien de stocké : la page marche même
   en double-cliquant sur index.html depuis le disque.
   ═══════════════════════════════════════════════════════════════════════ */

(function () {
  "use strict";

  const JOURS = ["dimanche", "lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi"];
  const MOIS = ["janv.", "févr.", "mars", "avril", "mai", "juin",
                "juil.", "août", "sept.", "oct.", "nov.", "déc."];

  const ICONES = {
    doc:   '<path d="M4 1.5h5l3 3v9a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1v-11a1 1 0 0 1 1-1Z"/><path d="M9 1.5v3h3"/>',
    code:  '<path d="M5.5 4.5 2 8l3.5 3.5"/><path d="M10.5 4.5 14 8l-3.5 3.5"/>',
    check: '<path d="M2.5 8.5l3.5 3.5 7.5-8"/>',
    play:  '<path d="M4 2.5v11l9-5.5-9-5.5Z"/>',
  };

  const svg = (nom) =>
    `<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"
      stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${ICONES[nom] || ""}</svg>`;

  const echappe = (s) =>
    String(s).replace(/[&<>"]/g, (c) =>
      ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

  /* ── le planning ────────────────────────────────────────────────────── */
  const planning = document.getElementById("planning");
  const aujourdhui = new Date();
  aujourdhui.setHours(0, 0, 0, 0);

  SEANCES.forEach((s) => {
    const j = new Date(s.date + "T00:00:00");
    const passee = j <= aujourdhui;

    // Seules les ressources réellement publiées apparaissent : une séance
    // sans vidéo n'affiche pas de bouton vidéo.
    const liens = RESSOURCES
      .filter((r) => s.liens && s.liens[r.cle])
      .map((r) => {
        const externe = /^https?:/.test(s.liens[r.cle]);
        return `<a class="ressource" href="${echappe(s.liens[r.cle])}"${
          externe ? ' target="_blank" rel="noopener"' : ""
        }>${svg(r.icone)}${r.libelle}</a>`;
      })
      .join("");

    const li = document.createElement("li");
    li.className = "seance" + (passee ? " seance--passee" : "");
    li.innerHTML = `
      <div class="seance__tete">
        <span class="seance__num">S${s.numero}</span>
        <span class="seance__date">
          <b>${j.getDate()} ${MOIS[j.getMonth()]}</b>
          <span class="seance__jour">${JOURS[j.getDay()]}</span>
        </span>
      </div>
      <h3 class="seance__titre">${echappe(s.titre)}</h3>
      <p class="seance__sous">${echappe(s.sousTitre)}</p>
      <div class="seance__pied">
        <span class="seance__duree">${echappe(s.duree)}</span>
        ${liens
          ? `<div class="seance__liens">${liens}</div>`
          : `<p class="seance__attente">${
              passee ? "Support en préparation." : "Séance à venir."
            }</p>`}
      </div>`;
    planning.appendChild(li);
  });

  /* ── les outils ─────────────────────────────────────────────────────── */
  const liste = document.getElementById("outils-liste");
  OUTILS.forEach((o) => {
    const li = document.createElement("li");
    li.className = "outil";
    li.innerHTML = `
      <img src="assets/logos/${o.fichier}" alt="${echappe(o.nom)}" width="46" height="46">
      <b>${echappe(o.nom)}</b>
      <span>${echappe(o.detail)}</span>`;
    liste.appendChild(li);
  });

  /* ── menu sur petit écran ───────────────────────────────────────────── */
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
})();
