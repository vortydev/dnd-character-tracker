// editor/class_step.js
import { newChar } from '../character_editor.js';
import { updateNextButtonState, updateNavHeader } from './shared_ui.js';

const MAX_LEVELS = 20;

export function initClassStep() {
    const container = document.getElementById("classContainer");
    const addBtn = document.getElementById("addClassBtn");
    if (!container || !addBtn) return;

    updateNavHeader(newChar.name || "Unnamed Character", true);  // Show character name

    container.innerHTML = ""; // Reset
    newChar.classes = [];

    // Add instructional message
    const msg = document.createElement("div");
    msg.className = "text-muted";
    msg.textContent = "Add at least one class to continue.";
    msg.id = "classStepMessage";
    container.appendChild(msg);

    const selectorSlot = document.createElement("div");
    selectorSlot.id = "classSelectorSlot";
    addBtn.insertAdjacentElement("afterend", selectorSlot);

    addBtn.onclick = () => renderTemporarySelector(selectorSlot, container);

    if (!window.classListCache) {
        fetch("/api/classes/get")
            .then(res => res.json())
            .then(data => {
                window.classListCache = data.class_list || [];
                window.levelListCache = data.level_list || [];
                updateNextButtonState(false);
            });
    } 
    else {
        updateNextButtonState(false);
    }
}

function syncClassData(container) {
    const entries = container.querySelectorAll("div.d-flex");
    newChar.classes = [];

    entries.forEach(entry => {
        const select = entry.querySelector("select");
        const input = entry.querySelector("select:nth-child(2)");
        const className = select?.value;
        const level = parseInt(input?.value);

        if (className && !isNaN(level)) {
            newChar.classes.push({ name: className, level });
        }
    });

    const hasClass = newChar.classes.length > 0;
    updateNextButtonState(hasClass);

    // ✅ Show/Hide instructional message
    const msg = document.getElementById("classStepMessage");
    if (msg) msg.classList.toggle("hidden", hasClass);

    // ✅ Update character level display
    const totalLevel = newChar.classes.reduce((sum, cls) => sum + cls.level, 0);
    const charLevelLabel = document.getElementById("charLevelTotal");
    if (charLevelLabel) charLevelLabel.textContent = totalLevel;

    // ✅ Cap all level dropdowns
    updateAllLevelOptions();
}


function getAvailableClasses() {
    const selectedNames = newChar.classes.map(cls => cls.name);
    return window.classListCache.filter(c => !selectedNames.includes(c.name));
}


function refreshAllClassSelectors() {
    document.querySelectorAll("#classContainer select").forEach(select => {
        const selectedValue = select.value;
        const isLevel = /^\d+$/.test(selectedValue);
        if (isLevel) return; // Skip level inputs

        const available = getAvailableClasses();
        select.innerHTML = `<option disabled value="">Choose a class</option>` +
            available.map(c => `<option value="${c.name}" ${c.name === selectedValue ? "selected" : ""}>${c.name}</option>`).join("");
    });
}


