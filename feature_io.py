# feature_io.py
import json
from feature import FeatureType, Feature
from class_feature import ClassFeature, SubclassFeature
from race_feature import RaceFeature


def save_features_to_file(features: list[Feature], path: str = "features.json"):
    """Save a list of Feature objects to a JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump([feat.to_dict() for feat in features], f, indent=2)


def load_features_from_file(path: str = "features.json") -> list[Feature]:
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
