# build_classes.py
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from class_base import Class
from class_registry import ClassRegistry
from class_io import save_classes_to_file


def load_class_list() -> list[Class]:
    """Load and return the list of base Class objects."""
    classes = []

    from class_list.druid import get_druid_class
    classes.append(get_druid_class())

    from class_list.fighter import get_fighter_class
    classes.append(get_fighter_class())

    from class_list.sorcerer import get_sorcerer_class
    classes.append(get_sorcerer_class())

    from class_list.wizard import get_wizard_class
    classes.append(get_wizard_class())

    # === TODO Add other classes ===

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