function renderClassDetailsFromAPI(classData) {
    let html = "";
    html += `<summary class="editor-class-features">
        <h4 class="class-features-title">Class Features</h4>
    </summary>`;

    // Extract class data
    const { class_name: name, level: level, hit_points: hp, proficiencies: prof, features, spells, requisite } = classData;

    if (requisite) {
        html += `<small class="dnd-feature-desc text-color-grey mt-2"><em>${requisite}</em></small>`
    }

    // Hit Points
    const hpBlock = `
        <details class="class-feature-block mt-3">
            <summary>
                <div class="flex-col">
                    <h5 class="class-feature-block-title">Hit Points</h5>
                    <small class="text-color-grey">${level}st level</small>
                </div>
            </summary>
            <ul class="dnd-feature-list">
                <li><strong>Hit Dice:</strong> 1d${hp.dice} per ${name.toLowerCase()} level</li>
                <li><strong>Hit Points at 1st Level:</strong> ${hp.at_1st_level} + your Constitution modifier</li>
                <li><strong>Hit Points at Higher Levels:</strong> 1d${hp.dice} (or ${hp.per_level}) + your Constitution modifier per ${name.toLowerCase()} level after the 1st</li>
            </ul>
        </details>`;
    html += hpBlock;

    let skillChoices = "";
    if (prof.skill_choices && prof.skill_pool?.length) {
        const skillHTML = Array.from({ length: prof.skill_choices }).map((_, i) => `
            <div class="form-group mb-2">
                <select class="form-control form-select skill-select" id="skillSelect_${name}_${i}">
                    <option value="" disabled selected>- Choose a ${name} Skill -</option>
                    ${prof.skill_pool.map(skill => `<option value="${skill}">${skill}</option>`).join("")}
                </select>
            </div>
        `).join("");

        skillChoices = `<div class="mt-3">
            ${skillHTML}
        </div>`;
    }
    const skillChoicesStr = prof.skill_choices > 0 ? `${prof.skill_choices} Choices • ` : "";


    // Proficiencies
    // TODO Add choice logic for skill selection within the prof block
    const profBlock = `
        <details class="class-feature-block mt-3">
            <summary>
                <div class="flex-col">
                    <h5 class="class-feature-block-title">Proficiencies</h5>
                    <small class="text-color-grey">${skillChoicesStr}${level}st level</small>
                </div>
            </summary>
            <ul class="dnd-feature-list">
                <li><strong>Armor:</strong> ${prof.armor.join(", ") || "None"}</li>
                <li><strong>Weapons:</strong> ${prof.weapons.join(", ") || "None"}</li>
                <li><strong>Specific Weapons:</strong> ${prof.specific_weapons.join(", ") || "None"}</li>
                <li><strong>Tools:</strong> ${prof.tools.join(", ") || "None"}</li>
                <li><strong>Saving Throws:</strong> ${prof.saving_throws.map(s => `ITALIC[${s.toUpperCase()}]`).join(", ")}</li>
                <li><strong>Skills:</strong> Choose ${prof.skill_choices} from ${prof.skill_pool.join(", ")}</li>
            </ul>
            ${skillChoices}
        </details>`;
    html += profBlock;

    // WIP Class Features
    const featuresGrouped = groupBy(features, "level");
    console.log("Features", features, featuresGrouped);
    
    html += `
        <details class="class-feature-block mt-3">
            <summary>
                <div class="flex-col">
                    <h5 class="class-feature-block-title">tmp</h5>
                    <small class="text-color-grey">${level} level</small>
                </div>
            </summary>
            <div>
                ${Object.entries(featuresGrouped).map(([lvl, feats]) => `
                    <details>
                        <summary><strong>Level ${lvl}</strong></summary>
                        <ul>${feats.map(f => `<li>${f.name}</li>`).join("")}</ul>
                    </details>
                `).join("")}
            </div>
        </details>
    `;

    // TODO Spells (if any)
    if (spells?.length) {
        const spellsGrouped = groupBy(spells, "level");
        html += `
            <details class="mb-3">
                <summary><strong>Spells</strong></summary>
                <div>
                    ${Object.entries(spellsGrouped).map(([lvl, spls]) => `
                        <details>
                            <summary><strong>Level ${lvl}</strong></summary>
                            <ul>${spls.map(s => `<li>${s.name}</li>`).join("")}</ul>
                        </details>
                    `).join("")}
                </div>
            </details>
        `;
    }

    return applyTextFormatting(html);
}


function groupBy(arr, key) {
    return arr.reduce((acc, item) => {
        const group = item[key] ?? "unknown";
        if (!acc[group]) acc[group] = [];
        acc[group].push(item);
        return acc;
    }, {});
}


function populateLevelSelect(selectEl, currentLevel = 1) {
    const totalUsed = newChar.classes.reduce((sum, cls) => sum + cls.level, 0);
    const remaining = MAX_LEVELS - totalUsed + currentLevel;

    selectEl.innerHTML = "";
    for (let i = 1; i <= Math.min(20, remaining); i++) {
        selectEl.innerHTML += `<option value="${i}" ${i === currentLevel ? "selected" : ""}>${i}</option>`;
    }
}

function updateAllLevelOptions() {
    const blocks = document.querySelectorAll("#classContainer .d-flex");
    blocks.forEach(block => {
        const select = block.querySelector("select:nth-child(2)");
        if (select) {
            const current = parseInt(select.value || "1");
            populateLevelSelect(select, current);
        }
    });
}


