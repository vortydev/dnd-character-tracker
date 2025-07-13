# class_feature.py
from typing import List, Optional
from class_base import ClassType
from subclass_ import SubclassType
from feature import Feature
from feature_types import FeatureType


class ClassFeature(Feature):
    """Represents a D&D 5e class feature."""
    def __init__(self, name: str, description: str, class_type: ClassType, subfeatures: Optional[List[Feature]] = None, tags: Optional[List[str]] = None):
        super().__init__(name, description, subfeatures, tags)
        self.class_type = class_type

    def __str__(self):
        sub_str = "\n  - " + "\n  - ".join(str(f) for f in self.subfeatures) if self.subfeatures else ""
        tags_str = " (" + ", #".join(t for t in self.tags) + ")" if self.tags else ""
        return f"[{self.class_type.value}] {self.name}: {self.description}{tags_str}{sub_str}"

    def to_dict(self):
        return {
            "type": FeatureType.CLASS.value,
            "name": self.name,
            "description": self.description,
            "class_type": self.class_type.value,
            "subfeatures": [sf.to_dict() for sf in self.subfeatures],
            "tags": [t for t in self.tags] if self.tags else [],
        }
    
    @staticmethod
    def from_dict(data: dict) -> "ClassFeature":
        base = Feature.from_dict(data)
        return ClassFeature(
            name=base.name,
            description=base.description,
            subfeatures=base.subfeatures,
            class_type=ClassType(data["class_type"]),
            tags=base.tags,
        )
    
    def get_context(self) -> Optional[str]:
        return self.class_type.value
    
    def get_html(self):
        return super().get_html()


class SubclassFeature(ClassFeature):
    """Represents a D&D 5e subclass feature."""
    def __init__(self, name: str, description: str, class_type: ClassType, subclass_type: SubclassType, subfeatures: Optional[List[Feature]] = None, tags: Optional[List[str]] = None):
        super().__init__(name, description, class_type, subfeatures, tags)
        self.subclass_type = subclass_type

    def __str__(self):
        sub_str = "\n  - " + "\n  - ".join(str(f) for f in self.subfeatures) if self.subfeatures else ""
        tags_str = " (" + ", #".join(t for t in self.tags) + ")" if self.tags else ""
        return f"[{self.class_type.value} - {self.subclass_type.value}] {self.name}: {self.description}{tags_str}{sub_str}"

    def to_dict(self):
        return {
            "type": FeatureType.SUBCLASS.value,
            "name": self.name,
            "description": self.description,
            "class_type": self.class_type.value,
            "subclass_type": self.subclass_type.value,
            "subfeatures": [sf.to_dict() for sf in self.subfeatures],
            "tags": [t for t in self.tags] if self.tags else [],
        }
    
    @staticmethod
    def from_dict(data: dict) -> "SubclassFeature":
        base = ClassFeature.from_dict(data)
        return SubclassFeature(
            name=base.name,
            description=base.description,
            subfeatures=base.subfeatures,
            class_type=ClassType(data["class_type"]),
            subclass_type=SubclassType(data["subclass_type"]),
            tags=base.tags,
        )
    
    def get_context(self) -> Optional[str]:
        return f"{self.class_type.value} - {self.subclass_type.value}"

    def get_html(self):
        return super().get_html()