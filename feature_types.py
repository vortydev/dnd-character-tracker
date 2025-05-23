# feature_types.py
from enum import Enum

class FeatureType(Enum):
    BASE = "Feature"
    CLASS = "Class Feature"
    SUBCLASS = "Subclass Feature"
    RACE = "Race Feature"
    BACKGROUND = "Background Feature"