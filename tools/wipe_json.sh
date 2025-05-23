#!/bin/bash

echo "🧹 Starting JSON wipe script..."

# Define array of JSON files to wipe
json_files=("spells.json" "features.json" "races.json" "class_levels.json")

# Loop through each file
for file in "${json_files[@]}"; do
    if [ -f "$file" ]; then
        echo ""
        echo "✏️  Wiping '$file'..."
        echo "[]" > "$file"
        echo "✅ Done."
    else
        echo "⚠️  File '$file' not found. Skipping."
    fi
done

echo ""
echo "🧼 All done! Selected JSON files have been cleared."
