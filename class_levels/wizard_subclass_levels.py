# class_levels/wizard_subclass_levels.py
from class_ import ClassType
from subclass_ import SubclassType
from class_level import ClassLevelSpellcaster
from feature import FeatureType
from feature_registry import FeatureRegistry
from feature_io import load_features_from_file

# Load features
feats = load_features_from_file("features.json")
FeatureRegistry.load_bulk(feats)

wizard_scl = [] # Empty array


# === School of Evocation ===
evocation_lvl2 = ClassLevelSpellcaster(
    lvl=2,
    class_type=ClassType.WIZARD,
    subclass=SubclassType.EVOCATION,
    features=[
        FeatureRegistry.get("Evocation Savant", FeatureType.SUBCLASS, ClassType.WIZARD),
        FeatureRegistry.get("Sculpt Spells", FeatureType.SUBCLASS, ClassType.WIZARD),
    ],
    known_cantrips=3
)

evocation_lvl6 = ClassLevelSpellcaster(
    lvl=6,
    class_type=ClassType.WIZARD,
    subclass=SubclassType.EVOCATION,
    features=[FeatureRegistry.get("Potent Cantrip", FeatureType.SUBCLASS, ClassType.WIZARD)],
    known_cantrips=4
)

evocation_lvl10 = ClassLevelSpellcaster(
    lvl=10,
    class_type=ClassType.WIZARD,
    subclass=SubclassType.EVOCATION,
    features=[FeatureRegistry.get("Empowered Evocation", FeatureType.SUBCLASS, ClassType.WIZARD)],
    known_cantrips=5
)

evocation_lvl14 = ClassLevelSpellcaster(
    lvl=14,
    class_type=ClassType.WIZARD,
    subclass=SubclassType.EVOCATION,
    features=[FeatureRegistry.get("Overchannel", FeatureType.SUBCLASS, ClassType.WIZARD)],
    known_cantrips=5
)

evocation_scl = [evocation_lvl2, evocation_lvl6, evocation_lvl10, evocation_lvl14]
wizard_scl.extend(evocation_scl)
