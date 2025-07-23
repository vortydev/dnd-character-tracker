# race_list/gnome.py
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
def load_gnome_base():
    gnome_base = Race(
        name=RaceType.GNOME,
        description="A constant hum of busy activity pervades the warrens and neighborhoods where gnomes form their close-knit communities. Louder sounds punctuate the hum: a crunch of grinding gears here, a minor explosion there, a yelp of surprise or triumph, and especially bursts of laughter. Gnomes take delight in life, enjoying every moment of invention, exploration, investigation, creation, and play.",
        speed=25,
        size=Size.SMALL,
        ability_score_increase={AbilityType.INT: 2},
        feats={
            1: [
                FeatureRegistry.get("Darkvision", FeatureType.RACE, RaceType.GNOME),
                FeatureRegistry.get("Gnome Cunning", FeatureType.RACE, RaceType.GNOME),
            ]
        },
        info={
            "Age": "Gnomes mature at the same rate as humans, and most are expected to settle into adult life around the age of 40. They can live to 350 years on average, but it's not too uncommon for them to reach 500 years of age.",
            "Alignment": "Gnomes are generally Good. Those who tend towards Law are sages, engineers, researchers, scholars, investigators, or inventors. Those who tend towards Chaos are often minstrels, tricksters, wanderers, or fanciful jewelers. Gnomes are light-hearted, and even the tricksters amongst them favor harmless pranks over vicious schemes.",
        },
        languages=[Language.COMMON, Language.GNOMISH]
    )
    return gnome_base


def load_gnome_subraces():
    forest = Subrace(
        name="Forest",
        parent_race=RaceType.GNOME,
        description="As a forest gnome, you have a natural knack for illusion and inherent quickness and stealth. In the worlds of D&D, forest gnomes are rare and secretive. They gather in hidden communities in sylvan forests, using illusions and trickery to conceal themselves from threats or to mask their escape should they be detected. Forest gnomes tend to be friendly with other good-spirited woodland folk, and they regard elves and good fey as their most important allies. These gnomes also befriend small forest animals and rely on them for information about threats that might prowl their lands.",
        ability_score_increase={AbilityType.DEX: 1},
        feats={
            1: [
                FeatureRegistry.get("Natural Illusionist", FeatureType.RACE, RaceType.GNOME),
                FeatureRegistry.get("Speak with Small Beasts", FeatureType.RACE, RaceType.GNOME),
            ]
        },
        spells={
            1: [
                SpellRegistry.get("Minor Illusion"),
            ]
        }
    )

    rock = Subrace(
        name="Rock",
        parent_race=RaceType.GNOME,
        description="As a rock gnome, you have a natural inventiveness and hardiness beyond that of other gnomes. Most gnomes in the worlds of D&D are rock gnomes, including the tinker gnomes of the Dragonlance setting.",
        ability_score_increase={AbilityType.CON: 1},
        feats={
            1: [
                FeatureRegistry.get("Artificer's Lore", FeatureType.RACE, RaceType.GNOME),
                FeatureRegistry.get("Tinker", FeatureType.RACE, RaceType.GNOME),
            ]
        }
    )

    return [forest, rock]


def get_gnome_races():
    """Load a list of defined Gnome Races"""
    races: list[Race] = [] # Empty array
    
    gnome_base = load_gnome_base()
    races.append(gnome_base)

    gnome_sb = load_gnome_subraces()
    for sb in gnome_sb:
        races.append(create_subrace_variant(gnome_base, sb))

    return races