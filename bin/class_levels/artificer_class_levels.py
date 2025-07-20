# class_levels/artificer_class_levels.py
from class_base import ClassType
from class_level import ClassLevelArtificer
from feature import FeatureType
from feature_registry import FeatureRegistry
from feature_io import load_features_from_file

# Load features
feats = load_features_from_file()
FeatureRegistry.load_bulk(feats)

artificer_cl = [] # Empty array

artificer_lvl1 = ClassLevelArtificer(
    lvl=1, class_type=ClassType.ARTIFICER,
    features=[
        FeatureRegistry.get("Magical Tinkering", FeatureType.CLASS, ClassType.ARTIFICER),
        FeatureRegistry.get("Spellcasting", FeatureType.CLASS, ClassType.ARTIFICER),
    ],
    known_cantrips=2,
)

artificer_lvl2 = ClassLevelArtificer(
    lvl=2, class_type=ClassType.ARTIFICER,
    features=[
        FeatureRegistry.get("Infuse Item", FeatureType.CLASS, ClassType.ARTIFICER),
    ],
    known_cantrips=2,
    infusions_known=4, infused_items=2,
)

artificer_lvl3 = ClassLevelArtificer(
    lvl=3, class_type=ClassType.ARTIFICER,
    features=[
        FeatureRegistry.get("Artificer Specialist", FeatureType.CLASS, ClassType.ARTIFICER),
        FeatureRegistry.get("The Right Tool for the Job", FeatureType.CLASS, ClassType.ARTIFICER),
    ],
    known_cantrips=2,
    infusions_known=4, infused_items=2,
)

artificer_lvl4 = ClassLevelArtificer(
    lvl=4, class_type=ClassType.ARTIFICER,
    features=[
        FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.ARTIFICER),
    ],
    known_cantrips=2,
    infusions_known=4, infused_items=2,
)

artificer_lvl5 = ClassLevelArtificer(
    lvl=5, class_type=ClassType.ARTIFICER,
    known_cantrips=2,
    infusions_known=4, infused_items=2,
)

artificer_lvl6 = ClassLevelArtificer(
    lvl=6, class_type=ClassType.ARTIFICER,
    features=[
        FeatureRegistry.get("Tool Expertise", FeatureType.CLASS, ClassType.ARTIFICER),
    ],
    known_cantrips=2,
    infusions_known=6, infused_items=3,
)

artificer_lvl7 = ClassLevelArtificer(
    lvl=7, class_type=ClassType.ARTIFICER,
    features=[
        FeatureRegistry.get("Flash of Genius", FeatureType.CLASS, ClassType.ARTIFICER),
    ],
    known_cantrips=2,
    infusions_known=6, infused_items=3,
)

artificer_lvl8 = ClassLevelArtificer(
    lvl=8, class_type=ClassType.ARTIFICER,
    features=[
        FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.ARTIFICER),
    ],
    known_cantrips=2,
    infusions_known=6, infused_items=3,
)

artificer_lvl9 = ClassLevelArtificer(
    lvl=9, class_type=ClassType.ARTIFICER,
    known_cantrips=2,
    infusions_known=6, infused_items=3,
)

artificer_lvl10 = ClassLevelArtificer(
    lvl=10, class_type=ClassType.ARTIFICER,
    features=[
        FeatureRegistry.get("Magic Item Adept", FeatureType.CLASS, ClassType.ARTIFICER),
    ],
    known_cantrips=3,
    infusions_known=8, infused_items=4,
)

artificer_lvl11 = ClassLevelArtificer(
    lvl=11, class_type=ClassType.ARTIFICER,
    features=[
        FeatureRegistry.get("Spell-Storing Item", FeatureType.CLASS, ClassType.ARTIFICER),
    ],
    known_cantrips=3,
    infusions_known=8, infused_items=4,
)

artificer_lvl12 = ClassLevelArtificer(
    lvl=12, class_type=ClassType.ARTIFICER,
    features=[
        FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.ARTIFICER),
    ],
    known_cantrips=3,
    infusions_known=8, infused_items=4,
)

artificer_lvl13 = ClassLevelArtificer(
    lvl=13, class_type=ClassType.ARTIFICER,
    known_cantrips=3,
    infusions_known=8, infused_items=4,
)

artificer_lvl14 = ClassLevelArtificer(
    lvl=14, class_type=ClassType.ARTIFICER,
    features=[
        FeatureRegistry.get("Magic Item Savant", FeatureType.CLASS, ClassType.ARTIFICER),
    ],
    known_cantrips=4,
    infusions_known=10, infused_items=5,
)

artificer_lvl15 = ClassLevelArtificer(
    lvl=15, class_type=ClassType.ARTIFICER,
    known_cantrips=4,
    infusions_known=10, infused_items=5,
)

artificer_lvl16 = ClassLevelArtificer(
    lvl=16, class_type=ClassType.ARTIFICER,
    features=[
        FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.ARTIFICER),
    ],
    known_cantrips=4,
    infusions_known=10, infused_items=5,
)

artificer_lvl17 = ClassLevelArtificer(
    lvl=17, class_type=ClassType.ARTIFICER,
    known_cantrips=4,
    infusions_known=10, infused_items=5,
)

artificer_lvl18 = ClassLevelArtificer(
    lvl=18, class_type=ClassType.ARTIFICER,
    features=[
        FeatureRegistry.get("Magic Item Master", FeatureType.CLASS, ClassType.ARTIFICER),
    ],
    known_cantrips=4,
    infusions_known=12, infused_items=6,
)

artificer_lvl19 = ClassLevelArtificer(
    lvl=19, class_type=ClassType.ARTIFICER,
    features=[
        FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.ARTIFICER),
    ],
    known_cantrips=4,
    infusions_known=12, infused_items=6,
)

artificer_lvl20 = ClassLevelArtificer(
    lvl=20, class_type=ClassType.ARTIFICER,
    features=[
        FeatureRegistry.get("Soul of Artifice", FeatureType.CLASS, ClassType.ARTIFICER)
    ],
    known_cantrips=4,
    infusions_known=12, infused_items=6,
)


# Load class levels in array
artificer_cl = [
    artificer_lvl1, artificer_lvl2, artificer_lvl3, artificer_lvl4, artificer_lvl5,
    artificer_lvl6, artificer_lvl7, artificer_lvl8, artificer_lvl9, artificer_lvl10,
    artificer_lvl11, artificer_lvl12, artificer_lvl13, artificer_lvl14, artificer_lvl15,
    artificer_lvl16, artificer_lvl17, artificer_lvl18, artificer_lvl19, artificer_lvl20,
]