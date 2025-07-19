# class_levels/ranger_class_levels.py
from class_base import ClassType
from class_level import ClassLevelSpellcaster
from feature import FeatureType
from feature_registry import FeatureRegistry
from feature_io import load_features_from_file

# Load features
feats = load_features_from_file()
FeatureRegistry.load_bulk(feats)

ranger_cl = [] # Empty array

ranger_lvl1 = ClassLevelSpellcaster(
    lvl=1, class_type=ClassType.RANGER,
    features=[
        FeatureRegistry.get("Favored Enemy", FeatureType.CLASS, ClassType.RANGER),
        FeatureRegistry.get("Favored Foe", FeatureType.CLASS, ClassType.RANGER),
        FeatureRegistry.get("Natural Explorer", FeatureType.CLASS, ClassType.RANGER),
        FeatureRegistry.get("Natural Explorer (Revised)", FeatureType.CLASS, ClassType.RANGER),
        FeatureRegistry.get("Deft Explorer (Optional)", FeatureType.CLASS, ClassType.RANGER),
    ],
)

ranger_lvl2 = ClassLevelSpellcaster(
    lvl=2, class_type=ClassType.RANGER,
    features=[
        FeatureRegistry.get("Fighting Style", FeatureType.CLASS, ClassType.RANGER),
        FeatureRegistry.get("Spellcasting", FeatureType.CLASS, ClassType.RANGER),
    ],
    known_spells=2,
)

ranger_lvl3 = ClassLevelSpellcaster(
    lvl=3, class_type=ClassType.RANGER,
    features=[
        FeatureRegistry.get("Ranger Conclave", FeatureType.CLASS, ClassType.RANGER),
        FeatureRegistry.get("Primeval Awareness", FeatureType.CLASS, ClassType.RANGER),
        FeatureRegistry.get("Primeval Awareness (Optional)", FeatureType.CLASS, ClassType.RANGER),
        FeatureRegistry.get("Primeval Awareness (Revised)", FeatureType.CLASS, ClassType.RANGER),
    ],
    known_spells=3,
)

ranger_lvl4 = ClassLevelSpellcaster(
    lvl=4, class_type=ClassType.RANGER,
    features=[
        FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.RANGER),
    ],
    known_spells=3,
)

ranger_lvl5 = ClassLevelSpellcaster(
    lvl=5, class_type=ClassType.RANGER,
    features=[
        FeatureRegistry.get("Extra Attack", FeatureType.CLASS, ClassType.RANGER),
    ],
    known_spells=4,
)

ranger_lvl6 = ClassLevelSpellcaster(
    lvl=6, class_type=ClassType.RANGER,
    known_spells=4,
)

ranger_lvl7 = ClassLevelSpellcaster(
    lvl=7, class_type=ClassType.RANGER,
    known_spells=5,
)

ranger_lvl8 = ClassLevelSpellcaster(
    lvl=8, class_type=ClassType.RANGER,
    features=[
        FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.RANGER),
        FeatureRegistry.get("Land's Stride", FeatureType.CLASS, ClassType.RANGER),
    ],
    known_spells=5,
)

ranger_lvl9 = ClassLevelSpellcaster(
    lvl=9, class_type=ClassType.RANGER,
    known_spells=6,
)

ranger_lvl10 = ClassLevelSpellcaster(
    lvl=10, class_type=ClassType.RANGER,
    features=[
        FeatureRegistry.get("Hide in Plain Sight", FeatureType.CLASS, ClassType.RANGER),
    ],
    known_spells=6,
)

ranger_lvl11 = ClassLevelSpellcaster(
    lvl=11, class_type=ClassType.RANGER,
    known_spells=7,
)

ranger_lvl12 = ClassLevelSpellcaster(
    lvl=12, class_type=ClassType.RANGER,
    features=[
        FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.RANGER),
    ],
    known_spells=7,
)

ranger_lvl13 = ClassLevelSpellcaster(
    lvl=13, class_type=ClassType.RANGER,
    known_spells=8,
)

ranger_lvl14 = ClassLevelSpellcaster(
    lvl=14, class_type=ClassType.RANGER,
    features=[
        FeatureRegistry.get("Vanish", FeatureType.CLASS, ClassType.RANGER),
    ],
    known_spells=8,
)

ranger_lvl15 = ClassLevelSpellcaster(
    lvl=15, class_type=ClassType.RANGER,
    known_spells=9,
)

ranger_lvl16 = ClassLevelSpellcaster(
    lvl=16, class_type=ClassType.RANGER,
    features=[
        FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.RANGER),
    ],
    known_spells=9,
)

ranger_lvl17 = ClassLevelSpellcaster(
    lvl=17, class_type=ClassType.RANGER,
    known_spells=10,
)

ranger_lvl18 = ClassLevelSpellcaster(
    lvl=18, class_type=ClassType.RANGER,
    features=[
        FeatureRegistry.get("Feral Senses", FeatureType.CLASS, ClassType.RANGER),
    ],
    known_spells=10,
)

ranger_lvl19 = ClassLevelSpellcaster(
    lvl=19, class_type=ClassType.RANGER,
    features=[
        FeatureRegistry.get("Ability Score Improvement", FeatureType.CLASS, ClassType.RANGER),
    ],
    known_spells=11,
)

ranger_lvl20 = ClassLevelSpellcaster(
    lvl=20, class_type=ClassType.RANGER,
    features=[
        FeatureRegistry.get("Foe Slayer", FeatureType.CLASS, ClassType.RANGER)
    ],
    known_spells=11,
)


# Load class levels in array
ranger_cl = [
    ranger_lvl1, ranger_lvl2, ranger_lvl3, ranger_lvl4, ranger_lvl5,
    ranger_lvl6, ranger_lvl7, ranger_lvl8, ranger_lvl9, ranger_lvl10,
    ranger_lvl11, ranger_lvl12, ranger_lvl13, ranger_lvl14, ranger_lvl15,
    ranger_lvl16, ranger_lvl17, ranger_lvl18, ranger_lvl19, ranger_lvl20,
]