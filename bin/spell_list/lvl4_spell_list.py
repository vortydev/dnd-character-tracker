# spell_list/lvl4_spell_list.py
from typing import List
from common import ActionCost
from spell import Spell, SpellSchool, SpellComponent, SpellTag

# === Define spells ===
lvl4_control_water = Spell(
    name="Control Water",
    level=4,
    school=SpellSchool.TRANSMUTATION,
    action_cost=ActionCost.ACTION,
    description="Until the spell ends, you control any freestanding water inside an area you choose that is a cube up to 100 feet on a side. You can choose from any of the following effects when you cast this spell. As an action on your turn, you can repeat the same effect or choose a different one.\
        \nBOLD[Flood :] You cause the water level of all standing water in the area to rise by as much as 20 feet. If the area includes a shore, the flooding water spills over onto dry land. If you choose an area in a large body of water, you instead create a 20-foot tall wave that travels from one side of the area to the other and then crashes down. Any Huge or smaller vehicles in the wave's path are carried with it to the other side. Any Huge or smaller vehicles struck by the wave have a 25 percent chance of capsizing. The water level remains elevated until the spell ends or you choose a different effect. If this effect produced a wave, the wave repeats on the start of your next turn while the flood effect lasts.\
        \nBOLD[Part Water :] You cause water in the area to move apart and create a trench. The trench extends across the spell's area, and the separated water forms a wall to either side. The trench remains until the spell ends or you choose a different effect. The water then slowly fills in the trench over the course of the next round until the normal water level is restored.\
        \nBOLD[Redirect Flow :] You cause flowing water in the area to move in a direction you choose, even if the water has to flow over obstacles, up walls, or in other unlikely directions. The water in the area moves as you direct it, but once it moves beyond the spell's area, it resumes its flow based on the terrain conditions. The water continues to move in the direction you chose until the spell ends or you choose a different effect.\
        \nBOLD[Whirlpool :] This effect requires a body of water at least 50 feet square and 25 feet deep. You cause a whirlpool to form in the center of the area. The whirlpool forms a vortex that is 5 feet wide at the base, up to 50 feet wide at the top, and 25 feet tall. Any creature or object in the water and within 25 feet of the vortex is pulled 10 feet toward it. A creature can swim away from the vortex by making a Strength (Athletics) check against your spell save DC.\
        \nWhen a creature enters the vortex for the first time on a turn or starts its turn there, it must make a Strength saving throw. On a failed save, the creature takes 2d8 bludgeoning damage and is caught in the vortex until the spell ends. On a successful save, the creature takes half damage, and isn't caught in the vortex. A creature caught in the vortex can use its action to try to swim away from the vortex as described above, but has disadvantage on the Strength (Athletics) check to do so.\
        \nThe first time each turn that an object enters the vortex, the object takes 2d8 bludgeoning damage, this damage occurs each round it remains in the vortex.",
    duration="Concentration, up to 10 minutes",
    casting_time="1 action",
    s_range="300 feet",
    components=[
        SpellComponent.V, 
        SpellComponent.S, 
        SpellComponent.M
    ],
    material_description=["a drop of water", "a pinch of dust"],
)

lvl4_freedom_of_movement = Spell(
    name="Freedom of Movement",
    level=4,
    school=SpellSchool.ABJURATION,
    action_cost=ActionCost.ACTION,
    description="You touch a willing creature. For the duration, the target's movement is unaffected by difficult terrain, and spells and other magical effects can neither reduce the target's speed nor cause the target to be paralyzed or restrained.\
        \nThe target can also spend 5 feet of movement to automatically escape from nonmagical restraints, such as manacles or a creature that has it grappled. Finally, being underwater imposes no penalties on the target's movement or attacks.",
    duration="1 hour",
    casting_time="1 action",
    s_range="Touch",
    components=[
        SpellComponent.V, 
        SpellComponent.S, 
        SpellComponent.M
    ],
    material_description=["a leather strap, bound around the arm or a similar appendage"],
)

lvl4_ice_storm = Spell(
    name="Ice Storm",
    level=4,
    school=SpellSchool.EVOCATION,
    action_cost=ActionCost.ACTION,
    description="A hail of rock-hard ice pounds to the ground in a 20-foot-radius, 40-foot-high cylinder centered on a point within range. Each creature in the cylinder must make a Dexterity saving throw. A creature takes 2d8 bludgeoning damage and 4d6 cold damage on a failed save, or half as much damage on a successful one.\
        \nHailstones turn the storm's area of effect into difficult terrain until the end of your next turn.",
    higher_levels="When you cast this spell using a spell slot of 5th level or higher, the bludgeoning damage increases by 1d8 for each slot level above 4th.",
    duration="Instantaneous",
    casting_time="1 action",
    s_range="300 feet",
    components=[
        SpellComponent.V, 
        SpellComponent.S, 
        SpellComponent.M
    ],
    material_description=["a pinch of dust", "a few drops of water"],
)


# === Array of Level 4 spells ===
lvl4_spells: List[Spell] = [
    lvl4_control_water,
    lvl4_freedom_of_movement,
    lvl4_ice_storm,
]
