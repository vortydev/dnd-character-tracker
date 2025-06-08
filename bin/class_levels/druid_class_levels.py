# class_levels/druid_class_levels.py
from class_base import ClassType
from class_level import ClassLevelSpellcaster
from feature import FeatureType
from feature_registry import FeatureRegistry
from feature_io import load_features_from_file

# Load features
feats = load_features_from_file()
FeatureRegistry.load_bulk(feats)

druid_cl = [] # Empty array

druid_lvl1 = ClassLevelSpellcaster(
    lvl=1, class_type=ClassType.DRUID,
    features=[
        FeatureRegistry.get("Druidic", FeatureType.CLASS, ClassType.DRUID),
        FeatureRegistry.get("Spellcasting", FeatureType.CLASS, ClassType.DRUID),
    ],
    known_cantrips=2
)

druid_lvl2 = ClassLevelSpellcaster(
    lvl=2, class_type=ClassType.DRUID,
    features=[
        FeatureRegistry.get("Wild Shape", FeatureType.CLASS, ClassType.DRUID),
        FeatureRegistry.get("Druid Circle", FeatureType.CLASS, ClassType.DRUID),
        FeatureRegistry.get("Wild Companion (Optional)", FeatureType.CLASS, ClassType.DRUID),
    ],
    known_cantrips=2
)

druid_lvl3 = ClassLevelSpellcaster(
    lvl=3, class_type=ClassType.DRUID,
    known_cantrips=2
)

druid_lvl4 = ClassLevelSpellcaster(
    lvl=4, class_type=ClassType.DRUID,
    features=[
        # FeatureRegistry.get("Wild Shape Improvement", FeatureType.CLASS, ClassType.DRUID),
        FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.DRUID),
        FeatureRegistry.get("Cantrip Versatility (Optional)", FeatureType.CLASS, ClassType.DRUID),
    ],
    known_cantrips=3
)

druid_lvl5 = ClassLevelSpellcaster(
    lvl=5, class_type=ClassType.DRUID,
    known_cantrips=3
)

druid_lvl6 = ClassLevelSpellcaster(
    lvl=6, class_type=ClassType.DRUID,
    known_cantrips=3
)

druid_lvl7 = ClassLevelSpellcaster(
    lvl=7, class_type=ClassType.DRUID,
    known_cantrips=3
)

druid_lvl8 = ClassLevelSpellcaster(
    lvl=8, class_type=ClassType.DRUID,
    features=[
        # FeatureRegistry.get("Wild Shape Improvement", FeatureType.CLASS, ClassType.DRUID),
        FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.DRUID),
        FeatureRegistry.get("Cantrip Versatility (Optional)", FeatureType.CLASS, ClassType.DRUID),
    ],
    known_cantrips=3
)

druid_lvl9 = ClassLevelSpellcaster(
    lvl=9, class_type=ClassType.DRUID,
    known_cantrips=3
)

druid_lvl10 = ClassLevelSpellcaster(
    lvl=10, class_type=ClassType.DRUID,
    known_cantrips=4
)

druid_lvl11 = ClassLevelSpellcaster(
    lvl=11, class_type=ClassType.DRUID,
    known_cantrips=4
)

druid_lvl12 = ClassLevelSpellcaster(
    lvl=12, class_type=ClassType.DRUID,
    features=[
        FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.DRUID),
        FeatureRegistry.get("Cantrip Versatility (Optional)", FeatureType.CLASS, ClassType.DRUID),
    ],
    known_cantrips=4
)

druid_lvl13 = ClassLevelSpellcaster(
    lvl=13, class_type=ClassType.DRUID,
    known_cantrips=4
)

druid_lvl14 = ClassLevelSpellcaster(
    lvl=14, class_type=ClassType.DRUID,
    known_cantrips=4
)

druid_lvl15 = ClassLevelSpellcaster(
    lvl=15, class_type=ClassType.DRUID,
    known_cantrips=4
)

druid_lvl16 = ClassLevelSpellcaster(
    lvl=16, class_type=ClassType.DRUID,
    features=[
        FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.DRUID),
        FeatureRegistry.get("Cantrip Versatility (Optional)", FeatureType.CLASS, ClassType.DRUID),
    ],
    known_cantrips=4
)

druid_lvl17 = ClassLevelSpellcaster(
    lvl=17, class_type=ClassType.DRUID,
    known_cantrips=4
)

druid_lvl18 = ClassLevelSpellcaster(
    lvl=18, class_type=ClassType.DRUID,
    features=[
        FeatureRegistry.get("Timeless Body", FeatureType.CLASS, ClassType.DRUID),
        FeatureRegistry.get("Beast Spells", FeatureType.CLASS, ClassType.DRUID),
    ],
    known_cantrips=4
)

druid_lvl19 = ClassLevelSpellcaster(
    lvl=19, class_type=ClassType.DRUID,
    features=[
        FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.DRUID),
        FeatureRegistry.get("Cantrip Versatility (Optional)", FeatureType.CLASS, ClassType.DRUID),
    ],
    known_cantrips=4
)

druid_lvl20 = ClassLevelSpellcaster(
    lvl=20, class_type=ClassType.DRUID,
    features=[FeatureRegistry.get("Archdruid", FeatureType.CLASS, ClassType.DRUID)],
    known_cantrips=4
)


# Load class levels in array
druid_cl = [
    druid_lvl1, druid_lvl2, druid_lvl3, druid_lvl4, druid_lvl5,
    druid_lvl6, druid_lvl7, druid_lvl8, druid_lvl9, druid_lvl10,
    druid_lvl11, druid_lvl12, druid_lvl13, druid_lvl14, druid_lvl15,
    druid_lvl16, druid_lvl17, druid_lvl18, druid_lvl19, druid_lvl20,
]