# spell_list/lvl0_spell_list.py
from typing import List
from common import ActionCost
from spell import Spell, SpellSchool, SpellComponent

# === Define spells ===
can_dancing_lights = Spell(
    name="Dancing Lights",
    level=0,
    school=SpellSchool.EVOCATION,
    action_cost=ActionCost.ACTION,
    description="You create up to four torch-sized lights within range, making them appear as torches, lanterns, or glowing orbs that hover in the air for the duration. You can also combine the four lights into one glowing vaguely humanoid form of Medium size. Whichever form you choose, each light sheds dim light in a 10-foot radius.\
        \nAs a bonus action on your turn, you can move the lights up to 60 feet to a new spot within range. A light must be within 20 feet of another light created by this spell, and a light winks out if it exceeds the spell's range.",
    duration="Concentration, up to 1 minute",
    casting_time="1 action",
    s_range="120 feet",
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=["a bit of phosphorus or wychwood, or a glowworm"],
)

can_friends = Spell(
    name="Friends",
    level=0,
    school=SpellSchool.ENCHANTMENT,
    action_cost=ActionCost.ACTION,
    description="For the duration, you have advantage on all Charisma checks directed at one creature of your choice that isn't hostile toward you. When the spell ends, the creature realizes that you used magic to influence its mood and becomes hostile toward you. A creature prone to violence might attack you. Another creature might seek retribution in other ways (at the DM's discretion), depending on the nature of your interaction with it.",
    duration="Concentration, up to 1 minute",
    casting_time="1 action",
    s_range="Self",
    components=[SpellComponent.S, SpellComponent.M],
    material_description=["a small amount of makeup applied to the face as this spell is cast"],
)

can_light = Spell(
    name="Light",
    level=0,
    school=SpellSchool.EVOCATION,
    action_cost=ActionCost.ACTION,
    description="You touch one object that is no larger than 10 feet in any dimension. Until the spell ends, the object sheds bright light in a 20-foot radius and dim light for an additional 20 feet. The light can be colored as you like. Completely covering the object with something opaque blocks the light. The spell ends if you cast it again or dismiss it as an action.\
        \nIf you target an object held or worn by a hostile creature, that creature must succeed on a Dexterity saving throw to avoid the spell.",
    duration="1 hour",
    casting_time="1 action",
    s_range="Touch",
    components=[SpellComponent.V, SpellComponent.M],
    material_description=["a firefly or phosphorescent moss"],
)

can_mage_hand = Spell(
    name="Mage Hand",
    level=0,
    school=SpellSchool.CONJURATION,
    action_cost=ActionCost.ACTION,
    description="A spectral, floating hand appears at a point you choose within range. The hand lasts for the duration or until you dismiss it as an action. The hand vanishes if it is ever more than 30 feet away from you or if you cast this spell again.\
        \nYou can use your action to control the hand. You can use the hand to manipulate an object, open an unlocked door or container, stow or retrieve an item from an open container, or pour the contents out of a vial. You can move the hand up to 30 feet each time you use it.\
        \nThe hand can't attack, activate magical items, or carry more than 10 pounds.",
    duration="1 minute",
    casting_time="1 action",
    s_range="30 feet",
    components=[SpellComponent.V, SpellComponent.S],
)

can_message = Spell(
    name="Message",
    level=0,
    school=SpellSchool.TRANSMUTATION,
    action_cost=ActionCost.ACTION,
    description="You point your finger toward a creature within range and whisper a message. The target (and only the target) hears the message and can reply in a whisper that only you can hear.\
        \nYou can cast this spell through solid objects if you are familiar with the target and know it is beyond the barrier. Magical silence, 1 foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood blocks the spell. The spell doesn't have to follow a straight line and can travel freely around corners or through openings.",
    duration="1 round",
    casting_time="1 action",
    s_range="120 feet",
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=["a short piece of copper wire"],
)

can_minor_illusion = Spell(
    name="Minor Illusion",
    level=0,
    school=SpellSchool.ILLUSION,
    action_cost=ActionCost.ACTION,
    description="You create a sound or an image of an object within range that lasts for the duration. The illusion also ends if you dismiss it as an action or cast this spell again.\
        \nIf you create a sound, its volume can range from a whisper to a scream. It can be your voice, someone else's voice, a lion's roar, a beating of drums, or any other sound you choose. The sound continues unabated throughout the duration, or you can make discrete sounds at different times before the spell ends.\
        \nIf you create an image of an object—such as a chair, muddy footprints, or a small chest—it must be no larger than a 5-foot cube. The image can't create sound, light, smell, or any other sensory effect. Physical interaction with the image reveals it to be an illusion, because things can pass through it.\
        \nIf a creature uses its action to examine the sound or image, the creature can determine that it is an illusion with a successful Intelligence (Investigation) check against your spell save DC. If a creature discerns the illusion for what it is, the illusion becomes faint to the creature.",
    duration="1 minute",
    casting_time="1 action",
    s_range="30 feet",
    components=[SpellComponent.S, SpellComponent.M],
    material_description=["a bit of fleece"],
)

