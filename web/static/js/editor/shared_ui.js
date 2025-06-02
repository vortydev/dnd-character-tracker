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

