# spell_list/lvl3_spell_list.py
from typing import List
from common import ActionCost
from spell import Spell, SpellSchool, SpellComponent, SpellTag

# === Define spells ===
lvl3_sleet_storm = Spell(
    name="Sleet Storm",
    level=3,
    school=SpellSchool.CONJURATION,
    action_cost=ActionCost.ACTION,
    description="Until the spell ends, freezing rain and sleet fall in a 20-foot-tall cylinder with a 40-foot radius centered on a point you choose within range. The area is heavily obscured, and exposed flames in the area are doused.\
        \nThe ground in the area is covered with slick ice, making it difficult terrain. When a creature enters the spell's area for the first time on a turn or starts its turn there, it must make a Dexterity saving throw. On a failed save, it falls prone.\
        \nIf a creature starts its turn in the spell's area and is concentrating on a spell, the creature must make a successful Constitution saving throw against your spell save DC or lose concentration.",
    duration="Concentration, up to 1 minute",
    casting_time="1 action",
    s_range="120 feet",
    components=[
        SpellComponent.V, 
        SpellComponent.S, 
        SpellComponent.M
    ],
    material_description=["a pinch of dust", "a few drops of water"],
)

lvl3_slow = Spell(
    name="Slow",
    level=3,
    school=SpellSchool.TRANSMUTATION,
    action_cost=ActionCost.ACTION,
    description="You alter time around up to six creatures of your choice in a 40-foot cube within range. Each target must succeed on a Wisdom saving throw or be affected by this spell for the duration.\
        \nAn affected target's speed is halved, it takes a -2 penalty to AC and Dexterity saving throws, and it can't use reactions. On its turn, it can use either an action or a bonus action, not both. Regardless of the creature's abilities or magic items, it can't make more than one melee or ranged attack during its turn.\
        \nIf the creature attempts to cast a spell with a casting time of 1 action, roll a d20. On an 11 or higher, the spell doesn't take effect until the creature's next turn, and the creature must use its action on that turn to complete the spell. If it can't, the spell is wasted.\
        \nA creature affected by this spell makes another Wisdom saving throw at the end of each of its turns. On a successful save, the effect ends for it.",
    duration="Concentration, up to 1 minute",
    casting_time="1 action",
    s_range="120 feet",
    components=[
        SpellComponent.V, 
        SpellComponent.S, 
        SpellComponent.M
    ],
    material_description=["a drop of molasses"],
)

lvl3_water_breathing = Spell(
    name="Water Breathing",
    level=3,
    school=SpellSchool.TRANSMUTATION,
    action_cost=ActionCost.ACTION,
    description="This spell grants up to ten willing creatures you can see within range the ability to breathe underwater until the spell ends. Affected creatures also retain their normal mode of respiration.",
    duration="24 hours",
    casting_time="1 action",
    s_range="30 feet",
    components=[ SpellComponent.V, SpellComponent.S, SpellComponent.M ],
    material_description=["a short reed or piece of straw"],
    tags=[SpellTag.RITUAL],
)

lvl3_water_walk = Spell(
    name="Water Walk",
    level=3,
    school=SpellSchool.TRANSMUTATION,
    action_cost=ActionCost.ACTION,
    description="This spell grants the ability to move across any liquid surface – such as water, acid, mud, snow, quicksand, or lava – as if it were harmless solid ground (creatures crossing molten lava can still take damage from the heat). Up to ten willing creatures you can see within range gain this ability for the duration.\
        \nIf you target a creature submerged in a liquid, the spell carries the target to the surface of the liquid at a rate of 60 feet per round.",
    duration="1 hour",
    casting_time="1 action",
    s_range="30 feet",
    components=[ SpellComponent.V, SpellComponent.S, SpellComponent.M ],
    material_description=["a piece of cork"],
    tags=[SpellTag.RITUAL],
)


# === Array of Level 3 spells ===
lvl3_spells: List[Spell] = [
    lvl3_sleet_storm, lvl3_slow,
    lvl3_water_breathing, lvl3_water_walk,
]