can_poison_spray = Spell(
    name="Poison Spray",
    level=0,
    school=SpellSchool.CONJURATION,
    action_cost=ActionCost.ACTION,
    description="You extend your hand toward a creature you can see within range and project a puff of noxious gas from your palm. The creature must succeed on a Constitution saving throw or take 1d12 poison damage.",
    higher_levels="This spell's damage increases by 1d12 when you reach 5th level (2d12), 11th level (3d12), and 17th level (4d12).",
    duration="1 minute",
    casting_time="Instantaneous",
    s_range="10 feet",
    components=[SpellComponent.V, SpellComponent.S],
)

can_prestidigitation = Spell(
    name="Prestidigitation",
    level=0,
    school=SpellSchool.TRANSMUTATION,
    action_cost=ActionCost.ACTION,
    description="This spell is a minor magical trick that novice spellcasters use for practice. You create one of the following magical effects within range:\
        \n- You create an instantaneous, harmless sensory effect, such as a shower of sparks, a puff of wind, faint musical notes, or an odd odor.\
        \n- You instantaneously light or snuff out a candle, a torch, or a small campfire.\
        \n- You instantaneously clean or soil an object no larger than 1 cubic foot.\
        \n- You chill, warm, or flavor up to 1 cubic foot of nonliving material for 1 hour.\
        \n- You make a color, a small mark, or a symbol appear on an object or a surface for 1 hour.\
        \n- You create a nonmagical trinket or an illusory image that can fit in your hand and that lasts until the end of your next turn.\
        \nIf you cast this spell multiple times, you can have up to three of its non-instantaneous effects active at a time, and you can dismiss such an effect as an action.",
    duration="Up to 1 hour",
    casting_time="1 action",
    s_range="10 feet",
    components=[SpellComponent.V, SpellComponent.S],
)

can_ray_of_frost = Spell(
    name="Ray of Frost",
    level=0,
    school=SpellSchool.EVOCATION,
    action_cost=ActionCost.ACTION,
    description="A frigid beam of blue-white light streaks toward a creature within range. Make a ranged spell attack against the target. On a hit, it takes 1d8 cold damage, and its speed is reduced by 10 feet until the start of your next turn.",
    higher_levels="The spell's damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and 17th level (4d8).",
    duration="Instantaneous",
    casting_time="1 action",
    s_range="60 feet",
    components=[SpellComponent.V, SpellComponent.S],
)

can_thaumaturgy = Spell(
    name="Thaumaturgy",
    level=0,
    school=SpellSchool.TRANSMUTATION,
    action_cost=ActionCost.ACTION,
    description="You manifest a minor wonder, a sign of supernatural power.",
    duration="Up to 1 minute",
    casting_time="1 action",
    s_range="30 feet",
    components=[SpellComponent.V],
)

can_true_strike = Spell(
    name="True Strike",
    level=0,
    school=SpellSchool.DIVINATION,
    action_cost=ActionCost.ACTION,
    description="You extend your hand and point a finger at a target in range. Your magic grants you a brief insight into the target's defenses. On your next turn, you gain advantage on your first attack roll against the target, provided that this spell hasn't ended.",
    duration="Concentration, up to 1 round",
    casting_time="1 action",
    s_range="30 feet",
    components=[SpellComponent.S],
)

can_spare_the_dying = Spell(
    name="Spare the Dying",
    level=0,
    school=SpellSchool.NECROMANCY,
    action_cost=ActionCost.ACTION,
    description="You touch a living creature that has 0 hit points. The creature becomes stable. This spell has no effect on undead or constructs.",
    duration="Instantaneous",
    casting_time="1 action",
    s_range="Touch",
    components=[SpellComponent.V, SpellComponent.S],
)

can_vicious_mockery = Spell(
    name="Vicious Mockery",
    level=0,
    school=SpellSchool.ENCHANTMENT,
    action_cost=ActionCost.ACTION,
    description="You unleash a string of insults laced with subtle enchantments at a creature you can see within range. If the target can hear you (though it need not understand you), it must succeed on a Wisdom saving throw or take 1d4 psychic damage and have disadvantage on the next attack roll it makes before the end of its next turn.",
    higher_levels="This spell's damage increases by 1d4 when you reach 5th level (2d4), 11th level (3d4), and 17th level (4d4).",
    duration="Instantaneous",
    casting_time="1 action",
    s_range="60 feet",
    components=[SpellComponent.V],
)


# === Array of Cantrips ===
lvl0_spells: List[Spell] = [
    can_dancing_lights,
    can_friends,
    can_light,
    can_mage_hand, can_message, can_minor_illusion,
    can_poison_spray, can_prestidigitation,
    can_ray_of_frost,
    can_spare_the_dying,
    can_thaumaturgy, can_true_strike,
    can_vicious_mockery,
]
