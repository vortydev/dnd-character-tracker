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


# === Circle of Stars ===
stars_lvl2 = ClassLevelSpellcaster(
    lvl=2,
    class_type=ClassType.DRUID,
    subclass=SubclassType.CIRCLE_STARS,
    features=[
        FeatureRegistry.get("Star Map", FeatureType.SUBCLASS, ClassType.DRUID),
        FeatureRegistry.get("Starry Form", FeatureType.SUBCLASS, ClassType.DRUID),
    ],
)

stars_lvl6 = ClassLevelSpellcaster(
    lvl=6,
    class_type=ClassType.DRUID,
    subclass=SubclassType.CIRCLE_STARS,
    features=[
        FeatureRegistry.get("Cosmic Omen", FeatureType.SUBCLASS, ClassType.DRUID),
    ],
)

stars_lvl10 = ClassLevelSpellcaster(
    lvl=10,
    class_type=ClassType.DRUID,
    subclass=SubclassType.CIRCLE_STARS,
    features=[
        FeatureRegistry.get("Twinkling Constellations", FeatureType.SUBCLASS, ClassType.DRUID),
    ],
)

stars_lvl14 = ClassLevelSpellcaster(
    lvl=14,
    class_type=ClassType.DRUID,
    subclass=SubclassType.CIRCLE_STARS,
    features=[
        FeatureRegistry.get("Full of Stars", FeatureType.SUBCLASS, ClassType.DRUID),
    ],
)

circle_stars_scl = [stars_lvl2, stars_lvl6, stars_lvl10, stars_lvl14]
druid_scl.extend(circle_stars_scl)


# === Circle of Dreams ===
dreams_lvl2 = ClassLevelSpellcaster(
    lvl=2,
    class_type=ClassType.DRUID,
    subclass=SubclassType.CIRCLE_DREAMS,
    features=[
        FeatureRegistry.get("Balm of the Summer Court", FeatureType.SUBCLASS, ClassType.DRUID),
    ],
)

dreams_lvl6 = ClassLevelSpellcaster(
    lvl=6,
    class_type=ClassType.DRUID,
    subclass=SubclassType.CIRCLE_DREAMS,
    features=[
        FeatureRegistry.get("Hearth of Moonlight and Shadow", FeatureType.SUBCLASS, ClassType.DRUID),
    ],
)

dreams_lvl10 = ClassLevelSpellcaster(
    lvl=10,
    class_type=ClassType.DRUID,
    subclass=SubclassType.CIRCLE_DREAMS,
    features=[
        FeatureRegistry.get("Hidden Paths", FeatureType.SUBCLASS, ClassType.DRUID),
    ],
)

dreams_lvl14 = ClassLevelSpellcaster(
    lvl=14,
    class_type=ClassType.DRUID,
    subclass=SubclassType.CIRCLE_DREAMS,
    features=[
        FeatureRegistry.get("Walker in Dreams", FeatureType.SUBCLASS, ClassType.DRUID),
    ],
)

circle_dreams_scl = [dreams_lvl2, dreams_lvl6, dreams_lvl10, dreams_lvl14]
druid_scl.extend(circle_dreams_scl)