# char_io.py
import os
import json
from character import Character

# Resolve the /data directory relative to this file
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
DEFAULT_PATH = os.path.join(DATA_DIR, "characters.json")

def save_characters(characters: list[Character], path=DEFAULT_PATH):
    """Save a list of Character objects to a JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump([char.to_dict() for char in characters], f, indent=2)

def load_characters(path=DEFAULT_PATH) -> list[Character]:
    """Load a list of Character objects from a JSON file."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return [Character.from_dict(obj) for obj in json.load(f)]
    except FileNotFoundError:
        return []
