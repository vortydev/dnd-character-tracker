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

/**
 * Highlights dice damage, damage types and other keywords in the string
 * @param {String} text String to analyse and highlight keywords in
 * @returns {String}
 */
function highlightDamageTypes(text) {
    if (!text) return "";

    const damageTypes = [
        "acid", "bludgeoning", "cold", "fire", "force", "lightning", "necrotic",
        "piercing", "poison", "psychic", "radiant", "slashing", "thunder"
    ];

    // Match any damage format: "1d8 cold damage", "5 fire damage", "cold damage"
    const fullDamageRegex = new RegExp(
        `(\\s*)(\\b(?:\\d+d\\d+|\\d+)?\\s*(${damageTypes.join("|")})(\\s+damage))`,
        "gi"
    );

    text = text.replace(fullDamageRegex, (match, leadingSpace, fullMatch, type) => {
        const typeLower = type.toLowerCase();
        const valueMatch = fullMatch.match(/\b(\d+d\d+|\d+)\b/);
        const value = valueMatch ? valueMatch[1] : null;

        if (value) {
            const valueSpan = `<span class="damage-dice damage-${typeLower}">${value}</span>`;
            const typeText = fullMatch.replace(value, "").trim();
            return `${leadingSpace}<span class="damage-${typeLower}">${valueSpan} ${typeText}</span>`;
        } else {
            return `${leadingSpace}<span class="damage-${typeLower}">${fullMatch.trim()}</span>`;
        }
    });

    // Highlight standalone dice (if not already wrapped)
    text = text.replace(/\b(\d+d\d+)\b/g, (match) => {
        return text.includes(`>${match}<`) ? match : `<span class="damage-dice">${match}</span>`;
    });

    // Highlight advantage / disadvantage
    text = highlightAdvantage(text);

    // Highlight healing terms
    text = hightlightHealingTerms(text);

    // Highlight vulnerabilies, resistances and immunities
    text = highlightResistanceTerms(text, damageTypes);

    // Highlight currencies
    text = highlightCurrency(text);

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
function highlightResistanceTerms(text, damageTypes) {
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