# spell_list/lvl2_spell_list.py
from typing import List
from common import ActionCost
from spell import Spell, SpellSchool, SpellComponent, SpellTag

# === Define spells ===
lvl2_alter_self = Spell(
    name="Alter Self",
    level=2,
    school=SpellSchool.TRANSMUTATION,
    action_cost=ActionCost.ACTION,
    description="You assume a different form. When you cast the spell, choose one of the following options, the effects of which last for the duration of the spell. While the spell lasts, you can end one option as an action to gain the benefits of a different one.\
        \n- BOLD[Aquatic Adaptation :] You adapt your body to an aquatic environment, sprouting gills, and growing webbing between your fingers. You can breathe underwater and gain a swimming speed equal to your walking speed.\
        \n- BOLD[Change Appearance :] You transform your appearance. You decide what you look like, including your height, weight, facial features, sound of your voice, hair length, coloration, and distinguishing characteristics, if any. You can make yourself appear as a member of another race, though none of your statistics change. You also don't appear as a creature of a different size than you, and your basic shape stays the same; if you're bipedal, you can't use this spell to become quadrupedal, for instance. At any time for the duration of the spell, you can use your action to change your appearance in this way again.\
        \n- BOLD[Natural Weapons :] You grow claws, fangs, spines, horns, or a different natural weapon of your choice. Your unarmed strikes deal 1d6 bludgeoning, piercing, or slashing damage, as appropriate to the natural weapon you chose, and you are proficient with your unarmed strikes. Finally, the natural weapon is magic and you have a +1 bonus to the attack and damage rolls you make using it.",
    duration="Concentration, up to 1 hour",
    casting_time="1 action",
    s_range="Self",
    components=[SpellComponent.V, SpellComponent.S],
)

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

