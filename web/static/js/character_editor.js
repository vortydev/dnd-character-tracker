// character_editor.js
const ABILITIES = ["STR", "DEX", "CON", "INT", "WIS", "CHA"];
let statMode = "rolled";
let pointBuyPoints = 27;

document.addEventListener("DOMContentLoaded", () => {
    const root = window.ROOT_PATH;  // defined globally in the HTML
    loadCharactersFromAPI(root);
    loadRacesForSelect(root);

    document.getElementById("btnNewChar").addEventListener("click", () => {
        // Show the form
        document.getElementById("charForm").classList.remove("hidden");

        // Hide character list
        const charList = document.getElementById("characterList");
        if (charList) charList.classList.add("hidden");

        // Reset name
        document.getElementById("charName").value = "";

        // Reset race select
        const raceSelect = document.getElementById("raceSelect");
        raceSelect.innerHTML = `<option disabled selected value="">Select a race</option>`;
        loadRacesForSelect();

        renderAbilityInputs(statMode);
    });

    document.querySelectorAll("#statModeTabs .nav-link").forEach(tab => {
        tab.addEventListener("click", function () {
            document.querySelectorAll("#statModeTabs .nav-link").forEach(t => t.classList.remove("active"));
            this.classList.add("active");
            statMode = this.dataset.mode;
            renderAbilityInputs(statMode);
        });
    });
});

function loadRacesForSelect() {
    fetch(root + "/api/races/get")
        .then(response => response.json())
        .then(data => {
            const select = document.getElementById("raceSelect");

            const options = data.race_list.map(r => {
                const sub = r.subrace ? ` (${r.subrace.name})` : "";
                return `<option value="${r.name}${sub ? ':' + r.subrace.name : ''}">${r.name}${sub}</option>`;
            });

            select.innerHTML += options.join("");
        });
}

function renderAbilityInputs(mode) {
    const container = document.getElementById("abilityInputArea");
    container.innerHTML = "";

    if (mode === "rolled") {
        const table = document.createElement("table");
        table.className = "table table-bordered";
        table.innerHTML = `
            <thead><tr><th>Ability</th><th>Score</th></tr></thead>
            <tbody>${ABILITIES.map(ab => `
                <tr>
                    <td>${ab}</td>
                    <td><input type="number" class="form-control ability-input" data-ab="${ab}" min="1" max="30" value="10"></td>
                </tr>`).join("")}
            </tbody>`;
        container.appendChild(table);
    }

    if (mode === "pointbuy") {
        pointBuyPoints = 27;

        const note = document.createElement("div");
        note.innerHTML = `<p><strong>Point Buy Mode</strong> – 27 points | 8–15 range</p><p>Remaining: <span id="pb-remaining">27</span></p>`;
        container.appendChild(note);

        const table = document.createElement("table");
        table.className = "table table-bordered";
        const body = document.createElement("tbody");

        for (const ab of ABILITIES) {
            const row = document.createElement("tr");
            row.innerHTML = `
                <td>${ab}</td>
                <td><input type="number" class="form-control pb-input" data-ab="${ab}" min="8" max="15" value="8"></td>
            `;
            body.appendChild(row);
        }

        table.appendChild(body);
        container.appendChild(table);

        document.querySelectorAll(".pb-input").forEach(input => {
            input.addEventListener("input", updatePointBuy);
        });

        updatePointBuy();
    }
}

function updatePointBuy() {
    const costTable = { 8: 0, 9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 7, 15: 9 };
    let used = 0;

    document.querySelectorAll(".pb-input").forEach(input => {
        const val = parseInt(input.value) || 8;
        used += costTable[Math.min(Math.max(val, 8), 15)];
    });

    pointBuyPoints = 27 - used;
    document.getElementById("pb-remaining").textContent = pointBuyPoints;
}

function submitNewCharacter() {
    const name = document.getElementById("charName").value.trim();
    if (!name) return alert("Please enter a character name.");

    const raceValue = document.getElementById("raceSelect").value;
    const [raceType, subraceName] = raceValue.split(":");
    const abilities = {};

    const selector = statMode === "rolled" ? ".ability-input" : ".pb-input";
    document.querySelectorAll(selector).forEach(input => {
        const ab = input.dataset.ab;
        const val = parseInt(input.value);
        if (!isNaN(val)) abilities[ab] = val;
    });

    const newChar = {
        name: name,
        race_type: raceType,
        subrace_name: subraceName || null,
        classes: [],
        abilities: abilities
    };

    saveCharacterToAPI(window.ROOT_PATH, newChar);
}