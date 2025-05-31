# spell_list/lvl1_spell_list.py
from typing import List
from common import ActionCost
from spell import Spell, SpellSchool, SpellComponent

# === Define spells ===
lvl1_animal_friendship = Spell(
    name="Animal Friendship",
    level=1,
    school=SpellSchool.ENCHANTMENT,
    action_cost=ActionCost.ACTION,
    description="This spell lets you convince a beast that you mean it no harm. Choose a beast that you can see within range. It must see and hear you. If the beast's Intelligence is 4 or higher, the spell fails. Otherwise, the beast must succeed on a Wisdom saving throw or be charmed by you for the spell's duration. If you or one of your companions harms the target, the spell ends.",
    higher_levels="When you cast this spell using a spell slot of 2nd level or higher, you can affect one additional beast for each slot level above 1st.",
    duration="24 hours",
    casting_time="1 action",
    s_range="30 feet",
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=["a morsel of food"],
)

lvl1_armor_of_agathys = Spell(
    name="Armor of Agathys",
    level=1,
    school=SpellSchool.ABJURATION,
    action_cost=ActionCost.ACTION,
    description="A protective magical force surrounds you, manifesting as a spectral frost that covers you and your gear. You gain 5 temporary hit points for the duration. If a creature hits you with a melee attack while you have these hit points, the creature takes 5 cold damage.",
    higher_levels="When you cast this spell using a spell slot of 2nd level or higher, both the temporary hit points and the cold damage increase by 5 for each slot.",
    duration="1 hour",
    casting_time="1 action",
    s_range="Self",
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=["a cup of water"],
)
lvl1_burning_hands = Spell(
    name="Burning Hands",
    level=1,
    school=SpellSchool.EVOCATION,
    action_cost=ActionCost.ACTION,
    description="As you hold your hands with thumbs touching and fingers spread, a thin sheet of flames shoots forth from your outstretched fingertips. Each creature in a 15-foot cone must make a Dexterity saving throw. A creature takes 3d6 fire damage on a failed save, or half as much damage on a successful one.\
        \nThe fire ignites any flammable objects in the area that aren't being worn or carried.",
    higher_levels="When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d6 for each slot level above 1st.",
    duration="Instantaneous",
    casting_time="1 action",
    s_range="Self (15-foot cone)",
    components=[SpellComponent.V, SpellComponent.S],
)
lvl1_charm_person = Spell(
    name="Charm Person",
    level=1,
    school=SpellSchool.ENCHANTMENT,
    action_cost=ActionCost.ACTION,
    description="You attempt to charm a humanoid you can see within range. It must make a Wisdom saving throw, and does so with advantage if you or your companions are fighting it. If it fails the saving throw, it is charmed by you until the spell ends or until you or your companions do anything harmful to it. The charmed creature regards you as a friendly acquaintance. When the spell ends, the creature knows it was charmed by you.",
    higher_levels="When you cast this spell using a spell slot of 2nd level or higher, you can target one additional creature for each slot level above 1st. The creatures must be within 30 feet of each other when you target them.",
    duration="1 hour",
    casting_time="1 action",
    s_range="30 feet",
    components=[SpellComponent.V, SpellComponent.S],
)

lvl1_cure_wounds = Spell(
    name="Cure Wounds",
    level=1,
    school=SpellSchool.EVOCATION,
    action_cost=ActionCost.ACTION,
    description="A creature you touch regains a number of hit points equal to 1d8 + your spellcasting ability modifier. This spell has no effect on undead or constructs.",
    higher_levels="When you cast this spell using a spell slot of 2nd level or higher, the healing increases by 1d8 for each slot level above 1st.",
    duration="Instantaneous",
    casting_time="1 action",
    s_range="Touch",
    components=[SpellComponent.V, SpellComponent.S],
)

lvl1_disguise_self = Spell(
    name="Disguise Self",
    level=1,
    school=SpellSchool.ILLUSION,
    action_cost=ActionCost.ACTION,
    description="You make yourself – including your clothing, armor, weapons, and other belongings on your person – look different until the spell ends or until you use your action to dismiss it. You can seem 1 foot shorter or taller and can appear thin, fat, or in between. You can't change your body type, so you must adopt a form that has the same basic arrangement of limbs. Otherwise, the extent of the illusion is up to you.\nThe changes wrought by this spell fail to hold up to physical inspection. For example, if you use this spell to add a hat to your outfit, objects pass through the hat, and anyone who touches it would feel nothing or would feel your head and hair. If you use this spell to appear thinner than you are, the hand of someone who reaches out to touch you would bump into you while it was seemingly still in midair. To discern that you are disguised, a creature can use its action to inspect your appearance and must succeed on an Intelligence (Investigation) check against your spell save DC.",
    duration="1 hour",
    casting_time="1 action",
    s_range="Self",
    components=[SpellComponent.V, SpellComponent.S],
)
lvl1_hellish_rebuke = Spell(
    name="Hellish Rebuke",
    level=1,
    school=SpellSchool.EVOCATION,
    action_cost=ActionCost.REACTION,
    description="You point your finger, and the creature that damaged you is momentarily surrounded by hellish flames. The creature must make a Dexterity saving throw. It takes 2d10 fire damage on a failed save, or half as much damage on a successful one.",
    higher_levels="When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d10 for each slot level above 1st.",
    duration="Instantaneous",
    casting_time="1 reaction",
    s_range="60 feet",
    components=[SpellComponent.V, SpellComponent.S],
)

