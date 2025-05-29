#!/bin/bash

echo "🚀 Started building of D&D Character Tracker resources."

# Set PYTHONPATH to project root
# export PYTHONPATH="$(dirname "$0")"

cd "./bin/builders" || exit 1

# Helper function to run and check a script
run_step() {
    local label="$1"
    local script="$2"

    echo ""
    echo "$label"
    python "$script"
    if [ $? -ne 0 ]; then
        echo "❌ Error while running $script. Exiting."
        exit 1
    fi
}

# Run build steps
run_step "📘 Building spells..." build_spells.py
run_step "✨ Building features..." build_features.py
run_step "🧬 Building races..." build_races.py
run_step "⚔️  Building class levels..." build_class_levels.py
run_step "🔨  Building items..." build_items.py
run_step "🧠 Building classes..." build_classes.py

# Back to project root and clear pycache
echo ""
cd ../..
bash tools/clear_pycache.sh

echo ""
echo "✅ Built D&D Character Tracker resources."
