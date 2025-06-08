# build_features.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from feature import Feature
from class_feature import ClassFeature, SubclassFeature
from race_feature import RaceFeature
from feature_registry import FeatureRegistry
from feature_io import save_features_to_file


def load_feature_list() -> list[Feature]:
    """Load array of defined Feature objects."""
    feats = []

    # Features

    # Class Features
    class_feats = load_class_features()
    feats.extend(class_feats)

    # Subclass features
    sublass_feats = load_subclass_features()
    feats.extend(sublass_feats)

    # Race features
    race_feats = load_race_features()
    feats.extend(race_feats)

    return feats


def load_class_features() -> list[ClassFeature]:
    """Load an array of class features for each class."""
    class_feats: list[ClassFeature] = []
    print("\n===== Class Features =====")

    # === Druid ===
    print("> Creating Druid Class features")
    from feature_list.class_features.druid_features import druid_feats
    class_feats.extend(druid_feats)

    # === Fighter ===
    print("> Creating Fighter Class features")
    from feature_list.class_features.fighter_features import fig_feats
    class_feats.extend(fig_feats)

    # === Sorcerer ===
    print("> Creating Sorcerer Class features")
    from feature_list.class_features.sorcerer_features import sorc_feats
    class_feats.extend(sorc_feats)

    # === Wizard ===
    print("> Creating Wizard Class features")
    from feature_list.class_features.wizard_features import wiz_feats
    class_feats.extend(wiz_feats)

    print(f"📦 Loaded {len(class_feats)} Class features.")
    return class_feats


def load_subclass_features() -> list[SubclassFeature]:
    """Load an array of subclass features for each class."""
    subclass_feats: list[SubclassFeature] = []
    print("\n===== Subclass Features =====")

    # === Fighter ===
    print("> Creating Fighter Subclass features")
    from feature_list.subclass_features.fighter_martial_archetype_features import ma_champion
    subclass_feats.extend(ma_champion)

    # === Sorcerer ===
    print("> Creating Sorcerer Subclass features")
    from feature_list.subclass_features.sorcerer_origin_features import draconic_bloodline
    subclass_feats.extend(draconic_bloodline)

    # === Wizard ===
    print("> Creating Wizard Subclass features")
    from feature_list.subclass_features.wizard_school_features import school_evocation
    subclass_feats.extend(school_evocation)

    print(f"📦 Loaded {len(subclass_feats)} Subclass features.")
    return subclass_feats


def load_race_features() -> list[RaceFeature]:
    """Load an array of race features for each race."""
    race_feats: list[RaceFeature] = []
    print("\n===== Race Features =====")

    # Elf
    print("> Creating Elf features")
    from feature_list.race_features.elf_features import elf_feats
    race_feats.extend(elf_feats)

    # Human
    print("> Creating Human features")
    from feature_list.race_features.human_features import human_variant_feats
    race_feats.extend(human_variant_feats)

    # Tiefling
    print("> Creating Tiefling features")
    from feature_list.race_features.tiefling_features import tiefling_feats
    race_feats.extend(tiefling_feats)

    # Yuan-Ti
    print("> Creating Yuan-Ti features")
    from feature_list.race_features.yuanti_features import yuanti_feats
    race_feats.extend(yuanti_feats)

    print(f"📦 Loaded {len(race_feats)} Race features.")
    return race_feats


def save_feature_list(feats: list[Feature]):
    """Register Feature objects and save them to a JSON file."""
    FeatureRegistry.load_bulk(feats)
    save_features_to_file(feats)
    print(f"✅ {len(feats)} features saved to 'features.json'")


def build_feature_list():
    """Load the defined Feature objects into a JSON file to load the FeatureRegistry."""
    feats = load_feature_list()
    save_feature_list(feats)


# === Run the main function ===
build_feature_list()