lvl2_blur = Spell(
    name="Blur",
    level=2,
    school=SpellSchool.ILLUSION,
    action_cost=ActionCost.ACTION,
    description="Your body becomes blurred, shifting and wavering to all who can see you. For the duration, any creature has disadvantage on attack rolls against you. An attacker is immune to this effect if it doesn't rely on sight, as with blindsight, or can see through illusions, as with truesight.",
    duration="Concentration, up to 1 minute",
    casting_time="1 action",
    s_range="Self",
    components=[SpellComponent.V],
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
    description="You weave a distracting string of words, causing creatures of your choice that you can see within range and that can hear you to make a Wisdom saving throw. Any creature that can't be charmed succeeds on this saving throw automatically, and if you or your companions are fighting a creature, it has advantage on the save. On a failed save, the target has disadvantage on Wisdom (Perception) checks made to perceive any creature other than you until the spell ends or until the target can no longer hear you. The spell ends if you are incapacitated or can no longer speak.",
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

lvl2_hold_person = Spell(
    name="Hold Person",
    level=2,
    school=SpellSchool.ENCHANTMENT,
    action_cost=ActionCost.ACTION,
    description="Choose a humanoid that you can see within range. The target must succeed on a Wisdom saving throw or be paralyzed for the duration. At the end of each of its turns, the target can make another Wisdom saving throw. On a success, the spell ends on the target.",
    higher_levels="When you cast this spell using a spell slot of 3rd level or higher, you can target one additional humanoid for each slot level above 2nd. The humanoids must be within 30 feet of each other when you target them.",
    duration="Concentration, up to 1 minute",
    casting_time="1 action",
    s_range="60 feet",
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=["a small, straight piece of iron"],
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

lvl2_levitate = Spell(
    name="Levitate",
    level=2,
    school=SpellSchool.TRANSMUTATION,
    action_cost=ActionCost.ACTION,
    description="One creature or loose object of your choice that you can see within range rises vertically, up to 20 feet, and remains suspended there for the duration. The spell can levitate a target that weighs up to 500 pounds. An unwilling creature that succeeds on a Constitution saving throw is unaffected.\
        \nThe target can move only by pushing or pulling against a fixed object or surface within reach (such as a wall or a ceiling), which allows it to move as if it were climbing. You can change the target's altitude by up to 20 feet in either direction on your turn. If you are the target, you can move up or down as part of your move. Otherwise, you can use your action to move the target, which must remain within the spell's range.\
        \nWhen the spell ends, the target floats gently to the ground if it is still aloft.",
    duration="Concentration, up to 10 minutes",
    casting_time="1 action",
    s_range="60 feet",
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=["either a small leather loop or a piece of golden wire bent into a cup shape with a long shank on one end"],
)

lvl2_misty_step = Spell(
    name="Misty Step",
    level=2,
    school=SpellSchool.CONJURATION,
    action_cost=ActionCost.BONUS_ACTION,
    description="Briefly surrounded by silvery mist, you teleport up to 30 feet to an unoccupied space that you can see.",
    duration="Instantaneous",
    casting_time="1 bonus action",
    s_range="Self",
    components=[SpellComponent.V],
)

lvl2_mirror_image = Spell(
    name="Mirror Image",
    level=2,
    school=SpellSchool.ILLUSION,
    action_cost=ActionCost.ACTION,
    description="Three illusory duplicates of yourself appear in your space. Until the spell ends, the duplicates move with you and mimic your actions, shifting position so it's impossible to track which image is real. You can use your action to dismiss the illusory duplicates.\
        \nEach time a creature targets you with an attack during the spell's duration, roll a d20 to determine whether the attack instead targets one of your duplicates.\
        \nIf you have three duplicates, you must roll a 6 or higher to change the attack's target to a duplicate. With two duplicates, you must roll an 8 or higher. With one duplicate, you must roll an 11 or higher.\
        \nA duplicate's AC equals 10 + your Dexterity modifier. If an attack hits a duplicate, the duplicate is destroyed. A duplicate can be destroyed only by an attack that hits it. It ignores all other damage and effects. The spell ends when all three duplicates are destroyed.\
        \nA creature is unaffected by this spell if it can't see, if it relies on senses other than sight, such as blindsight, or if it can perceive illusions as false, as with truesight.",
    duration="1 minute",
    casting_time="1 action",
    s_range="Self",
    components=[SpellComponent.V, SpellComponent.S],
)

lvl2_silence = Spell(
    name="Silence",
    level=2,
    school=SpellSchool.ILLUSION,
    action_cost=ActionCost.ACTION,
    description="For the duration, no sound can be created within or pass through a 20-foot-radius sphere centered on a point you choose within range. Any creature or object entirely inside the sphere is immune to thunder damage, and creatures are deafened while entirely inside it. Casting a spell that includes a verbal component is impossible there.",
    duration="Concentration, up to 10 minutes",
    casting_time="1 action",
    s_range="120 feet",
    components=[SpellComponent.V, SpellComponent.S],
    tags=[SpellTag.RITUAL],
)

lvl2_spider_climb = Spell(
    name="Spider Climb",
    level=2,
    school=SpellSchool.TRANSMUTATION,
    action_cost=ActionCost.ACTION,
    description="Until the spell ends, one willing creature you touch gains the ability to move up, down, and across vertical surfaces and upside down along ceilings, while leaving its hands free. The target also gains a climbing speed equal to its walking speed.",
    duration="Concentration, up to 1 hour",
    casting_time="1 action",
    s_range="Touch",
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=[
        "a drop of bitumen",
        "a spider"
    ],
)

lvl2_spike_growth = Spell(
    name="Spike Growth",
    level=2,
    school=SpellSchool.TRANSMUTATION,
    action_cost=ActionCost.ACTION,
    description="The ground in a 20-foot radius centered on a point within range twists and sprouts hard spikes and thorns. The area becomes difficult terrain for the duration. When a creature moves into or within the area, it takes 2d4 piercing damage for every 5 feet it travels.\
        \nThe transformation of the ground is camouflaged to look natural. Any creature that can't see the area at the time the spell is cast must make a Wisdom (Perception) check against your spell save DC to recognize the terrain as hazardous before entering it.",
    duration=" Concentration, up to 10 minutes",
    casting_time="1 action",
    s_range="150 feet",
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=["seven sharp thorns or seven small twigs, each sharpened to a point"],
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
    lvl2_alter_self, lvl2_arcane_lock,
    lvl2_blur, lvl2_branding_smite, 
    lvl2_crown_of_madness,
    lvl2_darkness, lvl2_detect_thoughts,
    lvl2_enthrall,
    lvl2_flame_blade,
    lvl2_hold_person,
    lvl2_invisibility,
    lvl2_levitate,
    lvl2_misty_step, lvl2_mirror_image,
    lvl2_silence, lvl2_spider_climb, lvl2_spike_growth, lvl2_suggestion,
]
