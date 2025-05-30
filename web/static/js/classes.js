function loadClassesFromAPI(root) {
    fetch(root+"/api/classes/get")
        .then(response => {
            if (!response.ok) throw new Error("Network response was not ok");
            return response.json();
        })
        .then(data => {
            let classList = data.class_list;
            let classLevels = data.level_list;
            prepareAndRenderClasses(classList, classLevels)
        })
        .catch(error => {
            console.error("Error loading classes:", error);
            alert("Failed to load classes.");
        });
}

function constructClassData(classList, classLevels) {
    const classData = {};
    console.log(classList, classLevels);
    

    // Load hit points and proficiencies
    for (const c of classList) {
        const cName = c.name;
        classData[cName] = { 
            "name": cName, 
            "info": {},  
            "hp": {}, 
            "prof": {}, 
            "levels": {} 
        };
        const curClass = classData[cName];

        // Info
        curClass.info["description"] = c.description;
        curClass.info["requisite"] = c.requisite;

        // Hit Points
        curClass.hp["dice"] = c.hit_dice;
        curClass.hp["hp_start"] = c.hp_1st_level;
        curClass.hp["hp_higher"] = c.fixed_hp_per_level;

        // Proficiencies
        curClass.prof["armor"] = c.proficiency_armor;
        curClass.prof["weapons"] = c.proficiency_weapons;
        curClass.prof["weapons2"] = c.proficiency_specific_weapons;
        curClass.prof["tools"] = c.proficiency_tools;
        curClass.prof["savingThrows"] = c.proficiency_saving_throws;
        curClass.prof["skills"] = c.proficiency_skill_pool;
        curClass.prof["skillChoices"] = c.skill_choices;
    }

    // Load class levels
    for (const cl of classLevels) {
        const cName = cl.class_type;
        const lvl = cl.level;
        const subclassKey = cl.subclass || "Base";

        if (!classData[cName]) continue;

        const curClass = classData[cName];

        if (!curClass.levels[subclassKey]) {
            curClass.levels[subclassKey] = {};
        }

        curClass.levels[subclassKey][lvl] = cl;
    }

    return classData;
}

function prepareAndRenderClasses(classList, classLevels) {
    // console.log("Classes",classList);
    // console.log("Class levels",classLevels);

    const container = document.getElementById("classContainer");
    if (!container) return;

    container.innerHTML = "";

    const classData = constructClassData(classList, classLevels);
    console.log("Class data:", classData);
    
    const classNames = Object.keys(classData);
    classNames.forEach((className, index) => {
        const block = renderClassData(classData[className]);
        container.innerHTML += block;

        // Add <hr> after each block except the last
        if (index < classNames.length - 1) {
            container.innerHTML += `<hr>`;
        }
    });
}

