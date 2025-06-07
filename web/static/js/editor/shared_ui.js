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

export function setupSkillSelectValidation(block) {
    const selects = block.querySelectorAll("select.skill-select");
    if (!selects.length) return;

    const validate = () => {
        syncSkillSelects(block);
        validateSkillChoicesBlock(block);
    };

    selects.forEach(select => {
        select.addEventListener("change", validate);
    });

    validate(); // Initial call
}

function syncSkillSelects(container) {
    const selects = container.querySelectorAll("select.skill-select");
    const selectedValues = Array.from(selects)
        .map(s => s.value)
        .filter(v => v !== "");

    selects.forEach(select => {
        const current = select.value;
        Array.from(select.options).forEach(opt => {
            if (opt.value === "") return; // Skip placeholder
            opt.disabled = selectedValues.includes(opt.value) && opt.value !== current;
        });
    });
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
