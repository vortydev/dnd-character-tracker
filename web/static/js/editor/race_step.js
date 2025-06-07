// editor/race_step.js
import { newChar } from "../character_editor.js";
import { updateNavHeader, updateNextButtonState } from "./shared_ui.js";

let raceList = [];
let subraceMap = {};

export async function initRaceStep() {
    updateNavHeader(newChar.name || "Unnamed Character", true);

    const container = document.getElementById("raceContainer");
    if (!container) return;

    container.innerHTML = `<div id="raceSelectorContainer"></div>`;

    if (!window.raceListCache) {
        try {
            const res = await fetch("/api/races/get");
            const data = await res.json();
            window.raceListCache = data.race_list || [];
            window.spellsRefCache = data.spells_ref || [];
        } catch (err) {
            console.error("Failed to load races", err);
            return;
        }
    }

    raceList = window.raceListCache;
    prepareRaceData();
    renderRaceSelectors(container.querySelector("#raceSelectorContainer"));
}

function prepareRaceData() {
    subraceMap = {};
    const unique = new Map();

    for (const race of raceList) {
        const raceName = race.name;
        const subraceObj = race.subrace;

        if (subraceObj && subraceObj.name) {
            if (!subraceMap[raceName]) subraceMap[raceName] = [];
            subraceMap[raceName].push(subraceObj);
        } else {
            if (!unique.has(raceName)) unique.set(raceName, race);
        }
    }

    raceList = [...unique.values()];
}

function renderRaceSelectors(container) {
    const raceSelect = document.createElement("select");
    raceSelect.className = "form-select mb-3";
    raceSelect.innerHTML = `<option disabled selected>Choose a Race</option>` +
        raceList.map(r => `<option value="${r.name}">${r.name}</option>`).join("");

    const subraceSelect = document.createElement("select");
    subraceSelect.className = "form-select mb-3 d-none";
    subraceSelect.innerHTML = `<option disabled selected>Choose a Subrace</option>`;

    // Restore previous selection if it exists
    if (newChar.race_type) raceSelect.value = newChar.race_type;
    if (newChar.subrace_name) subraceSelect.value = newChar.subrace_name;

    raceSelect.addEventListener("change", e => {
        const selected = e.target.value;
        newChar.race_type = selected;
        newChar.subrace_name = null;
        updateNextButtonState(true);

        if (subraceMap[selected]) {
            subraceSelect.innerHTML = `<option disabled selected>Choose a Subrace</option>` +
                subraceMap[selected]
                    .map(sub => `<option value="${sub.name}">${sub.name}</option>`)
                    .join("");
            subraceSelect.classList.remove("d-none");
        } else {
            subraceSelect.classList.add("d-none");
        }
    });

    subraceSelect.addEventListener("change", e => {
        newChar.subrace_name = e.target.value;
        updateNextButtonState(true);
    });

    container.append(raceSelect, subraceSelect);

    // Trigger subrace logic if returning to the step
    if (newChar.race_type && subraceMap[newChar.race_type]) {
        subraceSelect.innerHTML = `<option disabled selected>Choose a Subrace</option>` +
            subraceMap[newChar.race_type]
                .map(sub => `<option value="${sub.name}">${sub.name}</option>`)
                .join("");
        subraceSelect.classList.remove("d-none");
        if (newChar.subrace_name) subraceSelect.value = newChar.subrace_name;
    }
}
