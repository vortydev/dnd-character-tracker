# race_list/human.py
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

# ===== Human =====
def load_human_base():
    human_base = Race(
        name=RaceType.HUMAN,
        description="In the reckonings of most worlds, humans are the youngest of the common races, late to arrive on the world scene and short-lived in comparison to dwarves, elves, and dragons. Perhaps it is because of their shorter lives that they strive to achieve as much as they can in the years they are given. Or maybe they feel they have something to prove to the elder races, and that's why they build their mighty empires on the foundation of conquest and trade. Whatever drives them, humans are the innovators, the achievers, and the pioneers of the worlds.",
        subrace=None,
        speed=30,
        size=Size.MEDIUM,
        ability_score_increase={
            AbilityType.STR: 1, AbilityType.DEX: 1, AbilityType.CON: 1, 
            AbilityType.INT: 1, AbilityType.WIS: 1, AbilityType.CHA: 1
        },
        info={
            "Age": "Humans reach adulthood in their late teens and live less than a century.",
            "Alignment": "Humans tend toward no particular alignment. The best and the worst are found among them.",
            "Languages": "You can speak, read, and write Common and one extra language of your choice. Humans typically learn the languages of other peoples they deal with, including obscure dialects. They are fond of sprinkling their speech with words borrowed from other tongues: Orc curses, Elvish musical expressions, Dwarvish military phrases, and so on.",
        },
    )
    return human_base


def load_human_variant():
    human_base = Race(
        name=RaceType.VARIANT_HUMAN,
        description="If your campaign uses the optional feat rules from chapter 5 of the Player's Handbook, your Dungeon Master might allow these variant traits, all of which replace the human's Ability Score Increase trait.",
        subrace=None,
        speed=30,
        size=Size.MEDIUM,
        info={
            "Age": "Humans reach adulthood in their late teens and live less than a century.",
            "Alignment": "Humans tend toward no particular alignment. The best and the worst are found among them.",
        },
        languages=[Language.COMMON]
    )
    return human_base


def get_human_races():
    """Load a list of defined Human Races"""
    races: list[Race] = [] # Empty array
    
    human_base = load_human_base()
    races.append(human_base)

    human_variant = load_human_variant()
    races.append(human_variant)

    return races