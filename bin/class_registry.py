# class_registry.py

from typing import Dict
from class_base import Class, ClassType
from ability import AbilityType, Skill
from items.tool_item import ToolItem
from equipment import ArmorType, WeaponType

class ClassRegistry:
    _registry: Dict[ClassType, Class] = {}

    @classmethod
    def register(cls, class_obj: Class):
        cls._registry[class_obj.name] = class_obj

    @classmethod
    def get(cls, class_type: ClassType) -> Class:
        return cls._registry[class_type]

    @classmethod
    def all(cls) -> Dict[ClassType, Class]:
        return cls._registry.copy()
    
    @classmethod
    def register_defaults(cls):
        """Register the default core classes. Add more as needed."""
        fighter = Class(
            name=ClassType.FIGHTER,
            hit_die=10,
            fixed_hp_per_level=6,
            prof_armors=[ArmorType.LIGHT, ArmorType.MEDIUM, ArmorType.HEAVY, ArmorType.SHIELD],
            prof_weapons=[WeaponType.SIMPLE, WeaponType.MARTIAL],
            prof_saving_throws=[AbilityType.STRENGTH, AbilityType.CONSTITUTION],
            prof_skills=[
                Skill.ACROBATICS, Skill.ANIMAL_HANDLING, Skill.ATHLETICS,
                Skill.HISTORY, Skill.INSIGHT, Skill.INTIMIDATION,
                Skill.PERCEPTION, Skill.SURVIVAL
            ],
            skill_choices=2,
            prof_tools=[],  # Fighter has none
        )

        cls.register(fighter)

        # TODO: Add other classes
        # - barbarian = Class(...)
        # - cleric = Class(...)
        # - rogue = Class(...)
