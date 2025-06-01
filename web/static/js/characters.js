// characters.js
function loadCharactersFromAPI(root) {
    fetch(root + "/api/characters/get")
        .then(response => {
            if (!response.ok) throw new Error("Network response was not ok");
            return response.json();
        })
        .then(data => {
            let charList = data.characters;
            console.log("Characters:", charList);
            renderCharacterList(charList);
        })
        .catch(error => {
            console.error("Error loading characters:", error);
            alert("Failed to load characters.");
        });
}

function loadCharacterByName(root, name) {
    fetch(root + `/api/characters/${encodeURIComponent(name)}`)
        .then(response => {
            if (!response.ok) throw new Error("Character not found");
            return response.json();
        })
        .then(data => {
            console.log("Character:", data);
        })
        .catch(error => {
            console.error("Error loading character:", error);
            alert("Failed to load character.");
        });
}

function submitNewCharacter() {
    const name = document.getElementById("charName").value.trim();
    const raceValue = document.getElementById("raceSelect").value;
    const abilities = {};

    if (!name) {
        alert("Please enter a character name.");
        return;
    }

    if (!raceValue) {
        alert("Please select a race.");
        return;
    }

    const selector = statMode === "rolled" ? ".ability-input" : ".pb-input";
    let missingStat = false;

    document.querySelectorAll(selector).forEach(input => {
        const ab = input.dataset.ab;
        const val = parseInt(input.value);
        if (isNaN(val)) missingStat = true;
        else abilities[ab] = val;
    });

    if (missingStat || Object.keys(abilities).length !== 6) {
        alert("Please fill in all ability scores.");
        return;
    }

    const [raceType, subraceName] = raceValue.split(":");

    const newChar = {
        name: name,
        race_type: raceType,
        subrace_name: subraceName || null,
        classes: [],
        abilities: abilities
    };

    saveCharacterToAPI(root, newChar);
}

function deleteCharacterFromAPI(root, name) {
    fetch(root + `/api/characters/delete/${encodeURIComponent(name)}`, {
        method: "DELETE"
    })
    .then(response => response.json())
    .then(data => {
        console.log("Delete response:", data);
        if (data.status !== "success") alert("Delete failed: " + data.message);
    })
    .catch(error => {
        console.error("Error deleting character:", error);
        alert("Failed to delete character.");
    });
}

function renderCharacterList(characters) {
    const container = document.getElementById("characterList");
    container.innerHTML = "";  // Clear existing content

    if (!characters || characters.length === 0) {
        container.innerHTML = "<p>No characters found.</p>";
        return;
    }

    characters.forEach(char => {
        const card = document.createElement("div");
        card.className = "col-sm-6 col-md-4 col-lg-3";

        const raceLine = char.subrace_name
            ? `${char.subrace_name} (${char.race_type})`
            : char.race_type;

        const ABILITY_ORDER = ["STR", "DEX", "CON", "INT", "WIS", "CHA"];
        const abilities = ABILITY_ORDER
            .filter(ab => char.abilities && ab in char.abilities)
            .map(ab => `<span class="badge bg-dark-grey">${ab} : ${char.abilities[ab]}</span>`)
            .join(" ");

        card.innerHTML = `
            <div class="card h-100 character-card shadow">
                <div class="card-body d-flex flex-column">
                    <h4 class="card-title text-center mb-2">${char.name}</h4>
                    <p class="card-subtitle text-muted mb-2">${raceLine}</p>
                    <div class="char-card-ability-grid mb-3">${abilities}</div>
                    <button class="btn btn-outline-primary mt-auto" onclick="loadCharacterByName(root, '${char.name}')">
                        View
                    </button>
                </div>
            </div>
        `;

        container.appendChild(card);
    });
}
