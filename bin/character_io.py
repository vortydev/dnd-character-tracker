# character_io.py
import os
import json
from character import Character

# Path config
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
DEFAULT_PATH = os.path.join(DATA_DIR, "characters.json")

def save_characters_to_file(characters: list[Character], path: str = DEFAULT_PATH):
    """Save a list of Character objects to a JSON file."""
    path = DEFAULT_PATH if path is None else path
    with open(path, "w", encoding="utf-8") as f:
        json.dump([c.to_dict() for c in characters], f, indent=2)

def load_characters_from_file(path: str = DEFAULT_PATH, registries: dict[str] = None) -> list[Character]:
    """Load a list of Character objects from a JSON file."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return [Character.from_dict(obj, registries) for obj in json.load(f)]
    except FileNotFoundError:
        return []
