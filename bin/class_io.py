# class_io.py
import os
import json
from class_base import Class

# Resolve the /data directory relative to this file
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
DEFAULT_PATH = os.path.join(DATA_DIR, "classes.json")

def save_classes_to_file(classes: list[Class], path: str = DEFAULT_PATH):
    """Save a list of Class objects to a JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump([c.to_dict() for c in classes], f, indent=2)

def load_classes_from_file(path: str = DEFAULT_PATH) -> list[Class]:
    """Load a list of Class objects from a JSON file."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return [Class.from_dict(obj) for obj in json.load(f)]
    except FileNotFoundError:
        return []
