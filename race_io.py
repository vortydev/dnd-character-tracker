# race_io.py
import json
from race import Race

def save_races_to_file(races: list[Race], path: str = "races.json"):
    """Save a list of Race objects to a JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump([race.to_dict() for race in races], f, indent=2)

def load_races_from_file(path: str = "races.json") -> list[Race]:
    """Load a list of Race objects from a JSON file."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return [Race.from_dict(obj) for obj in json.load(f)]
    except FileNotFoundError:
        return []
