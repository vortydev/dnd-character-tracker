# build_spells.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from spell import Spell
from spell_registry import SpellRegistry
from spell_io import save_spells_to_file

# Spell list
from spell_list import (
    lvl0_spells, lvl1_spells, lvl2_spells, lvl3_spells, lvl4_spells,
    lvl5_spells, lvl6_spells, lvl7_spells, lvl8_spells, lvl9_spells
)


def load_spell_list() -> list[Spell]:
    """Load array of defined Spell objects."""
    spells = [] # Empty array

    spells.extend(lvl0_spells)  # Level 0 (Cantrip)
    spells.extend(lvl1_spells)  # Level 1
    spells.extend(lvl2_spells)  # Level 2
    spells.extend(lvl3_spells)  # Level 3
    spells.extend(lvl4_spells)  # Level 4
    spells.extend(lvl5_spells)  # Level 5
    spells.extend(lvl6_spells)  # Level 6
    spells.extend(lvl7_spells)  # Level 7
    spells.extend(lvl8_spells)  # Level 8
    spells.extend(lvl9_spells)  # Level 9

    return spells


def save_spell_list(spells: list[Spell]):
    """Register Spell objects and save them to a JSON file."""
    SpellRegistry.load_bulk(spells)
    save_spells_to_file(spells)

    print(f"✅ {len(spells)} spells saved to 'spells.json'")


def build_spell_list():
    """Load the defined Spell objects into a JSON file to load the SpellRegistry."""
    spells = load_spell_list()
    save_spell_list(spells)


# === Run the main function ===
build_spell_list()