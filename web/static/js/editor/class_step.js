// editor/class_step.js
import { newChar } from '../character_editor.js';
import { updateNextButtonState, updateNavHeader } from './shared_ui.js';

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

    addBtn.onclick = () => addClassSelector(container);

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
        const input = entry.querySelector("input");
        const className = select?.value;
        const level = parseInt(input?.value);

        if (className && !isNaN(level)) {
            newChar.classes.push({ name: className, level });
        }
    });

    const hasClass = newChar.classes.length > 0;
    updateNextButtonState(hasClass);

    const msg = document.getElementById("classStepMessage");
    if (msg) msg.classList.toggle("d-none", hasClass);
}

function addClassSelector(container) {
    const wrapper = document.createElement("div");
    wrapper.className = "d-flex flex-column gap-2 mb-3";

    const row = document.createElement("div");
    row.className = "d-flex align-items-center gap-2";

    const classSelect = document.createElement("select");
    classSelect.className = "form-control";
    classSelect.innerHTML = `<option disabled selected value="">Choose class</option>` +
        window.classListCache.map(c => `<option value="${c.name}">${c.name}</option>`).join("");

    const levelInput = document.createElement("input");
    levelInput.type = "number";
    levelInput.min = "1";
    levelInput.max = "20";
    levelInput.value = "1";
    levelInput.className = "form-control";
    levelInput.style = "width: 80px";

    const removeBtn = document.createElement("button");
    removeBtn.className = "btn btn-danger";
    removeBtn.innerHTML = `<i class="fas fa-times"></i>`;
    removeBtn.onclick = () => {
        container.removeChild(wrapper);
        syncClassData(container);
    };

    row.append(classSelect, levelInput, removeBtn);

    // Details container
    const details = document.createElement("div");
    details.className = "class-feature-box";

    // Update features on change
    const updateFeatures = () => {
        const className = classSelect.value;
        const level = parseInt(levelInput.value) || 1;
    
        if (!className) {
            details.innerHTML = "";
            return;
        }
    
        fetch(`/api/classes/features/${encodeURIComponent(className)}?level=${level}`)
            .then(res => res.json())
            .then(data => {
                if (data.status !== "success") {
                    details.innerHTML = "<em>Failed to load class data.</em>";
                    return;
                }
    
                details.innerHTML = renderClassDetailsWithSkills(data, className);
            });
    };    

    [classSelect, levelInput].forEach(el =>
        el.addEventListener("change", () => {
            syncClassData(container);
            updateFeatures();
        })
    );

    wrapper.append(row, details);
    container.appendChild(wrapper);

    syncClassData(container);
}

function renderClassDetailsFromAPI(classData) {
    let html = "";

    const { hit_points: hp, proficiencies: prof, features, spells, requisite } = classData;

    // Hit Points
    html += `
        <details open class="mb-3">
            <summary><strong>Hit Points</strong></summary>
            <div>
                <p><strong>Hit Dice:</strong> 1d${hp.dice} per level</p>
                <p><strong>HP at 1st Level:</strong> ${hp.at_1st_level} + ${hp.ability_mod.toUpperCase()} mod</p>
                <p><strong>HP at Higher Levels:</strong> d${hp.dice} (or ${hp.per_level}) + ${hp.ability_mod.toUpperCase()} mod</p>
            </div>
        </details>
    `;

    // Proficiencies
    html += `
        <details open class="mb-3">
            <summary><strong>Proficiencies</strong></summary>
            <div>
                <p><strong>Armor:</strong> ${prof.armor.join(", ") || "None"}</p>
                <p><strong>Weapons:</strong> ${prof.weapons.join(", ") || "None"}</p>
                <p><strong>Specific Weapons:</strong> ${prof.specific_weapons.join(", ") || "None"}</p>
                <p><strong>Tools:</strong> ${prof.tools.join(", ") || "None"}</p>
                <p><strong>Saving Throws:</strong> ${prof.saving_throws.map(s => s.toUpperCase()).join(", ")}</p>
                <p><strong>Skills:</strong> Choose ${prof.skill_choices} from ${prof.skill_pool.join(", ")}</p>
            </div>
        </details>
    `;

    // Class Features
    const featuresGrouped = groupBy(features, "level");
    html += `
        <details open class="mb-3">
            <summary><strong>Class Features</strong></summary>
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

    // Spells (if any)
    if (spells?.length) {
        const spellsGrouped = groupBy(spells, "level");
        html += `
            <details open class="mb-3">
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

    if (requisite) {
        html += `
            <details class="mb-3">
                <summary><strong>Multiclass Requirement</strong></summary>
                <p>${requisite}</p>
            </details>
        `;
    }

    return html;
}

function renderClassDetailsWithSkills(classData, className) {
    const html = renderClassDetailsFromAPI(classData);

    const { skill_pool, skill_choices } = classData.proficiencies;

    // Only add skill selector if the class has skill choices
    if (skill_choices && skill_pool?.length) {
        const skillHTML = Array.from({ length: skill_choices }).map((_, i) => `
            <div class="form-group mb-2">
                <label for="skillSelect_${className}_${i}">Choose a ${className} Skill</label>
                <select class="form-control skill-select" id="skillSelect_${className}_${i}">
                    <option value="" disabled selected>- Choose a Skill -</option>
                    ${skill_pool.map(skill => `<option value="${skill}">${skill}</option>`).join("")}
                </select>
            </div>
        `).join("");

        return html + `
            <details open class="mb-3">
                <summary><strong>Skill Selection</strong></summary>
                <div class="mt-2">${skillHTML}</div>
            </details>
        `;
    }

    return html;
}


function groupBy(arr, key) {
    return arr.reduce((acc, item) => {
        const group = item[key] ?? "unknown";
        if (!acc[group]) acc[group] = [];
        acc[group].push(item);
        return acc;
    }, {});
}

