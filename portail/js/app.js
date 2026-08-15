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

  /* Les icônes viennent de Lucide (lucide.dev, licence ISC). Les tracés sont
     recopiés tels quels : viewBox 24, trait de 2, bouts arrondis. Rien n'est
     chargé depuis un service extérieur. */
  const ICONES = {
    "file-text":
      '<path d="M6 22a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8a2.4 2.4 0 0 1 1.704.706l3.588 3.588A2.4 2.4 0 0 1 20 8v12a2 2 0 0 1-2 2z"/>' +
      '<path d="M14 2v5a1 1 0 0 0 1 1h5"/><path d="M10 9H8"/><path d="M16 13H8"/><path d="M16 17H8"/>',
    notebook:
      '<path d="M2 6h4"/><path d="M2 10h4"/><path d="M2 14h4"/><path d="M2 18h4"/>' +
      '<rect width="16" height="20" x="4" y="2" rx="2"/>' +
      '<path d="M9.5 8h5"/><path d="M9.5 12H16"/><path d="M9.5 16H14"/>',
    check:
      '<circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/>',
    video:
      '<path d="m16 13 5.223 3.482a.5.5 0 0 0 .777-.416V7.87a.5.5 0 0 0-.752-.432L16 10.5"/>' +
      '<rect x="2" y="6" width="14" height="12" rx="2"/>',
  };

  const svg = (nom) =>
    `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
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
