# race_types.py
from enum import Enum

class RaceType(Enum):
    """Enum representing the base playable races."""
    DRAGONBORN = "Dragonborn"
    DWARF = "Dwarf"
    ELF = "Elf"
    GNOME = "Gnome"
    HALF_ELF = "Half-Elf"
    HALF_ORC = "Half-Orc"
    HUMAN = "Human"
    TIEFLING = "Tiefling"
    VARIANT_HUMAN = "Variant Human"
    VARIANT_TIEFLING = "Variant Tiefling"
    YUANTI_PUREBLOOD = "Yuan-Ti Pureblood"