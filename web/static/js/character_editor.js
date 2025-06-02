// character_editor.js (main entry point)
import { initNameStep } from './editor/name_step.js';
import { initClassStep } from './editor/class_step.js';
import { initRaceStep } from './editor/race_step.js';
import { initBackgroundStep } from './editor/background_step.js';
import { initAbilitiesStep } from './editor/abilities_step.js';
import { initEquipmentStep } from './editor/equipment_step.js';

let currentStep = 0;
const steps = [
    initNameStep,
    initClassStep,
    initRaceStep,
    initBackgroundStep,
    initAbilitiesStep,
    initEquipmentStep
];

export let newChar = {
    name: null,
    race_type: null,
    subrace_name: null,
    classes: [],
    abilities: {},
    background: null,
    equipment: []
};

export function goToStep(index) {
    if (index < 0 || index >= steps.length) return;
    document.querySelectorAll(".step-section").forEach(el => el.classList.add("hidden"));
    steps[index]();
    document.getElementById(`step-${index}`).classList.remove("hidden");
    currentStep = index;
    updateNavButtons();
}

function updateNavButtons() {
    document.getElementById("prevStepBtn").disabled = currentStep === 0;
    document.getElementById("nextStepBtn").disabled = currentStep === steps.length - 1;
    document.getElementById("createCharBtn").classList.toggle("hidden", currentStep !== steps.length - 1);
}

document.addEventListener("DOMContentLoaded", () => {
    goToStep(0);

    document.getElementById("prevStepBtn").addEventListener("click", () => goToStep(currentStep - 1));
    document.getElementById("nextStepBtn").addEventListener("click", () => goToStep(currentStep + 1));
});
