# build_classes.py
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from bin.class_base import Class
from bin.class_registry import ClassRegistry
from bin.class_io import save_classes_to_file
from bin.class_list.class_list import (
    get_artificer_class, get_druid_class, get_fighter_class, get_ranger_class,
    get_rogue_class, get_sorcerer_class, get_wizard_class,
)

def load_class_list() -> list[Class]:
    """Load and return the list of base Class objects."""
    ARTIFICER = get_artificer_class()
    DRUID = get_druid_class()
    FIGHTER = get_fighter_class()
    RANGER = get_ranger_class()
    ROGUE = get_rogue_class()
    SORCERER = get_sorcerer_class()
    WIZARD = get_wizard_class()

    # === TODO Add other classes ===

    classes = [
        ARTIFICER, DRUID, FIGHTER,
        RANGER, ROGUE, SORCERER, WIZARD,
    ]

    return classes


def save_class_list(classes: list[Class]):
    """Register classes and save them to JSON file."""
    for cls in classes:
        ClassRegistry.register(cls)

    save_classes_to_file(classes)
    print(f"✅ {len(classes)} classes saved to 'classes.json'")


def build_class_list():
    """Builds and saves the class list to JSON using ClassRegistry."""
    classes = load_class_list()
    save_class_list(classes)


# === Run the builder ===
build_class_list()
