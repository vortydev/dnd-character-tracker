# spell_io.py
import os
import json
from spell import Spell

# Resolve the /data directory relative to this file
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
DEFAULT_PATH = os.path.join(DATA_DIR, "spells.json")

def save_spells_to_file(spells: list[Spell], path: str = DEFAULT_PATH):
    """Save a list of Spell objects to a JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump([s.to_dict() for s in spells], f, indent=2)

def load_spells_from_file(path: str = DEFAULT_PATH) -> list[Spell]:
    """Load a list of Spell objects from a JSON file."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return [Spell.from_dict(d) for d in json.load(f)]
    except FileNotFoundError:
        return []
