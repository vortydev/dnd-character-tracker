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
    SIMPLE = "Simple"
    MARTIAL = "Martial"

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
    WeaponName.CLUB: WeaponType.SIMPLE,
    WeaponName.DAGGER: WeaponType.SIMPLE,
    WeaponName.GREATCLUB: WeaponType.SIMPLE,
    WeaponName.HANDAXE: WeaponType.SIMPLE,
    WeaponName.JAVELIN: WeaponType.SIMPLE,
    WeaponName.LIGHT_HAMMER: WeaponType.SIMPLE,
    WeaponName.MACE: WeaponType.SIMPLE,
    WeaponName.QUARTERSTAFF: WeaponType.SIMPLE,
    WeaponName.SICKLE: WeaponType.SIMPLE,
    WeaponName.SPEAR: WeaponType.SIMPLE,

    # Simple Ranged
    WeaponName.LIGHT_CROSSBOW: WeaponType.SIMPLE,
    WeaponName.DART: WeaponType.SIMPLE,
    WeaponName.SHORTBOW: WeaponType.SIMPLE,
    WeaponName.SLING: WeaponType.SIMPLE,

    # Martial Melee
    WeaponName.BATTLEAXE: WeaponType.MARTIAL,
    WeaponName.FLAIL: WeaponType.MARTIAL,
    WeaponName.GLAIVE: WeaponType.MARTIAL,
    WeaponName.GREATAXE: WeaponType.MARTIAL,
    WeaponName.GREATSWORD: WeaponType.MARTIAL,
    WeaponName.HALBERD: WeaponType.MARTIAL,
    WeaponName.LANCE: WeaponType.MARTIAL,
    WeaponName.LONGSWORD: WeaponType.MARTIAL,
    WeaponName.MAUL: WeaponType.MARTIAL,
    WeaponName.MORNINGSTAR: WeaponType.MARTIAL,
    WeaponName.PIKE: WeaponType.MARTIAL,
    WeaponName.RAPIER: WeaponType.MARTIAL,
    WeaponName.SCIMITAR: WeaponType.MARTIAL,
    WeaponName.SHORTSWORD: WeaponType.MARTIAL,
    WeaponName.TRIDENT: WeaponType.MARTIAL,
    WeaponName.WAR_PICK: WeaponType.MARTIAL,
    WeaponName.WARHAMMER: WeaponType.MARTIAL,
    WeaponName.WHIP: WeaponType.MARTIAL,

    # Martial Ranged
    WeaponName.BLOWGUN: WeaponType.MARTIAL,
    WeaponName.HAND_CROSSBOW: WeaponType.MARTIAL,
    WeaponName.HEAVY_CROSSBOW: WeaponType.MARTIAL,
    WeaponName.LONGBOW: WeaponType.MARTIAL,
    WeaponName.NET: WeaponType.MARTIAL,
}

WEAPONS_BY_TYPE = defaultdict(list)
for weapon, weapon_type in WEAPON_TYPE_MAP.items():
    WEAPONS_BY_TYPE[weapon_type].append(weapon)