function renderClassData(classData) {
    console.log("Current class", classData);
    const cName = classData.name;

    // TODO Summary table
    
    // Hit points
    const hp = classData.hp;
    const hpBlock = `
    <div class="dnd-feature hp-block">
        <h5>Hit Points</h5>
        <ul class="dnd-feature-list">
            <li><strong>Hit Dice :</strong> 1d${hp.dice} per ${cName.toLowerCase()} level</li>
            <li><strong>Hit Points at 1st Level :</strong> ${hp.hp_start} + your Consitution modifier</li>
            <li><strong>Hit Points at Higher Levels :</strong> 1d${hp.dice} (or ${hp.hp_higher}) + your Constitution modifier per fighter level after 1st</li>
        </ul>
    </div>
    `;

    // Proficiencies
    const prof = classData.prof;

    const armorStr = prof.armor
    ? Object.values(prof.armor)
        .map(item => {
            const lower = item.toLowerCase();
            return lower === "shield" ? "shields" : `${lower} armors`;
        })
        .join(", ")
    : "None";

    const weaponsArr = [];
    if (prof.weapons && prof.weapons.length) {
        weaponsArr.push(
            ...prof.weapons.map(w => `${w.toLowerCase()} weapons`)
        );
    }
    if (prof.weapons2 && prof.weapons2.length) {
        weaponsArr.push(
            ...prof.weapons2.map(w => w)
        );
    }
    const weaponStr = weaponsArr.length > 0 ? weaponsArr.join(", ") : "None";
    
    const savingThrowsStr = prof.savingThrows
    ? Object.values(prof.savingThrows)
        .map(item => {
            const upper = item.toUpperCase();
            return `<em>${upper}</em>`;
        })
        .join(", ")
    : "None";

    const skillsStr = prof.skills
    ? Object.values(prof.skills)
        .join(", ")
    : "None";

    const profBlock = `
    <div class="dnd-feature prof-block">
        <h5>Proficiencies</h5>
        <ul class="dnd-feature-list">
            <li><strong>Armor :</strong> ${armorStr}</li>
            <li><strong>Weapons :</strong> ${weaponStr}</li>
            <li><strong>Saving Throws :</strong> ${savingThrowsStr}</li>
            <li><strong>Skills :</strong> Choose ${prof.skillChoices} skills from ${skillsStr}</li>
        </ul>
    </div>
    `;

    // LATER Equipment

    const classFeatures = `
    <details id="${cName.toLowerCase()}Features" class="mt-3" open>
        <summary><h3 class="section-title-black">Class Features</h3></summary>
        <section class="class-features">
            <p class="dnd-feature-desc mt-2">As a ${cName.toLowerCase()}, you gain the following features.</p>
            <div class="grid-auto mt-3">
                ${hpBlock}
                ${profBlock}
            </div>
        </section>
    </details>
    `;

    const baseLevels = classData.levels?.Base || {};
    const levelFeatureBlocks = renderLevelBlocks(baseLevels, cName);
    const classLevelSection = `
    <hr>
    <details id="${cName.toLowerCase()}Levels" open>
        <summary><h3 class="section-title-black">Class Levels</h3></summary>
        <section class="class-levels grid-auto mt-3">
            ${levelFeatureBlocks}
        </section>
    </details>
    `;

    let subclassBlocks = "";
    for (const subclassKey in classData.levels) {
        if (subclassKey === "Base") continue;

        const subclassLevels = classData.levels[subclassKey];
        const subclassName = subclassKey;

        const rendered = renderLevelBlocks(subclassLevels, cName, true, true);
        if (!rendered) continue;

        subclassBlocks += `
        <hr>
        <details id="${cName.toLowerCase()}-${subclassName.toLowerCase()}Levels">
            <summary><h3 class="section-title-black">${subclassName} Levels</h3></summary>
            <section class="class-subclass-levels grid-auto mt-3">
                ${rendered}
            </section>
        </details>`;
    }
    
    const classBlock = `
    <details id="${cName.toLowerCase()}" class="dnd-feature-section" open>
        <summary><h2 class="section-title">${cName}</h2></summary>
        ${classData.info.description ? `<i class="dnd-feature-desc text-bold mt-2">${classData.info.description}</i>` : ""}
        ${classData.info.requisite ? `<i class="dnd-feature-desc mt-2">${classData.info.requisite}</i>` : ""}
        ${classFeatures}
        ${classLevelSection}
        ${subclassBlocks}
    </details>
    `;

    return applyTextFormatting(classBlock);
}

function renderLevelBlocks(levels, cName, subclass = false, skipEmpty = false) {
    const levelBlocks = [];

    const maxLevel = 20;
    const levelsToRender = skipEmpty
        ? Object.keys(levels).map(Number).sort((a, b) => a - b)
        : Array.from({ length: maxLevel }, (_, i) => i + 1);

    for (const lvl of levelsToRender) {
        const entry = levels[lvl];

        let featuresPart = "";
        let spellsPart = "";

        // Features
        if (entry?.features?.length) {
            const featureList = entry.features.map(f => {
                const url = `/features?type=class&class=${cName}&name=${formatObjectNameForURL(f)}`;
                return `<li><a href="${url}">${f}</a></li>`;
            }).join("");

            featuresPart = `
            <div class="dnd-feature">
                <h5 class="dnd-feature-name">Features</h5>
                <ul class="dnd-feature-list">${featureList}</ul>
            </div>`;
        }

        // Spells
        if (entry && (entry.known_cantrips > 0 || entry.known_spells > 0)) {
            const spellList = [];

            if (entry.known_cantrips > 0) {
                spellList.push(`<li>Cantrips known : ${entry.known_cantrips}</li>`);
            }
            if (entry.known_spells > 0) {
                spellList.push(`<li>Spells known : ${entry.known_spells}</li>`);
            }

            spellsPart = `
            <div class="dnd-feature">
                <h5 class="dnd-feature-name">Spellcasting</h5>
                <ul class="dnd-feature-list">${spellList.join("")}</ul>
            </div>`;
        }

        const separator = featuresPart && spellsPart ? '<hr class="mt-3 mb-3">' : '';
        const content = featuresPart || spellsPart
            ? `${featuresPart}${separator}${spellsPart}`
            : (skipEmpty ? "" : `<p class="dnd-feature-desc text-center text-color-grey"><em>No new features or spells at this level.</em></p>`);

        if (skipEmpty && !content) continue;

        const levelBlock = `
        <div class="dnd-subfeatures level-block">
            <h4 class="section-title feature-context text-center text-bold mb-2">Level ${lvl}</h4>
            <div>${content}</div>
        </div>`;

        levelBlocks.push(levelBlock);
    }

    return levelBlocks.join("\n");
}