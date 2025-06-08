# spell_list/lvl8_spell_list.py
from typing import List
from common import ActionCost
from spell import Spell, SpellSchool, SpellComponent, SpellTag

# === Define spells ===
lvl8_sunburst = Spell(
    name="Sunburst",
    level=8,
    school=SpellSchool.EVOCATION,
    action_cost=ActionCost.ACTION,
    description="Brilliant sunlight flashes in a 60-foot radius centered on a point you choose within range. Each creature in that light must make a Constitution saving throw. On a failed save, a creature takes 12d6 radiant damage and is blinded for 1 minute. On a successful save, it takes half as much damage and isn’t blinded by this spell. Undead and oozes have disadvantage on this saving throw.\
        \nA creature blinded by this spell makes another Constitution saving throw at the end of each of its turns. On a successful save, it is no longer blinded.\
        \nThis spell dispels any darkness in its area that was created by a spell.",
    duration="Instantaneous",
    casting_time="1 action",
    s_range="150 feet",
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=["fire", "a piece of sunstone"],
)


# === Array of Level 8 spells ===
lvl8_spells: List[Spell] = [
    lvl8_sunburst,
]
