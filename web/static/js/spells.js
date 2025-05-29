function loadSpellsFromAPI(root) {
    fetch(root+"/api/spells/get")
        .then(response => {
            if (!response.ok) throw new Error("Network response was not ok");
            return response.json();
        })
        .then(data => {
            renderSpellTabsAndTables(data.spell_list);
            openSpellURL();
        })
        .catch(error => {
            console.error("Error loading spells:", error);
            alert("Failed to load spells.");
        });
}

function renderSpellTabsAndTables(spells) {
    const tabList = document.getElementById("spellTabs");
    const tabContent = document.getElementById("spellTabsContent");

    // Group spells by level
    const grouped = {};
    for (const spell of spells) {
        const level = spell.level;
        if (!grouped[level]) grouped[level] = [];
        grouped[level].push(spell);
    }

    const sortedLevels = Object.keys(grouped).map(Number).sort((a, b) => a - b);

    tabList.innerHTML = "";
    tabContent.innerHTML = "";

    sortedLevels.forEach((level, i) => {
        const levelLabel = level === 0 ? "Cantrip" : `${level}<sup>${ordinal(level)}</sup> Level`;
        const activeClass = i === 0 ? "active" : "";
        const showClass = i === 0 ? "show active" : "";

        const tabId = `level${level}`;

        // === Tab Button ===
        tabList.innerHTML += `
            <li class="nav-item" role="presentation">
                <button class="nav-link ${activeClass}" id="${tabId}-tab" data-bs-toggle="tab" data-bs-target="#${tabId}" type="button" role="tab" aria-controls="${tabId}" aria-selected="${i === 0}">
                    ${levelLabel}
                </button>
            </li>
        `;

        // === Tab Pane with Table ===
        const tableBodyId = `spellTableBody-${level}`;

        tabContent.innerHTML += `
            <div class="tab-pane fade ${showClass}" id="${tabId}" role="tabpanel" aria-labelledby="${tabId}-tab">
                <table class="table table-striped spell-table">
                    <thead>
                        <tr>
                            <th>Spell Name</th>
                            <th>School</th>
                            <th>Casting Time</th>
                            <th>Range</th>
                            <th>Duration</th>
                            <th>Components</th>
                        </tr>
                    </thead>
                    <tbody id="${tableBodyId}"></tbody>
                </table>
            </div>
        `;

        renderSpellsToTable(grouped[level], tableBodyId);
    });
}

function renderSpellsToTable(spells, containerId) {
    const tbody = document.getElementById(containerId);
    if (!tbody) return;

    tbody.innerHTML = spells.map(spell => {
        const components = spell.components.map(c => c[0]).join(", ");
        const rowId = `spell-desc-${spell.name.replace(/[^\w-]/g, "_").toLowerCase()}`;
        const hasDetails = spell.description || spell.higher_levels || spell.material_description.length > 0;

        return `
            <tr class="spell-row" onclick="toggleSpellDetails('${rowId}')">
                <td><strong>${spell.name}</strong></td>
                <td><em>${spell.school}</em></td>
                <td>${spell.casting_time || spell.action_cost}</td>
                <td>${spell.range || ""}</td>
                <td>${spell.duration || ""}</td>
                <td>${components}</td>
            </tr>
            ${hasDetails ? `
            <tr id="${rowId}" class="spell-details-row" style="display:none;">
                <td colspan="6">
                    ${spell.description ? formatSpellTextBlock(spell.description, "Description") : ""}
                    ${spell.higher_levels ? formatSpellTextBlock(spell.higher_levels, "At Higher Levels") : ""}
                    ${spell.material_description.length > 0 ? `<p><strong>Materials :</strong> ${applyTextFormatting(spell.material_description.join(", "))}</p>` : ""}
                </td>
            </tr>
            ` : ""}
        `;
    }).join("");

    // Collapse open spells when switching tabs
    document.getElementById("spellTabs").addEventListener("shown.bs.tab", () => {
        // Hide all expanded description rows
        document.querySelectorAll(".spell-details-row").forEach(row => {
            row.style.display = "none";
        });

        // Remove highlight class from all rows
        document.querySelectorAll(".spell-row.open").forEach(row => {
            row.classList.remove("open");
        });
    });
}

function formatSpellTextBlock(text, label = null) {
    if (!text) return "";

    const lines = text.split("\n").map(line => line.trim()).filter(Boolean);
    const blocks = [];
    let currentList = [];

    for (const line of lines) {
        const processedLine = applyTextFormatting(line);
        if (line.startsWith("- ")) {
            currentList.push(`<li>${processedLine.substring(2)}</li>`);
        } else {
            if (currentList.length > 0) {
                blocks.push(`<ul>${currentList.join("")}</ul>`);
                currentList = [];
            }
            blocks.push(`<p>${processedLine}</p>`);
        }
    }

    // Flush any remaining list items
    if (currentList.length > 0) {
        blocks.push(`<ul>${currentList.join("")}</ul>`);
    }

    if (blocks.length === 0) return "";

    // Apply label inline with first paragraph
    if (label && blocks[0].startsWith("<p>")) {
        blocks[0] = blocks[0].replace(
            "<p>",
            `<p><strong>${label}:</strong> `
        );
    }

    return blocks.join("");
}


function toggleSpellDetails(id) {
    const el = document.getElementById(id);
    const mainRow = el?.previousElementSibling;

    if (!el || !mainRow) return;

    const isOpen = el.style.display !== "none";

    if (isOpen) {
        el.style.display = "none";
        mainRow.classList.remove("open");
    } else {
        el.style.display = "table-row";
        mainRow.classList.add("open");
    }
}


function ordinal(n) {
    if (n === 1) return "st";
    if (n === 2) return "nd";
    if (n === 3) return "rd";
    return "th";
}

function openSpellURL() {
    const urlParams = new URLSearchParams(window.location.search);
    const targetLevel = urlParams.get('level');
    const targetSpell = urlParams.get('spell');

    if (targetLevel !== null) {
        const tabTrigger = document.querySelector(`#level${targetLevel}-tab`);
        if (tabTrigger) {
            const tab = new bootstrap.Tab(tabTrigger);
            tab.show();
        }
    }

    if (targetSpell) {
        const highlightDelay = 250;
        const highlightExpiry = 3000;

        setTimeout(() => {
            const spellId = `spell-desc-${targetSpell.replace(/[^\w-]/g, "_").toLowerCase()}`;
            const detailsRow = document.getElementById(spellId);
            const mainRow = detailsRow?.previousElementSibling;

            if (detailsRow && mainRow) {
                detailsRow.style.display = "table-row";
                mainRow.classList.add("open");
                mainRow.scrollIntoView({ behavior: "smooth", block: "center" });
                mainRow.classList.add("highlighted");

                setTimeout(() => {
                    mainRow.classList.remove("highlighted");
                }, highlightExpiry);
            }
        }, highlightDelay);
    }
}