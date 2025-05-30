# class_list/fighter.py
from class_base import Class, ClassType
from equipment import ArmorType, WeaponType
from ability import AbilityType, Skill

def get_fighter_class() -> Class:
    return Class(
        name=ClassType.FIGHTER,
        hit_dice=10,
        hp_1st_level=10,
        fixed_hp_per_level=6,
        prof_armors=[ArmorType.LIGHT, ArmorType.MEDIUM, ArmorType.HEAVY, ArmorType.SHIELD],
        prof_weapons=[WeaponType.SIMPLE, WeaponType.MARTIAL],
        prof_saving_throws=[AbilityType.STR, AbilityType.CON],
        prof_skills=[
            Skill.ACROBATICS, Skill.ANIMAL_HANDLING, Skill.ATHLETICS,
            Skill.HISTORY, Skill.INSIGHT, Skill.INTIMIDATION,
            Skill.PERCEPTION, Skill.SURVIVAL
        ],
        skill_choices=2,
        description="Fighters share an unparalleled mastery with weapons and armor, and a thorough knowledge of the skills of combat. They are well acquainted with death, both meting it out and staring it defiantly in the face.",
        requisite="You must have a Dexterity or Strength score of 13 or higher in order to multiclass in or out of this class.",
    )
