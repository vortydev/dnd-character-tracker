# spell_list/lvl4_spell_list.py
from typing import List
from common import ActionCost
from spell import Spell, SpellSchool, SpellComponent, SpellTag

# === Define spells ===
lvl4_blight = Spell(
    name="Blight",
    level=4,
    school=SpellSchool.NECROMANCY,
    action_cost=ActionCost.ACTION,
    description="Necromantic energy washes over a creature of your choice that you can see within range, draining moisture and vitality from it. The target must make a Constitution saving throw. The target takes 8d8 necrotic damage on a failed save, or half as much damage on a successful one. This spell has no effect on undead or constructs.\
        \nIf you target a plant creature or a magical plant, it makes the saving throw with disadvantage, and the spell deals maximum damage to it. If you target a nonmagical plant that isn't a creature, such as a tree or shrub, it doesn't make a saving throw; it simply withers and dies.",
    higher_levels="When you cast this spell using a spell slot of 5th level or higher, the damage increases by 1d8 for each slot level above 4th.",
    duration="Instantaneous",
    casting_time="1 action",
    s_range="30 feet",
    components=[SpellComponent.V, SpellComponent.S],
)

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
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=["a drop of water", "a pinch of dust"],
)

lvl4_divination = Spell(
    name="Divination",
    level=4,
    school=SpellSchool.DIVINATION,
    action_cost=ActionCost.ACTION,
    description="Your magic and an offering put you in contact with a god or a god's servants. You ask a single question concerning a specific goal, event, or activity to occur within 7 days. The DM offers a truthful reply. The reply might be a short phrase, a cryptic rhyme, or an omen.\
        \nThe spell doesn't take into account any possible circumstances that might change the outcome, such as the casting of additional spells or the loss or gain of a companion.\
        \nIf you cast this spell two or more times before finishing your next long rest, there is a cumulative 25 percent chance for each casting after the first that you get a random reading. The DM makes this roll in secret.",
    duration="Instantaneous",
    casting_time="1 action",
    s_range="Self",
    components=[SpellComponent.V, SpellComponent.S],
    material_description=["incense and a sacrificial offering appropriate to your religion, together worth at least 25 gp, which the spell consumes"],
    tags=[SpellTag.RITUAL],
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
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=["a leather strap, bound around the arm or a similar appendage"],
)

lvl4_geater_invisibility = Spell(
    name="Greater Invisibility",
    level=4,
    school=SpellSchool.ILLUSION,
    action_cost=ActionCost.ACTION,
    description="You or a creature you touch becomes invisible until the spell ends. Anything the target is wearing or carrying is invisible as long as it is on the target's person.",
    duration="Concentration, up to 1 minute",
    casting_time="1 action",
    s_range="Touch",
    components=[SpellComponent.V, SpellComponent.S],
)

lvl4_hallucinatory_terrain = Spell(
    name="Hallucinatory Terrain",
    level=4,
    school=SpellSchool.ILLUSION,
    action_cost=ActionCost.ACTION,
    description="You make natural terrain in a 150-foot cube in range look, sound, and smell like some other sort of natural terrain. Thus, open fields or a road can be made to resemble a swamp, hill, crevasse, or some other difficult or impassable terrain. A pond can be made to seem like a grassy meadow, a precipice like a gentle slope, or a rock-strewn gully like a wide and smooth road. Manufactured structures, equipment, and creatures within the area aren't changed in appearance.\
        \nThe tactile characteristics of the terrain are unchanged, so creatures entering the area are likely to see through the illusion. If the difference isn't obvious by touch, a creature carefully examining the illusion can attempt an Intelligence (Investigation) check against your spell save DC to disbelieve it. A creature who discerns the illusion for what it is, sees it as a vague image superimposed on the terrain.",
    duration="24 hours",
    casting_time="10 minutes",
    s_range="300 feet",
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=["a stone", "a twig", "a bit of green plant"],
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
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=["a pinch of dust", "a few drops of water"],
)

lvl4_locate_creature = Spell(
    name="Locate Creature",
    level=4,
    school=SpellSchool.DIVINATION,
    action_cost=ActionCost.ACTION,
    description="Describe or name a creature that is familiar to you. You sense the direction to the creature's location, as long as that creature is within 1,000 feet of you. If the creature is moving, you know the direction of its movement.\
        \nThe spell can locate a specific creature known to you, or the nearest creature of a specific kind (such as a human or a unicorn), so long as you have seen such a creature up close – within 30 feet – at least once. If the creature you described or named is in a different form, such as being under the effects of a polymorph spell, this spell doesn't locate the creature.\
        \nThis spell can't locate a creature if running water at least 10 feet wide blocks a direct path between you and the creature.",
    duration="Concentration, up to 1 hour",
    casting_time="1 action",
    s_range="Self",
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=["a bit of fur from a bloodhound"],
)

lvl4_stone_shape = Spell(
    name="Stone Shape",
    level=4,
    school=SpellSchool.TRANSMUTATION,
    action_cost=ActionCost.ACTION,
    description="You touch a stone object of Medium size or smaller or a section of stone no more than 5 feet in any dimension and form it into any shape that suits your purpose. So, for example, you could shape a large rock into a weapon, idol, or coffer, or make a small passage through a wall, as long as the wall is less than 5 feet thick. You could also shape a stone door or its frame to seal the door shut. The object you create can have up to two hinges and a latch, but finer mechanical detail isn't possible.",
    duration="Instantaneous",
    casting_time="1 action",
    s_range="Touch",
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=["soft clay, which must be worked into roughly the desired shape of the stone object"],
)

lvl4_stoneskin = Spell(
    name="Stoneskin",
    level=4,
    school=SpellSchool.ABJURATION,
    action_cost=ActionCost.ACTION,
    description="This spell turns the flesh of a willing creature you touch as hard as stone. Until the spell ends, the target has resistance to nonmagical bludgeoning, piercing, and slashing damage.",
    duration="Concentration, up to 1 hour",
    casting_time="1 action",
    s_range="Touch",
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=["diamond dust worth 100 gp, which the spell consumes"],
)


# === Array of Level 4 spells ===
lvl4_spells: List[Spell] = [
    lvl4_blight,
    lvl4_control_water,
    lvl4_divination,
    lvl4_freedom_of_movement,
    lvl4_geater_invisibility,
    lvl4_hallucinatory_terrain,
    lvl4_ice_storm,
    lvl4_stone_shape, lvl4_stoneskin,
]
