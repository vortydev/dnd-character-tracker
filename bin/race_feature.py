# race_feature.py
from typing import Optional, List
from feature import FeatureType, Feature
from race_types import RaceType

class RaceFeature(Feature):
    """Represents a D&D 5e race feature."""
    def __init__(self, name: str, description: str, race_type: RaceType, subfeatures: Optional[List[Feature]] = None):
        super().__init__(name, description, subfeatures)
        self.race_type = race_type

    def __str__(self):
        sub_str = "\n  - " + "\n  - ".join(str(f) for f in self.subfeatures) if self.subfeatures else ""
        return f"[{self.race_type.value}] {self.name}: {self.description}{sub_str}"

    def to_dict(self):
        return {
            "type": FeatureType.RACE.value,
            "name": self.name,
            "description": self.description,
            "race_type": self.race_type.value,
            "subfeatures": [sf.to_dict() for sf in self.subfeatures],
        }
    
    @staticmethod
    def from_dict(data: dict) -> "RaceFeature":
        base = Feature.from_dict(data)
        return RaceFeature(
            name=base.name,
            description=base.description,
            subfeatures=base.subfeatures,
            race_type=RaceType(data["race_type"]),
        )
    
    def get_context(self) -> Optional[str]:
        return self.race_type.value
    
    def get_html(self):
        return super().get_html()