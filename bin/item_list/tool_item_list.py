# tool_item_list.py
from items.tool_item import ToolItem, ToolType
from currency import Currency, CurrencyCost

# === Define Tools ===

# Artisan's tools ============================================================================================

art_alchemist = ToolItem(
    name="Alchemist's supplies",
    tool_type=ToolType.ARTISAN,
    cost=50,
    weight=8
)

art_brewer = ToolItem(
    name="Brewer's supplies",
    tool_type=ToolType.ARTISAN,
    cost=20,
    weight=9
)

art_calligrapher = ToolItem(
    name="Calligrapher's supplies",
    tool_type=ToolType.ARTISAN,
    cost=10,
    weight=5
)

art_carpenter = ToolItem(
    name="Carpenter's tools",
    tool_type=ToolType.ARTISAN,
    cost=8,
    weight=6
)

art_cartographer = ToolItem(
    name="Cartographer's tools",
    tool_type=ToolType.ARTISAN,
    cost=15,
    weight=6
)

art_cobbler = ToolItem(
    name="Cobbler's tools",
    tool_type=ToolType.ARTISAN,
    cost=5,
    weight=5
)

art_cook = ToolItem(
    name="Cook's utensils",
    tool_type=ToolType.ARTISAN,
    cost=1,
    weight=8
)

art_glassblower = ToolItem(
    name="Glassblower's tools",
    tool_type=ToolType.ARTISAN,
    cost=30,
    weight=5
)

art_jeweler = ToolItem(
    name="Jeweler's tools",
    tool_type=ToolType.ARTISAN,
    cost=25,
    weight=2
)

art_leatherworker = ToolItem(
    name="Leatherworker's tools",
    tool_type=ToolType.ARTISAN,
    cost=5,
    weight=5
)

art_mason = ToolItem(
    name="Mason's tools",
    tool_type=ToolType.ARTISAN,
    cost=10,
    weight=8
)

art_painter = ToolItem(
    name="Painter's supplies",
    tool_type=ToolType.ARTISAN,
    cost=10,
    weight=5
)

art_potter = ToolItem(
    name="Potter's tools",
    tool_type=ToolType.ARTISAN,
    cost=10,
    weight=3
)

art_smith = ToolItem(
    name="Smith's tools",
    tool_type=ToolType.ARTISAN,
    cost=20,
    weight=8
)

art_tinker = ToolItem(
    name="Tinker's tools",
    tool_type=ToolType.ARTISAN,
    cost=50,
    weight=10
)

art_weaver = ToolItem(
    name="Weaver's tools",
    tool_type=ToolType.ARTISAN,
    cost=1,
    weight=5
)

art_woodcarver = ToolItem(
    name="Woodcarver's tools",
    tool_type=ToolType.ARTISAN,
    cost=1,
    weight=5
)

artisan_tools: list[ToolItem] = [
    art_alchemist, art_brewer, art_calligrapher, art_carpenter, art_cartographer,
    art_cobbler, art_cook, art_glassblower, art_jeweler, art_leatherworker,
    art_mason, art_painter, art_potter, art_smith, art_tinker,
    art_weaver, art_woodcarver
]

# Gaming sets ================================================================================================

gs_dice = ToolItem(
    name="Dice set",
    tool_type=ToolType.GAMING,
    cost=CurrencyCost(1, Currency.SP),
)

gs_dragonchess = ToolItem(
    name="Dragonchess set",
    tool_type=ToolType.GAMING,
    cost=1,
    weight=0.5
)

gs_cards = ToolItem(
    name="Playing card set",
    tool_type=ToolType.GAMING,
    cost=CurrencyCost(5, Currency.SP),
)

gs_three_dragon_ante = ToolItem(
    name="Three-Dragon Ante set",
    tool_type=ToolType.GAMING,
    cost=1,
)

gaming_set_items: list[ToolItem] = [gs_dice,gs_dragonchess, gs_cards, gs_three_dragon_ante]

# Musical items ==============================================================================================

mus_bagpipes = ToolItem(name="Bagpipes", tool_type=ToolType.MUSICAL, cost=30, weight=6)
mus_drum = ToolItem(name="Drum", tool_type=ToolType.MUSICAL, cost=6, weight=3)
mus_dulcimer = ToolItem(name="Dulcimer", tool_type=ToolType.MUSICAL, cost=25, weight=10)
mus_flute = ToolItem(name="Flute", tool_type=ToolType.MUSICAL, cost=2, weight=1)
mus_lute = ToolItem(name="Lute", tool_type=ToolType.MUSICAL, cost=35, weight=2)
mus_lyre = ToolItem(name="Lyre", tool_type=ToolType.MUSICAL, cost=30, weight=2)
mus_horn = ToolItem(name="Horn", tool_type=ToolType.MUSICAL, cost=3, weight=2)
mus_pan_flute = ToolItem(name="Pan flute", tool_type=ToolType.MUSICAL, cost=12, weight=2)
mus_shawn = ToolItem(name="Shawm", tool_type=ToolType.MUSICAL, cost=2, weight=1)
mus_viol = ToolItem(name="Viol", tool_type=ToolType.MUSICAL, cost=30, weight=1)

musical_items: list[ToolItem] = [
    mus_bagpipes, mus_drum, mus_dulcimer, mus_flute, mus_lute,
    mus_lyre, mus_horn, mus_pan_flute, mus_shawn, mus_viol
]


# Miscellaneous items ========================================================================================

misc_disguise_kit = ToolItem(name="Disguise kit", tool_type=ToolType.MISC, cost=25, weight=3)
misc_forgery_kit = ToolItem(name="Forgery  kit", tool_type=ToolType.MISC, cost=15, weight=5)
misc_herbalism_kit = ToolItem(name="Herbalism kit", tool_type=ToolType.MISC, cost=5, weight=3)
misc_navigators_tools = ToolItem(name="Navigator's tools", tool_type=ToolType.MISC, cost=25, weight=2)
misc_poisoners_kit = ToolItem(name="Poisoner's kit", tool_type=ToolType.MISC, cost=50, weight=2)
misc_thieves_tools = ToolItem(name="Thieves' tools", tool_type=ToolType.MISC, cost=25, weight=1)

misc_items: list[ToolItem] = [
    misc_disguise_kit, misc_forgery_kit, misc_herbalism_kit, 
    misc_navigators_tools, misc_poisoners_kit, misc_thieves_tools
]