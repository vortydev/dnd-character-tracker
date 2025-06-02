#!/bin/bash

echo "🚀 Started building of D&D Character Tracker resources."

# Always start from project root
ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT_DIR/.." || exit 1
BUILDER_DIR="./bin/builders"

export PYTHONPATH="$ROOT_DIR"

mkdir -p data

# cd "./bin/builders" || exit 1

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
run_step "📘 Building spells..." $BUILDER_DIR/build_spells.py
run_step "✨ Building features..." $BUILDER_DIR/build_features.py
run_step "🧬 Building races..." $BUILDER_DIR/build_races.py
run_step "⚔️  Building class levels..." $BUILDER_DIR/build_class_levels.py
run_step "🔨  Building items..." $BUILDER_DIR/build_items.py
run_step "🧠 Building classes..." $BUILDER_DIR/build_classes.py

# Back to project root and clear pycache
echo ""
cd ../..
bash tools/clear_pycache.sh

echo ""
echo "✅ Built D&D Character Tracker resources."