function renderTemporarySelector(slot, container) {
    slot.innerHTML = "";  // Clear any existing one

    const row = document.createElement("div");
    row.className = "d-flex align-items-center gap-2 mt-3";

    const availableClasses = getAvailableClasses();
    if (availableClasses.length === 0) {
        row.innerHTML = `<div class="text-muted">No classes left to add.</div>`;
        slot.appendChild(row);
        return;
    }

    const classSelect = document.createElement("select");
    classSelect.className = "form-control";
    classSelect.innerHTML = `<option disabled selected value="">Choose class</option>` +
        availableClasses.map(c => `<option value="${c.name}">${c.name}</option>`).join("");

    const levelSelect = document.createElement("select");
    levelSelect.className = "form-control";
    levelSelect.style = "width: 80px";
    populateLevelSelect(levelSelect);

    const confirmBtn = document.createElement("button");
    confirmBtn.className = "btn btn-primary";
    confirmBtn.textContent = "Confirm";
    confirmBtn.onclick = () => {
        const className = classSelect.value;
        const level = parseInt(levelSelect.value);

        if (!className || isNaN(level)) {
            alert("Please choose a class and level.");
            return;
        }

        // Add to character
        newChar.classes.push({ name: className, level });
        slot.innerHTML = "";  // Clear selector
        appendRealClassBlock(container, className, level);
        updateNextButtonState(true);
    };

    const cancelBtn = document.createElement("button");
    cancelBtn.className = "btn btn-light";
    cancelBtn.textContent = "Cancel";
    cancelBtn.onclick = () => slot.innerHTML = "";

    row.append(classSelect, levelSelect, confirmBtn, cancelBtn);
    slot.appendChild(row);
}

function appendRealClassBlock(container, className, level) {
    const wrapper = document.createElement("div");
    wrapper.className = "d-flex flex-column gap-2 mb-3";

    const row = document.createElement("div");
    row.className = "d-flex align-items-center gap-2";

    const classHeader = document.createElement("h3");
    classHeader.className = "mb-2";
    classHeader.textContent = className;

    const subclassHeading = document.createElement("div");
    subclassHeading.className = "text-muted";
    subclassHeading.style.fontSize = "0.85rem";
    subclassHeading.style.display = "none";

    const levelSelect = document.createElement("select");
    levelSelect.className = "form-control";
    levelSelect.style = "width: 80px";
    populateLevelSelect(levelSelect, level);

    levelSelect.value = level;

    const removeBtn = document.createElement("button");
    removeBtn.className = "btn btn-danger btn-icon";
    removeBtn.innerHTML = `<i class="fas fa-xmark"></i>`;
    removeBtn.onclick = () => {
        container.removeChild(wrapper);
        newChar.classes = newChar.classes.filter(c => c.name !== className);
        syncClassData(container);
        refreshAllClassSelectors();
        updateAllLevelOptions();
    };

    row.append(levelSelect, removeBtn);

    const details = document.createElement("details");
    details.className = "class-feature-box";

    wrapper.append(subclassHeading, classHeader, row, details);
    container.appendChild(wrapper);

    // Fetch & render data
    fetch(`/api/classes/features/${encodeURIComponent(className)}?level=${level}`)
        .then(res => res.json())
        .then(data => {
            if (data.status !== "success") {
                details.innerHTML = "<em>Failed to load class data.</em>";
                return;
            }

            subclassHeading.textContent = data.subclass || "";
            subclassHeading.style.display = data.subclass ? "block" : "none";
            details.innerHTML = renderClassDetailsFromAPI(data, className);
        });

    // Update on level change
    levelSelect.addEventListener("change", () => {
        const newLevel = parseInt(levelSelect.value);
        const cls = newChar.classes.find(c => c.name === className);
        cls.level = newLevel;
        updateAllLevelOptions();

        fetch(`/api/classes/features/${encodeURIComponent(className)}?level=${newLevel}`)
            .then(res => res.json())
            .then(data => {
                if (data.status !== "success") {
                    details.innerHTML = "<em>Failed to load class data.</em>";
                    return;
                }

                subclassHeading.textContent = data.subclass || "";
                subclassHeading.style.display = data.subclass ? "block" : "none";
                details.innerHTML = renderClassDetailsFromAPI(data, className);
            });
    });
}
