# class_levels/rogue_class_levels.py
from class_base import ClassType
from class_level import ClassLevelRogue
from feature import FeatureType
from feature_registry import FeatureRegistry
from feature_io import load_features_from_file

# Load features
feats = load_features_from_file()
FeatureRegistry.load_bulk(feats)

rogue_cl = [] # Empty array

rogue_lvl1 = ClassLevelRogue(
    lvl=1, class_type=ClassType.ROGUE,
    features=[
        FeatureRegistry.get("Expertise", FeatureType.CLASS, ClassType.ROGUE),
        FeatureRegistry.get("Sneak Attack", FeatureType.CLASS, ClassType.ROGUE),
        FeatureRegistry.get("Thieves' Cant", FeatureType.CLASS, ClassType.ROGUE),
    ],
)

rogue_lvl2 = ClassLevelRogue(
    lvl=2, class_type=ClassType.ROGUE,
    features=[
        FeatureRegistry.get("Cunning Action", FeatureType.CLASS, ClassType.ROGUE),
    ],
)

rogue_lvl3 = ClassLevelRogue(
    lvl=3, class_type=ClassType.ROGUE,
    features=[
        FeatureRegistry.get("Roguish Archetype", FeatureType.CLASS, ClassType.ROGUE),
        FeatureRegistry.get("Steady Aim (Optional)", FeatureType.CLASS, ClassType.ROGUE),
    ],
    sneak_attack_dice=2,
)

rogue_lvl4 = ClassLevelRogue(
    lvl=4, class_type=ClassType.ROGUE,
    features=[
        FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.ROGUE),
    ],
    sneak_attack_dice=2,
)

rogue_lvl5 = ClassLevelRogue(
    lvl=5, class_type=ClassType.ROGUE,
    features=[
        FeatureRegistry.get("Uncanny Dodge", FeatureType.CLASS, ClassType.ROGUE),
    ],
    sneak_attack_dice=3,
)

rogue_lvl6 = ClassLevelRogue(
    lvl=6, class_type=ClassType.ROGUE,
    features=[
        FeatureRegistry.get("Expertise", FeatureType.CLASS, ClassType.ROGUE),
    ],
    sneak_attack_dice=3,
)

rogue_lvl7 = ClassLevelRogue(
    lvl=7, class_type=ClassType.ROGUE,
    features=[
        FeatureRegistry.get("Evasion", FeatureType.CLASS, ClassType.ROGUE),
    ],
    sneak_attack_dice=4,
)

rogue_lvl8 = ClassLevelRogue(
    lvl=8, class_type=ClassType.ROGUE,
    features=[
        FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.ROGUE),
    ],
    sneak_attack_dice=4,
)

rogue_lvl9 = ClassLevelRogue(
    lvl=9, class_type=ClassType.ROGUE,
    sneak_attack_dice=5,
)

rogue_lvl10 = ClassLevelRogue(
    lvl=10, class_type=ClassType.ROGUE,
    features=[
        FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.ROGUE),
    ],
    sneak_attack_dice=5,
)

rogue_lvl11 = ClassLevelRogue(
    lvl=11, class_type=ClassType.ROGUE,
    features=[
        FeatureRegistry.get("Reliable Talent", FeatureType.CLASS, ClassType.ROGUE),
    ],
    sneak_attack_dice=6,
)

rogue_lvl12 = ClassLevelRogue(
    lvl=12, class_type=ClassType.ROGUE,
    features=[
        FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.ROGUE),
    ],
    sneak_attack_dice=6,
)

rogue_lvl13 = ClassLevelRogue(
    lvl=13, class_type=ClassType.ROGUE,
    sneak_attack_dice=7,
)

rogue_lvl14 = ClassLevelRogue(
    lvl=14, class_type=ClassType.ROGUE,
    features=[
        FeatureRegistry.get("Blindsense", FeatureType.CLASS, ClassType.ROGUE),
    ],
    sneak_attack_dice=7,
)

rogue_lvl15 = ClassLevelRogue(
    lvl=15, class_type=ClassType.ROGUE,
    features=[
        FeatureRegistry.get("Slippery Mind", FeatureType.CLASS, ClassType.ROGUE),
    ],
    sneak_attack_dice=8,
)

rogue_lvl16 = ClassLevelRogue(
    lvl=16, class_type=ClassType.ROGUE,
    features=[
        FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.ROGUE),
    ],
    sneak_attack_dice=8,
)

rogue_lvl17 = ClassLevelRogue(
    lvl=17, class_type=ClassType.ROGUE,
    sneak_attack_dice=9,
)

rogue_lvl18 = ClassLevelRogue(
    lvl=18, class_type=ClassType.ROGUE,
    features=[
        FeatureRegistry.get("Elusive", FeatureType.CLASS, ClassType.ROGUE),
    ],
    sneak_attack_dice=9,
)

rogue_lvl19 = ClassLevelRogue(
    lvl=19, class_type=ClassType.ROGUE,
    features=[
        FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.ROGUE),
    ],
    sneak_attack_dice=10,
)

rogue_lvl20 = ClassLevelRogue(
    lvl=20, class_type=ClassType.ROGUE,
    features=[
        FeatureRegistry.get("Stroke of Luck", FeatureType.CLASS, ClassType.ROGUE)
    ],
    sneak_attack_dice=10,
)


# Load class levels in array
rogue_cl = [
    rogue_lvl1, rogue_lvl2, rogue_lvl3, rogue_lvl4, rogue_lvl5,
    rogue_lvl6, rogue_lvl7, rogue_lvl8, rogue_lvl9, rogue_lvl10,
    rogue_lvl11, rogue_lvl12, rogue_lvl13, rogue_lvl14, rogue_lvl15,
    rogue_lvl16, rogue_lvl17, rogue_lvl18, rogue_lvl19, rogue_lvl20,
]