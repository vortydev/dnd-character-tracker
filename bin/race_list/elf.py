# race_list/elf.py
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

# ===== Elf =====
def load_elf_base():
    human_base = Race(
        name=RaceType.ELF,
        description="Elves are a magical people of otherworldly grace, living in places of ethereal beauty, in the midst of ancient forests or in silvery spires glittering with faerie light, where soft music drifts through the air and gentle fragrances waft on the breeze. Elves love nature and magic, art and artistry, music and poetry.",
        speed=30,
        size=Size.MEDIUM,
        ability_score_increase={AbilityType.DEX: 2},
        feats={
            1: [
                FeatureRegistry.get("Darkvision", FeatureType.RACE, RaceType.ELF),
                FeatureRegistry.get("Fey Ancestry", FeatureType.RACE, RaceType.ELF),
                FeatureRegistry.get("Trance", FeatureType.RACE, RaceType.ELF),
                FeatureRegistry.get("Keen Senses", FeatureType.RACE, RaceType.ELF)
            ]
        },
        info={
            "Age": "Although elves reach physical maturity at about the same age as humans, the elven understanding of adulthood goes beyond physical growth to encompass worldly experience. An elf typically claims adulthood and an adult name around the age of 100 and can live to be 750 years old.",
            "Alignment": "Elves love freedom, variety, and self-expression, so they lean strongly towards the gentler aspects of chaos. They value and protect others' freedom as well as their own, and are good more often than not. Drow are an exception; their exile into the Underdark has made them vicious and dangerous. Drow are more often evil than not.",
        },
        languages=[Language.COMMON, Language.ELVISH]
    )
    return human_base


def load_elf_subraces():
    drow = Subrace(
        name="Dark Elf",
        parent_race=RaceType.ELF,
        description="Descended from an earlier subrace of dark-skinned elves, the drow were banished from the surface world for following the goddess Lolth down the path to evil and corruption. Now they have built their own civilization in the depths of the Underdark, patterned after the Way of Lolth. Also called dark elves. The drow have black skin that resembles polished obsidian and stark white or pale yellow hair. They commonly have very pale eyes (so pale as to be mistaken for white) in shades of lilac, silver, pink, red, and blue. They lend to be smaller and thinner than most elves.\
            \nDrow adventurers are rare, and the race does not exist in all worlds. Check with your Dungeon Master to see if you can play a drow character.",
        ability_score_increase={AbilityType.CHA: 1},
        feats={
            1: [
                FeatureRegistry.get("Superior Darkvision", FeatureType.RACE, RaceType.ELF),
                FeatureRegistry.get("Sunlight Sensitivity", FeatureType.RACE, RaceType.ELF),
                FeatureRegistry.get("Drow Magic", FeatureType.RACE, RaceType.ELF),
                FeatureRegistry.get("Drow Weapon Training", FeatureType.RACE, RaceType.ELF),
            ]
        },
        spells={
            0: [SpellRegistry.get("Dancing Lights")],
            3: [SpellRegistry.get("Faerie Fire")],
            5: [SpellRegistry.get("Darkness")]
        }
    )

    high_elf = Subrace(
        name="High Elf",
        parent_race=RaceType.ELF,
        description="As a high elf, you have a keen mind and a mastery of at least the basics of magic. In many of the worlds of D&D, there are two kinds of high elves. One type (which includes the gray elves and valley elves of Greyhawk, the Silvanesti of Dragonlance, and the sun elves of the Forgotten Realms) is haughty and reclusive, believing themselves to be superior to non-elves and even other elves. The other type (including the high elves of Greyhawk. the Qualinesti of Dragonlance, and the moon elves of the Forgotten Realms) are more common and more friendly, and often encountered among humans and other races.\
            \nThe sun elves of Faerun (also called gold elves or sunrise elves) have bronze skin and hair of copper, black, or golden blood. Their eyes are golden, silver, or black. Moon elves (also called silver elves or gray elves) are much paler, with alabaster skin sometimes tinged with blue. They often have hair of silver-while, black, or blue, but various shades of blond, brown, and red are not uncommon. Their eyes are blue or green and flecked with gold.",
        ability_score_increase={AbilityType.INT: 1},
        feats={
            1: [
                FeatureRegistry.get("Cantrip", FeatureType.RACE, RaceType.ELF),
                FeatureRegistry.get("Elf Weapon Training", FeatureType.RACE, RaceType.ELF),
                FeatureRegistry.get("Extra Language", FeatureType.RACE, RaceType.ELF),
            ]
        }
    )

    wood_elf = Subrace(
        name="Wood Elf",
        parent_race=RaceType.ELF,
        description="As a wood elf, you have keen senses and intuition, and your fleet feet carry you quickly and stealthily through your native forests. This category includes the wild elves (grugach) of Greyhawk and the Kagonesti of Dragonlance, as well as the races called wood elves in Greyhawk and the Forgotten Realms. In Faerun, wood elves (also called wild elves. green elves, or forest elves) are reclusive and distrusting of non-elves.\
            \nWood elves' skin tends to be copperish in hue, sometimes with traces of green. Their hair tends toward browns and blacks, but it is occasionally blond or copper-colored. Their eyes are green, brown, or hazel.",
        ability_score_increase={AbilityType.WIS: 1},
        speed=35,
        feats={
            1: [
                FeatureRegistry.get("Elf Weapon Training", FeatureType.RACE, RaceType.ELF),
                FeatureRegistry.get("Fleet of Foot", FeatureType.RACE, RaceType.ELF),
                FeatureRegistry.get("Mask of the Wild", FeatureType.RACE, RaceType.ELF),
            ]
        }
    )

    return [drow, high_elf, wood_elf]


def get_elf_races():
    """Load a list of defined Human Races"""
    races: list[Race] = [] # Empty array
    
    elf_base = load_elf_base()
    races.append(elf_base)

    elf_sb = load_elf_subraces()
    for sb in elf_sb:
        races.append(create_subrace_variant(elf_base, sb))

    return races