function debounce(func, delay) {
    let timeout;
    return function(...args) {
        clearTimeout(timeout);
        timeout = setTimeout(() => func.apply(this, args), delay);
    };
}

function findByData(key, value) {
    return document.querySelector(`[data-${key}="${value}"]`);
}

function showElem(el, state, className = "hidden") {
    if (!el) return;
    state ? el.classList.remove(className) : el.classList.add(className);
}

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

function highlightDamageTypes(text) {
    if (!text) return "";

    const damageTypes = [
        "acid", "bludgeoning", "cold", "fire", "force", "lightning", "necrotic",
        "piercing", "poison", "psychic", "radiant", "slashing", "thunder"
    ];

    const healingTerms = [
        "healing", "regains hit points", "regain hit points", "regain hp", "regains hp"
    ];

    // Normalize status keywords
    const statusMap = {
        "resistant": "resistance",
        "resistance": "resistance",
        "immune": "immune",
        "vulnerable": "vulnerable"
    };

    // Match: 1d8 fire damage or 2d6 necrotic, etc.
    const comboRegex = new RegExp(
        `(\\b\\d+d\\d+\\b)\\s+(${damageTypes.join("|")})(\\s+damage)?`,
        "gi"
    );

    // Highlight full expressions like "1d8 cold damage"
    text = text.replace(comboRegex, (match, dice, type, damageWord) => {
        const typeLower = type.toLowerCase();
        const typeSpan = `<span class="damage-${typeLower}">${type}</span>`;
        const diceSpan = `<span class="damage-dice damage-${typeLower}">${dice}</span>`;
        const wordSpan = damageWord ? ` <span class="damage-${typeLower}">damage</span>` : "";
        return `${diceSpan} ${typeSpan}${wordSpan}`;
    });

    // Highlight standalone dice (if not already wrapped)
    text = text.replace(/\b(\d+d\d+)\b/g, (match) => {
        return text.includes(`>${match}<`) ? match : `<span class="damage-dice">${match}</span>`;
    });

    // Highlight healing terms
    healingTerms.forEach(term => {
        const regex = new RegExp(`\\b(${term})\\b`, "gi");
        text = text.replace(regex, `<span class="healing">$1</span>`);
    });

    // Highlight advantage / disadvantage
    text = text.replace(/\badvantage\b/gi, '<span class="advantage">Advantage</span>');
    text = text.replace(/\bdisadvantage\b/gi, '<span class="disadvantage">Disadvantage</span>');

    // Match [type] to [damage type] damage
    text = text.replace(
        /\b(resistant|resistance|immune|vulnerable)\s+to\s+(\w+)( damage)/gi,
        (match, rawStatus, type, suffix) => {
            const statusKey = rawStatus.toLowerCase();
            const normalizedStatus = statusMap[statusKey];
            const typeLower = type.toLowerCase();

            if (!normalizedStatus || !damageTypes.includes(typeLower)) {
                return match;
            }

            const emoji = normalizedStatus === "immune"
                ? "🛡️🛡️"
                : normalizedStatus === "vulnerable"
                    ? "💥"
                    : "🛡️";

            const typeSpan = `<span class="damage-${typeLower}">${type}${suffix}</span>`;
            const labelSpan = `<span class="${normalizedStatus}">${emoji} <strong>${rawStatus}</strong></span>`;

            return `${labelSpan} to ${typeSpan}`;
        }
    );

    return text;
}
