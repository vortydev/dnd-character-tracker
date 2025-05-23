# race_io.py
import os
import json
from race import Race

# Resolve the /data directory relative to this file
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
DEFAULT_PATH = os.path.join(DATA_DIR, "races.json")

def save_races_to_file(races: list[Race], path: str = DEFAULT_PATH):
    """Save a list of Race objects to a JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump([race.to_dict() for race in races], f, indent=2)

def load_races_from_file(path: str = DEFAULT_PATH) -> list[Race]:
    """Load a list of Race objects from a JSON file."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return [Race.from_dict(obj) for obj in json.load(f)]
    except FileNotFoundError:
        return []
