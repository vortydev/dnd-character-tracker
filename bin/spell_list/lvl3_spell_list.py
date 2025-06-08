# spell_list/lvl3_spell_list.py
from typing import List
from common import ActionCost
from spell import Spell, SpellSchool, SpellComponent, SpellTag

# === Define spells ===
lvl3_call_lightning = Spell(
    name="Call Lightning",
    level=3,
    school=SpellSchool.CONJURATION,
    action_cost=ActionCost.ACTION,
    description="A storm cloud appears in the shape of a cylinder that is 10 feet tall with a 60-foot radius, centered on a point you can see within range directly above you. The spell fails if you can't see a point in the air where the storm cloud could appear (for example, if you are in a room that can't accommodate the cloud).\
        \nWhen you cast the spell, choose a point you can see under the cloud. A bolt of lightning flashes down from the cloud to that point. Each creature within 5 feet of that point must make a Dexterity saving throw. A creature takes 3d10 lightning damage on a failed save, or half as much damage on a successful one. On each of your turns until the spell ends, you can use your action to call down lightning in this way again, targeting the same point or a different one.\
        \nIf you are outdoors in stormy conditions when you cast this spell, the spell gives you control over the existing storm instead of creating a new one. Under such conditions, the spell's damage increases by 1d10.",
    higher_levels="When you cast this spell using a spell slot of 4th or higher level, the damage increases by 1d10 for each slot level above 3rd.",
    duration="Concentration, up to 10 minutes",
    casting_time="1 action",
    s_range="120 feet",
    components=[SpellComponent.V, SpellComponent.S],
)

lvl3_create_food_water = Spell(
    name="Create Food and Water",
    level=3,
    school=SpellSchool.CONJURATION,
    action_cost=ActionCost.ACTION,
    description="You create 45 pounds of food and 30 gallons of water on the ground or in containers within range, enough to sustain up to fifteen humanoids or five steeds for 24 hours. The food is bland but nourishing, and spoils if uneaten after 24 hours. The water is clean and doesn't go bad.",
    duration="Instantaneous",
    casting_time="1 action",
    s_range="30 feet",
    components=[SpellComponent.V, SpellComponent.S],
)

lvl3_daylight = Spell(
    name="Daylight",
    level=3,
    school=SpellSchool.EVOCATION,
    action_cost=ActionCost.ACTION,
    description="A 60-foot-radius sphere of light spreads out from a point you choose within range. The sphere is bright light and sheds dim light for an additional 60 feet.\
        \nIf you chose a point on an object you are holding or one that isn't being worn or carried, the light shines from the object with and moves with it. Completely covering the affected object with an opaque object, such as a bowl or a helm, blocks the light.\
        \nIf any of this spell's area overlaps with an area of darkness created by a spell of 3rd level or lower, the spell that created the darkness is dispelled.",
    duration="1 hour",
    casting_time="1 action",
    s_range="60 feet",
    components=[SpellComponent.V, SpellComponent.S],
)

lvl3_gaseous_form = Spell(
    name="Gaseous Form",
    level=3,
    school=SpellSchool.TRANSMUTATION,
    action_cost=ActionCost.ACTION,
    description="You transform a willing creature you touch, along with everything it's wearing and carrying, into a misty cloud for the duration. The spell ends if the creature drops to 0 hit points. An incorporeal creature isn't affected.\
        \nWhile in this form, the target's only method of movement is a flying speed of 10 feet. The target can enter and occupy the space of another creature. The target has resistance to nonmagical damage, and it has advantage on Strength, Dexterity, and Constitution saving throws. The target can pass through small holes, narrow openings, and even mere cracks, though it treats liquids as though they were solid surfaces. The target can't fall and remains hovering in the air even when stunned or otherwise incapacitated.\
        \nWhile in the form of a misty cloud, the target can't talk or manipulate objects, and any objects it was carrying or holding can't be dropped, used, or otherwise interacted with. The target can't attack or cast spells.",
    duration="Concentration, up to 1 hour",
    casting_time="1 action",
    s_range="Touch",
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=["a bit of gauze", "a wisp of smoke"],
)

lvl3_haste = Spell(
    name="Haste",
    level=3,
    school=SpellSchool.TRANSMUTATION,
    action_cost=ActionCost.ACTION,
    description="Choose a willing creature that you can see within range. Until the spell ends, the target's speed is doubled, it gains a +2 bonus to AC, it has advantage on Dexterity saving throws, and it gains an additional action on each of its turns. That action can be used only to take the Attack (one weapon attack only), Dash, Disengage, Hide, or Use an Object action.\
        \nWhen the spell ends, the target can't move or take actions until after its next turn, as a wave of lethargy sweeps over it.",
    duration="Concentration, up to 1 minute",
    casting_time="1 action",
    s_range="30 feet",
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=["a shaving of licorice root"],
)

