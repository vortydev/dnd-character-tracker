// editor/name_step.js
import { newChar } from '../character_editor.js';
import { updateNextButtonState, updateNavHeader } from './shared_ui.js';

export async function initNameStep() {
    updateNavHeader("", false);

    const input = document.getElementById("charNameInput");
    const feedback = document.getElementById("nameFeedback");

    if (!input) {
        updateNextButtonState(false);
        return;
    }

    // 🟢 Restore and revalidate if name exists
    if (newChar.name) {
        input.value = newChar.name;
        await validateCharacterName(
            newChar.name,
            feedback,
            () => updateNextButtonState(true),
            () => {
                newChar.name = null;
                updateNextButtonState(false);
            }
        );
    }

    input.addEventListener("input", async () => {
        const value = input.value.trim();
        if (!value) {
            feedback.textContent = "Name is required.";
            feedback.classList.add("text-danger");
            feedback.classList.remove("text-success");
            newChar.name = null;
            updateNextButtonState(false);
            return;
        }

        await validateCharacterName(
            value,
            feedback,
            () => {
                newChar.name = value;
                updateNextButtonState(true);
            },
            () => {
                newChar.name = null;
                updateNextButtonState(false);
            }
        );
    });

    updateNextButtonState(!!newChar.name);
}

async function validateCharacterName(name, feedbackEl, onValid, onInvalid) {
    fetch(`/api/characters/check-name/${encodeURIComponent(name)}`)
        .then(res => res.json())
        .then(data => {
            if (data.exists) {
                feedbackEl.textContent = "Name already exists. Please choose another.";
                feedbackEl.classList.add("text-danger");
                feedbackEl.classList.remove("text-success");
                onInvalid();
            } else {
                feedbackEl.textContent = "Name is available!";
                feedbackEl.classList.remove("text-danger");
                feedbackEl.classList.add("text-success");
                onValid();
            }
        })
        .catch(() => {
            feedbackEl.textContent = "Error checking name. Try again.";
            feedbackEl.classList.add("text-danger");
            feedbackEl.classList.remove("text-success");
            onInvalid();
        });
}
