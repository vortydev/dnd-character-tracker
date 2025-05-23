# class_levels/sorcerer_class_levels.py
from class_ import ClassType
from class_level import ClassLevelSorcerer
from feature import FeatureType
from feature_registry import FeatureRegistry
from feature_io import load_features_from_file

# Load features
feats = load_features_from_file("features.json")
FeatureRegistry.load_bulk(feats)

sorcerer_cl = [] # Empty array

sorc_lvl1 = ClassLevelSorcerer(
    lvl=1, class_type=ClassType.SORCERER,
    features=[
        FeatureRegistry.get("Spellcasting", FeatureType.CLASS, ClassType.SORCERER),
        FeatureRegistry.get("Sorcerous Origin", FeatureType.CLASS, ClassType.SORCERER)
    ],
    known_cantrips=4
)

sorc_lvl2 = ClassLevelSorcerer(
    lvl=2, class_type=ClassType.SORCERER,
    features=[FeatureRegistry.get("Font of Magic", FeatureType.CLASS, ClassType.SORCERER)],
    known_cantrips=4
)

sorc_lvl3 = ClassLevelSorcerer(
    lvl=3, class_type=ClassType.SORCERER,
    features=[FeatureRegistry.get("Metamagic", FeatureType.CLASS, ClassType.SORCERER)],
    known_cantrips=4
)

sorc_lvl4 = ClassLevelSorcerer(
    lvl=4, class_type=ClassType.SORCERER,
    features=[FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.SORCERER)],
    known_cantrips=5
)

sorc_lvl5 = ClassLevelSorcerer(
    lvl=5, class_type=ClassType.SORCERER,
    known_cantrips=5
)

sorc_lvl6 = ClassLevelSorcerer(
    lvl=6, class_type=ClassType.SORCERER,
    known_cantrips=5
)

sorc_lvl7 = ClassLevelSorcerer(
    lvl=7, class_type=ClassType.SORCERER,
    known_cantrips=5
)

sorc_lvl8 = ClassLevelSorcerer(
    lvl=8, class_type=ClassType.SORCERER,
    features=[FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.SORCERER)],
    known_cantrips=5
)

sorc_lvl9 = ClassLevelSorcerer(
    lvl=9, class_type=ClassType.SORCERER,
    known_cantrips=5
)

sorc_lvl10 = ClassLevelSorcerer(
    lvl=10, class_type=ClassType.SORCERER,
    features=[FeatureRegistry.get("Metamagic", FeatureType.CLASS, ClassType.SORCERER)],
    known_cantrips=6
)

sorc_lvl11 = ClassLevelSorcerer(
    lvl=11, class_type=ClassType.SORCERER,
    known_cantrips=6
)

sorc_lvl12 = ClassLevelSorcerer(
    lvl=12, class_type=ClassType.SORCERER,
    features=[FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.SORCERER)],
    known_cantrips=6
)

sorc_lvl13 = ClassLevelSorcerer(
    lvl=13, class_type=ClassType.SORCERER,
    known_cantrips=6
)

sorc_lvl14 = ClassLevelSorcerer(
    lvl=14, class_type=ClassType.SORCERER,
    known_cantrips=6
)

sorc_lvl15 = ClassLevelSorcerer(
    lvl=15, class_type=ClassType.SORCERER,
    known_cantrips=6
)

sorc_lvl16 = ClassLevelSorcerer(
    lvl=16, class_type=ClassType.SORCERER,
    features=[FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.SORCERER)],
    known_cantrips=6
)

sorc_lvl17 = ClassLevelSorcerer(
    lvl=17, class_type=ClassType.SORCERER,
    features=[FeatureRegistry.get("Metamagic", FeatureType.CLASS, ClassType.SORCERER)],
    known_cantrips=6
)

sorc_lvl18 = ClassLevelSorcerer(
    lvl=18, class_type=ClassType.SORCERER,
    known_cantrips=6
)

sorc_lvl19 = ClassLevelSorcerer(
    lvl=19, class_type=ClassType.SORCERER,
    features=[FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.SORCERER)],
    known_cantrips=6
)

sorc_lvl20 = ClassLevelSorcerer(
    lvl=20, class_type=ClassType.SORCERER,
    features=[FeatureRegistry.get("Sorcerous Restoration", FeatureType.CLASS, ClassType.SORCERER)],
    known_cantrips=6
)


# Load class levels in array
sorcerer_cl = [
    sorc_lvl1, sorc_lvl2, sorc_lvl3, sorc_lvl4, sorc_lvl5,
    sorc_lvl6, sorc_lvl7, sorc_lvl8, sorc_lvl9, sorc_lvl10,
    sorc_lvl11, sorc_lvl12, sorc_lvl13, sorc_lvl14, sorc_lvl15,
    sorc_lvl16, sorc_lvl17, sorc_lvl18, sorc_lvl19, sorc_lvl20,
]