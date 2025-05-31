# race_list/tiefling.py
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


# ===== TIEFLINGS =====
def load_tiefling_base():
    # Base tiefling
    tiefling_base = Race(
        name=RaceType.TIEFLING,
        description="To be greeted with stares and whispers, to suffer violence and insult on the street, to see mistrust and fear in every eye: this is the lot of the tiefling. And to twist the knife, tieflings know that this is because a pact struck generations ago infused the essence of Asmodeus, overlord of the Nine Hells (and many of the other powerful devils serving under him) into their bloodline. Their appearance and their nature are not their fault but the result of an ancient sin, for which they and their children and their children's children will always be held accountable.",
        subrace=None,
        speed=30,
        size=Size.MEDIUM,
        ability_score_increase={AbilityType.CHA: 2},
        feats={
            1: [
                FeatureRegistry.get("Darkvision", FeatureType.RACE, RaceType.TIEFLING),
                FeatureRegistry.get("Hellish Resistance", FeatureType.RACE, RaceType.TIEFLING),
            ]
        },
        info={
            "Age": "Tieflings mature at the same rate as humans but live a few years longer.",
            "Alignment": "Tieflings might not have an innate tendency toward evil, but many of them end up there. Evil or not, an independent nature inclines many tieflings toward a chaotic alignment.",
        },
        languages=[Language.COMMON, Language.INFERNAL],
    )
    return tiefling_base


