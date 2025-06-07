// editor/shared_ui.js
export function updateNextButtonState(enabled) {
    document.getElementById("nextStepBtn").disabled = !enabled;
}

export function updateNavHeader(text, visible = true) {
    const header = document.getElementById("charNavHeader");
    if (!header) return;

    header.textContent = text;
    header.classList.toggle("hidden", !visible);
}

export function setupSkillSelectValidation(block, charData) {
    const selects = block.querySelectorAll("select.skill-select");
    if (!selects.length) return;

    const className = block.closest(".class-block")?.querySelector("h3")?.textContent;
    if (!className) return;

    const validate = () => {
        syncSkillSelects(block, className, charData);
        validateSkillChoicesBlock(block);
    };

    selects.forEach(select => {
        select.addEventListener("change", validate);
    });

    validate();
}

function validateSkillChoicesBlock(container) {
    const selects = container.querySelectorAll("select.skill-select");
    const hasMissing = Array.from(selects).some(s => !s.value);

    const block = container.closest(".class-feature-block");
    if (!block) return;

    block.classList.toggle("highlight-border", hasMissing);
    selects.forEach(s => s.classList.toggle("select-missing", !s.value));

    updateFeatureBlockIcon(block, hasMissing);
}

function updateFeatureBlockIcon(container) {
    const details = container.closest(".class-feature-block");
    if (!details) return;

    // If already wrapped, get the wrapper
    let wrapper = details.parentElement;
    const alreadyWrapped = wrapper.classList.contains("wrapper-class-feature-block");

    if (!alreadyWrapped) {
        // Create a wrapper div
        const newWrapper = document.createElement("div");
        newWrapper.classList.add("wrapper-class-feature-block");

        // Insert before and move details into it
        details.parentElement.insertBefore(newWrapper, details);
        newWrapper.appendChild(details);

        wrapper = newWrapper; // Use new wrapper
    }

    // Remove all existing icons
    wrapper.querySelectorAll(".feature-warning-icon").forEach(el => el.remove());

    const hasMissing = Array.from(container.querySelectorAll("select.skill-select")).some(s => !s.value);
    if (hasMissing) {
        const icon = document.createElement("i");
        icon.className = "fas fa-exclamation-circle feature-warning-icon";
        wrapper.appendChild(icon);
    }
}

export function updateAbilityScores(char) {
    const abilityKeys = ['str', 'dex', 'con', 'int', 'wis', 'cha'];
    const abilities = {};

    abilityKeys.forEach(key => {
        const el = document.getElementById(`ability-${key}`);
        if (el) {
            const val = parseInt(el.value);
            abilities[key] = isNaN(val) ? null : val;
        }
    });

    char.abilities = abilities;

    // Optionally, log or trigger further updates
    console.log("Updated Abilities:", char.abilities);
}

export function getAllSelectedSkills(charData, excludeClass = null) {
    return charData.classes
        .filter(c => c.name !== excludeClass)
        .flatMap(c => c.skills || []);
}

export function syncSkillSelects(container, currentClass, charData) {
    const selects = container.querySelectorAll("select.skill-select");
    const selectedValues = Array.from(selects)
        .map(s => s.value)
        .filter(v => v !== "");

    const otherClassSkills = getAllSelectedSkills(charData, currentClass);

    selects.forEach(select => {
        const current = select.value;
        Array.from(select.options).forEach(opt => {
            if (opt.value === "") return;

            const takenInThisBlock = selectedValues.includes(opt.value) && opt.value !== current;
            const takenInOtherBlock = otherClassSkills.includes(opt.value);

            opt.disabled = takenInThisBlock || takenInOtherBlock;
        });
    });
}
