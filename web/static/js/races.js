function loadRacesFromAPI() {
    fetch("/api/races/get")
        .then(response => {
            if (!response.ok) throw new Error("Network response was not ok");
            return response.json();
        })
        .then(data => {
            let raceList = data.race_list;
            let spellsRef = data.spells_ref;
            console.log(spellsRef);
            
            prepareAndRenderRaces(raceList, spellsRef);
        })
        .catch(error => {
            console.error("Error loading races:", error);
            alert("Failed to load races.");
        });
}

function prepareAndRenderRaces(raceList, spellsRef) {
    console.log("Race list:", raceList);
    
    const container = document.getElementById("raceContainer");
    if (!container) return;

    container.innerHTML = "";

    const raceMap = {};
    const subraceMap = {};

    // Iterate the list of races
    for (const race of raceList) {
        const raceName = race.name;

        if (race.subrace) {
            // Insert the first occurence of the race
            if (!raceMap[raceName]) {
                let baseRace = structuredClone(race);
                delete baseRace.subrace;
                raceMap[raceName] = baseRace;
            }
            
            if (!subraceMap[raceName]) subraceMap[raceName] = [];
            subraceMap[raceName].push(race);
        } 
        else {
            raceMap[raceName] = race;
        }
    }

    for (const raceName of Object.keys(raceMap)) {
        const baseRace = raceMap[raceName];
        const subraces = subraceMap[raceName] || [];

        const block = renderRaceGroup(baseRace, subraces, spellsRef);
        container.innerHTML += block;
    }
}

function renderRaceGroup(baseRace, subraces, spellsRef) {
    const mainRaceBlock = renderRaceCard(baseRace, spellsRef);

    const subraceBlocks = subraces.map(race => {
        let subraceBlock = `
        <details class="subrace-block mt-3">
            <summary><h3 class="section-title">${race.subrace.name}</h3></summary>
            ${renderSubraceCard(race, spellsRef)}
        </details>
        `;
        return subraceBlock;
    }).join("");

    const raceBlock = `
    <details class="dnd-feature-section" open>
        <summary><h2 class="section-title underline-primary">${baseRace.name}</h2></summary>
        ${baseRace.description ? `<i class="dnd-feature-desc mt-2">${baseRace.description}</i>` : ""}
        ${mainRaceBlock}
        ${subraceBlocks}
    </details>
    `;


    return raceBlock;
}

function renderRaceCard(race, spellsRef) {
    const asi = Object.entries(race.ability_score_increase || {})
        .map(([k, v]) => `${k.toUpperCase()} +${v}`)
        .join(", ");

    const languages = (race.languages || []).join(", ");

    const infoHtml = Object.entries(race.info || {})
        .map(([k, v]) => `<li><strong>${k} :</strong> ${v}</li>`)
        .join("");

    // TODO Speed, Size, Features, Spells
    const features = Object.entries(race.feats || {}).map(([lvl, list]) =>
        list.length ? `<li><strong>Level ${lvl} :</strong> ${list.join(", ")}</li>` : ""
    ).join("");

    const spells = getLinkedSpellList(race.spells, spellsRef);

    let raceInfo = `
    <section class="dnd-feature race-info">
        <h4 class="dnd-feature-name">Details</h4>
        <ul>
            ${asi ? `<li><strong>Ability Score Increase:</strong> ${asi}</li>` : ""}
            ${infoHtml}
            ${race.size ? `<li><strong>Size :</strong> ${race.size}</li>` : ""}
            ${race.speed ? `<li><strong>Speed :</strong> ${race.speed}</li>` : ""}
            ${languages ? `<li><strong>Languages :</strong> ${languages}</li>` : ""}
        </ul>
    </section>

    ${features ? `<section class="dnd-feature"><h4 class="dnd-feature-name">Features</h4><ul>${features}</ul></section>` : ""}
    ${spells ? `<section class="dnd-feature"><h4 class="dnd-feature-name">Spells</h4>${spells}</section>` : ""}
    `;

    let raceSection = `
    
    `;

    return raceInfo;
}

function renderSubraceCard(race, spellsRef) {
    const sub = race.subrace;
    const asi = Object.entries(sub?.ability_score_increase || {})
        .map(([k, v]) => `${k} +${v}`)
        .join(", ");

    const lore = sub?.info?.Lore ? `<p><strong>Lore:</strong> ${sub.info.Lore}</p>` : "";

    const features = Object.entries(race.feats || {}).map(([lvl, list]) =>
        list.length ? `<li><strong>Level ${lvl}:</strong> ${list.join(", ")}</li>` : ""
    ).join("");

    const spells = Object.entries(race.spells || {}).map(([lvl, list]) =>
        list.length ? `<li><strong>Level ${lvl}:</strong> ${list.join(", ")}</li>` : ""
    ).join("");

    let subraceInfo =  `
    <section class="subrace-info">
        ${lore}
        ${asi ? `<p><strong>Ability Score Increase:</strong> ${asi}</p>` : ""}
    </section>

    ${features ? `<section class="subrace-features"><h4>Features</h4><ul>${features}</ul></section>` : ""}
    ${spells ? `<section class="subrace-spells"><h4>Spells</h4><ul>${spells}</ul></section>` : ""}
    `;

    return subraceInfo;
}

function getLinkedSpellList(spellMap, spellsRef) {
    if (!spellMap || typeof spellMap !== 'object') return "";

    const spellSection = Object.entries(spellMap).map(([level, spellList]) => {
        if (!spellList.length) return "";

        const spellLinks = spellList.map(spellName => {
            console.log("Spell name:", spellName);
            
            const refLevel = findSpellLevelInRefs(spellName, spellsRef);
            const url = `/spells?level=${refLevel}&spell=${formatObjectNameForURL(spellName)}`;
            return `<a href="${url}">${spellName}</a>`;
        }).join(", ");

        const label = parseInt(level) === 0 ? "You know:" : `Level ${level}:`;
        return `<li><strong>${label}</strong> ${spellLinks}</li>`;
    }).join("");

    return `<ul class="spell-list">${spellSection}</ul>`;
}

function findSpellLevelInRefs(spellName, spellsRef) {
    for (const [level, list] of Object.entries(spellsRef)) {
        if (list.includes(spellName)) return level;
    }
    return "0"; // fallback
}


// TODO
function buildFeaturesPerLevel(data) {
    return data;
}