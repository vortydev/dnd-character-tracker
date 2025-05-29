# class_.py
from typing import Optional, Dict, List
from enum import Enum
from collections import defaultdict

from subclass_ import SubclassType
from ability import AbilityType, Skill
from equipment import ArmorType, WeaponType

# ===== Classes =====
class ClassType(Enum):
    """Enum representing the available classes."""
    BARBARIAN = "Barbarian"
    BARD = "Bard"
    CLERIC = "Cleric"
    DRUID = "Druid"
    FIGHTER = "Fighter"
    MONK = "Monk"
    PALADIN = "Paladin"
    RANGER = "Ranger"
    ROGUE = "Rogue"
    SORCERER = "Sorcerer"
    WARLOCK = "Warlock"
    WIZARD = "Wizard"
    ARTIFICER = "Artificer"


# === Mapping ===
SUBCLASS_MAP = {
    # Fighter
    SubclassType.BATTLE_MASTER: ClassType.FIGHTER,
    SubclassType.CHAMPION: ClassType.FIGHTER,
    SubclassType.ELDRITCH_KNIGHT: ClassType.FIGHTER,
    SubclassType.ARCANE_ARCHER: ClassType.FIGHTER,
    SubclassType.CAVALIER: ClassType.FIGHTER,
    SubclassType.SAMURAI: ClassType.FIGHTER,
    SubclassType.PSI_WARRIOR: ClassType.FIGHTER,
    SubclassType.RUNE_KNIGHT: ClassType.FIGHTER,
    SubclassType.BANNERET: ClassType.FIGHTER,
    SubclassType.ECHO_KNIGHT: ClassType.FIGHTER,

    # WIP Sorcerer
    SubclassType.DRACONIC_BLOODLINE: ClassType.SORCERER,

    # Wizard
    SubclassType.ABJURATION: ClassType.WIZARD,
    SubclassType.CONJURATION: ClassType.WIZARD,
    SubclassType.DIVINATION: ClassType.WIZARD,
    SubclassType.ENCHANTMENT: ClassType.WIZARD,
    SubclassType.EVOCATION: ClassType.WIZARD,
    SubclassType.ILLUSION: ClassType.WIZARD,
    SubclassType.NECROMANCY: ClassType.WIZARD,
    SubclassType.TRANSMUTATION: ClassType.WIZARD,
    SubclassType.BLADESINGING: ClassType.WIZARD,
    SubclassType.WAR_MAGIC: ClassType.WIZARD,
    SubclassType.ORDER_OF_SCRIBES: ClassType.WIZARD,
    SubclassType.GRAVITURGY_MAGIC: ClassType.WIZARD,
    SubclassType.CHRONURGY_MAGIC: ClassType.WIZARD,
}


SUBCLASSES_BY_CLASS = defaultdict(list)
for sc, c in SUBCLASS_MAP.items():
    SUBCLASSES_BY_CLASS[c].append(sc)


SUBCLASS_MIN_LEVEL = {
    ClassType.FIGHTER: 3,
    ClassType.SORCERER: 1,
    ClassType.WIZARD: 2,
    # WIP
}

def validate_subclass_assignment(class_type: ClassType, level: int, subclass: SubclassType):
    required = SUBCLASS_MIN_LEVEL.get(class_type, 3)
    if level < required:
        raise ValueError(f"{subclass.name} requires at least level {required} in {class_type.name}")


# WIP
# TODO Add Hit point logic
# TODO Add subclass
# TODO Add Tools
# TODO add skill pools => selected skills in character
# TODO proficiency bonus => calculated based on global character level
# TODO SpellSlot object
class Class:
    """Represents a playable class with optional subclass."""

    def __init__(self, 
                 name: ClassType,
                 prof_armors: Optional[List[ArmorType]] = None,
                 prof_weapons: Optional[List[WeaponType]] = None,
                 prof_saving_throws: Optional[List[AbilityType]] = None,
                 prof_skills: Optional[List[Skill]] = None,
                 prof_tools: Optional[List[str]] = None,
                ):
        self.name = name    # Class name
        self.proficiency_armor = prof_armors or []      # Armor proficiencies
        self.proficiency_weapons = prof_weapons or []   # Weapon proficiencies
        self.proficiency_saving_throws = prof_saving_throws or []
        self.proficiency_skill_pool = prof_skills or []
        self.chosen_skills: list[Skill] = []

    # TODO describe method

    # TODO to_dict method

    # TODO from_dict method
    # @staticmethod

    # TODO __str__ method
