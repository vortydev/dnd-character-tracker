function loadRacesFromAPI(root) {
    fetch(root+"/api/races/get")
        .then(response => {
            if (!response.ok) throw new Error("Network response was not ok");
            return response.json();
        })
        .then(data => {
            let raceList = data.race_list;
            let spellsRef = data.spells_ref;
            prepareAndRenderRaces(raceList, spellsRef);
        })
        .catch(error => {
            console.error("Error loading races:", error);
            alert("Failed to load races.");
        });
}

function prepareAndRenderRaces(raceList, spellsRef) {    
    const container = document.getElementById("raceContainer");
    if (!container) return;

    container.innerHTML = "";

    const raceMap = {};
    const subraceMap = {};

    // Iterate the list of races
    for (const race of raceList) {
        const raceName = race.name;

        if (race.subrace) {            
            if (!subraceMap[raceName]) subraceMap[raceName] = [];
            subraceMap[raceName].push(race);
        } 
        else {
            raceMap[raceName] = race;
        }
    }

    const raceNames = Object.keys(raceMap);
    raceNames.forEach((raceName, index) => {
        const baseRace = raceMap[raceName];
        const subraces = subraceMap[raceName] || [];

        const block = renderRaceGroup(baseRace, subraces, spellsRef);
        container.innerHTML += block;

        // Add <hr> after each block except the last
        if (index < raceNames.length - 1) {
            container.innerHTML += `<hr>`;
        }
    });
}

function renderRaceGroup(baseRace, subraces, spellsRef) {
    const mainRaceBlock = renderRaceCard(baseRace, spellsRef);

    const subraceBlocks = subraces.map(race => {
        let subraceBlock = `
        <details class="subrace-block feature-context-group">
            <summary><h4 class="section-title feature-context">${race.subrace.name}</h4></summary>
            ${renderSubraceCard(race, spellsRef)}
        </details>`;
        return subraceBlock;
    }).join("<hr>");

    const subraceSection = `
    <div class="dnd-feature">
        <h3 class="dnd-feature-name">Subraces</h3>
        ${subraceBlocks}
    </div>`;

    const raceBlock = `
    <details class="dnd-feature-section" open>
        <summary><h2 class="section-title underline-primary">${baseRace.name}</h2></summary>
        ${mainRaceBlock}
        ${Object.keys(subraces).length ? subraceSection : ''}
    </details>`;

    return raceBlock;
}

function renderRaceCard(race, spellsRef) {
    const asi = Object.entries(race.ability_score_increase || {})
        .map(([k, v]) => `${k.toUpperCase()} +${v}`)
        .join(", ");

    const languages = (race.languages || []).join(", ");

    const infoHtml = Object.entries(race.info || {})
        .map(([k, v]) => `<li><strong>${k} :</strong> ${applyTextFormatting(v)}</li>`)
        .join("");

    const features = race.feats ? getFeatureList(race.feats) : "";
    const spells = race.spells ? getLinkedSpellList(race.spells, spellsRef) : "";

    let subFeats = `
        ${features || spells ? `
        <section class="dnd-subfeatures grid-auto">
            ${features ? `<div class="dnd-feature"><h4 class="dnd-feature-name">Features</h4>${features}</div>` : ""}
            ${spells ? `<div class="dnd-feature"><h4 class="dnd-feature-name">Spells</h4>${spells}</div>` : ""}
        </section>
        ` : ""}
    `;

    let raceInfo = `
    ${race.description ? `<i class="dnd-feature-desc mt-2">${race.description}</i>` : ""}
    <section class="dnd-feature race-info">
        <ul class="dnd-feature-list">
            ${asi ? `<li><strong>Ability Score Increase:</strong> ${asi}</li>` : ""}
            ${infoHtml}
            ${race.size ? `<li><strong>Size :</strong> ${race.size}</li>` : ""}
            ${race.speed ? `<li><strong>Speed :</strong> ${race.speed} feet</li>` : ""}
            ${languages ? `<li><strong>Languages :</strong> ${languages}</li>` : ""}
        </ul>
    </section>
    ${subFeats}
    `;

    return raceInfo;
}

function renderSubraceCard(race, spellsRef) {    
    const sub = race.subrace;

    const asi = Object.entries(sub?.ability_score_increase || {})
        .map(([k, v]) => `${k.toUpperCase()} +${v}`)
        .join(", ");

    const infoHtml = Object.entries(sub.info || {})
        .map(([k, v]) => `<li><strong>${k} : </strong> ${applyTextFormatting(v)}</li>`)
        .join("");

    const features = race.feats ? getFeatureList(sub.feats) : "";
    const spells = sub.spells ? getLinkedSpellList(sub.spells, spellsRef) : "";

    let subFeats = `
        ${features || spells ? `
        <section class="dnd-subfeatures grid-auto">
            ${features ? `<div class="dnd-feature subrace-features"><h5>Features</h5>${features}</div>` : ""}
            ${spells ? `<div class="dnd-feature subrace-spells"><h5>Spells</h5>${spells}</div>` : ""}
        </section>
        ` : ""}
    `;

    let subraceInfo =  `
    ${sub.description ? `<i class="dnd-feature-desc mt-2">${sub.description}</i>` : ""}
    <section class="dnd-feature subrace-info">
        <ul>
            ${asi ? `<li><strong>Ability Score Increase:</strong> ${asi}</li>` : ""}
            ${infoHtml}
        </ul>
    </section>
    ${subFeats}
    `;

    return subraceInfo;
}

function getLinkedSpellList(spellMap, spellsRef) {
    if (!spellMap || typeof spellMap !== 'object') return "";
    
    if (Object.keys(spellMap).length === 0) return "";

    const spellSection = Object.entries(spellMap).map(([level, spellList]) => {
        if (!spellList.length) return "";

        const spellLinks = spellList.map(spellName => {            
            const refLevel = findSpellLevelInRefs(spellName, spellsRef);
            const url = `/spells?level=${refLevel}&spell=${formatObjectNameForURL(spellName)}`;
            return `<a href="${url}">${spellName}</a>`;
        }).join(", ");

        const label = parseInt(level) === 0 ? "You know:" : `Level ${level}:`;
        return `<li><strong>${label}</strong> ${spellLinks}</li>`;
    }).join("");

    return `<ul class="dnd-feature-list">${spellSection}</ul>`;
}

function findSpellLevelInRefs(spellName, spellsRef) {
    for (const [level, list] of Object.entries(spellsRef)) {
        if (list.includes(spellName)) return level;
    }
    return "0"; // fallback
}

function getFeatureList(featsMap) {
    if (!featsMap || typeof featsMap !== 'object') return "";
    if (Object.keys(featsMap).length === 0) return "";
    const features = getLinkedFeatureList(featsMap, "race");
    return features;
}

function getLinkedFeatureList(featuresMap, featType) {
    if (!featuresMap || typeof featuresMap !== 'object') return "";

    const featureSection = Object.entries(featuresMap).map(([level, featureList]) => {
        if (!featureList.length) return "";

        const links = featureList.map(name => {
            const url = `/features?type=${featType}&name=${formatObjectNameForURL(name)}`;
            return `<a href="${url}">${name}</a>`;
        }).join(", ");

        return `<li><strong>Level ${level} :</strong> ${links}</li>`;
    }).join("");

    return `<ul class="dnd-feature-list">${featureSection}</ul>`;
}
