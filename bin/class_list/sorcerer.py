# class_list/sorcerer.py
from class_base import Class, ClassType
from equipment import WeaponName
from ability import AbilityType, Skill

def get_sorcerer_class() -> Class:
    return Class(
        name=ClassType.SORCERER,
        hit_dice=6,
        hp_1st_level=6,
        fixed_hp_per_level=4,
        prof_specific_weapons=[
            WeaponName.DAGGER, WeaponName.DART, WeaponName.SLING, 
            WeaponName.QUARTERSTAFF, WeaponName.LIGHT_CROSSBOW
        ],
        prof_saving_throws=[AbilityType.CON, AbilityType.CHA],
        prof_skills=[
            Skill.ARCANA, Skill.DECEPTION, Skill.INSIGHT,
            Skill.INTIMIDATION, Skill.PERSUASION, Skill.RELIGION,
        ],
        skill_choices=2,
        description="Sorcerers carry a magical birthright conferred upon them by an exotic bloodline, some otherworldly influence, or exposure to unknown cosmic forces. No one chooses sorcery; the power chooses the sorcerer.",
        requisite="You must have a Charisma score of 13 or higher in order to multiclass in or out of this class.",
    )
