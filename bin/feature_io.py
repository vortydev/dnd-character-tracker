# feature_io.py
import os
import json

from feature import FeatureType, Feature
from class_feature import ClassFeature, SubclassFeature
from race_feature import RaceFeature

# Resolve the /data directory relative to this file
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
DEFAULT_PATH = os.path.join(DATA_DIR, "features.json")


def save_features_to_file(features: list[Feature], path: str = DEFAULT_PATH):
    """Save a list of Feature objects to a JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump([feat.to_dict() for feat in features], f, indent=2)


def load_features_from_file(path: str = DEFAULT_PATH) -> list[Feature]:
    """Load a list of Feature objects from a JSON file."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
            features = []
            for d in raw_data:
                f_type = d["type"]
                if f_type == FeatureType.CLASS.value:
                    features.append(ClassFeature.from_dict(d))
                elif f_type == FeatureType.SUBCLASS.value:
                    features.append(SubclassFeature.from_dict(d))
                elif f_type == FeatureType.RACE.value:
                    features.append(RaceFeature.from_dict(d))
                else:
                    features.append(Feature.from_dict(d))
            return features
    except FileNotFoundError:
        return []
