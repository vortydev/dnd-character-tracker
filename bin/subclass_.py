# subclass_.py
from enum import Enum

# ===== Subclasses =====
# WIP
class SubclassType(Enum):
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


    # === SORCERER Sorcerous Origins ===
    DRACONIC_BLOODLINE = "Draconic Bloodline"


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
