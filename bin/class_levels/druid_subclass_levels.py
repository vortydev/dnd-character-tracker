# class_levels/druid_subclass_levels.py
from class_base import ClassType
from subclass_ import SubclassType
from class_level import ClassLevelSpellcaster
from feature import FeatureType
from feature_registry import FeatureRegistry
from feature_io import load_features_from_file

# Load features
feats = load_features_from_file()
FeatureRegistry.load_bulk(feats)

druid_scl = [] # Empty array


# === Circle of the Land ===
land_lvl2 = ClassLevelSpellcaster(
    lvl=2,
    class_type=ClassType.DRUID,
    subclass=SubclassType.CIRCLE_LAND,
    features=[
        FeatureRegistry.get("Bonus Cantrip", FeatureType.SUBCLASS, ClassType.DRUID),
        FeatureRegistry.get("Natural Recovery", FeatureType.SUBCLASS, ClassType.DRUID),
    ],
)

land_lvl3 = ClassLevelSpellcaster(
    lvl=3,
    class_type=ClassType.DRUID,
    subclass=SubclassType.CIRCLE_LAND,
    features=[FeatureRegistry.get("Circle Spells", FeatureType.SUBCLASS, ClassType.DRUID)],
)

land_lvl6 = ClassLevelSpellcaster(
    lvl=6,
    class_type=ClassType.DRUID,
    subclass=SubclassType.CIRCLE_LAND,
    features=[FeatureRegistry.get("Land's Stride", FeatureType.SUBCLASS, ClassType.DRUID)],
)

land_lvl10 = ClassLevelSpellcaster(
    lvl=10,
    class_type=ClassType.DRUID,
    subclass=SubclassType.CIRCLE_LAND,
    features=[FeatureRegistry.get("Nature's Ward", FeatureType.SUBCLASS, ClassType.DRUID)],
)

land_lvl14 = ClassLevelSpellcaster(
    lvl=14,
    class_type=ClassType.DRUID,
    subclass=SubclassType.CIRCLE_LAND,
    features=[FeatureRegistry.get("Nature's Sanctuary", FeatureType.SUBCLASS, ClassType.DRUID)],
)

circle_land_scl = [land_lvl2, land_lvl3, land_lvl6, land_lvl10, land_lvl14]
druid_scl.extend(circle_land_scl)
