# spell_list/lvl5_spell_list.py
from typing import List
from common import ActionCost
from spell import Spell, SpellSchool, SpellComponent, SpellTag

# === Define spells ===
lvl5_cloudkill = Spell(
    name="Cloudkill",
    level=5,
    school=SpellSchool.CONJURATION,
    action_cost=ActionCost.ACTION,
    description="You create a 20-foot-radius sphere of poisonous, yellow-green fog centered on a point you choose within range. The fog spreads around corners. It lasts for the duration or until strong wind disperses the fog, ending the spell. Its area is heavily obscured.\
        \nWhen a creature enters the spell's area for the first time on a turn or starts its turn there, that creature must make a Constitution saving throw. The creature takes 5d8 poison damage on a failed save, or half as much damage on a successful one. Creatures are affected even if they hold their breath or don't need to breathe.\
        \nThe fog moves 10 feet away from you at the start of each of your turns, rolling along the surface of the ground. The vapors, being heavier than air, sink to the lowest level of the land, even pouring down openings.",
    higher_levels="When you cast this spell using a spell slot of 6th level or higher, the damage increases by 1d8 for each slot level above 5th.",
    duration="Concentration, up to 10 minutes",
    casting_time="1 action",
    s_range="120 feet",
    components=[SpellComponent.V, SpellComponent.S],
)

lvl5_conjure_elemental = Spell(
    name="Conjure Elemental",
    level=5,
    school=SpellSchool.CONJURATION,
    action_cost=ActionCost.ACTION,
    description="You call forth an elemental servant. Choose an area of air, earth, fire, or water that fills a 10-foot cube within range. An elemental of challenge rating 5 or lower appropriate to the area you chose appears in an unoccupied space within 10 feet of it. For example, a fire elemental emerges from a bonfire, and an earth elemental rises up from the ground. The elemental disappears when it drops to 0 hit points or when the spell ends.\
        \nThe elemental is friendly to you and your companions for the duration. Roll initiative for the elemental, which has its own turns. It obeys any verbal commands that you issue to it (no action required by you). If you don't issue any commands to the elemental, it defends itself from hostile creatures but otherwise takes no actions.\
        \nIf your concentration is broken, the elemental doesn't disappear. Instead, you lose control of the elemental, it becomes hostile toward you and your companions, and it might attack. An uncontrolled elemental can't be dismissed by you, and it disappears 1 hour after you summoned it. The DM has the elemental's statistics.",
    higher_levels="When you cast this spell using a spell slot of 6th level or higher, the challenge rating increases by 1 for each slot level above 5th.",
    duration="Concentration, up to 1 hour",
    casting_time="1 minute",
    s_range="90 feet",
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=["burning incense for air, soft clay for earth, sulfur and phosphorus for fire, or water and sand for water"],
)

lvl5_commune_with_nature = Spell(
    name="Commune with Nature",
    level=5,
    school=SpellSchool.DIVINATION,
    action_cost=ActionCost.RITUAL,
    description="You briefly become one with nature and gain knowledge of the surrounding territory. In the outdoors, the spell gives you knowledge of the land within 3 miles of you. In caves and other natural underground settings, the radius is limited to 300 feet. The spell doesn't function where nature has been replaced by construction, such as in dungeons and towns.\
        \nYou instantly gain knowledge of up to three facts of your choice about any of the following subjects as they relate to the area :\
        \n- terrain and bodies of water\
        \n- prevalent plants, minerals, animals, or peoples\
        \n- powerful celestials, fey, fiends, elementals, or undead\
        \n- influence from other planes of existence\
        \n- buildings\
        \nFor example, you could determine the location of powerful undead in the area, the location of major sources of safe drinking water, and the location of any nearby towns.",
    duration="Instantaneous",
    casting_time="1 minute",
    s_range="Self",
    components=[SpellComponent.V, SpellComponent.S],
    tags=[SpellTag.RITUAL],
)

