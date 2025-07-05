// editor/race_step.js
import { newChar } from "../character_editor.js";
import { updateNavHeader, updateNextButtonState } from "./shared_ui.js";

let raceList = [];
let subraceMap = {};

const abilityMap = {
    str: "Strength",
    dex: "Dexterity",
    con: "Constitution",
    int: "Intelligence",
    wis: "Wisdom",
    cha: "Charisma"
};

export async function initRaceStep() {
    const container = document.getElementById("raceContainer");
    const addBtn = document.getElementById("addRaceBtn");
    if (!container || !addBtn) return;

    updateNavHeader(newChar.name || "Unnamed Character", true);

    // TODO Load existing race

    container.innerHTML = "";

    const summaryContainer = document.createElement("div");
    summaryContainer.id = "raceSummaryContainer";
    // summaryContainer.className = "mb-3";
    container.appendChild(summaryContainer);

    const selectorSlot = document.createElement("div");
    selectorSlot.id = "raceSelectorSlot";
    addBtn.insertAdjacentElement("afterend", selectorSlot);

    addBtn.innerHTML = newChar.race_type ? `Change Race` : `Select Race`;
    addBtn.onclick = () => renderTemporaryRaceSelector(selectorSlot);

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
    updateNextButtonState(isValidRaceSelection());

    if (newChar.race_type) renderRaceSummary(container);
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

function renderTemporaryRaceSelector(slot) {
    slot.innerHTML = "";

    const row = document.createElement("div");
    row.className = "d-flex align-items-center gap-2 mt-3";

    const raceSelect = document.createElement("select");
    raceSelect.className = "form-select";
    raceSelect.innerHTML = `<option disabled selected value="">Choose a Race</option>` +
        raceList.map(r => `<option value="${r.name}">${r.name}</option>`).join("");

    const subraceSelect = document.createElement("select");
    subraceSelect.className = "form-select d-none";
    subraceSelect.innerHTML = `<option disabled selected value="">Choose a Subrace</option>`;

    raceSelect.addEventListener("change", e => {
        const selected = e.target.value;
        if (subraceMap[selected]) {
            subraceSelect.innerHTML = `<option disabled selected value="">Choose a Subrace</option>` +
                subraceMap[selected].map(sub => `<option value="${sub.name}">${sub.name}</option>`).join("");
            subraceSelect.classList.remove("d-none");
        } 
        else {
            subraceSelect.classList.add("d-none");
        }

        updateNextButtonState(isValidRaceSelection());
    });

    subraceSelect.addEventListener("change", e => {
        newChar.subrace_name = e.target.value;
        updateNextButtonState(isValidRaceSelection());
    });


    const confirmBtn = document.createElement("button");
    confirmBtn.className = "btn btn-green";
    confirmBtn.textContent = "Confirm";
    confirmBtn.onclick = () => {
        const race = raceSelect.value;
        const subrace = !subraceSelect.classList.contains("d-none") ? subraceSelect.value : null;

        if (!race) {
            alert("Please select a race.");
            return;
        }

        if (!subraceSelect.classList.contains("d-none") && !subrace) {
            alert("Please select a subrace.");
            return;
        }

        // Store previous values to detect change
        const prevRace = newChar.race_type;
        const prevSubrace = newChar.subrace_name;

        newChar.race_type = race;
        newChar.subrace_name = subrace;
        // console.log(`Previous | Race: ${prevRace} Subrace: ${prevRace}`);
        // console.log((`New | Race: ${race} Subrace: ${subrace}`));
        

        // Refresh summary only if race or subrace changed
        if (race !== prevRace || subrace !== prevSubrace) {
            const summary = document.getElementById("raceSummaryContainer");
            if (summary) {
                renderRaceSummary(summary);
            } 
            else {
                const mainContainer = document.getElementById("raceContainer");
                if (mainContainer) renderRaceSummary(mainContainer);
            }
        }

        // Update main button
        const addBtn = document.getElementById("addRaceBtn");
        if (addBtn) addBtn.textContent = "Change Race";

        slot.innerHTML = "";
        updateNextButtonState(isValidRaceSelection());
    };

    const cancelBtn = document.createElement("button");
    cancelBtn.className = "btn btn-light";
    cancelBtn.textContent = "Cancel";
    cancelBtn.onclick = () => (slot.innerHTML = "");

    row.append(raceSelect, subraceSelect, confirmBtn, cancelBtn);
    slot.appendChild(row);
}

function renderRaceSummary(container) {
    container.innerHTML = "";

    const raceName = newChar.race_type;
    const subraceName = newChar.subrace_name;

    const header = document.createElement("h3");
    header.className = "mb-3";
    header.textContent = `${raceName}${subraceName ? ` – ${subraceName}` : ""}`;
    container.appendChild(header);

    const raceBlock = document.createElement("section");
    raceBlock.className = "race-block mb-3";

    const featuresBox = document.createElement("details");
    featuresBox.className = "race-feature-box fa-chevron";
    featuresBox.innerHTML = "<em>Loading features...</em>";

    raceBlock.appendChild(featuresBox);
    container.appendChild(raceBlock);

    fetch(`/api/races/features/${encodeURIComponent(raceName)}${subraceName ? `?subrace=${encodeURIComponent(subraceName)}` : ""}`)
        .then(res => res.json())
        .then(data => {
            if (data.status !== "success") {
                featuresBox.innerHTML = `<em class="text-danger">Failed to load race data.</em>`;
                return;
            }

            featuresBox.innerHTML = renderRaceFeaturesFromAPI(data);
            featuresBox.setAttribute("open", "true");

            insertChevronsIntoDetailsFA();
        })
        .catch(err => {
            console.error("Error loading race features", err);
            featuresBox.innerHTML = `<em class="text-danger">Error loading race data.</em>`;
        });
}


function renderRaceFeaturesFromAPI(data) {
    let html = "";
    // console.log("Data", data);
    
    const {
        name,
        sr_name,
        features: {
            race: features = [],
            subrace: sr_features = []
        } = {},
        description,
        sr_description,
        languages,
        asi,
        info: {
            age: age,
            alignment: alignment,
            size: size,
            speed: speed
        } = {},
    } = data;

    // Optional summary header (like in class)
    html += `
    <summary class="editor-race-features fit-chevron">
        <h4 class="class-features-title">Race Features</h4>
    </summary>
    `;

    // Description(s)
    if (description) {
        html += `<p class="dnd-feature-desc text-color-grey mt-2"><em>${description}</em></p>`;
    }

    if (sr_description) {
        html += `<p class="dnd-feature-desc text-color-grey mt-2"><em>${sr_description}</em></p>`;
    }

    // Features
    html += `<section class="class-feature-grid mt-3">`;

    // ASI
    const asiList = Object.entries(asi).map(([key, value]) => {
        const label = abilityMap[key] || key;
        return `<li>Your ${label} score increases by ${value}.</li>`;
    });
    html += `
    <details class="fa-chevron class-feature-block">
        <summary>
            <div class="flex-col">
                <h5 class="class-feature-block-title">Ability Score Increase</h5>
                <small class="text-color-grey">Racial Trait</small>
            </div>
        </summary>
        <div class="class-feature-content">
            <ul class="dnd-feature-list">${asiList.join("")}</ul>
        </div>
    </details>
    `;

    // Age
    html += `
    <details class="fa-chevron class-feature-block">
        <summary>
            <div class="flex-col">
                <h5 class="class-feature-block-title">Age</h5>
                <small class="text-color-grey">Racial Trait</small>
            </div>
        </summary>
        <div class="class-feature-content">
            <p class="dnd-feature-desc">${age}</p>
        </div>
    </details>
    `;

    // Alignment
    html += `
    <details class="fa-chevron class-feature-block">
        <summary>
            <div class="flex-col">
                <h5 class="class-feature-block-title">Alignment</h5>
                <small class="text-color-grey">Racial Trait</small>
            </div>
        </summary>
        <div class="class-feature-content">
            <p class="dnd-feature-desc">${alignment}</p>
        </div>
    </details>
    `;

    // Size
    html += `
    <details class="fa-chevron class-feature-block">
        <summary>
            <div class="flex-col">
                <h5 class="class-feature-block-title">Size</h5>
                <small class="text-color-grey">Racial Trait</small>
            </div>
        </summary>
        <div class="class-feature-content">
            <p class="dnd-feature-desc">Your size is ${size}.</p>
        </div>
    </details>
    `;

    // Speed
    html += `
    <details class="fa-chevron class-feature-block">
        <summary>
            <div class="flex-col">
                <h5 class="class-feature-block-title">Speed</h5>
                <small class="text-color-grey">Racial Trait</small>
            </div>
        </summary>
        <div class="class-feature-content">
            <p class="dnd-feature-desc">Your base walking speed is ${speed} feet.</p>
        </div>
    </details>
    `;

    // Race features
    features.forEach((f, idx) => {
        html += `<details class="fa-chevron class-feature-block">
            <summary>
                <div class="flex-col">
                    <h5 class="class-feature-block-title">${f.name}</h5>
                    <small class="text-color-grey">${name} Trait</small>
                </div>
            </summary>
            <div class="class-feature-content">
                <p class="dnd-feature-desc">${f.description}</p>
            </div>
        </details>`;
    });

    // Subrace features
    sr_features.forEach((f, idx) => {
        html += `<details class="fa-chevron class-feature-block">
            <summary>
                <div class="flex-col">
                    <h5 class="class-feature-block-title">${f.name}</h5>
                    <small class="text-color-grey">${sr_name} Trait</small>
                </div>
            </summary>
            <div class="class-feature-content">
                <p class="dnd-feature-desc">${f.description}</p>
            </div>
        </details>`;
    });

    // Languages
    const langList = languages.map(l => `<li>${l}</li>`).join("");
    const langBlock = `
    <details class="fa-chevron class-feature-block">
        <summary>
            <div class="flex-col">
                <h5 class="class-feature-block-title">Languages</h5>
                <small class="text-color-grey">Racial Trait</small>
            </div>
        </summary>
        <div class="class-feature-content">
            <p class="dnd-feature-desc">You can speak, read and write the following languages :</p>
            <ul class="dnd-feature-list">${langList}</ul>
        </div>
    </details>
    `;
    if (languages.length) {
        html += langBlock;
    }

    html += `</section>`;
    return applyTextFormatting(html);
}

function isValidRaceSelection() {
    const hasRace = !!newChar.race_type;
    const needsSubrace = subraceMap[newChar.race_type]?.length > 0;
    const hasSubrace = !!newChar.subrace_name;

    return hasRace && (!needsSubrace || hasSubrace);
}
