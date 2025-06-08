# spell_list/lvl5_spell_list.py
from typing import List
from common import ActionCost
from spell import Spell, SpellSchool, SpellComponent, SpellTag

# === Define spells ===
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
    components=[ SpellComponent.V, SpellComponent.S, SpellComponent.M ],
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
    components=[ SpellComponent.V, SpellComponent.S ],
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
    components=[ SpellComponent.V, SpellComponent.S, SpellComponent.M ],
    material_description=["a small crystal or glass cone"],
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
    components=[ SpellComponent.V, SpellComponent.S, SpellComponent.M ],
    material_description=["a focus worth at least 1,000 gp, such as a crystal ball, a silver mirror, or a font filled with holy water"],
)


# === Array of Level 5 spells ===
lvl5_spells: List[Spell] = [
    lvl5_conjure_elemental, lvl5_commune_with_nature, lvl5_cone_of_cold,
    lvl5_scrying,
]
