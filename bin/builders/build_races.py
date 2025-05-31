# build_races.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from race import Race
from race_registry import RaceRegistry
from race_io import save_races_to_file


def load_race_list():
    """Load array of defined Race objects."""
    races = []  # Empty array

    # Elf
    from race_list.elf import get_elf_races
    races.extend(get_elf_races())

    # Human
    from race_list.human import get_human_races
    races.extend(get_human_races())

    # Tieflings
    from race_list.tiefling import get_tiefling_races
    races.extend(get_tiefling_races())

    # Yuan-Ti
    from race_list.yuanti import get_yuanti_races
    races.extend(get_yuanti_races())

    return races


def save_race_list(races: list[Race]):
    """Register Race objects and save them to a JSON file."""
    RaceRegistry.load_bulk(races)
    save_races_to_file(races)

    print(f"✅ {len(races)} races saved to races.json")


def build_race_list():
    """Load the defined Race objects and dump them into a JSON file using the RaceRegistry."""
    races = load_race_list()
    save_race_list(races)


# === Run the main function ===
build_race_list()
