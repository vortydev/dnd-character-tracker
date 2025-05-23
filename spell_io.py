# spell_io.py
import json
from spell import Spell

def save_spells_to_file(spells: list[Spell], path: str = "spells.json"):
    """Save a list of Spell objects to a JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump([s.to_dict() for s in spells], f, indent=2)

def load_spells_from_file(path: str = "spells.json") -> list[Spell]:
    """Load a list of Spell objects from a JSON file."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return [Spell.from_dict(d) for d in json.load(f)]
    except FileNotFoundError:
        return []
