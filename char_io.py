# char_io.py
import json
from character import Character

def save_characters(characters: list[Character], path="characters.json"):
    """Save a list of Character objects to a JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump([char.to_dict() for char in characters], f, indent=2)

def load_characters(path="characters.json") -> list[Character]:
    """Load a list of Character objects from a JSON file."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return [Character.from_dict(obj) for obj in json.load(f)]
    except FileNotFoundError:
        return []
