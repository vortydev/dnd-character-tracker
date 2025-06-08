# misc.py
from enum import Enum

class Size(Enum):
    """Standard creature size categories in D&D 5e."""
    TINY = "Tiny"
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"
    HUGE = "Huge"
    GARGANTUAN = "Gargantuan"


class Language(Enum):
    """Common languages used in D&D 5e."""
    COMMON = "Common"
    DWARVISH = "Dwarvish"
    ELVISH = "Elvish"
    GIANT = "Giant"
    GNOMISH = "Gnomish"
    GOBLIN = "Goblin"
    HALFLING = "Halfling"
    INFERNAL = "Infernal"
    DRACONIC = "Draconic"
    CELESTIAL = "Celestial"
    ABYSSAL = "Abyssal"
    ORC = "Orc"
    DEEP_SPEECH = "Deep Speech"
    PRIMORDIAL = "Primordial"
    SYLVAN = "Sylvan"
    UNDERCOMMON = "Undercommon"


class DamageType(Enum):
    """All damage types recognized in D&D 5e."""
    ACID = "Acid"
    BLUDGEONING = "Bludgeoning"
    COLD = "Cold"
    FIRE = "Fire"
    FORCE = "Force"
    LIGHTNING = "Lightning"
    NECROTIC = "Necrotic"
    PIERCING = "Piercing"
    POISON = "Poison"
    PSYCHIC = "Psychic"
    RADIANT = "Radiant"
    SLASHING = "Slashing"
    THUNDER = "Thunder"
    

class ActionCost(Enum):
    """Types of action costs in D&D 5e."""
    NONE = "None"
    ACTION = "Action"
    BONUS_ACTION = "Bonus Action"
    REACTION = "Reaction"
    RITUAL = "Ritual"


class Source(Enum):
    """Sourcebooks for D&D 5e material."""
    PHB = "Player's Handbook"
    DMG = "Dungeon Master's Guide"
    MM = "Monster Manual"
    VGTM = "Volo's Guide to Monsters"
    XGTE = "Xanathar's Guide to Everything"
    MTOF = "Mordenkainen's Tome of Foes"
    SCAG = "Sword Coast Adventurer's Guide"
    UA = "Unearthed Arcana"
