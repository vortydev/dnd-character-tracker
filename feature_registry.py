# feature_registry.py
from typing import Dict, Optional, Tuple, Union
from feature import Feature
from feature_types import FeatureType
from race_feature import RaceFeature
from race_types import RaceType
from class_feature import ClassFeature
from class_ import ClassType

class FeatureRegistry:
    _feats: Dict[Tuple[str, str, Optional[Union[RaceType, ClassType]]], Feature] = {}

    @classmethod
    def register(cls, feat: Feature):
        feat_type = feat.to_dict()["type"]
        context: Optional[Union[RaceType, ClassType]] = None

        if feat_type == FeatureType.RACE.value and isinstance(feat, RaceFeature):
            context = feat.race_type
        elif feat_type == FeatureType.CLASS.value and isinstance(feat, ClassFeature):
            context = feat.class_type

        key = (feat.name.lower(), feat_type, context)
        cls._feats[key] = feat

    @classmethod
    def get(cls, name: str, feat_type: FeatureType = FeatureType.BASE, context: Optional[Union[RaceType, ClassType]] = None) -> Feature:
        key = (name.lower(), feat_type.value, context)
        if key in cls._feats:
            return cls._feats[key]
        
        fallback_key = (name.lower(), feat_type.value, None)
        if fallback_key in cls._feats:
            return cls._feats[fallback_key]
        
        raise KeyError(f"Feature '{name}' (type={feat_type}) not found with context {context}")

    @classmethod
    def all(cls) -> Dict[Tuple[str, str, Optional[Union[RaceType, ClassType]]], Feature]:
        return cls._feats

    @classmethod
    def clear(cls):
        cls._feats.clear()

    @classmethod
    def load_bulk(cls, feats: list[Feature]):
        cls.clear()
        for feat in feats:
            cls.register(feat)
