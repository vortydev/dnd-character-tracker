# class_list/druid.py
from class_base import Class, ClassType
from equipment import WeaponName, ArmorType
from ability import AbilityType, Skill
# from items.tool_item import ToolItem, ToolType

def get_druid_class() -> Class:
    return Class(
        name=ClassType.DRUID,
        hit_dice=8,
        hp_1st_level=8,
        fixed_hp_per_level=5,
        prof_armors=[
            ArmorType.LIGHT, ArmorType.MEDIUM, ArmorType.SHIELD
        ],
        prof_specific_weapons=[
            WeaponName.CLUB, WeaponName.DAGGER, WeaponName.DART, 
            WeaponName.MACE, WeaponName.QUARTERSTAFF, WeaponName.SCIMITAR, 
            WeaponName.SICKLE, WeaponName.SLING, WeaponName.SPEAR
        ],
        prof_saving_throws=[AbilityType.INT, AbilityType.WIS],
        prof_skills=[
            Skill.ARCANA, Skill.ANIMAL_HANDLING, Skill.INSIGHT,
            Skill.MEDICINE, Skill.NATURE, Skill.PERCEPTION,
            Skill.RELIGION, Skill.SURVIVAL
        ],
        skill_choices=2,
        # prof_tools=["Herbalism kit"] # TODO
        description="Whether calling on the elemental forces of nature or emulating the creatures of the animal world, druids are an embodiment of nature's resilience, cunning, and fury. They claim no mastery over nature, but see themselves as extensions of nature's indomitable will.",
        requisite="You must have a Wisdom score of 13 or higher in order to multiclass in or out of this class.",
    )
