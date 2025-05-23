# class_levels/wizard_subclass_levels.py
from class_ import ClassType
from subclass_ import SubclassType
from class_level import ClassLevel
from feature import FeatureType
from feature_registry import FeatureRegistry
from feature_io import load_features_from_file

# Load features
feats = load_features_from_file()
FeatureRegistry.load_bulk(feats)

fighter_scl = [] # Empty array


# === Champion ===
champ_lvl3 = ClassLevel(
    lvl=3,
    class_type=ClassType.FIGHTER,
    subclass=SubclassType.CHAMPION,
    features=[ FeatureRegistry.get("Improved Critical", FeatureType.SUBCLASS, ClassType.FIGHTER) ],
)

champ_lvl7 = ClassLevel(
    lvl=7,
    class_type=ClassType.FIGHTER,
    subclass=SubclassType.CHAMPION,
    features=[FeatureRegistry.get("Remarkable Athlete", FeatureType.SUBCLASS, ClassType.FIGHTER)],
)

champ_lvl10 = ClassLevel(
    lvl=10,
    class_type=ClassType.FIGHTER,
    subclass=SubclassType.CHAMPION,
    features=[FeatureRegistry.get("Additional Fighting Style", FeatureType.SUBCLASS, ClassType.FIGHTER)],
)

champ_lvl15 = ClassLevel(
    lvl=15,
    class_type=ClassType.FIGHTER,
    subclass=SubclassType.CHAMPION,
    features=[FeatureRegistry.get("Superior Critical", FeatureType.SUBCLASS, ClassType.FIGHTER)],
)

champ_lvl18 = ClassLevel(
    lvl=18,
    class_type=ClassType.FIGHTER,
    subclass=SubclassType.CHAMPION,
    features=[FeatureRegistry.get("Survivor", FeatureType.SUBCLASS, ClassType.FIGHTER)],
)

champ_scl = [champ_lvl3, champ_lvl7, champ_lvl10, champ_lvl15, champ_lvl18]
fighter_scl.extend(champ_scl)
