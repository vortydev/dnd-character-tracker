# build_races.py
from race import Race
from race_registry import RaceRegistry
from race_io import save_races_to_file


def load_race_list():
    """Load array of defined Race objects."""
    races = []  # Empty array

    # === Tieflings ===
    from race_list.tiefling import get_tiefling_races
    tieflings = get_tiefling_races()
    races.extend(tieflings)

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
