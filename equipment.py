# equipment.py
from enum import Enum
from collections import defaultdict


# ===== Armor =====
class ArmorType(Enum):
    LIGHT = "Light"
    MEDIUM = "Medium"
    HEAVY = "Heavy"
    SHIELD = "Shield"

class ArmorName(Enum):
    PADDED = "Padded"
    LEATHER = "Leather"
    STUDDED_LEATHER = "Studded Leather"
    HIDE = "Hide"
    CHAIN_SHIRT = "Chain Shirt"
    SCALE_MAIL = "Scale Mail"
    BREASTPLATE = "Breastplate"
    HALF_PLATE = "Half-Plate"
    RING_MAIL = "Ring Mail"
    CHAIN_MAIL = "Chain Mail"
    SPLINT = "Splint"
    PLATE = "Plate"
    SHIELD = "Shield"

ARMOR_TYPE_MAP = {
    # Light armor
    ArmorName.PADDED: ArmorType.LIGHT,
    ArmorName.LEATHER: ArmorType.LIGHT,
    ArmorName.STUDDED_LEATHER: ArmorType.LIGHT,

    # Medium armor
    ArmorName.HIDE: ArmorType.MEDIUM,
    ArmorName.CHAIN_SHIRT: ArmorType.MEDIUM,
    ArmorName.SCALE_MAIL: ArmorType.MEDIUM,
    ArmorName.BREASTPLATE: ArmorType.MEDIUM,
    ArmorName.HALF_PLATE: ArmorType.MEDIUM,

    # Heavy armor
    ArmorName.RING_MAIL: ArmorType.HEAVY,
    ArmorName.CHAIN_MAIL: ArmorType.HEAVY,
    ArmorName.SPLINT: ArmorType.HEAVY,
    ArmorName.PLATE: ArmorType.HEAVY,

    # Shield
    ArmorName.SHIELD: ArmorType.SHIELD,
}

ARMORS_BY_TYPE = defaultdict(list)
for armor, armor_type in ARMOR_TYPE_MAP.items():
    ARMORS_BY_TYPE[armor_type].append(armor)


# ===== Weapons =====
class WeaponType(Enum):
    SIMPLE_MELEE = "Simple Melee"
    SIMPLE_RANGED = "Simple Ranged"
    MARTIAL_MELEE = "Martial Melee"
    MARTIAL_RANGED = "Martial Ranged"

class WeaponName(Enum):
    # Simple Melee
    CLUB = "Club"
    DAGGER = "Dagger"
    GREATCLUB = "Greatclub"
    HANDAXE = "Handaxe"
    JAVELIN = "Javelin"
    LIGHT_HAMMER = "Light Hammer"
    MACE = "Mace"
    QUARTERSTAFF = "Quarterstaff"
    SICKLE = "Sickle"
    SPEAR = "Spear"

    # Simple Ranged
    LIGHT_CROSSBOW = "Light Crossbow"
    DART = "Dart"
    SHORTBOW = "Shortbow"
    SLING = "Sling"

    # Martial Melee
    BATTLEAXE = "Battleaxe"
    FLAIL = "Flail"
    GLAIVE = "Glaive"
    GREATAXE = "Greataxe"
    GREATSWORD = "Greatsword"
    HALBERD = "Halberd"
    LANCE = "Lance"
    LONGSWORD = "Longsword"
    MAUL = "Maul"
    MORNINGSTAR = "Morningstar"
    PIKE = "Pike"
    RAPIER = "Rapier"
    SCIMITAR = "Scimitar"
    SHORTSWORD = "Shortsword"
    TRIDENT = "Trident"
    WAR_PICK = "War Pick"
    WARHAMMER = "Warhammer"
    WHIP = "Whip"

    # Martial Ranged
    BLOWGUN = "Blowgun"
    HAND_CROSSBOW = "Hand Crossbow"
    HEAVY_CROSSBOW = "Heavy Crossbow"
    LONGBOW = "Longbow"
    NET = "Net"


WEAPON_TYPE_MAP = {
    # Simple Melee
    WeaponName.CLUB: WeaponType.SIMPLE_MELEE,
    WeaponName.DAGGER: WeaponType.SIMPLE_MELEE,
    WeaponName.GREATCLUB: WeaponType.SIMPLE_MELEE,
    WeaponName.HANDAXE: WeaponType.SIMPLE_MELEE,
    WeaponName.JAVELIN: WeaponType.SIMPLE_MELEE,
    WeaponName.LIGHT_HAMMER: WeaponType.SIMPLE_MELEE,
    WeaponName.MACE: WeaponType.SIMPLE_MELEE,
    WeaponName.QUARTERSTAFF: WeaponType.SIMPLE_MELEE,
    WeaponName.SICKLE: WeaponType.SIMPLE_MELEE,
    WeaponName.SPEAR: WeaponType.SIMPLE_MELEE,

    # Simple Ranged
    WeaponName.LIGHT_CROSSBOW: WeaponType.SIMPLE_RANGED,
    WeaponName.DART: WeaponType.SIMPLE_RANGED,
    WeaponName.SHORTBOW: WeaponType.SIMPLE_RANGED,
    WeaponName.SLING: WeaponType.SIMPLE_RANGED,

    # Martial Melee
    WeaponName.BATTLEAXE: WeaponType.MARTIAL_MELEE,
    WeaponName.FLAIL: WeaponType.MARTIAL_MELEE,
    WeaponName.GLAIVE: WeaponType.MARTIAL_MELEE,
    WeaponName.GREATAXE: WeaponType.MARTIAL_MELEE,
    WeaponName.GREATSWORD: WeaponType.MARTIAL_MELEE,
    WeaponName.HALBERD: WeaponType.MARTIAL_MELEE,
    WeaponName.LANCE: WeaponType.MARTIAL_MELEE,
    WeaponName.LONGSWORD: WeaponType.MARTIAL_MELEE,
    WeaponName.MAUL: WeaponType.MARTIAL_MELEE,
    WeaponName.MORNINGSTAR: WeaponType.MARTIAL_MELEE,
    WeaponName.PIKE: WeaponType.MARTIAL_MELEE,
    WeaponName.RAPIER: WeaponType.MARTIAL_MELEE,
    WeaponName.SCIMITAR: WeaponType.MARTIAL_MELEE,
    WeaponName.SHORTSWORD: WeaponType.MARTIAL_MELEE,
    WeaponName.TRIDENT: WeaponType.MARTIAL_MELEE,
    WeaponName.WAR_PICK: WeaponType.MARTIAL_MELEE,
    WeaponName.WARHAMMER: WeaponType.MARTIAL_MELEE,
    WeaponName.WHIP: WeaponType.MARTIAL_MELEE,

    # Martial Ranged
    WeaponName.BLOWGUN: WeaponType.MARTIAL_RANGED,
    WeaponName.HAND_CROSSBOW: WeaponType.MARTIAL_RANGED,
    WeaponName.HEAVY_CROSSBOW: WeaponType.MARTIAL_RANGED,
    WeaponName.LONGBOW: WeaponType.MARTIAL_RANGED,
    WeaponName.NET: WeaponType.MARTIAL_RANGED,
}

WEAPONS_BY_TYPE = defaultdict(list)
for weapon, weapon_type in WEAPON_TYPE_MAP.items():
    WEAPONS_BY_TYPE[weapon_type].append(weapon)
