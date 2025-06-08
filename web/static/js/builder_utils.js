// web/static/js/builder_utils.js
export async function runBuilderScript(scriptName, root = "") {
    try {
        const response = await fetch(`${root}/admin/run-builder`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ script: scriptName })
        });

        const data = await response.json();
        if (data.status === "success") {
            console.log(`✅ ${scriptName} ran successfully:\n`, data.output);
        } 
        else {
            console.error(`❌ Error running ${scriptName}:`, data.message);
        }
    } catch (err) {
        console.error(`❌ Exception while running ${scriptName}:`, err);
    }
}

export async function runMultipleBuilderScripts(scripts, root = "") {
    for (const script of scripts) {
        await runBuilderScript(script, root);
    }
    alert("Resources successfully rebuilt!");
}
