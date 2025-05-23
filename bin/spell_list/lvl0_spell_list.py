# spell_list/lvl0_spell_list.py
from typing import List
from common import ActionCost
from spell import Spell, SpellSchool, SpellComponent

# === Define spells ===
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
    can_friends,
    can_mage_hand,
    can_minor_illusion,
    can_ray_of_frost,
    can_thaumaturgy,
    can_vicious_mockery,
]
