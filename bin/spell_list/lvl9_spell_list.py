# spell_list/lvl9_spell_list.py
from typing import List
from common import ActionCost
from spell import Spell, SpellSchool, SpellComponent

# === Define spells ===
lvl9_wish = Spell(
    name="Wish",
    level=9,
    school=SpellSchool.CONJURATION,
    action_cost=ActionCost.ACTION,
    description="Wish is the mightiest spell a mortal creature can cast. By simply speaking aloud, you can alter the very foundations of reality in accord with your desires.\
        \nThe basic use of this spell is to duplicate any other spell of 8th level or lower. You don't need to meet any requirements in that spell, including costly components. The spell simply takes effect.\
        \nAlternatively, you can create one of the following effects of your choice:\
        \n- You create one object of up to 25,000 gp in value that isn't a magic item. The object can be no more than 300 feet in any dimension, and it appears in an unoccupied space you can see on the ground.\
        \n- You allow up to twenty creatures that you can see to regain all hit points, and you end all effects on them described in the greater restoration spell.\
        \n- You grant up to ten creatures that you can see resistance to a damage type you choose.\
        \n- You grant up to ten creatures you can see immunity to a single spell or other magical effect for 8 hours. For instance, you could make yourself and all your companions immune to a lich's life drain attack.\
        \n- You undo a single recent event by forcing a reroll of any roll made within the last round (including your last turn). Reality reshapes itself to accommodate the new result. For example, a wish spell could undo an opponent's successful save, a foe's critical hit, or a friend's failed save. You can force the reroll to be made with advantage or disadvantage, and you can choose whether to use the reroll or the original roll.\
        \nYou might be able to achieve something beyond the scope of the above examples. State your wish to the DM as precisely as possible. The DM has great latitude in ruling what occurs in such an instance; the greater the wish, the greater the likelihood that something goes wrong. This spell might simply fail, the effect you desire might only be partly achieved, or you might suffer some unforeseen consequence as a result of how you worded the wish. For example, wishing that a villain were dead might propel you forward in time to a period when that villain is no longer alive, effectively removing you from the game. Similarly, wishing for a legendary magic item or artifact might instantly transport you to the presence of the item's current owner.\
        \nThe stress of casting this spell to produce any effect other than duplicating another spell weakens you. After enduring that stress, each time you cast a spell until you finish a long rest, you take 1d10 necrotic damage per level of that spell. This damage can't be reduced or prevented in any way. In addition, your Strength drops to 3, if it isn't 3 or lower already, for 2d4 days. For each of those days that you spend resting and doing nothing more than light activity, your remaining recovery time decreases by 2 days. Finally, there is a 33 percent chance that you are unable to cast wish ever again if you suffer this stress.",
    duration="Instantaneous",
    casting_time="1 action",
    s_range="Self",
    components=[SpellComponent.V],
)

# === Array of Level 9 spells ===
lvl9_spells: List[Spell] = [
    lvl9_wish,
]
