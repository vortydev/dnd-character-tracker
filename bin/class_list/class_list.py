# class_list/class_list.py
from class_base import Class, ClassType
from equipment import WeaponName, WeaponType, ArmorType
from ability import AbilityType, Skill
from items.tool_item import ToolItem, ToolType

# TODO Artificer
def get_artificer_class() -> Class:
    """Get Artificer Class object"""
    ARTIFICER = Class(
        name=ClassType.ARTIFICER,
        hit_dice=8,
        hp_1st_level=8,
        fixed_hp_per_level=5,
        prof_armors=[
            ArmorType.LIGHT, ArmorType.MEDIUM, ArmorType.SHIELD
        ],
        prof_weapons=[ WeaponType.SIMPLE ],
        prof_saving_throws=[ AbilityType.CON, AbilityType.INT ],
        prof_skills=[
            Skill.ARCANA, Skill.HISTORY, Skill.INVESTIGATION,
            Skill.MEDICINE, Skill.NATURE, Skill.PERCEPTION, Skill.SLEIGHT_OF_HAND,
        ],
        skill_choices=2,
        # TODO thieves tools, tinkers tools, one type of artisans tools of your choice
        description="TODO Artificer description",
        requisite="TODO Artificer description requisite",
    )
    return ARTIFICER

# Druid
def get_druid_class() -> Class:
    """Get Druid Class object"""
    DRUID = Class(
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
    return DRUID

# Fighter
def get_fighter_class() -> Class:
    """Get Fighter Class object"""
    FIGHTER = Class(
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
    return FIGHTER

# WIP Ranger
def get_ranger_class() -> Class:
    """Get Ranger Class object"""
    RANGER = Class(
        name=ClassType.RANGER,
        hit_dice=10,
        hp_1st_level=10,
        fixed_hp_per_level=6,
        prof_armors=[
            ArmorType.LIGHT, ArmorType.MEDIUM, ArmorType.SHIELD
        ],
        prof_weapons=[
            WeaponType.SIMPLE, WeaponType.MARTIAL
        ],
        prof_saving_throws=[
            AbilityType.STR, AbilityType.DEX
        ],
        prof_skills=[
            Skill.ANIMAL_HANDLING, Skill.ATHLETICS, 
            Skill.INSIGHT, Skill.INVESTIGATION, Skill.NATURE,
            Skill.PERCEPTION, Skill.STEALTH, Skill.SURVIVAL
        ],
        skill_choices=3,
        description="Far fram the bustle of cities and towns, past the hedges that shelter the most distant farms fram the terrors of the wild, amid the dense-packed trees of trackJess forests and across wide and empty plains, rangers keep their unending watch.",
        requisite="You must have a Dexterity or Wisdom score of 13 or higher in order to multiclass in or out of this class.",
    )
    return RANGER

# WIP Rogue
def get_rogue_class() -> Class:
    """Get Rogue Class object"""
    ROGUE = Class(
        name=ClassType.ROGUE,
        hit_dice=8,
        hp_1st_level=8,
        fixed_hp_per_level=5,
        prof_armors=[ ArmorType.LIGHT ],
        prof_weapons=[ WeaponType.SIMPLE ],
        prof_specific_weapons=[ 
            WeaponName.HAND_CROSSBOW, WeaponName.LONGSWORD, 
            WeaponName.RAPIER, WeaponName.SHORTSWORD 
        ],
        prof_saving_throws=[ AbilityType.STR, AbilityType.CON ],
        prof_skills=[
            Skill.ACROBATICS, Skill.ATHLETICS, Skill.DECEPTION,
            Skill.INSIGHT, Skill.INTIMIDATION, Skill.INVESTIGATION,
            Skill.PERCEPTION, Skill.PERFORMANCE, Skill.PERSUASION,
            Skill.SLEIGHT_OF_HAND, Skill.STEALTH,
        ],
        skill_choices=4,
        # TODO tools=[ ThievesTools ],
        description="TODO Rogue description",
        requisite="You must have a Dexterity or Strength score of 13 or higher in order to multiclass in or out of this class.",
    )
    return ROGUE

# Sorcerer
def get_sorcerer_class() -> Class:
    """Get Sorcerer Class object"""
    SORCERER = Class(
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
    return SORCERER

# Wizard
def get_wizard_class() -> Class:
    """Get Wizard Class object"""
    WIZARD = Class(
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
    return WIZARD
