# subclass_.py
from enum import Enum

# ===== Subclasses =====
# WIP
class SubclassType(Enum):
    # === Wizard Schools ===
    # PHB Arcane Traditions
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

    # === Sorcerous Origins ===
    DRACONIC_BLOODLINE = "Draconic Bloodline"
