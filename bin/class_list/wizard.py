# class_list/wizard.py
from class_base import Class, ClassType
from equipment import WeaponName
from ability import AbilityType, Skill

def get_wizard_class() -> Class:
    return Class(
        name=ClassType.WIZARD,
        hit_dice=6,
        hp_1st_level=6,
        fixed_hp_per_level=4,
        prof_specific_weapons=[
            WeaponName.DAGGER, WeaponName.DART, WeaponName.SLING, 
            WeaponName.QUARTERSTAFF, WeaponName.LIGHT_CROSSBOW
        ],
        prof_saving_throws=[AbilityType.INT, AbilityType.WIS],
        prof_skills=[
            Skill.ARCANA, Skill.HISTORY, Skill.INSIGHT,
            Skill.INVESTIGATION, Skill.MEDICINE, Skill.RELIGION,
        ],
        skill_choices=2,
        description="Wizards are supreme magic-users, defined and united as a class by the spells they cast. Drawing on the subtle weave of magic that permeates the cosmos, wizards cast spells of explosive fire, arcing lightning, subtle deception, brute-force mind control, and much more.",
        requisite="You must have an Intelligence score of 13 or higher in order to multiclass in or out of this class.",
    )
