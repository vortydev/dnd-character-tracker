# spell_list/lvl2_spell_list.py
from typing import List
from common import ActionCost
from spell import Spell, SpellSchool, SpellComponent

# === Define spells ===
lvl2_arcane_lock = Spell(
    name="Arcane Lock",
    level=2,
    school=SpellSchool.ABJURATION,
    action_cost=ActionCost.ACTION,
    description="You touch a closed door, window, gate, chest, or other entryway, and it becomes locked for the duration.\
        \nYou and the creatures you designate when you cast this spell can open the object normally. You can also set a password that, when spoken within 5 feet of the object, suppresses this spell for 1 minute. Otherwise, it is impassable until it is broken or the spell is dispelled or suppressed. Casting Knock on the object suppresses Arcane Lock for 10 minutes.\
        \nWhile affected by this spell, the object is more difficult to break or force open; the DC to break it or pick any locks on it increases by 10.",
    duration="Until dispelled",
    casting_time="1 action",
    s_range="Touch",
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=["gold dust worth at least 25 gp, which the spell consumes"],
)
lvl2_branding_smite = Spell(
    name="Branding Smite",
    level=2,
    school=SpellSchool.EVOCATION,
    action_cost=ActionCost.BONUS_ACTION,
    description="The next time you hit a creature with a weapon attack before this spell ends, the weapon gleams with astral radiance as you strike. The attack deals an extra 2d6 radiant damage to the target, which becomes visible if it is invisible, and the target sheds dim light in a 5-foot radius and can't become invisible until the spell ends.",
    higher_levels="When you cast this spell using a spell slot of 3rd level or higher, the extra damage increases by 1d6 for each slot level above 2nd.",
    duration="Concentration, up to 1 minute",
    casting_time="1 bonus action",
    s_range="Self",
    components=[SpellComponent.V],
)
lvl2_crown_of_madness = Spell(
    name="Crown of Madness",
    level=2,
    school=SpellSchool.ENCHANTMENT,
    action_cost=ActionCost.ACTION,
    description="One humanoid of your choice that you can see within range must succeed on a Wisdom saving throw or become charmed by you for the duration. While the target is charmed in this way, a twisted crown of jagged iron appears on its head, and a madness glows in its eyes.\nThe charmed target must use its action before moving on each of its turns to make a melee attack against a creature other than itself that you mentally choose. The target can act normally on its turn if you choose no creature or if none are within its reach.\nOn your subsequent turns, you must use your action to maintain control over the target, or the spell ends. Also, the target can make a Wisdom saving throw at the end of each of its turns. On a success, the spell ends.",
    duration="Concentration, up to 1 minute",
    casting_time="1 action",
    s_range="120 feet",
    components=[SpellComponent.V, SpellComponent.S],
)
lvl2_darkness = Spell(
    name="Darkness",
    level=2,
    school=SpellSchool.EVOCATION,
    action_cost=ActionCost.ACTION,
    description="Magical darkness spreads from a point you choose within range to fill a 15-foot radius sphere for the duration. The darkness spreads around corners. A creature with darkvision can't see through this darkness, and nonmagical light can't illuminate it.\nIf the point you choose is on an object you are holding or one that isn't being worn or carried, the darkness emanates from the object and moves with it. Completely covering the source of the darkness with an opaque object, such as a bowl or a helm, blocks the darkness.\nIf any of this spell's area overlaps with an area of light created by a spell of 2nd level or lower, the spell that created the light is dispelled.",
    duration="Concentration, up to 10 minutes",
    casting_time="1 action",
    s_range="60 feet",
    components=[SpellComponent.V, SpellComponent.M],
    material_description=[
        "Bat fur",
        "A drop of pitch or piece of coal"
    ],
)
lvl2_detect_thoughts = Spell(
    name="Detect Thoughts",
    level=2,
    school=SpellSchool.DIVINATION,
    action_cost=ActionCost.ACTION,
    description="For the duration, you can read the thoughts of certain creatures. When you cast the spell and as your action on each turn until the spell ends, you can focus your mind on any one creature that you can see within 30 feet of you. If the creature you choose has an Intelligence of 3 or lower or doesn't speak any language, the creature is unaffected.\
        \nYou initially learn the surface thoughts of the creature - what is most on its mind in that moment. As an action, you can either shift your attention to another creature's thoughts or attempt to probe deeper into the same creature's mind. If you probe deeper, the target must make a Wisdom saving throw. If it fails, you gain insight into its reasoning (if any), its emotional state, and something that looms large in its mind (such as something it worries over, loves, or hates). If it succeeds, the spell ends. Either way, the target knows that you are probing into its mind, and unless you shift your attention to another creature's thoughts, the creature can use its action on its turn to make an Intelligence check contested by your Intelligence check; if it succeeds, the spell ends.\
        \nQuestions verbally directed at the target creature naturally shape the course of its thoughts, so this spell is particularly effective as part of an interrogation.\
        \nYou can also use this spell to detect the presence of thinking creatures you can't see. When you cast the spell or as your action during the duration, you can search for thoughts within 30 feet of you. The spell can penetrate barriers, but 2 feet of rock, 2 inches of any metal other than lead, or a thin sheet of lead blocks you. You can't detect a creature with an Intelligence of 3 or lower or one that doesn't speak any language.\
        \nOnce you detect the presence of a creature in this way, you can read its thoughts for the rest of the duration as described above, even if you can't see it, but it must still be within range.",
    duration="Concentration, up to 1 minute",
    casting_time="1 action",
    s_range="Self",
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=["a copper piece"],
)
lvl2_enthrall = Spell(
    name="Enthrall",
    level=2,
    school=SpellSchool.ENCHANTMENT,
    action_cost=ActionCost.ACTION,
    description="You weave a distracting string of words, causing creatures of your choice that you can see within range and that can hear you to make a Wisdom saving throw. Any creature that can’t be charmed succeeds on this saving throw automatically, and if you or your companions are fighting a creature, it has advantage on the save. On a failed save, the target has disadvantage on Wisdom (Perception) checks made to perceive any creature other than you until the spell ends or until the target can no longer hear you. The spell ends if you are incapacitated or can no longer speak.",
    duration="1 minute",
    casting_time="1 action",
    s_range="60 feet",
    components=[SpellComponent.V, SpellComponent.S],
)
lvl2_flame_blade = Spell(
    name="Flame Blade",
    level=2,
    school=SpellSchool.EVOCATION,
    action_cost=ActionCost.BONUS_ACTION,
    description="You evoke a fiery blade in your free hand. The blade is similar in size and shape to a scimitar, and it lasts for the duration. If you let go of the blade, it disappears, but you can evoke the blade again as a bonus action.\
        \nYou can use your action to make a melee spell attack with the fiery blade. On a hit, the target takes 3d6 fire damage. The flaming blade sheds bright light in a 10-foot radius and dim light for an additional 10 feet.",
    higher_levels="When you cast this spell using a spell slot of 4th level or higher, the damage increases by 1d6 for every two slot levels above 2nd.",
    duration="Concentration, up to 10 minutes",
    casting_time="1 bonus action",
    s_range="Self",
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=["a leaf of sumac"],
)
lvl2_invisibility = Spell(
    name="Invisibility",
    level=2,
    school=SpellSchool.ILLUSION,
    action_cost=ActionCost.ACTION,
    description="A creature you touch becomes invisible until the spell ends. Anything the target is wearing or carrying is invisible as long as it is on the target's person. The spell ends for a target that attacks or casts a spell.",
    higher_levels="When you cast this spell using a spell slot of 3rd level or higher, you can target one additional creature for each slot level above 2nd.",
    duration="Concentration, up to 1 hour",
    casting_time="1 action",
    s_range="Touch",
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=["an eyelash encased in gum arabic"],
)
lvl2_suggestion = Spell(
    name="Suggestion",
    level=2,
    school=SpellSchool.ENCHANTMENT,
    action_cost=ActionCost.ACTION,
    description="You suggest a course of activity (limited to a sentence or two) and magically influence a creature you can see within range that can hear and understand you. Creatures that can't be charmed are immune to this effect. The suggestion must be worded in such a manner as to make the course of action sound reasonable. Asking the creature to stab itself, throw itself onto a spear, immolate itself, or do some other obviously harmful act ends the spell. \
        \nThe target must make a Wisdom saving throw. On a failed save, it purses the course of action you described to the best of its ability. The suggested course of action can continue for the entire duration. If the suggested activity can be completed in a shorter time, the spell ends when the subject finishes what it was asked to do.\
        \nYou can also specify conditions that will trigger a special activity during the duration. For example, you might suggest that a knight give her warhorse to the first beggar she meets. If the condition isn't met before the spell expires, the activity isn't performed.\
        \nIf you or any of your companions damage the target, the spell ends.",
    duration="Concentration, up to 8 hours",
    casting_time="1 action",
    s_range="30 feet",
    components=[SpellComponent.V, SpellComponent.M],
    material_description=[
        "a snake's tongue",
        "a bit of honeycomb or a drop of sweet oil"
    ],
)

# === Array of Level 2 spells ===
lvl2_spells: List[Spell] = [
    lvl2_arcane_lock,
    lvl2_branding_smite, 
    lvl2_crown_of_madness,
    lvl2_darkness,
    lvl2_detect_thoughts,
    lvl2_enthrall,
    lvl2_flame_blade,
    lvl2_invisibility,
    lvl2_suggestion,
]