lvl5_cone_of_cold = Spell(
    name="Cone of Cold",
    level=5,
    school=SpellSchool.EVOCATION,
    action_cost=ActionCost.ACTION,
    description="A blast of cold air erupts from your hands. Each creature in a 60-foot cone must make a Constitution saving throw. A creature takes 8d8 cold damage on a failed save, or half as much damage on a successful one. A creature killed by this spell becomes a frozen statue until it thaws.",
    higher_levels="When you cast this spell using a spell slot of 6th level or higher, the damage increases by 1d8 for each slot level above 5th.",
    duration="Instantaneous",
    casting_time="1 action",
    s_range="Self (60-foot cone)",
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=["a small crystal or glass cone"],
)

lvl5_dream = Spell(
    name="Dream",
    level=5,
    school=SpellSchool.ILLUSION,
    action_cost=ActionCost.ACTION,
    description="This spell shapes a creature's dreams. Choose a creature known to you as the target of this spell. The target must be on the same plane of existence as you. Creatures that don't sleep, such as elves, can't be contacted by this spell. You, or a willing creature you touch, enters a trance state, acting as a messenger. While in the trance, the messenger is aware of their surroundings, but can't take actions or move.\
        \nIf the target is asleep, the messenger appears in the target's dreams and can converse with the target as long as it remains asleep, through the duration of the spell. The messenger can also shape the environment of the dream, creating landscapes, objects, and other images. The messenger can emerge from the trance at any time, ending the effect of the spell early. The target recalls the dream perfectly upon waking. If the target is awake when you cast the spell, the messenger knows it, and can either end the trance (and the spell) or wait for the target to fall asleep, at which point the messenger appears in the target's dreams.\
        \nYou can make the messenger appear monstrous and terrifying to the target. If you do, the messenger can deliver a message of no more than ten words and then the target must make a Wisdom saving throw. On a failed save, echoes of the phantasmal monstrosity spawn a nightmare that lasts the duration of the target's sleep and prevents the target from gaining any benefit from that rest. In addition, when the target wakes up, it takes 3d6 psychic damage.\
        \nIf you have a body part, lock of hair, clipping from a nail, or similar portion of the target's body, the target makes its saving throw with disadvantage.",
    duration="8 hours",
    casting_time="1 minute",
    s_range="Special",
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=["a handful of sand", "a dab of ink", "a writing quill plucked from a sleeping bird"],
)

lvl5_insect_plague = Spell(
    name="Insect Plague",
    level=5,
    school=SpellSchool.CONJURATION,
    action_cost=ActionCost.ACTION,
    description="Swarming, biting locusts fill a 20-foot-radius sphere centered on a point you choose within range. The sphere spreads around corners. The sphere remains for the duration, and its area is lightly obscured. The sphere's area is difficult terrain.\
        \nWhen the area appears, each creature in it must make a Constitution saving throw. A creature takes 4d10 piercing damage on a failed save, or half as much damage on a successful one. A creature must also make this saving throw when it enters the spell's area for the first time on a turn or ends its turn there.",
    higher_levels="When you cast this spell using a spell slot of 6th level or higher, the damage increases by 1d10 for each slot level above 5th.",
    duration="Concentration, up to 10 minutes",
    casting_time="1 action",
    s_range="300 feet",
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=["a few grains of sugar", "some kernels of grain", "a smear of fat"],
)

lvl5_passwall = Spell(
    name="Passwall",
    level=5,
    school=SpellSchool.TRANSMUTATION,
    action_cost=ActionCost.ACTION,
    description="A passage appears at a point of your choice that you can see on a wooden, plaster, or stone surface (such as a wall, a ceiling, or a floor) within range, and lasts for the duration. You choose the opening's dimensions: up to 5 feet wide, 8 feet tall, and 20 feet deep. The passage creates no instability in a structure surrounding it.\
        \nWhen the opening disappears, any creatures or objects still in the passage created by the spell are safely ejected to an unoccupied space nearest to the surface on which you cast the spell.",
    duration="1 hour",
    casting_time="1 action",
    s_range="30 feet",
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=["a pinch of sesame seeds"],
)

