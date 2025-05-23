# class_levels/fighter_class_levels.py
from class_ import ClassType
from class_level import ClassLevel
from feature import FeatureType
from feature_registry import FeatureRegistry
from feature_io import load_features_from_file

# Load features
feats = load_features_from_file()
FeatureRegistry.load_bulk(feats)

fighter_cl = [] # Empty array

fig_lvl1 = ClassLevel(
    lvl=1, class_type=ClassType.FIGHTER,
    features=[
        FeatureRegistry.get("Fighting Style", FeatureType.CLASS, ClassType.FIGHTER),
        FeatureRegistry.get("Second Wind", FeatureType.CLASS, ClassType.FIGHTER)
    ],
)

fig_lvl2 = ClassLevel(
    lvl=2, class_type=ClassType.FIGHTER,
    features=[FeatureRegistry.get("Action Surge", FeatureType.CLASS, ClassType.FIGHTER)],
)

fig_lvl3 = ClassLevel(
    lvl=3, class_type=ClassType.FIGHTER,
    features=[FeatureRegistry.get("Martial Archetype", FeatureType.CLASS, ClassType.FIGHTER)],
)

fig_lvl4 = ClassLevel(
    lvl=4, class_type=ClassType.FIGHTER,
    features=[FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.FIGHTER)],
)

fig_lvl5 = ClassLevel(
    lvl=5, class_type=ClassType.FIGHTER,
    features=[FeatureRegistry.get("Extra Attack", FeatureType.CLASS, ClassType.FIGHTER)],
)

fig_lvl6 = ClassLevel(
    lvl=6, class_type=ClassType.FIGHTER,
    features=[FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.FIGHTER)],
)

fig_lvl7 = ClassLevel(
    lvl=7, class_type=ClassType.FIGHTER,
)

fig_lvl8 = ClassLevel(
    lvl=8, class_type=ClassType.FIGHTER,
    features=[FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.FIGHTER)],
)

fig_lvl9 = ClassLevel(
    lvl=9, class_type=ClassType.FIGHTER,
    features=[FeatureRegistry.get("Indomitable", FeatureType.CLASS, ClassType.FIGHTER)],
)

fig_lvl10 = ClassLevel(
    lvl=10, class_type=ClassType.FIGHTER,
)

fig_lvl11 = ClassLevel(
    lvl=11, class_type=ClassType.FIGHTER,
    features=[FeatureRegistry.get("Extra Attack", FeatureType.CLASS, ClassType.FIGHTER)],
)

fig_lvl12 = ClassLevel(
    lvl=12, class_type=ClassType.FIGHTER,
    features=[FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.FIGHTER)],
)

fig_lvl13 = ClassLevel(
    lvl=13, class_type=ClassType.FIGHTER,
    features=[FeatureRegistry.get("Indomitable", FeatureType.CLASS, ClassType.FIGHTER)],
)

fig_lvl14 = ClassLevel(
    lvl=14, class_type=ClassType.FIGHTER,
    features=[FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.FIGHTER)],
)

fig_lvl15 = ClassLevel(
    lvl=15, class_type=ClassType.FIGHTER,
)

fig_lvl16 = ClassLevel(
    lvl=16, class_type=ClassType.FIGHTER,
    features=[FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.FIGHTER)],
)

fig_lvl17 = ClassLevel(
    lvl=17, class_type=ClassType.FIGHTER,
    features=[
        FeatureRegistry.get("Action Surge", FeatureType.CLASS, ClassType.FIGHTER),
        FeatureRegistry.get("Indomitable", FeatureType.CLASS, ClassType.FIGHTER)
    ],
)

fig_lvl18 = ClassLevel(
    lvl=18, class_type=ClassType.FIGHTER,
)

fig_lvl19 = ClassLevel(
    lvl=19, class_type=ClassType.FIGHTER,
    features=[FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.FIGHTER)],
)

fig_lvl20 = ClassLevel(
    lvl=20, class_type=ClassType.FIGHTER,
    features=[FeatureRegistry.get("Extra Attack", FeatureType.CLASS, ClassType.FIGHTER)],
)


# Load class levels in array
fighter_cl = [
    fig_lvl1, fig_lvl2, fig_lvl3, fig_lvl4, fig_lvl5,
    fig_lvl6, fig_lvl7, fig_lvl8, fig_lvl9, fig_lvl10,
    fig_lvl11, fig_lvl12, fig_lvl13, fig_lvl14, fig_lvl15,
    fig_lvl16, fig_lvl17, fig_lvl18, fig_lvl19, fig_lvl20,
]