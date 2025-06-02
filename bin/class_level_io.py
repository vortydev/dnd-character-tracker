# class_level_io.py
import os, json
from bin.class_level import ClassLevelType, ClassLevel, ClassLevelSpellcaster, ClassLevelSorcerer

# Resolve the /data directory relative to this file
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
DEFAULT_PATH = os.path.join(DATA_DIR, "class_levels.json")

def save_class_levels_to_file(class_levels: list[ClassLevel], path: str = DEFAULT_PATH):
    """Save a list of ClassLevel objects to a JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump([cl.to_dict() for cl in class_levels], f, indent=2)


def load_class_levels_from_file(path: str = DEFAULT_PATH, registries: dict[str] = None) -> list[ClassLevel]:
    """Load a list of ClassLevel objects from a JSON file."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
            class_levels = []
            for d in raw_data:
                cl_type = d["type"]
                if cl_type == ClassLevelType.SPELLCASTER.value:
                    class_levels.append(ClassLevelSpellcaster.from_dict(d, registries))
                elif cl_type == ClassLevelType.SORCERER.value:
                    class_levels.append(ClassLevelSorcerer.from_dict(d, registries))
                else:
                    class_levels.append(ClassLevel.from_dict(d, registries))
            return class_levels
    except FileNotFoundError:
        return []
