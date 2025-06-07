// editor/name_step.js
import { newChar } from '../character_editor.js';
import { updateNextButtonState, updateNavHeader } from './shared_ui.js';

export function initNameStep() {
    updateNavHeader("", false);

    const input = document.getElementById("charNameInput");
    const feedback = document.getElementById("nameFeedback");

    if (!input) {
        updateNextButtonState(false);
        return;
    }

    input.addEventListener("input", () => {
        const value = input.value.trim();
        if (!value) {
            feedback.textContent = "Name is required.";
            feedback.classList.add("text-danger");
            feedback.classList.remove("text-success");
            newChar.name = null;
            updateNextButtonState(false);
            return;
        }

        fetch(`/api/characters/check-name/${encodeURIComponent(value)}`)
            .then(res => res.json())
            .then(data => {
                if (data.exists) {
                    feedback.textContent = "Name already exists. Please choose another.";
                    feedback.classList.add("text-danger");
                    feedback.classList.remove("text-success");
                    newChar.name = null;
                    updateNextButtonState(false);
                } else {
                    feedback.textContent = "Name is available!";
                    feedback.classList.remove("text-danger");
                    feedback.classList.add("text-success");
                    newChar.name = value;
                    updateNextButtonState(true);
                }
            })
            .catch(() => {
                feedback.textContent = "Error checking name. Try again.";
                feedback.classList.add("text-danger");
                feedback.classList.remove("text-success");
                newChar.name = null;
                updateNextButtonState(false);
            });
    });

    input.focus();

    updateNextButtonState(!!newChar.name);
}