lvl3_lightning_bolt = Spell(
    name="Lightning Bolt",
    level=3,
    school=SpellSchool.EVOCATION,
    action_cost=ActionCost.ACTION,
    description="A stroke of lightning forming a line of 100 feet long and 5 feet wide blasts out from you in a direction you choose. Each creature in the line must make a Dexterity saving throw. A creature takes 8d6 lightning damage on a failed save, or half as much damage on a successful one.\
        \nThe lightning ignites flammable objects in the area that aren't being worn or carried.",
    higher_levels="When you cast this spell using a spell slot of 4th level or higher, the damage increases by 1d6 for each slot level above 3rd.",
    duration="Instantaneous",
    casting_time="1 action",
    s_range="Self (100-foot line)",
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=["a bit of fur", "a rod of amber, crystal, or glass"],
)

lvl3_meld_into_stone = Spell(
    name="Meld into Stone",
    level=3,
    school=SpellSchool.TRANSMUTATION,
    action_cost=ActionCost.ACTION,
    description="You step into a stone object or surface large enough to fully contain your body, melding yourself and all the equipment you carry with the stone for the duration. Using your movement, you step into the stone at a point you can touch. Nothing of your presence remains visible or otherwise detectable by nonmagical senses.\
        \nWhile merged with the stone, you can't see what occurs outside it, and any Wisdom (Perception) checks you make to hear sounds outside it are made with disadvantage. You remain aware of the passage of time and can cast spells on yourself while merged in the stone. You can use your movement to leave the stone where you entered it, which ends the spell. You otherwise can't move.\
        \nMinor physical damage to the stone doesn't harm you, but its partial destruction or a change in its shape (to the extent that you no longer fit within it) expels you and deals 6d6 bludgeoning damage to you. The stone's complete destruction (or transmutation into a different substance) expels you and deals 50 bludgeoning damage to you. If expelled, you fall prone in an unoccupied space closest to where you first entered.",
    duration="8 hours",
    casting_time="1 action",
    s_range="Touch",
    components=[SpellComponent.V, SpellComponent.S],
    tags=[SpellTag.RITUAL],
)

lvl3_plant_growth = Spell(
    name="Protection from Energy",
    level=3,
    school=SpellSchool.TRANSMUTATION,
    action_cost=ActionCost.ACTION,
    description="This spell channels vitality into plants within a specific area. There are two possible uses for the spell, granting either immediate or long-term benefits.\
        \nIf you cast this spell using 1 action, choose a point within range. All normal plants in a 100-foot radius centered on that point become thick and overgrown. A creature moving through the area must spend 4 feet of movement for every 1 foot it moves.\
        \nYou can exclude one or more areas of any size within the spell's area from being affected.\
        \nIf you cast this spell over 8 hours, you enrich the land. All plants in a half-mile radius centered on a point within range become enriched for 1 year. The plants yield twice the normal amount of food when harvested.",
    duration="Instantaneous",
    casting_time="1 action",
    s_range="150 feet",
    components=[SpellComponent.V, SpellComponent.S],
)

lvl3_protection_from_energy = Spell(
    name="Protection from Energy",
    level=3,
    school=SpellSchool.ABJURATION,
    action_cost=ActionCost.ACTION,
    description="For the duration, the willing creature you touch has resistance to one damage type of your choice: acid, cold, fire, lightning, or thunder.",
    duration="Concentration, up to 1 hour",
    casting_time="1 action",
    s_range="Touch",
    components=[SpellComponent.V, SpellComponent.S],
)

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
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
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
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=["a drop of molasses"],
)

lvl3_stinking_cloud = Spell(
    name="Stinking Cloud",
    level=3,
    school=SpellSchool.CONJURATION,
    action_cost=ActionCost.ACTION,
    description="You create a 20-foot-radius sphere of yellow, nauseating gas centered on a point within range. The cloud spreads around corners, and its area is heavily obscured. The cloud lingers in the air for the duration.\
        \nEach creature that is completely within the cloud at the start of its turn must make a Constitution saving throw against poison. On a failed save, the creature spends its action that turn retching and reeling. Creatures that don't need to breathe or are immune to poison automatically succeed on this saving throw.\
        \nA moderate wind (at least 10 miles per hour) disperses the cloud after 4 rounds. A strong wind (at least 20 miles per hour) disperses it after 1 round.",
    duration="Concentration, up to 1 minute",
    casting_time="1 action",
    s_range="90 feet",
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=["a rotten egg or several skunk cabbage leaves"],
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
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
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
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=["a piece of cork"],
    tags=[SpellTag.RITUAL],
)


# === Array of Level 3 spells ===
lvl3_spells: List[Spell] = [
    lvl3_call_lightning, lvl3_create_food_water,
    lvl3_daylight,
    lvl3_gaseous_form,
    lvl3_haste,
    lvl3_lightning_bolt,
    lvl3_meld_into_stone,
    lvl3_plant_growth, lvl3_protection_from_energy,
    lvl3_sleet_storm, lvl3_slow, lvl3_stinking_cloud,
    lvl3_water_breathing, lvl3_water_walk,
]
