# race_list/yuan-ti.py
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

# ===== YUAN-TI =====
def load_yuanti_pureblood():
    # Base tiefling
    yuanti_base = Race(
        name=RaceType.YUANTI_PUREBLOOD,
        description="The serpent creatures known as yuan-ti are all that remains of an ancient, decadent human empire. Ages ago their dark gods taught them profane, cannibalistic rituals to mix their flesh with that of snakes, producing a caste-based society of hybrids in which the most snakelike are the leaders and the most humanlike are spies and agents in foreign lands.",
        subrace=None,
        speed=30,
        size=Size.MEDIUM,
        ability_score_increase={AbilityType.CHA: 2, AbilityType.INT: 1},
        feats={
            1: [
                FeatureRegistry.get("Darkvision", FeatureType.RACE, RaceType.YUANTI_PUREBLOOD),
                FeatureRegistry.get("Innate Spellcasting", FeatureType.RACE, RaceType.YUANTI_PUREBLOOD),
                FeatureRegistry.get("Magic Resistance", FeatureType.RACE, RaceType.YUANTI_PUREBLOOD),
                FeatureRegistry.get("Poison Immunity", FeatureType.RACE, RaceType.YUANTI_PUREBLOOD),
            ]
        },
        spells={
            0: [
                SpellRegistry.get("Poison Spray"),
                SpellRegistry.get("Animal Friendship"),
            ],
            3: [SpellRegistry.get("Suggestion")],
        },
        info={
            "Age": "Purebloods mature at the same rate as humans and have lifespans similar in length to theirs.",
            "Alignment": "Purebloods are devoid of emotion and see others as tools to manipulate. They care little for law or chaos and are typically neutral evil.",
        },
        languages=[Language.COMMON, Language.ABYSSAL, Language.DRACONIC],
    )
    return yuanti_base


def load_yuanti_gorgon():
    yuanti_gorgon = Subrace(
        name="Yuan-Ti Gorgon (Homebrew)",
        parent_race=RaceType.YUANTI_PUREBLOOD,
        description="This is a custom subrace for Ethel's character Ava. Due to a genetic mutation, she was born with snakes for hair. Her unique medusa-like appearance amongst her people led to oppression and violence towards her since her birth. \
            The snakes on her head are semi-sentient and show no sign of physical needs. Their bodily language usually reflect her strong emotions.",
        feats={
            1: [
                FeatureRegistry.get("Main Snake Heads", FeatureType.RACE, RaceType.YUANTI_PUREBLOOD),
                FeatureRegistry.get("Poisonous Bite", FeatureType.RACE, RaceType.YUANTI_PUREBLOOD),
            ],
        }
    )
    return yuanti_gorgon


def get_yuanti_races():
    """Load a list of defined Yuan-Ti Races"""
    races: list[Race] = [] # Empty array
    
    yuanti_pureblood = load_yuanti_pureblood()
    races.append(yuanti_pureblood)

    yuanti_gorgon = load_yuanti_gorgon()
    races.append(create_subrace_variant(yuanti_pureblood, yuanti_gorgon))

    return races