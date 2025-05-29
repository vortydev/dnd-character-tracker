# feature_list/class_features/fighter_features.py
from class_base import ClassType
from class_feature import ClassFeature

# === Fighting Style ===
fig_feat_fighting_style = ClassFeature(
    name="Fighting Style",
    description="You adopt a particular style of fighting as your specialty. Choose one of the following options. You can't take a Fighting Style option more than once, even if you later get to choose again.",
    class_type=ClassType.FIGHTER,
    subfeatures=[
        ClassFeature(name="Archery (PHB)",
            description="You gain a +2 bonus to attack rolls you make with ranged weapons.",
            class_type=ClassType.FIGHTER),
        ClassFeature(name="Blind Fighting (TCE)",
            description="You have blindsight with a range of 10 feet. Within that range, you can effectively see anything that isn't behind total cover, even if you're blinded or in darkness. Moreover, you can see an invisible creature within that range, unless the creature successfully hides from you.",
            class_type=ClassType.FIGHTER),
        ClassFeature(name="Defense (PHB)",
            description="While you are wearing armor, you gain a +1 bonus to AC.",
            class_type=ClassType.FIGHTER),
        ClassFeature(name="Dueling (PHB)",
            description="When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon.",
            class_type=ClassType.FIGHTER),
        ClassFeature(name="Great Weapon Fighting (PHB)",
            description="When you roll a 1 or 2 on a damage die for an attack you make with a melee weapon that you are wielding with two hands, you can reroll the die and must use the new roll, even if the new roll is a 1 or a 2. The weapon must have the two-handed or versatile property for you to gain this benefit.",
            class_type=ClassType.FIGHTER),
        ClassFeature(name="Interception (TCE)",
            description="When a creature you can see hits a target, other than you, within 5 feet of you with an attack, you can use your reaction to reduce the damage the target takes by 1d10 + your proficiency bonus (to a minimum of 0 damage). You must be wielding a shield or a simple or martial weapon to use this reaction.",
            class_type=ClassType.FIGHTER),
        ClassFeature(name="Protection (PHB)",
            description="When a creature you can see attacks a target other than you that is within 5 feet of you, you can use your reaction to impose disadvantage on the attack roll. You must be wielding a shield.",
            class_type=ClassType.FIGHTER),
        ClassFeature(name="Superior Technique (TCE)",
            description="You learn one maneuver of your choice from among those available to the Battle Master archetype. If a maneuver you use requires your target to make a saving throw to resist the maneuver's effects, the saving throw DC equals 8 + your proficiency bonus + your Strength or Dexterity modifier (your choice.)\
                \nYou gain one superiority die, which is a d6 (this die is added to any superiority dice you have from another source). This die is used to fuel your maneuvers. A superiority die is expended when you use it. You regain your expended superiority dice when you finish a short or long rest.",
            class_type=ClassType.FIGHTER),
        ClassFeature(name="Thrown Weapon Fighting (TCE)",
            description="You can draw a weapon that has the thrown property as part of the attack you make with the weapon.\
                \nIn addition, when you hit with a ranged attack using a thrown weapon, you gain a +2 bonus to the damage roll.",
            class_type=ClassType.FIGHTER),
        ClassFeature(name="Two-Weapon Fighting (PHB)",
            description="When you engage in two-weapon fighting, you can add your ability modifier to the damage of the second attack.",
            class_type=ClassType.FIGHTER),
        ClassFeature(name="Unarmed Fighting (TCE)",
            description="Your unarmed strikes can deal bludgeoning damage equal to 1d6 + your Strength modifier on a hit. If you aren't wielding any weapons or a shield when you make the attack roll, the d6 becomes a d8.\
                \nAt the start of each of your turns, you can deal 1d4 bludgeoning damage to one creature grappled by you.",
            class_type=ClassType.FIGHTER),
    ]
)

# === Second Wind ===
fig_feat_second_wind = ClassFeature(
    name="Second Wind",
    description="You have a limited well of stamina that you can draw on to protect yourself from harm. On your turn, you can use a bonus action to regain hit points equal to 1d10 + your fighter level.\
        \nOnce you use this feature, you must finish a short or long rest before you can use it again.",
    class_type=ClassType.FIGHTER
)

# === Action Surge ===
fig_feat_action_surge = ClassFeature(
    name="Action Surge",
    description="Starting at 2nd level, you can push yourself beyond your normal limits for a moment. On your turn, you can take one additional action.\
        \nOnce you use this feature, you must finish a short or long rest before you can use it again. Starting at 17th level, you can use it twice before a rest, but only once on the same turn.",
    class_type=ClassType.FIGHTER
)

# === Martial Archetype ===
fig_feat_martial_archetype = ClassFeature(
    name="Martial Archetype",
    description="At 3rd level, you choose an archetype that you strive to emulate in your combat styles and techniques. The archetype you choose grants you features at 3rd level and again at 7th, 10th, 15th, and 18th level.",
    class_type=ClassType.FIGHTER
)

# === Ability Score Improvement ===
fig_feat_ability_score_improvement = ClassFeature(
    name="Ability Score Improvement",
    description="When you reach 4th level, and again at 6th, 8th, 12th, 14th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.",
    class_type=ClassType.FIGHTER
)

# === Martial Versatility (Optional) ===
fig_feat_martial_versatility = ClassFeature(
    name="Martial Versatility (Optional)",
    description="Whenever you reach a level in this class that grants the Ability Score Improvement feature, you can do one of the following, as you shift the focus of your martial practice:\
        \n- Replace a fighting style you know with another fighting style available to fighters.\
        \n- If you know any maneuvers from the Battle Master archetype, you can replace one maneuver you know with a different maneuver.",
    class_type=ClassType.FIGHTER
)

# === Extra Attack ===
fig_feat_extra_attack = ClassFeature(
    name="Extra Attack",
    description="Beginning at 5th level, you can attack twice, instead of once, whenever you take the Attack action on your turn.\
        \nThe number of attacks increases to three when you reach 11th level in this class and to four when you reach 20th level in this class.",
    class_type=ClassType.FIGHTER
)

# === Indomitable ===
fig_feat_indomitable = ClassFeature(
    name="Indomitable",
    description="Beginning at 9th level, you can reroll a saving throw that you fail. If you do so, you must use the new roll, and you can't use this feature again until you finish a long rest.\
        \nYou can use this feature twice between long rests starting at 13th level and three times between long rests starting at 17th level.",
    class_type=ClassType.FIGHTER
)


# === Array of Fighter class features
fig_feats: list[ClassFeature] = [
    fig_feat_fighting_style,
    fig_feat_second_wind,
    fig_feat_action_surge,
    fig_feat_martial_archetype,
    fig_feat_ability_score_improvement,
    fig_feat_martial_versatility,
    fig_feat_extra_attack,
    fig_feat_indomitable
]
