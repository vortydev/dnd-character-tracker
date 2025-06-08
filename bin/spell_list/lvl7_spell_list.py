# spell_list/lvl7_spell_list.py
from typing import List
from common import ActionCost
from spell import Spell, SpellSchool, SpellComponent, SpellTag

# === Define spells ===
lvl7_resurrection = Spell(
    name="Resurrection",
    level=7,
    school=SpellSchool.NECROMANCY,
    action_cost=ActionCost.ACTION,
    description="You touch a dead creature that has been dead for no more than a century, that didn't die of old age, and that isn't undead. If its soul is free and willing, the target returns to life with all its hit points.\
        \nThis spell neutralizes any poisons and cures normal diseases afflicting the creature when it died. It doesn't, however, remove magical diseases, curses, and the like; if such affects aren't removed prior to casting the spell, they afflict the target on its return to life.\
        \nThis spell closes all mortal wounds and restores any missing body parts.\
        \nComing back from the dead is an ordeal. The target takes a -4 penalty to all attack rolls, saving throws, and ability checks. Every time the target finishes a long rest, the penalty is reduced by 1 until it disappears.\
        \nCasting this spell to restore life to a creature that has been dead for one year or longer taxes you greatly. Until you finish a long rest, you can't cast spells again, and you have disadvantage on all attack rolls, ability checks, and saving throws.",
    duration="Instantaneous",
    casting_time="1 hour",
    s_range="Touch",
    components=[SpellComponent.V, SpellComponent.S, SpellComponent.M],
    material_description=["a diamond worth at least 1,000 gp, which the spell consumes"],
)

# === Array of Level 7 spells ===
lvl7_spells: List[Spell] = [
    lvl7_resurrection,
]