def load_bloodline_tieflings():
    """Load Tiefling Bloodline subraces."""
    # === Player's Handbook ===
    # Tiefling - Asmodeus
    bloodline_asmodeus = Subrace(
        name="Bloodline of Asmodeus",
        parent_race=RaceType.TIEFLING,
        description="The tieflings connected to Nessus command the power of fire and darkness, guided by a keener than normal intellect, as befits those linked to Asmodeus himself.",
        ability_score_increase={AbilityType.INT: 1},
        feats={ 1: [FeatureRegistry.get("Infernal Legacy", FeatureType.RACE, RaceType.TIEFLING)] },
        spells={
            0: [SpellRegistry.get("Thaumaturgy")], 
            3: [SpellRegistry.get("Hellish Rebuke")], 
            5: [SpellRegistry.get("Darkness")]
        }
    )

    # === Mordenkainen's Tome of Foes ===
    # Tiefling - Baalzebul
    bloodline_baalzebul = Subrace(
        name="Bloodline of Baalzebul",
        parent_race=RaceType.TIEFLING,
        description="The crumbling realm of Maladomini is ruled by Baalzebul, who excels at corrupting those whose minor sins can be transformed into acts of damnation. Tieflings linked to this archdevil can corrupt others both physically and psychically.",
        ability_score_increase={AbilityType.INT: 1},
        feats={ 1: [FeatureRegistry.get("Legacy of Maladomini", FeatureType.RACE, RaceType.TIEFLING)] },
        spells={
            0: [SpellRegistry.get("Thaumaturgy")], 
            3: [SpellRegistry.get("Ray of Sickness")], 
            5: [SpellRegistry.get("Crown of Madness")]
        }
    )

    # Tiefling - Dispater
    bloodline_dispater = Subrace(
        name="Bloodline of Dispater",
        parent_race=RaceType.TIEFLING,
        description="The great city of Dis occupies most of Hell's second layer. It is a place where secrets are uncovered and shared with the highest bidder, making tieflings tied to Dispater excellent spies and infiltrators.",
        ability_score_increase={AbilityType.DEX: 1},
        feats={ 1: [FeatureRegistry.get("Legacy of Dis", FeatureType.RACE, RaceType.TIEFLING)] },
        spells={
            0: [SpellRegistry.get("Thaumaturgy")], 
            3: [SpellRegistry.get("Disguise Self")], 
            5: [SpellRegistry.get("Detect Thoughts")]
        }
    )

    # Tiefling - Fierna
    bloodline_fierna = Subrace(
        name="Bloodline of Fierna",
        parent_race=RaceType.TIEFLING,
        description="A master manipulator, Fierna grants tieflings tied to her forceful personalities.",
        ability_score_increase={AbilityType.WIS: 1},
        feats={ 1: [FeatureRegistry.get("Legacy of Phlegethos", FeatureType.RACE, RaceType.TIEFLING)] },
        spells={
            0: [SpellRegistry.get("Friends")], 
            3: [SpellRegistry.get("Charm Person")], 
            5: [SpellRegistry.get("Suggestion")]
        }
    )

    # Tiefling - Glasya
    bloodline_glasya = Subrace(
        name="Bloodline of Glasya",
        parent_race=RaceType.TIEFLING,
        description="Glasya, Hell's criminal mastermind, grants her tiefiings magic that is useful for committing heists.",
        ability_score_increase={AbilityType.DEX: 1},
        feats={ 1: [FeatureRegistry.get("Legacy of Malbolge", FeatureType.RACE, RaceType.TIEFLING)] },
        spells={
            0: [SpellRegistry.get("Minor Illusion")], 
            3: [SpellRegistry.get("Disguise Self")], 
            5: [SpellRegistry.get("Invisibility")]
        }
    )

    # Tiefling - Levistus
    bloodline_levistus = Subrace(
        name="Bloodline of Levistus",
        parent_race=RaceType.TIEFLING,
        description="Frozen Stygia is ruled by Levistus, an archdevil known for offering bargains to those who face an inescapable doom.",
        ability_score_increase={AbilityType.CON: 1},
        feats={ 1: [FeatureRegistry.get("Legacy of Stygia", FeatureType.RACE, RaceType.TIEFLING)] },
        spells={
            0: [SpellRegistry.get("Ray of Frost")], 
            3: [SpellRegistry.get("Armor of Agathys")], 
            5: [SpellRegistry.get("Darkness")]
        }
    )

    # Tiefling - Mammon
    bloodline_mammon = Subrace(
        name="Bloodline of Mammon",
        parent_race=RaceType.TIEFLING,
        description="The great miser Mammon loves coins above all else. Tieflings tied to him excel at gathering and safeguarding wealth.",
        ability_score_increase={AbilityType.INT: 1},
        feats={ 1: [FeatureRegistry.get("Legacy of Minauros", FeatureType.RACE, RaceType.TIEFLING)] },
        spells={
            0: [SpellRegistry.get("Mage Hand")], 
            3: [SpellRegistry.get("Tenser's Floating Disk")], 
            5: [SpellRegistry.get("Arcane Lock")]
        }
    )

    # Tiefling - Mephistopheles
    bloodline_mephistopheles = Subrace(
        name="Bloodline of Mephistopheles",
        parent_race=RaceType.TIEFLING,
        description="In the frozen realm of Cania, Mephistopheles offers arcane power to those who entreat with him. Tieflings linked to him master some arcane magic.",
        ability_score_increase={AbilityType.INT: 1},
        feats={ 1: [FeatureRegistry.get("Legacy of Cania", FeatureType.RACE, RaceType.TIEFLING)] },
        spells={
            0: [SpellRegistry.get("Mage Hand")], 
            3: [SpellRegistry.get("Burning Hands")], 
            5: [SpellRegistry.get("Flame Blade")]
        }
    )

    # Tiefling - Zariel
    bloodline_zariel = Subrace(
        name="Bloodline of Zariel",
        parent_race=RaceType.TIEFLING,
        description="Tieflings with a blood tie to Zariel are stronger than the typical tiefling and receive magical abilities that aid them in battle.",
        ability_score_increase={AbilityType.STR: 1},
        feats={ 1: [FeatureRegistry.get("Legacy of Avernus", FeatureType.RACE, RaceType.TIEFLING)] },
        spells={
            0: [SpellRegistry.get("Thaumaturgy")], 
            3: [SpellRegistry.get("Searing Smite")], 
            5: [SpellRegistry.get("Branding Smite")]
        }
    )

    return [bloodline_asmodeus, 
            bloodline_baalzebul, 
            bloodline_dispater, 
            bloodline_fierna, 
            bloodline_glasya, 
            bloodline_levistus, 
            bloodline_mammon, 
            bloodline_mephistopheles, 
            bloodline_zariel]


def load_variant_tiefling_base():
    # Tiefling - Variant Base
    tiefling_variant_base = Race(
        name=RaceType.VARIANT_TIEFLING,
        description="Since not all tieflings are of the blood of Asmodeus, some have traits that differ from those in the Player's Handbook. The Dungeon Master may permit the following variants for your tiefling character, although Devil's Tongue, Hellfire, and Winged are mutually exclusive.",
        subrace=None,
        speed=30,
        size=Size.MEDIUM,
        ability_score_increase={AbilityType.DEX: 2, AbilityType.INT: 1},
        feats={ 1: [FeatureRegistry.get("Feral", FeatureType.RACE, RaceType.VARIANT_TIEFLING)] },
        info={
            "Appearance": "Your tiefling might not look like other tieflings. Rather than having the physical characteristics described in the Player's Handbook, choose 1d4 + 1 of the following features: small horns; fangs or sharp teeth; a forked tongue; catlike eyes; six fingers on each hand; goat-like legs; cloven hoofs; a forked tail; leathery or scaly skin; red or dark blue skin; cast no shadow or reflection; exude a smell of brimstone.",
        },
        languages=[Language.COMMON, Language.INFERNAL],
    )
    return tiefling_variant_base

