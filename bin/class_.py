# class_.py
from typing import Optional, Dict, List
from enum import Enum

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

# WIP
SUBCLASS_MIN_LEVEL = {
    ClassType.WIZARD: 2,
    ClassType.FIGHTER: 3,
    # etc.
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
# TODO proficiency bonus
# TODO SpellSlot object
class Class:
    """Represents a playable class with optional subclass."""

    def __init__(self, 
                 name: ClassType,
                 prof_armors: Optional[List[ArmorType]] = None,
                 prof_weapons: Optional[List[WeaponType]] = None,
                 prof_saving_throws: Optional[List[AbilityType]] = None,
                 prof_skills: Optional[List[Skill]] = None,
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
