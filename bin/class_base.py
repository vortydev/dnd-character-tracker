# class_.py
from typing import Optional, Dict, List
from enum import Enum
from collections import defaultdict

from subclass_ import SubclassType
from ability import AbilityType, Skill
from equipment import ArmorType, WeaponType, WeaponName
from items.tool_item import ToolItem

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


class Class:
    """Represents a playable class (e.g., Fighter), not tied to any specific character."""

    def __init__(self, 
                 name: ClassType,
                 hit_dice: int,
                 hp_1st_level: int,
                 hp_ability_mod: AbilityType = AbilityType.CON,
                 fixed_hp_per_level: Optional[int] = None,
                 prof_armors: Optional[List[ArmorType]] = None,
                 prof_weapons: Optional[List[WeaponType]] = None,
                 prof_specific_weapons: Optional[List[WeaponName]] = None,
                 prof_saving_throws: Optional[List[AbilityType]] = None,
                 prof_skills: Optional[List[Skill]] = None,
                 prof_tools: Optional[List[ToolItem]] = None,
                 skill_choices: int = 0,
                 description: Optional[str] = None,
                 requisite: Optional[str] = None,
                ):
        self.name = name  # ClassType enum
        self.description = description
        self.requisite = requisite

        # Hit Point info
        self.hit_dice = hit_dice  # e.g., 10 for Fighter
        self.hp_1st_level = hp_1st_level
        self.hp_ability_mod = hp_ability_mod
        self.fixed_hp_per_level = fixed_hp_per_level or (hit_dice // 2 + 1)  # e.g., 6 for d10

        # Proficiencies
        self.proficiency_armor = prof_armors or []
        self.proficiency_weapons = prof_weapons or []
        self.proficiency_specific_weapons = prof_specific_weapons or []
        self.proficiency_saving_throws = prof_saving_throws or []
        self.proficiency_skill_pool = prof_skills or []
        self.proficiency_tools = prof_tools or []

        self.skill_choices = skill_choices  # e.g., choose 2 from pool

    def to_dict(self) -> Dict:
        return {
            "name": self.name.value,
            "description": self.description,
            "requisite": self.requisite,
            "hit_dice": self.hit_dice,
            "hp_1st_level": self.hp_1st_level,
            "hp_ability_mod": self.hp_ability_mod.value,
            "fixed_hp_per_level": self.fixed_hp_per_level,
            "proficiency_armor": [a.value for a in self.proficiency_armor],
            "proficiency_weapons": [w.value for w in self.proficiency_weapons],
            "proficiency_specific_weapons": [w.value for w in self.proficiency_specific_weapons],
            "proficiency_saving_throws": [a.value for a in self.proficiency_saving_throws],
            "proficiency_skill_pool": [s.value for s in self.proficiency_skill_pool],
            "proficiency_tools": [t.to_dict() for t in self.proficiency_tools],
            "skill_choices": self.skill_choices,
        }

    @staticmethod
    def from_dict(data: Dict) -> "Class":
        # Assuming ArmorType, WeaponType, AbilityType, Skill, ToolItem have enums or lookup methods
        return Class(
            name=ClassType(data["name"]),
            hit_dice=data["hit_dice"],
            hp_1st_level=data["hp_1st_level"],
            hp_ability_mod=AbilityType(data["hp_ability_mod"]),
            fixed_hp_per_level=data.get("fixed_hp_per_level"),
            prof_armors=[ArmorType(a) for a in data["proficiency_armor"]],
            prof_weapons=[WeaponType(w) for w in data["proficiency_weapons"]],
            prof_specific_weapons=[WeaponName(w) for w in data["proficiency_specific_weapons"]],
            prof_saving_throws=[AbilityType(a) for a in data["proficiency_saving_throws"]],
            prof_skills=[Skill(s) for s in data["proficiency_skill_pool"]],
            prof_tools=[ToolItem(t) for t in data["proficiency_tools"]],
            skill_choices=data.get("skill_choices", 0),
            description=data.get("description"),
            requisite=data.get("requisite"),
        )