def load_variant_tieflings():
    """Load Tiefling Variant subraces."""
    # === Sword Coast Adventurer's Guide ===
    # Tiefling - Variant: Devil's Tongue
    variant_devils_tongue = Subrace(
        name="Devil's Tongue",
        parent_race=RaceType.VARIANT_TIEFLING,
        description="Some tieflings inherit the charming tongue of devils rather than their fiery legacy.",
        feats={ 1: [FeatureRegistry.get("Devil's Tongue", FeatureType.RACE, RaceType.VARIANT_TIEFLING)]  },
        spells={
            0: [SpellRegistry.get("Vicious Mockery")],
            3: [SpellRegistry.get("Charm Person")],
            5: [SpellRegistry.get("Enthrall")],
        }
    )

    # Tiefling - Variant: Hellfire
    variant_hellfire = Subrace(
        name="Hellfire",
        parent_race=RaceType.VARIANT_TIEFLING,
        description="You wield flame as a natural gift of your infernal blood.",
        feats={ 1: [FeatureRegistry.get("Hellfire", FeatureType.RACE, RaceType.VARIANT_TIEFLING)]  },
        spells={
            0: [SpellRegistry.get("Thaumaturgy")], 
            3: [SpellRegistry.get("Burning Hands")], 
            5: [SpellRegistry.get("Darkness")],
        }
    )

    # Tiefling - Variant: Winged
    variant_winged = Subrace(
        name="Winged",
        parent_race=RaceType.VARIANT_TIEFLING,
        description="Bat-like wings grow from your shoulders, granting flight.",
        feats={ 1: [FeatureRegistry.get("Winged", FeatureType.RACE, RaceType.VARIANT_TIEFLING)]  },
        info={
            "Flight": "30 feet"
        }
    )

    return [variant_devils_tongue, variant_hellfire, variant_winged]


def load_ua_subraces():
    """Load Unearthed Aracana Tiefling subraces."""
    # === Unearthed Arcana 11 - That Old Black Magic ===
    # Abyssal Tiefling
    ua_abyssal_tiefling = Subrace(
        name="Abyssal Tiefling",
        parent_race=RaceType.TIEFLING,
        description="All abyssal tieflings trace their bloodline to the demons of the Abyss. These tieflings have the following additional features.",
        ability_score_increase={AbilityType.CON: 1},
        feats={
            1: [
                FeatureRegistry.get("Abyssal Arcana", FeatureType.RACE, RaceType.TIEFLING),
                FeatureRegistry.get("Abyssal Fortitude", FeatureType.RACE, RaceType.TIEFLING),
            ] 
        },
        spells={
            1: [
                SpellRegistry.get("Dancing Lights"),
                SpellRegistry.get("True Strike"),
                SpellRegistry.get("Light"),
                SpellRegistry.get("Message"),
                SpellRegistry.get("Spare the Dying"),
                SpellRegistry.get("Prestidigitation"),
            ], 
            3: [
                SpellRegistry.get("Burning Hands"),
                SpellRegistry.get("Charm Person"),
                SpellRegistry.get("Magic Missile"),
                SpellRegistry.get("Cure Wounds"),
                SpellRegistry.get("Tasha's Hideous Laughter"),
                SpellRegistry.get("Thunderwave"),
            ], 
            5: [
                SpellRegistry.get("Alter Self"),
                SpellRegistry.get("Darkness"),
                SpellRegistry.get("Invisibility"),
                SpellRegistry.get("Levitate"),
                SpellRegistry.get("Mirror Image"),
                SpellRegistry.get("Spider Climb"),
            ]
        },
        languages=[Language.ABYSSAL],
    )

    return [ua_abyssal_tiefling]


def get_tiefling_races():
    """Load a list of defined Tiefling Races"""
    tieflings: list[Race] = [] # Empty array
    tiefling_base = load_tiefling_base()
    tieflings.append(tiefling_base)

    # Tiefling Bloodlines
    bloodline_tieflings = load_bloodline_tieflings()
    print("> Creating Tiefling Bloodline subraces")
    for bloodline in bloodline_tieflings:
        tieflings.append(create_subrace_variant(tiefling_base, bloodline))

    ua_tieflings = load_ua_subraces()
    print("> Creating Unearthed Arcana Tiefling subraces")
    for ua in ua_tieflings:
        tieflings.append(create_subrace_variant(tiefling_base, ua))

    # Variant Tiefling
    variant_tiefling_base = load_variant_tiefling_base()
    tieflings.append(variant_tiefling_base)

    variant_tieflings = load_variant_tieflings()
    print("> Creating Tiefling Variant subraces")
    for variant in variant_tieflings:
        tieflings.append(create_subrace_variant(variant_tiefling_base, variant))

    return tieflings
    