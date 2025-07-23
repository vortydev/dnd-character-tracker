# race_list/half_elf.py
from ability import AbilityType
from common import Size, Language
from race import Race, Subrace
from race_types import RaceType
from race_utils import create_subrace_variant
from spell_io import load_spells_from_file
from spell_registry import SpellRegistry
from feature_types import FeatureType
from feature_io import load_features_from_file
from feature_registry import FeatureRegistry

# Load spells
spells = load_spells_from_file()
SpellRegistry.load_bulk(spells)

# Load features
features = load_features_from_file()
FeatureRegistry.load_bulk(features)

# ===== Half-Elf =====
def load_half_elf_base():
    half_elf_base = Race(
        name=RaceType.HALF_ELF,
        description="Walking in two worlds but truly belonging to neither, half-elves combine what some say are the best qualities of their elf and human parents: human curiosity, inventiveness, and ambition tempered by the refined senses, love of nature, and artistic tastes of the elves.",
        speed=30,
        size=Size.MEDIUM,
        ability_score_increase={AbilityType.CHA: 2}, # TODO 2 other choices +1
        feats={
            1: [
                FeatureRegistry.get("Darkvision", FeatureType.RACE, RaceType.HALF_ELF),
                FeatureRegistry.get("Fey Ancestry", FeatureType.RACE, RaceType.HALF_ELF),
                FeatureRegistry.get("Half-Elf Versatility", FeatureType.RACE, RaceType.HALF_ELF),
            ]
        },
        info={
            "Age": "Half-elves age at much the same rate as humans, reaching adulthood at the age of 20. They live much longer than humans, however, often exceeding 180 years.",
            "Alignment": "Half-elves share the chaotic bent of their elven heritage. They both value personal freedom and creative expression, demonstrating neither love of leaders nor desire for followers. They chafe at rules, resent others' demands, and sometimes prove unreliable, or at least unpredictable. They are good and evil in equal numbers, a trait they share with their human parents.",
            "Ability Score Increase": "Your Charisma score increases by 2, and two other ability scores of your choice each increase by 1.",
            "Languages": "You can read, speak, and write Common, Elven, and one language of your choice.",
        },
        languages=[Language.COMMON, Language.ELVISH]
    )
    return half_elf_base


def get_half_elf_races():
    """Load a list of defined Half-Elf Races"""
    races: list[Race] = [] # Empty array
    
    half_elf_base = load_half_elf_base()
    races.append(half_elf_base)

    return races