/**
 * Delay the execution of a function
 * @param {*} func Function to run with a delay
 * @param {Number} delay Amount of delay (ms)
 * @returns 
 */
function debounce(func, delay) {
    let timeout;
    return function(...args) {
        clearTimeout(timeout);
        timeout = setTimeout(() => func.apply(this, args), delay);
    };
}

/**
 * Find an HTML element by its data
 * @param {String} key Dataset key
 * @param {String} value Dataset value
 * @returns 
 */
function findByData(key, value) {
    return document.querySelector(`[data-${key}="${value}"]`);
}

/**
 * Toggles the visibility of an HTML element
 * @param {HTMLElement} el Element to show or hide
 * @param {Boolean} state `true` shows the element, `false` hides the element
 * @param {String} className Name of the class to toggle. "hidden" by default
 * @returns 
 */
function showElem(el, state, className = "hidden") {
    if (!el) return;
    state ? el.classList.remove(className) : el.classList.add(className);
}

/**
 * Open a `details` HTML element if it has content
 * @param {HTMLDetailsElement} container Element to open
 * @param {Number} delayMs Amount of delay (ms) before opening the element
 * @param {String} resourceType
 * @returns 
 */
function openIfHasContent(container, delayMs = 0, resourceType) {
    const details = container.closest("details");
    if (!details) return;

    const hasContent = container.innerHTML.trim() !== "" &&
                       !container.innerHTML.includes(`No ${resourceType} available`);

    if (hasContent) {
        setTimeout(() => {
            details.setAttribute("open", "");
        }, delayMs);
    }
}


function applyTextFormatting(text) {
    if (!text) return "";

    text = applyBoldFormatting(text);
    text = applyItalicFormatting(text);

    // Highlights
    text = highlightDamageTypes(text);
    text = highlightAdvantage(text);
    text = hightlightHealingTerms(text);
    text = highlightResistanceTerms(text);
    text = highlightCurrency(text);

    return text;
}

function applyBoldFormatting(text) {
    return text.replace(/BOLD\[(.+?)\]/g, (_, boldText) => {
        return `<strong>${boldText}</strong>`;
    });
}

function applyItalicFormatting(text) {
    return text.replace(/ITALIC\[(.+?)\]/g, (_, italicText) => {
        return `<em>${italicText}</em>`;
    });
}

/**
 * Highlights dice damage, damage types and other keywords in the string
 * @param {String} text String to analyse and highlight keywords in
 * @returns {String}
 */
function highlightDamageTypes(text) {
    const damageTypes = [
        "acid", "bludgeoning", "cold", "fire", "force", "lightning", "necrotic",
        "piercing", "poison", "psychic", "radiant", "slashing", "thunder"
    ];
    const typeGroup = damageTypes.join("|");

    // 1. Dice + Type + "damage"
    text = text.replace(
        new RegExp(`(\\s*)(\\d+d\\d+|\\d+)\\s+(${typeGroup})\\s+damage\\b`, "gi"),
        (match, leading, dice, type) => {
            const lower = type.toLowerCase();
            return `${leading}<span class="damage-${lower}"><span class="damage-dice damage-${lower}">${dice}</span> ${type} damage</span>`;
        }
    );

    // 2. Dice + Type (without "damage")
    text = text.replace(
        new RegExp(`(\\s*)(\\d+d\\d+|\\d+)\\s+(${typeGroup})(?!\\s+damage)\\b`, "gi"),
        (match, leading, dice, type) => {
            const lower = type.toLowerCase();
            return `${leading}<span class="damage-${lower}"><span class="damage-dice damage-${lower}">${dice}</span> ${type}</span>`;
        }
    );

    // 3. Type + "damage" (not preceded by dice)
    text = text.replace(
        new RegExp(`(\\s*)\\b(${typeGroup})\\s+damage\\b`, "gi"),
        (match, leading, type) => {
            const lower = type.toLowerCase();
            return `${leading}<span class="damage-${lower}">${type} damage</span>`;
        }
    );

    // 4. Dice only (skip if already wrapped)
    text = text.replace(/\b(\d+d\d+)\b/g, (match) => {
        return text.includes(`>${match}<`) ? match : `<span class="damage-dice">${match}</span>`;
    });

    // 5. Post-process: Highlight adjacent types via comma/or/and
    text = text.replace(
        new RegExp(
            `(<span class="damage-(${typeGroup})">.*?</span>)(\\s*(?:,|and|or)\\s*)\\b(${typeGroup})\\b(?![^<]*>)`, 
            "gi"
        ),
        (match, firstSpan, firstType, separator, secondType) => {
            const lower = secondType.toLowerCase();
            return `${firstSpan}${separator}<span class="damage-${lower}">${secondType}</span>`;
        }
    );

    return text;
}


/**
 * Highlight Advantage and Disadvantage keywords in a string
 * @param {String} text String to analyse and highlight keywords in
 * @returns {String}
 */
function highlightAdvantage(text) {
    text = text.replace(/\badvantage\b/gi, '<span class="advantage">Advantage</span>');
    text = text.replace(/\bdisadvantage\b/gi, '<span class="disadvantage">Disadvantage</span>');
    return text;
}

/**
 * Highlight healing terms in a string
 * @param {String} text String to highlight keywords in
 * @returns {String}
 */
