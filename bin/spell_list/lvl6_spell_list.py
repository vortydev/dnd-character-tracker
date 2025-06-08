# spell_list/lvl6_spell_list.py
from typing import List
from common import ActionCost
from spell import Spell, SpellSchool, SpellComponent, SpellTag

# === Define spells ===
lvl6_sunbeam = Spell(
    name="Sunbeam",
    level=6,
    school=SpellSchool.EVOCATION,
    action_cost=ActionCost.ACTION,
    description="A beam of brilliant light flashes out from your hand in a 5-foot-wide, 60-foot-line. Each creature in the line must make a Constitution saving throw. On a failed save, a creature takes 6d8 radiant damage and is blinded until your next turn. On a successful save, it takes half as much damage and isn't blinded by this spell. Undead and oozes have disadvantage on this saving throw.\
        \nYou can create a new line of radiance as your action on any turn until the spell ends.\
        \nFor the duration, a mote of brilliant radiance shines in your hand. It sheds bright light in a 30-foot radius and dim light for an additional 30 feet. The light is sunlight.",
    duration="Concentration, up to 1 minute",
    casting_time="1 action",
    s_range="Self (60-foot line)",
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=["a magnifying glass"],
)

# === Array of Level 6 spells ===
lvl6_spells: List[Spell] = [
    lvl6_sunbeam,
]
