// js/character_spells.js
// Global cache object
window.cachedSpells = {
    all: [],
    grouped: {},
};

export async function fetchAndCacheSpells(root) {
    try {
        const response = await fetch(`${root}/api/spells/get`);
        if (!response.ok) throw new Error("Failed to fetch spells");

        const data = await response.json();
        const spells = data.spell_list || [];

        // Sort by level
        spells.sort((a, b) => a.level - b.level);

        // Group by level
        const grouped = {};
        for (const spell of spells) {
            if (!grouped[spell.level]) grouped[spell.level] = [];
            grouped[spell.level].push(spell);
        }

        window.cachedSpells.all = spells;
        window.cachedSpells.grouped = grouped;

        console.log("✅ Spells fetched and cached.");
        console.log("Spells:", spells, grouped);
        
    } 
    catch (err) {
        console.error("❌ Error in fetchAndCacheSpells:", err);
    }
}

export function createSpellCard(spell, show_level=false) {
    const card = document.createElement("div");
    card.className = "spell-card";

    const components = spell.components?.map(c => c[0]).join(", ") || "";
    const hasMaterials = spell.material_description?.length > 0;
    const hasHigherLevels = !!spell.higher_levels;
    const hasDescription = !!spell.description;
    
    let spellName = spell.name;
    if (show_level){
        spellName += ` <small class="text-muted">(${spell.level === 0 ? "Cantrip" : `Level ${spell.level}`})</small>`;
    }

    // Create header section (always visible)
    const header = document.createElement("div");
    header.className = "spell-header";
    header.innerHTML = `<h4>${spell.name}</h4>`;

    // Create toggle button
    const toggleBtn = document.createElement("button");
    toggleBtn.className = "spell-toggle-btn";
    toggleBtn.textContent = "Show info";

    // Create expandable section
    const infoSection = document.createElement("div");
    infoSection.className = "spell-info";
    infoSection.style.display = "none"; // initially hidden

    const list = document.createElement("ul");
    list.className = "spell-info-list";

    list.innerHTML = `
        <li><strong>Level:</strong> ${spell.level === 0 ? "Cantrip" : spell.level}</li>
        <li><strong>School:</strong> ${spell.school}</li>
        <li><strong>Casting Time:</strong> ${spell.casting_time || spell.action_cost}</li>
        <li><strong>Range:</strong> ${spell.range || "—"}</li>
        <li><strong>Duration:</strong> ${spell.duration || "—"}</li>
        <li><strong>Components:</strong> ${components}</li>
        ${hasMaterials ? `<li><strong>Materials:</strong> ${spell.material_description.join(", ")}</li>` : ""}
        ${hasDescription ? `<li><strong>Description:</strong> ${formatMultilineToList(spell.description)}</li>` : ""}
        ${hasHigherLevels ? `<li><strong>At Higher Levels:</strong> ${formatMultilineToList(spell.higher_levels)}</li>` : ""}
    `;

    infoSection.appendChild(list);

    // Add toggle behavior
    toggleBtn.addEventListener("click", () => {
        const isOpen = infoSection.style.display === "block";
        infoSection.style.display = isOpen ? "none" : "block";
        toggleBtn.textContent = isOpen ? "Show info" : "Hide info";
        toggleBtn.classList.toggle("active", !isOpen);
    });

    card.appendChild(header);
    card.appendChild(toggleBtn);
    card.appendChild(infoSection);

    return card;
}

function formatMultilineText(text) {
    const lines = text.split("\n").map(l => l.trim()).filter(Boolean);
    return lines.map(line => {
        if (line.startsWith("- ")) {
            return `<li>${line.slice(2)}</li>`;
        }
        return `<p>${line}</p>`;
    }).join("");
}

function formatMultilineToList(text) {
    const lines = text.split("\n").map(l => l.trim()).filter(Boolean);
    const listItems = lines.map(line =>
        line.startsWith("- ") ? `<li>${line.slice(2)}</li>` : `<li>${line}</li>`
    );
    return `<ul>${listItems.join("")}</ul>`;
}


/**
 * Renders spell cards grouped by level.
 * Each level has its own section with a header and a list of spells.
 * The spells are displayed as cards with relevant details.
 */
export function renderSpellCardsByLevel() {
    const container = document.getElementById("spellCardsContainer");
    container.innerHTML = "";

    const grouped = window.cachedSpells.grouped;
    const sortedLevels = Object.keys(grouped).map(Number).sort((a, b) => a - b);

    sortedLevels.forEach(level => {
        const levelLabel = level === 0 ? "Cantrips" : `Level ${level}`;

        const detailsEl = document.createElement("details");
        detailsEl.className = "fa-chevron dnd-feature-section";
        if (level === 0) detailsEl.open = true; // optionally auto-open cantrips

        const summary = document.createElement("summary");
        summary.className = "section-title";
        summary.innerHTML = `<h2>${levelLabel}</h2>`;

        const spellList = document.createElement("div");
        spellList.className = "spell-list grid gap-3"; // customize layout as needed

        grouped[level].forEach(spell => {
            const card = createSpellCard(spell);
            spellList.appendChild(card);
        });

        detailsEl.appendChild(summary);
        detailsEl.appendChild(spellList);
        container.appendChild(detailsEl);
    });
}



document.addEventListener("DOMContentLoaded", async () => {
    // TODO
    await fetchAndCacheSpells(root);
    renderSpellCardsByLevel();

    insertChevronsIntoDetailsFA();
});
