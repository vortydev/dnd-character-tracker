# subclass_.py
from enum import Enum

# ===== Subclasses =====
# WIP
class SubclassType(Enum):
    # === DRUID Circles ===
    CIRCLE_DREAMS = "Circle of Dreams"
    CIRCLE_LAND = "Circle of the Land"
    CIRCLE_MOON = "Circle of the Moon"
    CIRCLE_SHEPERD = "Circle of the Sheperd"
    CIRCLE_SPORES = "Circle of Spores"
    CIRCLE_STARS = "Circle of Stars"
    CIRCLE_WILDLIFE = "Circle of Wildlife"


    # === FIGHTER Martial Archetypes ===
    # Player's Handbook
    BATTLE_MASTER = "Battle Master"
    CHAMPION = "Champion"
    ELDRITCH_KNIGHT = "Eldritch Knight"

    # Xanathar's Guide to Everything
    ARCANE_ARCHER = "Arcane Archer"
    CAVALIER = "Cavalier"
    SAMURAI = "Samurai"

    # Tasha's Cauldron of Everything
    PSI_WARRIOR = "Psi Warrior"
    RUNE_KNIGHT = "Rune Knight"

    # Sword Coast Adventurer's Guide
    BANNERET = "Banneret"

    # Explorer's Guide to Wildemount
    ECHO_KNIGHT = "Echo Knight"


    # === MONK Monastic Traditions ===
    ASTRAL_SELF = "Astral Self"
    ASCENDANT_DRAGON = "Ascendant Dragon"
    DRUNKEN_MASTER = "Drunken Master"
    FOUR_ELEMENTS = "Four Elements"
    KENSEI = "Kensei"
    LONG_DEATH = "Long Death"
    MERCY = "Mercy"
    OPEN_HAND = "Open Hand"
    SHADOW = "Shadow"
    SUN_SOUL = "Sun Soul"


    # === RANGER Conclaves ===
    BEAST_MASTER = "Beast Master"
    FEY_WANDERER = "Fey Wanderer"
    GLOOM_STALKER = "Gloom Stalker"
    HORIZON_WALKER = "Horizon Walker"
    HUNTER = "Hunter"
    MONSTER_SLAYER = "Monster Slayer"
    SWARMKEEPER = "Swarmkeeper"
    DRAKEWARDEN = "Drakewarden"


    # === ROGUE Roguish Archetype ===
    ARCANE_TRICKSTER = "Arcane Trickster"
    ASSASSIN = "Assassin"
    INQUISITIVE = "Inquisitive"
    MASTERMIND = "Mastermind"
    PHANTOM = "Phantom"
    SCOUT = "Scout"
    SOULKNIFE = "Soulknife"
    SWASHBUCKLER = "Swashbuckler"
    THIEF = "Thief"


    # === SORCERER Sorcerous Origins ===
    # Player's Handbook
    DRACONIC_BLOODLINE = "Draconic Bloodline"
    WILD_MAGIC = "Wild Magic"

    # Xanathar's Guide to Everything
    DIVINE_SOUL = "Divine Soul"
    SHADOW_MAGIC = "Shadow Magic"
    STORM_SORCERY = "Storm Sorcery"

    # Tasha's Cauldron of Everything
    ABERRANT_MIND = "Aberrant Mind"
    CLOCKWORK_SOUL = "Clockwork Soul"

    # Dragonlance: Shadow of the Dragon Queen
    LUNAR_SORCERY = "Lunar Sorcery"


    # === WARLOCK Otherwrdly Patron ===
    # Player's Handbook
    ARCHFEY = "Archfey"
    FIEND = "Fiend"
    GREAT_OLD_ONE = "Great Old One"

    # Xanathar's Guide to Everything
    CELESTIAL = "Celestial"
    HEXBLADE = "Hexblade"

    # Tasha's Cauldron of Everything
    FATHOMLESS = "Fathomless"
    GENIE = "Genie"

    # Van Richten's Guide to Ravenloft
    UNDEAD = "Undead"

    # Sword Coast Adventurer's Guide
    UNDYING = "Undying"

    # === WIZARD Arcane Traditions ===
    # Player's Handbook
    ABJURATION = "School of Abjuration"
    CONJURATION = "School of Conjuration"
    DIVINATION = "School of Divination"
    ENCHANTMENT = "School of Enchantment"
    EVOCATION = "School of Evocation"
    ILLUSION = "School of Illusion"
    NECROMANCY = "School of Necromancy"
    TRANSMUTATION = "School of Transmutation"

    # Additional Wizard subclasses from other sources
    BLADESINGING = "Bladesinging"
    WAR_MAGIC = "War Magic"
    ORDER_OF_SCRIBES = "Order of Scribes"
    GRAVITURGY_MAGIC = "Graviturgy Magic"
    CHRONURGY_MAGIC = "Chronurgy Magic"

    # === ARTIFICER Specialist ===
    ALCHEMIST = "Alchemist"
    ARMORER = "Armorer"
    ARTILLERIST = "Artillerist"
    BATTLE_SMITH = "Battle Smith"