# character_class.py
from typing import Optional, List, Dict, Any
from class_base import ClassType, Class, validate_subclass_assignment
from class_registry import ClassRegistry
from subclass_ import SubclassType
from ability import Skill


class CharacterClass:
    def __init__(self, class_type: ClassType, level: int, subclass: Optional[SubclassType] = None):
        self.class_type = class_type
        self.level = level
        self._base_class: Optional[Class] = None  # Lazy-loaded reference

        self.subclass: Optional[SubclassType] = None
        if subclass:
            validate_subclass_assignment(class_type, level, subclass)
            self.subclass = subclass

        # Optional character-specific data (extend later)
        self.chosen_skills: List[Skill] = []  # Filled after creation

    def set_subclass(self, subclass: SubclassType):
        validate_subclass_assignment(self.class_type, self.level, subclass)
        self.subclass = subclass
    
    def get_class_name(self):
        return self.class_type.value
    
    @property
    def base_class(self) -> Class:
        if self._base_class is None:
            self._base_class = ClassRegistry.get(self.class_type)
        return self._base_class
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "class_type": self.class_type.value,
            "level": self.level,
            "subclass": self.subclass.value if self.subclass else None,
            "chosen_skills": [s.name for s in self.chosen_skills],
        }

    @staticmethod
    def from_dict(data: Dict[str, Any], registries: Dict[str, Any] = None) -> "CharacterClass":
        registries = registries or {}

        # Use the provided registry if available
        class_registry: ClassRegistry = registries.get("classes", ClassRegistry)

        class_type = ClassType(data["class_type"])
        subclass = SubclassType[data["subclass"]] if data.get("subclass") else None
        level = data["level"]

        cc = CharacterClass(class_type=class_type, level=level, subclass=subclass)
        cc._base_class = class_registry.get(class_type)

        cc.chosen_skills = [Skill[s] for s in data.get("chosen_skills", [])]
        return cc
