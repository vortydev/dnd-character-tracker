# class_list/fighter.py
from class_base import Class, ClassType
from equipment import ArmorType, WeaponType
from ability import AbilityType, Skill

def get_fighter_class() -> Class:
    return Class(
        name=ClassType.FIGHTER,
        hit_die=10,
        fixed_hp_per_level=6,
        prof_armors=[ArmorType.LIGHT, ArmorType.MEDIUM, ArmorType.HEAVY, ArmorType.SHIELD],
        prof_weapons=[WeaponType.SIMPLE, WeaponType.MARTIAL],
        prof_saving_throws=[AbilityType.STR, AbilityType.CON],
        prof_skills=[
            Skill.ACROBATICS, Skill.ANIMAL_HANDLING, Skill.ATHLETICS,
            Skill.HISTORY, Skill.INSIGHT, Skill.INTIMIDATION,
            Skill.PERCEPTION, Skill.SURVIVAL
        ],
        skill_choices=2
    )
