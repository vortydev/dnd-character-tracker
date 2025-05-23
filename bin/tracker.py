# tracker.py
from cli_utils import menu, pause

from ability import AbilityType
from character import Character
from char_io import load_characters, save_characters

from spell import Spell
from spell_io import load_spells_from_file
from spell_registry import SpellRegistry

from feature import Feature
from feature_io import load_features_from_file
from feature_registry import FeatureRegistry

from race import Race, RaceType
from race_io import load_races_from_file
from race_registry import RaceRegistry

from class_level import ClassLevel
from class_level_io import load_class_levels_from_file
from class_level_registry import ClassLevelRegistry


# In-memory character list
characters: list[Character] = []


# === Character Menu ===
def characters_menu():
    while True:
        choice = menu(title=f"Characters Menu ({len(characters)} loaded)",
                      options=[
                          "List Characters", 
                          "Create Character", 
                          "Edit Character", 
                          "Remove Character", 
                          "Save Characters"
                        ])

        if choice == 1:
            char_list()
        elif choice == 2:
            char_create()
        elif choice == 3:
            char_edit()
        elif choice == 4:
            char_remove()
        elif choice == 5:
            save_characters(characters)
            print("✅ Characters saved to file.")
            pause()
        elif choice == -1:
            break


def char_list():
    """List loaded characters"""
    if not characters:
        print("No characters loaded.")
    for i, char in enumerate(characters, 1):
        print(f"\n[{i}] {char.name}")
        print(char)
    pause()


def char_create():
    """Create new character in memory."""
    name = input("Enter character name: ").strip()
    health = int(input("Max HP: "))
    print("Enter ability scores (default 10):")
    scores = {}
    for atype in AbilityType:
        val = input(f"  {atype.full_name()}: ") or "10"
        scores[atype] = int(val)

    print("\nAvailable races:")
    race_options = list(RaceType)
    for idx, r in enumerate(race_options, 1):
        print(f"{idx}. {r.value}")
    race_index = int(input("Choose race (number): ").strip()) - 1
    race_type = race_options[race_index]

    # Filter subraces for the selected race
    print("\nAvailable subraces:")
    subrace_objects = [
        race.subrace for race in RaceRegistry.all().values()
        if race.name == race_type and race.subrace
    ]
    # Deduplicate by subrace name
    unique_subraces = {sr.name: sr for sr in subrace_objects}.values()

    subrace_options = [None] + sorted(unique_subraces, key=lambda s: s.name)  # None first
    for idx, sr in enumerate(subrace_options, 1):
        label = sr.name if sr else "None"
        print(f"{idx}. {label}")

    sub_input = input("Choose subrace (number or leave blank): ").strip()
    if sub_input.isdigit() and 1 <= int(sub_input) <= len(subrace_options):
        subrace_obj = subrace_options[int(sub_input) - 1]
    else:
        subrace_obj = None

    race = Race(race_type, subrace_obj)
    char = Character(name=name, health=health, ability_scores=scores, race=race)
    characters.append(char)
    print(f"✅ Character '{name}' created.")
    pause()


def char_edit():
    """Edit loaded character."""
    if not characters:
        print("No characters to edit.")
        pause()
        return
    for i, char in enumerate(characters, 1):
        print(f"{i}. {char.name}")
    index = int(input("Choose character to edit: ")) - 1
    if 0 <= index < len(characters):
        new_name = input(f"New name for {characters[index].name} (leave blank to keep): ").strip()
        if new_name:
            characters[index].name = new_name
        print("✅ Character updated.")
    pause()


def char_remove():
    """Remove character from memory."""
    for i, char in enumerate(characters, 1):
        print(f"{i}. {char.name}")
    index = int(input("Choose character to remove: ")) - 1
    if 0 <= index < len(characters):
        removed = characters.pop(index)
        print(f"✅ Removed '{removed.name}'.")
    pause()


