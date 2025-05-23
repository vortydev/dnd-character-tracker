# class_levels/wizard_class_levels.py
from class_ import ClassType
from class_level import ClassLevelSpellcaster
from feature import FeatureType
from feature_registry import FeatureRegistry
from feature_io import load_features_from_file

# Load features
feats = load_features_from_file()
FeatureRegistry.load_bulk(feats)

wizard_cl = [] # Empty array

wiz_lvl1 = ClassLevelSpellcaster(
    lvl=1, class_type=ClassType.WIZARD,
    features=[
        FeatureRegistry.get("Spellcasting", FeatureType.CLASS, ClassType.WIZARD),
        FeatureRegistry.get("Your Spellbook", FeatureType.CLASS, ClassType.WIZARD),
        FeatureRegistry.get("Arcane Recovery", FeatureType.CLASS, ClassType.WIZARD)
    ],
    known_cantrips=3
)

wiz_lvl2 = ClassLevelSpellcaster(
    lvl=2, class_type=ClassType.WIZARD,
    features=[FeatureRegistry.get("Arcane Tradition", FeatureType.CLASS, ClassType.WIZARD)],
    known_cantrips=3
)

wiz_lvl3 = ClassLevelSpellcaster(
    lvl=3, class_type=ClassType.WIZARD,
    known_cantrips=3
)

wiz_lvl4 = ClassLevelSpellcaster(
    lvl=4, class_type=ClassType.WIZARD,
    features=[FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.WIZARD)],
    known_cantrips=4
)

wiz_lvl5 = ClassLevelSpellcaster(
    lvl=5, class_type=ClassType.WIZARD,
    known_cantrips=4
)

wiz_lvl6 = ClassLevelSpellcaster(
    lvl=6, class_type=ClassType.WIZARD,
    known_cantrips=4
)

wiz_lvl7 = ClassLevelSpellcaster(
    lvl=7, class_type=ClassType.WIZARD,
    known_cantrips=4
)

wiz_lvl8 = ClassLevelSpellcaster(
    lvl=8, class_type=ClassType.WIZARD,
    features=[FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.WIZARD)],
    known_cantrips=4
)

wiz_lvl9 = ClassLevelSpellcaster(
    lvl=9, class_type=ClassType.WIZARD,
    known_cantrips=4
)

wiz_lvl10 = ClassLevelSpellcaster(
    lvl=10, class_type=ClassType.WIZARD,
    known_cantrips=5
)

wiz_lvl11 = ClassLevelSpellcaster(
    lvl=11, class_type=ClassType.WIZARD,
    known_cantrips=5
)

wiz_lvl12 = ClassLevelSpellcaster(
    lvl=12, class_type=ClassType.WIZARD,
    features=[FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.WIZARD)],
    known_cantrips=5
)

wiz_lvl13 = ClassLevelSpellcaster(
    lvl=13, class_type=ClassType.WIZARD,
    known_cantrips=5
)

wiz_lvl14 = ClassLevelSpellcaster(
    lvl=14, class_type=ClassType.WIZARD,
    known_cantrips=5
)

wiz_lvl15 = ClassLevelSpellcaster(
    lvl=15, class_type=ClassType.WIZARD,
    known_cantrips=5
)

wiz_lvl16 = ClassLevelSpellcaster(
    lvl=16, class_type=ClassType.WIZARD,
    features=[FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.WIZARD)],
    known_cantrips=5
)

wiz_lvl17 = ClassLevelSpellcaster(
    lvl=17, class_type=ClassType.WIZARD,
    known_cantrips=5
)

wiz_lvl18 = ClassLevelSpellcaster(
    lvl=18, class_type=ClassType.WIZARD,
    features=[FeatureRegistry.get("Spell Mastery", FeatureType.CLASS, ClassType.WIZARD)],
    known_cantrips=5
)

wiz_lvl19 = ClassLevelSpellcaster(
    lvl=19, class_type=ClassType.WIZARD,
    features=[FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.WIZARD)],
    known_cantrips=5
)

wiz_lvl20 = ClassLevelSpellcaster(
    lvl=20, class_type=ClassType.WIZARD,
    features=[FeatureRegistry.get("Signature Spells", FeatureType.CLASS, ClassType.WIZARD)],
    known_cantrips=5
)


# Load class levels in array
wizard_cl = [
    wiz_lvl1, wiz_lvl2, wiz_lvl3, wiz_lvl4, wiz_lvl5,
    wiz_lvl6, wiz_lvl7, wiz_lvl8, wiz_lvl9, wiz_lvl10,
    wiz_lvl11, wiz_lvl12, wiz_lvl13, wiz_lvl14, wiz_lvl15,
    wiz_lvl16, wiz_lvl17, wiz_lvl18, wiz_lvl19, wiz_lvl20,
]