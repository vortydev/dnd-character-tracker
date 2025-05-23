#!/bin/bash

echo "🚀 Started building of D&D Character Tracker resources."

echo ""
echo "Building spells..."
python build_spells.py

echo ""
echo "Building features..."
python build_features.py

echo ""
echo "Building races..."
python build_races.py

echo ""
echo "Building class levels..."
python build_class_levels.py

# echo ""
# echo "Building classes..."
# python build_classes.py

echo ""
echo "🧹 Clearing pycache..."
clear_pycache() {
    find . -type d -name '__pycache__' -exec rm -rf {} +
}
clear_pycache

echo ""
echo "✅ Builded D&D Character Tracker resources."