function hightlightHealingTerms(text) {
    const healingTerms = [
        "healing", "regains hit points", "regain hit points", "regain hp", "regains hp", "temporary hit points"
    ];

    healingTerms.forEach(term => {
        // Capture leading whitespace and an optional dice/number before the term
        const regex = new RegExp(`(\\s*)(\\d+d\\d+|\\d+)?\\s*\\b(${term})\\b`, "gi");

        text = text.replace(regex, (match, leadingSpace, dice, keyword) => {
            const diceSpan = dice ? `<span class="healing-dice">${dice}</span> ` : "";
            return `${leadingSpace}<span class="healing">${diceSpan}${keyword}</span>`;
        });
    });

    return text;
}

/**
 * Highlight resistance terms in a string
 * @param {String} text String to highlight keywords in
 * @param {Array} damageTypes List of damage types
 * @returns {String}
 */
function highlightResistanceTerms(text) {
    const statusKeywords = [
        { keywords: ["resistance", "resistant"], key: "resistance", emoji: "🛡️" },
        { keywords: ["immune", "immunity"], key: "immune", emoji: "🚫" },
        { keywords: ["vulnerable", "vulnerability"], key: "vulnerable", emoji: "💥" }
    ];

    const flatKeywords = statusKeywords.flatMap(entry => entry.keywords);
    const keywordRegex = new RegExp(`\\b(${flatKeywords.join("|")})\\b(?=\\s+\\S)`, "gi");

    return text.replace(keywordRegex, (match, rawStatus) => {
        const entry = statusKeywords.find(e => e.keywords.includes(rawStatus.toLowerCase()));
        if (!entry) {
            // console.log(`[🔴 Error] Could not resolve status for: "${rawStatus}"`);
            return match;
        }

        // console.log(`[✅ Match] ${rawStatus}`);
        return `<span class="${entry.key}">${entry.emoji}${rawStatus}</span>`;
    });
}

/**
 * Highlight currencies in a string
 * @param {String} text String to highlight keywords in
 * @returns {String}
 */
function highlightCurrency(text) {
    text = text.replace(
        /\b((?:\d{1,3}(?:[ ,.]?\d{3})*|\d+(?:[.,]\d+)?))\s*gp\b/gi,
        (match, value) => `<span class="currency-gold">${value} gp</span>`
    );
    return text;
}

function formatObjectNameForURL(str) {
    return str.replace(/[^\w-]/g, "_").toLowerCase();
}

/**
 * Build a string for proficiencies
 * @param {String} profType "armor", "weapon", "savingThrows", "skills"
 * @param {Array} profList List of proficiency elements
 * @param {Array} optProfList Optional second list of proficiency elements
 */
function buildProficiencyStr(profType, profList, optProfList) {
    if (profType == "armor") {
         const armorStr = profList
        ? Object.values(profList)
            .map(item => {
                const lower = item.toLowerCase();
                return lower === "shield" ? "shields" : `${lower} armors`;
            })
            .join(", ")
        : "None";
        return armorStr;
    }
    else if (profType == "weapon") {
        const weaponsArr = [];
        if (profList && profList.length) {
            weaponsArr.push(
                ...profList.map(w => `${w.toLowerCase()} weapons`)
            );
        }
        if (optProfList && optProfList.length) {
            weaponsArr.push(
                ...optProfList.map(w => w)
            );
        }
        const weaponStr = weaponsArr.length > 0 ? weaponsArr.join(", ") : "None";
        return weaponStr;
    }
    else if (profType == "skills") {
        const skillsStr = profList
        ? Object.values(profList)
            .join(", ")
        : "None";
        return skillsStr;
    }
    else if (profType == "savingThrows") {
        const savingThrowsStr = profList
        ? Object.values(profList)
            .map(item => {
                const upper = item.toUpperCase();
                return `<em>${upper}</em>`;
            })
            .join(", ")
        : "None";
        return savingThrowsStr;
    }
    return '<em>Not a valid profType!</em>';
}

function levelStr(level) {
    if (level == 1) {
        return "1st";
    }
    else if (level == 2) {
        return "2nd";
    }
    else {
        return `${level}th`;
    }
}

function insertChevronsIntoDetailsFA() {
    console.log("🔧 Inserting chevrons into <details.fa-chevron> blocks...");

    const detailsList = document.querySelectorAll("details.fa-chevron");

    detailsList.forEach(detailsEl => {
        console.log(detailsEl);
        
        const summary = detailsEl.querySelector("summary");
        if (!summary) {
            console.warn("⚠️ No <summary> found in:", detailsEl);
            return;
        }

        // Avoid duplicating
        if (summary.querySelector(".summary-content")) {
            console.log("⏭️ Already processed:", summary);
            return;
        }

        console.log("✅ Processing:", summary);

        // Remove ::before content fallback (e.g. emoji/arrow icon via inline span or old node)
        [...summary.childNodes].forEach(child => {
            if (child.nodeType === Node.TEXT_NODE && child.textContent.trim() === "") return;
            if (child.nodeType === Node.ELEMENT_NODE && child.tagName === "SPAN" && child.classList.contains("fallback-icon")) {
                console.log("🗑️ Removing fallback icon:", child);
                summary.removeChild(child);
            }
        });

        // Create wrapper
        const wrapper = document.createElement("div");
        wrapper.classList.add("summary-content");

        // Move children into wrapper
        while (summary.firstChild) {
            wrapper.appendChild(summary.firstChild);
        }

        // Create chevron icon
        const chevron = document.createElement("i");
        chevron.className = "fas fa-chevron-down chevron-icon";
        wrapper.appendChild(chevron);

        summary.appendChild(wrapper);

        console.log("✅ Chevron inserted!");
    });

    console.log("✅ Done processing all <details.fa-chevron> blocks.");
}


