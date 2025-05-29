function loadFeaturesFromAPI() {
    const baseFeatureContainer = document.getElementById("baseFeatureContainer");
    const raceFeatureContainer = document.getElementById("raceFeatureContainer");
    const classFeatureContainer = document.getElementById("classFeatureContainer");
    const subclassFeatureContainer = document.getElementById("subclassFeatureContainer");

    fetch("/api/features/get")
        .then(response => {
            if (!response.ok) throw new Error("Network response was not ok");
            return response.json();
        })
        .then(data => {
            const delayStep = 0; // ms between each section opening
            renderFeatureList(baseFeatureContainer, data.base_feats, delayStep * 0);
            renderFeatureList(raceFeatureContainer, data.race_feats, delayStep * 1);
            renderFeatureList(classFeatureContainer, data.class_feats, delayStep * 2);
            renderFeatureList(subclassFeatureContainer, data.subclass_feats, delayStep * 3);
        })
        .catch(error => {
            console.error("Error loading features:", error);
            alert("Failed to load features.");
        });

    openFeatureURL();
}

function renderFeatureList(container, list, delayMs = 0) {
    if (list.length === 0) {
        container.innerHTML = "<i>No features available.</i>";
        return;
    }

    const grouped = {};
    for (const f of list) {
        const ctx = f.context || "General";
        if (!grouped[ctx]) grouped[ctx] = [];
        grouped[ctx].push(f.html);
    }

    const sortedKeys = Object.keys(grouped).sort((a, b) => a.localeCompare(b));

    container.innerHTML = sortedKeys.map(ctx => {
        const content = grouped[ctx].join("");
        return `
            <details class="feature-context-group">
                <summary><h3 class="section-title feature-context">${ctx}</h3></summary>
                ${highlightDamageTypes(content)}
            </details>
        `;
    }).join("");

    // Open section if it has content
    openIfHasContent(container, delayMs, "feature");

    // Also auto-open each context group, staggered a bit
    const contextGroups = container.querySelectorAll(".feature-context-group");
    contextGroups.forEach((ctxDetail, i) => {
        setTimeout(() => {
            ctxDetail.setAttribute("open", "");
        }, delayMs + (i * 75));
    });
}

function openFeatureURL() {
    const urlParams = new URLSearchParams(window.location.search);
    const featName = urlParams.get("name");
    const featType = urlParams.get("type");

    if (!featName) return;

    const highlightDelay = 250;
    const highlightExpiry = 3000;
    const scrollOffset = 10;

    setTimeout(() => {
        const el = document.getElementById(featName);
        if (el) {
            const top = el.getBoundingClientRect().top + window.scrollY - scrollOffset;
            window.scrollTo({
                top,
                behavior: "smooth"
            });

            setTimeout(() => {
                el.classList.add("highlighted");
            }, highlightDelay);

            setTimeout(() => {
                el.classList.remove("highlighted");
            }, highlightExpiry);
        }
    }, highlightDelay);
}