# === Races Menu ===
def races_menu():
    while True:
        choice = menu("Races Menu", ["List Races", "List Subraces"])

        if choice == 1:
            print(f"\n=== Registered Races by Type ({len(RaceRegistry.all())} total) ===")
            for race_type in RaceType:
                count = sum(1 for race in RaceRegistry.all().values() if race.name == race_type)
                label = f"{race_type.value} ({count} variant{'s' if count != 1 else ''})"
                print(f"- {label}")
            pause()

        elif choice == 2:
            race_options = list(RaceType)
            race_index = menu("Select a Race to View Subraces", [r.value for r in race_options])
            if race_index == -1:
                continue
            selected_race = race_options[race_index - 1]

            # Filter and display subraces
            print(f"\n=== Subraces for {selected_race.value} ===")
            found = False
            for race in RaceRegistry.all().values():
                if race.name == selected_race and race.subrace:
                    print(f"- {race.subrace.name}")
                    found = True
            if not found:
                print("No subraces found.")
            pause()

        elif choice == -1:
            break


# === Spells Menu ===
def spells_menu():
    while True:
        choice = menu("Spells Menu", ["List Spells by Level", "View Spell Details"])

        # === Option 1: List spell names by level ===
        if choice == 1:
            spell_list()

        # === Option 2: View full spell info ===
        elif choice == 2:
            spell_view()
        
        elif choice == -1:
            break


def choose_spell_level() -> int:
    """Prompt user to select a spell level. Returns level or -1 if canceled."""
    levels = sorted({s.level for s in SpellRegistry.all().values()})
    labels = [
        f"{'Cantrip' if lvl == 0 else f'Level {lvl}'} ({sum(1 for s in SpellRegistry.all().values() if s.level == lvl)} spell{'s' if sum(1 for s in SpellRegistry.all().values() if s.level == lvl) > 1 else ''})"
        for lvl in levels
    ]
    index = menu("Choose Spell Level", labels)
    return -1 if index == -1 else levels[index - 1]


def print_spell_info(spell: Spell):
    print(f"Level: {'Cantrip' if spell.level == 0 else spell.level}")
    print(f"School: {spell.school.value}")
    print(f"Casting Time: {spell.casting_time}")
    print(f"Range: {spell.s_range}")
    print(f"Duration: {spell.duration}")
    print(f"Components: {', '.join(c.value[:1] for c in spell.components)}")
    if spell.material_description:
        print(f"Material{'s' if len(spell.material_description) > 1 else ''}: {', '.join(spell.material_description)}")
    print(f"\nDescription:\n{spell.description}")
    if spell.higher_levels:
        print(f"\nAt Higher Levels:\n{spell.higher_levels}")


def spell_list():
    """List spells by level."""
    level = choose_spell_level()
    if level == -1:
        return

    spells = sorted([
        s for s in SpellRegistry.all().values() if s.level == level
    ], key=lambda s: s.name)

    print(f"\n== Spells at {'Cantrip' if level == 0 else f'Level {level}'} ==")
    for spell in spells:
        print(f"- {spell.name}")
    pause()


def spell_view():
    """View the details of a specific spell."""
    level = choose_spell_level()
    if level == -1:
        return

    spells = sorted([
        s for s in SpellRegistry.all().values() if s.level == level
    ], key=lambda s: s.name)

    if not spells:
        print("No spells found at that level.")
        pause()
        return

    spell_index = menu(
        f"Spells at {'Cantrip' if level == 0 else f'Level {level}'}",
        [s.name for s in spells]
    )
    if spell_index == -1:
        return

    selected_spell = spells[spell_index - 1]
    print(f"\n=== {selected_spell.name} ===")
    print_spell_info(selected_spell)
    pause()


# === Main Menu ===
def main_menu():
    while True:
        choice = menu(title="Main Menu",
                      options=[
                        f"Characters ({len(characters)} loaded)",
                        f"Races ({len(RaceRegistry.all())} registered)",
                        f"Spells ({len(SpellRegistry.all())} registered)",
                      ],
                      disable_back=True,
                      )

        if choice == 1:
            characters_menu()
        elif choice == 2:
            races_menu()
        elif choice == 3:
            spells_menu()


if __name__ == "__main__":
    try:
        # Load spells
        spells = load_spells_from_file()
        SpellRegistry.load_bulk(spells)

        # Load features
        features = load_features_from_file()
        FeatureRegistry.load_bulk(features)

        # Load races
        races = load_races_from_file()
        RaceRegistry.load_bulk(races)

        # Load class levels
        class_levels = load_class_levels_from_file()
        ClassLevelRegistry.load_bulk(class_levels)

        # TODO Load classes
        
        # Load characters
        characters.extend(load_characters())
        
        main_menu()

    except KeyboardInterrupt:
        print("\nUser aborted program!")
        exit()
    except Exception as e:
        print(f"\nAn error occured: {e}")
