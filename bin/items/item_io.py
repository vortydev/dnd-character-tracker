# item_io.py
import os, json
from items.item import Item, ItemType
from items.tool_item import ToolItem

# Resolve the /data directory relative to this file
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
DEFAULT_PATH = os.path.join(DATA_DIR, "items.json")

def save_items_to_file(items: list[Item], path: str = DEFAULT_PATH):
    """Save a list of Item objects to a JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump([i.to_dict() for i in items], f, indent=2)

def load_items_from_file(path: str = DEFAULT_PATH) -> list[Item]:
    """Load a list of Item objects from a JSON file."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
            items = []
            for d in raw_data:
                i_type = ItemType(d["type"])
                if i_type == ItemType.TOOL:
                    items.append(ToolItem.from_dict(d))
                else:
                    items.append(Item.from_dict(d))
            return items
    except FileNotFoundError:
        return []