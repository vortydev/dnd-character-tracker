# race_list/halfling.py
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

# ===== Halfling =====
def load_halfling_base():
    halfling_base = Race(
        name=RaceType.HALFLING,
        description="The comforts of home are the goals of most halflings' lives: a place to settle in peace and quiet, far from marauding monsters and clashing armies. Others form nomadic bands that travel constantly, lured by the open road and the wide horizon to discover the wonders of new lands and peoples. Halflings work readily with others, and they are loyal to their friends, whether halfling or otherwise. They can display remarkable ferocity when their friends, families, or communities are threatened.",
        speed=25,
        size=Size.SMALL,
        ability_score_increase={AbilityType.DEX: 2},
        feats={
            1: [
                FeatureRegistry.get("Lucky", FeatureType.RACE, RaceType.HALFLING),
                FeatureRegistry.get("Brave", FeatureType.RACE, RaceType.HALFLING),
                FeatureRegistry.get("Nimble", FeatureType.RACE, RaceType.HALFLING),
            ]
        },
        info={
            "Age": "A halfling reaches adulthood at the age of 20 and generally lives into the middle of his or her second century.",
            "Alignment": "Most halflings are lawful good. As a rule, they are good-hearted and kind, hate to see others in pain, and have no tolerance for oppression. They are also very orderly and traditional, leaning heavily on the support of their community and the comfort of the old ways.",
        },
        languages=[Language.COMMON, Language.HALFLING]
    )
    return halfling_base


def load_halfling_subraces():
    lightfoot = Subrace(
        name="Lightfoot",
        parent_race=RaceType.HALFLING,
        description="As a lightfoot halfling, you can easily hide from notice, even using other people as cover. You're inclined to be affable and get along well with others. In the Forgotten Realms, lightfoot halflings have spread the farthest and thus are the most common variety.\
            \nLightfoots are more prone to wanderlust than other halflings, and often dwell alongside other races or take up a nomadic life. In the world of Grayhawk, these halflings are called hairfeet or tallfellows.",
        ability_score_increase={AbilityType.CHA: 1},
        feats={
            1: [
                FeatureRegistry.get("Naturally Stealthy", FeatureType.RACE, RaceType.HALFLING),
            ]
        },
    )

    stout = Subrace(
        name="Stout",
        parent_race=RaceType.HALFLING,
        description="As a stout halfling, you're hardier than average and have some resistance to poison. Some say that stouts have dwarven blood. In the Forgotten Realms, these halflings are called stronghearts, and they're most common in the south.",
        ability_score_increase={AbilityType.CON: 1},
        feats={
            1: [
                FeatureRegistry.get("Stout Resilience", FeatureType.RACE, RaceType.HALFLING),
            ]
        }
    )

    return [lightfoot, stout]


def get_halfling_races():
    """Load a list of defined Halfling Races"""
    races: list[Race] = [] # Empty array
    
    halfling_base = load_halfling_base()
    races.append(halfling_base)

    halfling_sb = load_halfling_subraces()
    for sb in halfling_sb:
        races.append(create_subrace_variant(halfling_base, sb))

    return races