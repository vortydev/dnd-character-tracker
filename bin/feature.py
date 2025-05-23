# feature.py
from typing import List, Optional
from feature_types import FeatureType


class Feature():
    """Represents a basic D&D 5e feature."""
    def __init__(self, name: str, description: str, subfeatures: Optional[List["Feature"]] = None):
        self.name = name
        self.description = description
        self.subfeatures = subfeatures or []

    def __str__(self):
        sub_str = "\n  - " + "\n  - ".join(str(f) for f in self.subfeatures) if self.subfeatures else ""
        return f"{self.name}: {self.description}{sub_str}"

    def to_dict(self):
        return {
            "type": FeatureType.BASE.value,
            "name": self.name,
            "description": self.description,
            "subfeatures": [sf.to_dict() for sf in self.subfeatures] if self.subfeatures else [],
        }
    
    @staticmethod
    def from_dict(data: dict) -> "Feature":
        subfeatures = [Feature.from_dict(sf) for sf in data.get("subfeatures", [])]
        return Feature(
            name=data["name"],
            description=data["description"],
            subfeatures=subfeatures,
        )
    
    def get_context(self) -> Optional[str]:
        return None