# class_levels/sorcerer_subclass_levels.py
from class_base import ClassType
from subclass_ import SubclassType
from class_level import ClassLevelSorcerer
from feature import FeatureType
from feature_registry import FeatureRegistry
from feature_io import load_features_from_file

# Load features
feats = load_features_from_file()
FeatureRegistry.load_bulk(feats)

sorcerer_scl = [] # Empty array


# === Draconic Bloodline ===
db_lvl1 = ClassLevelSorcerer(
    lvl=1,
    class_type=ClassType.SORCERER,
    subclass=SubclassType.DRACONIC_BLOODLINE,
    features=[
        FeatureRegistry.get("Dragon Ancestor", FeatureType.SUBCLASS, ClassType.SORCERER),
        FeatureRegistry.get("Draconic Resilience", FeatureType.SUBCLASS, ClassType.SORCERER),
    ],
    known_cantrips=4
)

db_lvl6 = ClassLevelSorcerer(
    lvl=6,
    class_type=ClassType.SORCERER,
    subclass=SubclassType.DRACONIC_BLOODLINE,
    features=[FeatureRegistry.get("Elemental Affinity", FeatureType.SUBCLASS, ClassType.SORCERER)],
    known_cantrips=5
)

db_lvl14 = ClassLevelSorcerer(
    lvl=14,
    class_type=ClassType.SORCERER,
    subclass=SubclassType.DRACONIC_BLOODLINE,
    features=[FeatureRegistry.get("Dragon Wings", FeatureType.SUBCLASS, ClassType.SORCERER)],
    known_cantrips=6
)

db_lvl18 = ClassLevelSorcerer(
    lvl=18,
    class_type=ClassType.SORCERER,
    subclass=SubclassType.DRACONIC_BLOODLINE,
    features=[FeatureRegistry.get("Draconic Presence", FeatureType.SUBCLASS, ClassType.SORCERER)],
    known_cantrips=6
)

draconic_bloodline_scl = [db_lvl1, db_lvl6, db_lvl14, db_lvl18]
sorcerer_scl.extend(draconic_bloodline_scl)

# === Divine Soul ===
ds_lvl1 = ClassLevelSorcerer(
    lvl=1,
    class_type=ClassType.SORCERER,
    subclass=SubclassType.DIVINE_SOUL,
    features=[
        FeatureRegistry.get("Divine Magic", FeatureType.SUBCLASS, ClassType.SORCERER),
        FeatureRegistry.get("Favored by the Gods", FeatureType.SUBCLASS, ClassType.SORCERER),
    ],
    known_cantrips=4,
)

ds_lvl6 = ClassLevelSorcerer(
    lvl=6,
    class_type=ClassType.SORCERER,
    subclass=SubclassType.DIVINE_SOUL,
    features=[FeatureRegistry.get("Empowered Healing", FeatureType.SUBCLASS, ClassType.SORCERER)],
    known_cantrips=5
)

ds_lvl14 = ClassLevelSorcerer(
    lvl=14,
    class_type=ClassType.SORCERER,
    subclass=SubclassType.DIVINE_SOUL,
    features=[FeatureRegistry.get("Angelic Form", FeatureType.SUBCLASS, ClassType.SORCERER)],
    known_cantrips=6
)

ds_lvl18 = ClassLevelSorcerer(
    lvl=18,
    class_type=ClassType.SORCERER,
    subclass=SubclassType.DIVINE_SOUL,
    features=[FeatureRegistry.get("Unearthly Recovery", FeatureType.SUBCLASS, ClassType.SORCERER)],
    known_cantrips=6
)

divine_soul_scl = [ds_lvl1, ds_lvl6, ds_lvl14, ds_lvl18]
sorcerer_scl.extend(divine_soul_scl)

