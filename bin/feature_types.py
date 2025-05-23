# feature_types.py
from enum import Enum

class FeatureType(Enum):
    BASE = "Feature"
    CLASS = "Class"
    SUBCLASS = "Subclass"
    RACE = "Race"
    BACKGROUND = "Background"