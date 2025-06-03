// editor/class_step.js
import { newChar } from '../character_editor.js';
import { updateNextButtonState, updateNavHeader, setupSkillSelectValidation } from './shared_ui.js';

const MAX_LEVELS = 20;

export async function initClassStep() {
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

    addBtn.onclick = async () => await renderTemporarySelector(selectorSlot, container);

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
    const entries = container.querySelectorAll("div.class-block");
    newChar.classes = [];

    entries.forEach(entry => {
        const selects = entry.querySelectorAll("select");
        const className = entry.querySelector("h3")?.textContent;
        const level = parseInt(selects[0]?.value);

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
    html += `
    <summary class="editor-class-features">
        <h4 class="class-features-title">Class Features</h4>
    </summary>
    `;

    // Extract class data
    const { class_name: name, level: level, hit_points: hp, proficiencies: prof, features, spells, requisite } = classData;

    if (requisite) {
        html += `<small class="dnd-feature-desc text-color-grey mt-2"><em>${requisite}</em></small>`
    }

    html += `<section class="class-feature-grid mt-3">`; // Start the grid

    // Hit Points
    const hpBlock = `
        <details class="fa-chevron class-feature-block">
            <summary>
                <div class="flex-col">
                    <h5 class="class-feature-block-title">Hit Points</h5>
                    <small class="text-color-grey">${levelStr(1)} level</small>
                </div>
            </summary>
            <div class="class-feature-content">
                <ul class="dnd-feature-list">
                    <li><strong>Hit Dice:</strong> 1d${hp.dice} per ${name.toLowerCase()} level</li>
                    <li><strong>Hit Points at 1st Level:</strong> ${hp.at_1st_level} + your Constitution modifier</li>
                    <li><strong>Hit Points at Higher Levels:</strong> 1d${hp.dice} (or ${hp.per_level}) + your Constitution modifier per ${name.toLowerCase()} level after the 1st</li>
                </ul>
            </div>
        </details>`;
    html += hpBlock;

    let skillChoices = "";
    if (prof.skill_choices && prof.skill_pool?.length) {
        const skillHTML = Array.from({ length: prof.skill_choices }).map((_, i) => `
            <div class="form-group mb-2">
                <select class="form-control form-select skill-select" id="skillSelect_${name}_${i}">
                    <option value="" selected>- Choose a ${name} Skill -</option>
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
    // WIP Add choice logic for skill selection within the prof block
    const profBlock = `
        <details class="fa-chevron class-feature-block">
            <summary>
                <div class="flex-col">
                    <h5 class="class-feature-block-title">Proficiencies</h5>
                    <small class="text-color-grey">${skillChoicesStr}${levelStr(1)} level</small>
                </div>
            </summary>
            <div class="class-feature-content">
                <ul class="dnd-feature-list">
                    <li><strong>Armor:</strong> ${buildProficiencyStr("armor", prof.armor)}</li>
                    <li><strong>Weapons:</strong> ${buildProficiencyStr("weapon", prof.weapons, prof.specific_weapons)}</li>
                    <li><strong>Tools:</strong> ${prof.tools.join(", ") || "None"}</li>
                    <li><strong>Saving Throws:</strong> ${buildProficiencyStr("savingThrows", prof.saving_throws)}</li>
                    <li><strong>Skills:</strong> Choose ${prof.skill_choices} from ${buildProficiencyStr("skills", prof.skill_pool)}</li>
                </ul>
                ${skillChoices}
            </div>
        </details>`;
    html += profBlock;

    // Class Features    
    features.forEach((f, idx) => {
        const desc = f.data.description ? `<p class="dnd-feature-desc">${f.data.description}</p>` : "";
        const featBlock = `<details class="fa-chevron class-feature-block">
            <summary>
                <div class="flex-col">
                    <h5 class="class-feature-block-title">${f.name}</h5>
                    <small class="text-color-grey">${levelStr(f.level)} level</small>
                </div>
            </summary>
            <div class="class-feature-content">
                ${desc}
            </div>
        </details>`;
        html += featBlock;
    });

    html += `</section>`; // Close the grid

    return applyTextFormatting(html);
}


function populateLevelSelect(selectEl, currentLevel = 1) {
    const totalUsed = newChar.classes.reduce((sum, cls) => sum + cls.level, 0);
    const remaining = MAX_LEVELS - totalUsed + currentLevel;
    console.log(`Max: ${MAX_LEVELS}, Total used: ${totalUsed}, Current: ${currentLevel}, Remaining: ${remaining}`);
    

    selectEl.innerHTML = "";
    for (let i = 1; i <= Math.min(20, remaining); i++) {
        selectEl.innerHTML += `<option value="${i}" ${i === currentLevel ? "selected" : ""}>${i}</option>`;
    }
}


function updateAllLevelOptions() {
    const blocks = document.querySelectorAll("#classContainer .d-flex");
    const totalUsed = newChar.classes.reduce((sum, cls) => sum + cls.level, 0);

    blocks.forEach(block => {
        const select = block.querySelector("select.level-select");
        if (!select) return;

        const current = parseInt(select.value || "1");
        const max = Math.min(20, MAX_LEVELS - totalUsed + current);

        select.innerHTML = "";
        for (let i = 1; i <= max; i++) {
            select.innerHTML += `<option value="${i}" ${i === current ? "selected" : ""}>${i}</option>`;
        }
    });

    updateCharacterLevelDisplay();

    // const total = newChar.classes.reduce((sum, cls) => sum + cls.level, 0);
    const addBtn = document.getElementById("addClassBtn");
    if (addBtn) addBtn.disabled = totalUsed >= MAX_LEVELS;
}


async function renderTemporarySelector(slot, container) {
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
    classSelect.className = "form-control form-select class-select";
    classSelect.innerHTML = `<option disabled selected value="">Choose a class</option>` +
        availableClasses.map(c => `<option value="${c.name}">${c.name}</option>`).join("");

    const levelSelect = document.createElement("select");
    levelSelect.className = "form-control form-select level-select";

    const totalUsed = newChar.classes.reduce((sum, cls) => sum + cls.level, 0);
    const remaining = MAX_LEVELS - totalUsed;
    levelSelect.innerHTML = "";
    for (let i = 1; i <= remaining; i++) {
        levelSelect.innerHTML += `<option value="${i}">${i}</option>`;
    }

    // updateAllLevelOptions();

    const confirmBtn = document.createElement("button");
    confirmBtn.className = "btn btn-green";
    confirmBtn.textContent = "Confirm";
    confirmBtn.onclick = async () => {
        const className = classSelect.value;
        const level = parseInt(levelSelect.value);

        if (!className || isNaN(level)) {
            alert("Please choose a class and level.");
            return;
        }

        // Add to character
        newChar.classes.push({ name: className, level });
        slot.innerHTML = "";  // Clear selector
        await appendRealClassBlock(container, className, level);
        syncClassData(container);
        updateNextButtonState(true);
    };

    const cancelBtn = document.createElement("button");
    cancelBtn.className = "btn btn-light";
    cancelBtn.textContent = "Cancel";
    cancelBtn.onclick = () => slot.innerHTML = "";

    row.append(classSelect, levelSelect, confirmBtn, cancelBtn);
    slot.appendChild(row);
}

async function appendRealClassBlock(container, className, level) {
    const wrapper = document.createElement("div");
    wrapper.className = "class-block d-flex flex-column gap-2 mb-3";

    // WIP
    const classHeader = document.createElement("section");
    classHeader.className = "class-block-header";

    // Class + Subclass
    const classHeaderNameStack = document.createElement("div");
    classHeaderNameStack.className = "flex-col";

    const classHeaderName = document.createElement("h3");
    classHeaderName.className = "class-block-header-name";
    classHeaderName.textContent = className;

    const subclassHeading = document.createElement("h5");
    subclassHeading.className = "class-block-header-subclass";

    classHeaderNameStack.append(subclassHeading, classHeaderName);

    newChar.classes.push({ name: className, level });
    
    const levelSelect = document.createElement("select");
    levelSelect.className = "form-control form-select level-select";

    populateLevelSelect(levelSelect, level);

    levelSelect.value = level;
    updateAllLevelOptions();

    const removeBtn = document.createElement("button");
    removeBtn.className = "btn btn-danger btn-icon";
    removeBtn.innerHTML = `<i class="fas fa-xmark"></i>`;
    removeBtn.onclick = () => {
        container.removeChild(wrapper);
        // newChar.classes = newChar.classes.filter(c => c.name !== className);
        syncClassData(container);
        refreshAllClassSelectors();
        updateAllLevelOptions();
    };

    // Level selection + Delete button
    const row = document.createElement("div");
    row.className = "d-flex align-items-center gap-2";
    row.append(levelSelect, removeBtn);

    classHeader.append(classHeaderNameStack, row);

    const details = document.createElement("details");
    details.className = "class-feature-box";

    wrapper.append(classHeader, details);
    container.appendChild(wrapper);

    // Fetch & render data
    await fetchClassFeatures(className, level, subclassHeading, details);

    // Update on level change
    levelSelect.addEventListener("change", async () => {
        const newLevel = parseInt(levelSelect.value);
        syncClassData(container);
        await fetchClassFeatures(className, newLevel, subclassHeading, details);
    });

    // TODO Append horizontal rule after each class block
    // const hr = document.createElement("hr");
    // hr.className = "class-block-separator";
    // container.appendChild(hr);
}

async function fetchClassFeatures(className, classLevel, subclassHeading, details) {
    fetch(`/api/classes/features/${encodeURIComponent(className)}?level=${classLevel}`)
        .then(res => res.json())
        .then(data => {
            if (data.status !== "success") {
                details.innerHTML = "<em>Failed to load class data.</em>";
                return;
            }

            subclassHeading.textContent = data.subclass || "";
            details.innerHTML = renderClassDetailsFromAPI(data);

            insertChevronsIntoDetailsFA();

            setTimeout(() => {
                const blocks = document.querySelectorAll(".class-feature-block");
                blocks.forEach(setupSkillSelectValidation);
            }, 0);
        });
}

function updateCharacterLevelDisplay() {
    const totalLevel = newChar.classes.reduce((sum, cls) => sum + cls.level, 0);
    const label = document.getElementById("charLevelTotal");
    if (label) label.textContent = totalLevel;
}

function getRemainingLevels(forClass = null) {
    const used = newChar.classes.reduce((sum, cls) => sum + cls.level, 0);
    const already = forClass ? (newChar.classes.find(c => c.name === forClass)?.level || 0) : 0;
    return MAX_LEVELS - used + already;
}
