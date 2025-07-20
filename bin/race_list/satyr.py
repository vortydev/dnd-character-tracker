# race_list/satyr.py
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

# ===== SATYR =====
def load_satyr():
    satyr = Race(
        name=RaceType.SATYR,
        description="Satyrs have a well-earned reputation for their good spirits, gregarious personalities, and love of revels. Most satyrs are driven by simple desires, to see the world and to sample its every pleasure. While their spontaneity and whimsy sometimes put them at odds with more stoic peoples, satyrs rarely let the moodiness of others hinder their own happiness. Life is a blessing from the gods, after all, and the proper response to such a gift, as far as most satyrs are concerned, is to accept it with relish.",
        subrace=None,
        speed=35,
        size=Size.MEDIUM,
        ability_score_increase={AbilityType.CHA: 2, AbilityType.DEX: 1},
        feats={
            1: [
                FeatureRegistry.get("Fey", FeatureType.RACE, RaceType.SATYR),
                FeatureRegistry.get("Ram", FeatureType.RACE, RaceType.SATYR),
                FeatureRegistry.get("Magic Resistance", FeatureType.RACE, RaceType.SATYR),
                FeatureRegistry.get("Mirthful Leaps", FeatureType.RACE, RaceType.SATYR),
                FeatureRegistry.get("Reveler", FeatureType.RACE, RaceType.SATYR),
            ]
        },
        info={
            "Age": "Satyrs mature and age at about the same rate as humans.",
            "Alignment": "Satyrs delight in living a life free of the mantle of law. They gravitate toward being good, but some have devious streaks and enjoy causing dismay.",
        },
        languages=[Language.COMMON, Language.SYLVAN],
    )
    return satyr


def get_satyr_races():
    """Load a list of defined Satyr Races"""
    races: list[Race] = [] # Empty array
    
    satyr = load_satyr()
    races.append(satyr)

    # yuanti_gorgon = load_yuanti_gorgon()
    # races.append(create_subrace_variant(yuanti_pureblood, yuanti_gorgon))

    return races