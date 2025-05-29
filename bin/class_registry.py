# class_registry.py

from typing import Dict
from class_base import Class, ClassType
from ability import AbilityType, Skill
from items.tool_item import ToolItem
from equipment import ArmorType, WeaponType

class ClassRegistry:
    _registry: Dict[ClassType, Class] = {}

    @classmethod
    def register(cls, class_obj: Class):
        cls._registry[class_obj.name] = class_obj

    @classmethod
    def get(cls, class_type: ClassType) -> Class:
        return cls._registry[class_type]

    @classmethod
    def all(cls) -> Dict[ClassType, Class]:
        return cls._registry.copy()
    
    @classmethod
    def register_defaults(cls):
        """Load class definitions from JSON and register them."""
        from class_io import load_classes_from_file
        classes = load_classes_from_file()
        for c in classes:
            cls.register(c)
