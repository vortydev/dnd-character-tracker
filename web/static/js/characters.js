function loadCharactersFromAPI(root) {
    fetch(root + "/api/characters/get")
        .then(response => {
            if (!response.ok) throw new Error("Network response was not ok");
            return response.json();
        })
        .then(data => {
            let charList = data.characters;
            console.log("Characters:", charList);
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

function saveCharacterToAPI(root, charData) {
    fetch(root + "/api/characters/save", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(charData)
    })
    .then(response => response.json())
    .then(data => {
        console.log("Save response:", data);
        if (data.status !== "success") alert("Save failed: " + data.message);
    })
    .catch(error => {
        console.error("Error saving character:", error);
        alert("Failed to save character.");
    });
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