lvl1_magic_missile = Spell(
    name="Magic Missile",
    level=1,
    school=SpellSchool.EVOCATION,
    action_cost=ActionCost.ACTION,
    description="You create three glowing darts of magical force. Each dart hits a creature of your choice that you can see within range. A dart deals 1d4 + 1 force damage to its target. The darts all strike simultaneously and you can direct them to hit one creature or several.",
    higher_levels="When you cast this spell using a spell slot of 2nd level or higher, the spell creates one more dart for each slot level above 1st.",
    duration="Instantaneous",
    casting_time="1 action",
    s_range="120 feet",
    components=[SpellComponent.V, SpellComponent.S],
)

lvl1_ray_of_sickness = Spell(
    name="Ray of Sickness",
    level=1,
    school=SpellSchool.NECROMANCY,
    action_cost=ActionCost.ACTION,
    description="A ray of sickening greenish energy lashes out toward a creature within range. Make a ranged spell attack against the target. On a hit, the target takes 2d8 poison damage and must make a Constitution saving throw. On a failed save, it is also poisoned until the end of your next turn.",
    higher_levels="When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d8 for each slot level above 1st.",
    duration="Instantaneous",
    casting_time="1 action",
    s_range="60 feet",
    components=[SpellComponent.V, SpellComponent.S],
)
lvl1_searing_smite = Spell(
    name="Searing Smite",
    level=1,
    school=SpellSchool.EVOCATION,
    action_cost=ActionCost.BONUS_ACTION,
    description="The next time you hit a creature with a melee weapon attack during this spell's duration, your weapon flares with white-hot intensity.\nAt the start of each of its turns until the spell ends, the target must make a Constitution saving throw. On a failed save, it takes 1d6 fire damage. On a successful save, the spells ends. If the target or a creature within 5 feet of it uses an action to put out the flames, or if some other effect douses the flames (such as the target being submerged in water), the spell ends.",
    higher_levels="When you cast this spell using a spell slot of 2nd level or higher, the initial extra damage dealt by the attack increases by 1d6 for each slot above 1st.",
    duration="Concentration, up to 1 minute",
    casting_time="1 bonus action",
    s_range="Self",
    components=[SpellComponent.V],
)

lvl1_tashas_hideous_laughter = Spell(
    name="Tasha's Hideous Laughter",
    level=1,
    school=SpellSchool.ENCHANTMENT,
    action_cost=ActionCost.ACTION,
    description="A creature of your choice that you can see within range perceives everything as hilariously funny and falls into fits of laughter if this spell affects it. The target must succeed on a Wisdom saving throw or fall prone, becoming incapacitated and unable to stand up for the duration. A creature with an Intelligence score of 4 or less isn't affected.\
        \nAt the end of each of its turns, and each time it takes damage, the target can make another Wisdom saving throw. The target has advantage on the saving throw if it's triggered by damage. On a success, the spell ends.",
    duration="Concentration, up to 1 minute",
    casting_time="1 action",
    s_range="30 feet",
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=["tiny tarts", "a feather that is waved in the air"],
)

lvl1_tensers_floating_disk = Spell(
    name="Tenser's Floating Disk",
    level=1,
    school=SpellSchool.CONJURATION,
    action_cost=ActionCost.ACTION,
    description="[RITUAL] This spell creates a circular, horizontal plane of force, 3 feet in diameter and 1 inch thick, that floats 3 feet above the ground in an unoccupied space of your choice that you can see within range. The disk remains for the duration, and can hold up to 500 pounds. If more weight is placed on it, the spell ends, and everything on the disk falls to the ground.\
        \nThe disk is immobile while you are within 20 feet of it. If you move more than 20 feet away from it, the disk follows you so that it remains within 20 feet of you. It can move across uneven terrain, up or down stairs, slopes, and the like, but it can't cross an elevation change of 10 feet or more. For example, the disk can't move across a 10-foot-deep pit, nor could it leave such a pit if it were created at the bottom.\
        \nIf you move more than 100 feet from the disk (typically because it can't move around an obstacle to follow you), the spell ends.",
    duration="1 hour",
    casting_time="1 action",
    s_range="30 feet",
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=["a drop of mercury"],
)

lvl1_thunderwave = Spell(
    name="Thunderwave",
    level=1,
    school=SpellSchool.EVOCATION,
    action_cost=ActionCost.ACTION,
    description="A wave of thunderous force sweeps out from you. Each creature in a 15-foot cube originating from you must make a Constitution saving throw. On a failed save, a creature takes 2d8 thunder damage and is pushed 10 feet away from you. On a successful save, the creature takes half as much damage and isn't pushed.\
        \nIn addition, unsecured objects that are completely within the area of effect are automatically pushed 10 feet away from you by the spell's effect, and the spell emits a thunderous boom audible out to 300 feet.",
    higher_levels="When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d8 for each slot level above 1st.",
    duration="Instantaneous",
    casting_time="1 action",
    s_range="Self (15-foot cube)",
    components=[SpellComponent.V, SpellComponent.S],
)


# === Array of Level 1 spells ===
lvl1_spells: List[Spell] = [
    lvl1_animal_friendship, lvl1_armor_of_agathys,
    lvl1_burning_hands,
    lvl1_charm_person, lvl1_cure_wounds,
    lvl1_disguise_self,
    lvl1_hellish_rebuke,
    lvl1_magic_missile,
    lvl1_ray_of_sickness,
    lvl1_searing_smite,
    lvl1_tashas_hideous_laughter, lvl1_tensers_floating_disk, lvl1_thunderwave,
]
