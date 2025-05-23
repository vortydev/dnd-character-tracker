# build_class_levels.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from class_level import ClassLevel
from class_level_registry import ClassLevelRegistry
from class_level_io import save_class_levels_to_file


def load_class_level_list() -> list[ClassLevel]:
    """Load array of defined ClassLevel objects."""
    cl = []

    # === Fighter ===
    # Class
    from class_levels.fighter_class_levels import fighter_cl
    cl.extend(fighter_cl)

    # Subclass
    from class_levels.fighter_subclass_levels import fighter_scl
    cl.extend(fighter_scl)

    # === Sorcerer ===
    # Class
    from class_levels.sorcerer_class_levels import sorcerer_cl
    cl.extend(sorcerer_cl)

    # Subclass
    from class_levels.sorcerer_subclass_levels import sorcerer_scl
    cl.extend(sorcerer_scl)

    # === Wizard ===
    # Class
    from class_levels.wizard_class_levels import wizard_cl
    cl.extend(wizard_cl)

    # Subclass
    from class_levels.wizard_subclass_levels import wizard_scl
    cl.extend(wizard_scl)
    
    return cl


def save_class_level_list(class_levels: list[ClassLevel]):
    """Register ClassLevel objects and save them to a JSON file."""
    ClassLevelRegistry.load_bulk(class_levels)
    save_class_levels_to_file(class_levels)
    print(f"✅ {len(class_levels)} Class/Subclass levels saved to 'class_levels.json'")


def build_class_level_list():
    """Load the defined Feature objects into a JSON file to load the FeatureRegistry."""
    class_levels = load_class_level_list()
    save_class_level_list(class_levels)


# === Run the main function ===
build_class_level_list()
