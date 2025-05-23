# class_level_io.py
import json
from class_level import ClassLevelType, ClassLevel, ClassLevelSpellcaster

def save_class_levels_to_file(class_levels: list[ClassLevel], path: str = "class_levels.json"):
    """Save a list of ClassLevel objects to a JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump([cl.to_dict() for cl in class_levels], f, indent=2)


def load_class_levels_from_file(path: str = "class_levels.json") -> list[ClassLevel]:
    """Load a list of ClassLevel objects from a JSON file."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
            class_levels = []
            for d in raw_data:
                if d["type"] == ClassLevelType.SPELLCASTER.value:
                    class_levels.append(ClassLevelSpellcaster.from_dict(d))
                # WIP
                else:
                    class_levels.append(ClassLevel.from_dict(d))
            return class_levels
    except FileNotFoundError:
        return []
