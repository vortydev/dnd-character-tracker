# build_items.py
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from items.item import Item, ItemType
from items.item_registry import ItemRegistry
from items.item_io import save_items_to_file
from items.tool_item import ToolItem, ToolType

def load_item_list():
    items: list[Item] = []
    # === Base Items ===

    # === Tools ===
    print("> Creating Tool items")
    from item_list.tool_item_list import artisan_tools, gaming_set_items, musical_items, misc_items
    items.extend(artisan_tools)
    items.extend(gaming_set_items)
    items.extend(musical_items)
    items.extend(misc_items)

    # === Armor ===

    # === Weapons ===

    return items

def build_item_list():
    """Load the defined Item objects into a JSON file to load the ItemRegistry."""
    items = load_item_list()

    ItemRegistry.load_bulk(items)
    save_items_to_file(items)

    print(f"✅ {len(items)} items saved to 'items.json'")


# === Run the main function ===
build_item_list()