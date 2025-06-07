import { newChar } from "../character_editor.js";
import { updateNextButtonState, updateNavHeader } from "./shared_ui.js";

let selectedRaceName = null;
let raceMap = {};

export async function initRaceStep() {
    const container = document.getElementById("raceContainer");
    if (!container) return;

    updateNavHeader(newChar.name || "Unnamed Character", true);
    container.innerHTML = "<p>Loading races...</p>";

    try {
        const response = await fetch("/api/races/get");
        const data = await response.json();
        const raceList = data.race_list;

        raceMap = groupRaces(raceList);
        renderRaceOptions(container, raceMap);

        if (newChar.race_type) {
            selectRace(newChar.race_type, newChar.subrace_name);
        }

    } catch (err) {
        console.error("Failed to load races:", err);
        container.innerHTML = "<p class='text-danger'>Failed to load races.</p>";
    }
}

function groupRaces(raceList) {
    const grouped = {};
    for (const race of raceList) {
        const base = race.name;
        if (race.subrace) {
            if (!grouped[base]) grouped[base] = [];
            grouped[base].push(race);
        } else {
            grouped[base] = [race];
        }
    }
    return grouped;
}

function renderRaceOptions(container, raceMap) {
    container.innerHTML = "";

    for (const [raceName, variants] of Object.entries(raceMap)) {
        const section = document.createElement("div");
        section.className = "race-section mb-4";

        const label = document.createElement("h5");
        label.textContent = raceName;
        section.appendChild(label);

        for (const race of variants) {
            const btn = document.createElement("button");
            btn.className = "btn btn-outline-primary m-1";
            btn.textContent = race.subrace || race.name;
            btn.onclick = () => selectRace(race.name, race.subrace);
            section.appendChild(btn);
        }

        container.appendChild(section);
    }
}

function selectRace(raceName, subraceName = null) {
    const variants = raceMap[raceName];
    const match = variants.find(r => r.subrace === subraceName);

    if (!match) return;

    newChar.race_type = raceName;
    newChar.subrace_name = subraceName;
    updateNextButtonState(true);

    renderRaceDetails(match);
}

function renderRaceDetails(race) {
    const detailPanel = document.getElementById("raceDetails");
    if (!detailPanel) return;

    detailPanel.innerHTML = `
        <h4>${race.subrace || race.name}</h4>
        <p><strong>Speed:</strong> ${race.speed} ft</p>
        <p><strong>Size:</strong> ${race.size}</p>
        <p><strong>Ability Score Increase:</strong> ${formatASI(race.ability_score_increase)}</p>
        <ul class="list-group">${Object.entries(race.info).map(([k,v]) => `<li class="list-group-item"><strong>${k}</strong>: ${v}</li>`).join("")}</ul>
    `;
}

function formatASI(asiObj) {
    return Object.entries(asiObj).map(([ab, v]) => `${ab.toUpperCase()} +${v}`).join(", ");
}