lvl5_scrying = Spell(
    name="Scrying",
    level=5,
    school=SpellSchool.DIVINATION,
    action_cost=ActionCost.ACTION,
    description="You can see and hear a particular creature you choose that is on the same plane of existence as you. The target must make a Wisdom saving throw, which is modified by how well you know the target and the sort of physical connection you have to it. If a target knows you're casting this spell, it can fail the saving throw voluntarily if it wants to be observed.\
        \nTABLE [Knowledge,, Save Modifier]: [Secondhand (you have heard of the target),, +5]; [Firsthand (you have met the target),, +0]; [Familiar (you know the target well),, -5]\
        \nTABLE [Connection,, Save Modifier]: [Likeness or picture,, -2]; [Possession or garment,, -4]; [Body part, lock of hair, bit of nail, or the like,, -10]\
        \nOn a successful save, the target isn't affected, and you can't use this spell against it again for 24 hours.\
        \nOn a failed save, the spell creates an invisible sensor within 10 feet of the target. You can see and hear through the sensor as if you were there. The sensor moves with the target, remaining within 10 feet of it for the duration. A creature that can see invisible objects sees the sensor as a luminous orb about the size of your fist.\
        \nInstead of targeting a creature, you can choose a location you have seen before as the target of this spell. When you do, the sensor appears at that location and doesn't move.",
    duration="Concentration, up to 10 minutes",
    casting_time="10 minutes",
    s_range="Self",
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=["a focus worth at least 1,000 gp, such as a crystal ball, a silver mirror, or a font filled with holy water"],
)

lvl5_tree_stride = Spell(
    name="Tree Stride",
    level=5,
    school=SpellSchool.CONJURATION,
    action_cost=ActionCost.ACTION,
    description="You gain the ability to enter a tree and move from inside it to inside another tree of the same kind within 500 feet.\
        \nBoth trees must be living and at least the same size as you. You must use 5 feet of movement to enter a tree. You instantly know the location of all other trees of the same kind within 500 feet and, as part of the move used to enter the tree, can either pass into one of those trees or step out of the tree you're in. You appear in a spot of your choice within 5 feet of the destination tree, using another 5 feet of movement. If you have no movement left, you appear within 5 feet of the tree you entered.\
        \nYou can use this transportation ability once per round for the duration. You must end each turn outside a tree.",
    duration="Concentration, up to 1 minute",
    casting_time="1 action",
    s_range="Self",
    components=[SpellComponent.V, SpellComponent.S],
)

lvl5_wall_of_stone = Spell(
    name="Wall of Stone",
    level=5,
    school=SpellSchool.EVOCATION,
    action_cost=ActionCost.ACTION,
    description="A nonmagical wall of solid stone springs into existence at a point you choose within range. The wall is 6 inches thick and is composed of ten 10-foot-by-10-foot panels. Each panel must be contiguous with at least one other panel. Alternatively, you can create 10-foot-by-20-foot panels that are only 3 inches thick.\
        \nIf the wall cuts through a creature's space when it appears, the creature is pushed to one side of the wall (your choice). If a creature would be surrounded on all sides by the wall (or the wall and another solid surface), that creature can make a Dexterity saving throw. On a success, it can use its reaction to move up to its speed so that it is no longer enclosed by the wall.\
        \nThe wall can have any shape you desire, though it can't occupy the same space as a creature or object. The wall doesn't need to be vertical or resting on any firm foundation. It must, however, merge with and be solidly supported by existing stone. Thus, you can use this spell to bridge a chasm or create a ramp.\
        \nIf you create a span greater than 20 feet in length, you must halve the size of each panel to create supports. You can crudely shape the wall to create crenellations, battlements, and so on.\
        \nThe wall is an object made of stone that can be damaged and thus breached. Each panel has AC 15 and 30 hit points per inch of thickness. Reducing a panel to 0 hit points destroys it and might cause connected panels to collapse at the DM's discretion.\
        \nIf you maintain your concentration on this spell for its whole duration, the wall becomes permanent and can't be dispelled. Otherwise, the wall disappears when the spell ends.",
    duration="Concentration, up to 10 minutes",
    casting_time="1 action",
    s_range="120 feet",
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=["a small block of granite"],
)


# === Array of Level 5 spells ===
lvl5_spells: List[Spell] = [
    lvl5_cloudkill, lvl5_conjure_elemental, lvl5_commune_with_nature, lvl5_cone_of_cold,
    lvl5_dream,
    lvl5_insect_plague,
    lvl5_passwall,
    lvl5_scrying,
    lvl5_tree_stride,
    lvl5_wall_of_stone,
]
