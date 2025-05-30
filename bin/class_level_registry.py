# class_level_registry.py
from typing import Dict, Optional, Tuple
from class_level import ClassLevel
from class_base import ClassType
from subclass_ import SubclassType

class ClassLevelRegistry:
    _class_levels: Dict[Tuple[ClassType, int, Optional[SubclassType]], ClassLevel] = {}

    @classmethod
    def register(cls, cl: ClassLevel):
        cls._class_levels[(cl.class_type, cl.level, cl.subclass)] = cl

    @classmethod
    def get(cls, ct: ClassType, lvl: int, subclass: Optional[SubclassType] = None) -> ClassLevel:
        return cls._class_levels[(ct, lvl, subclass)]

    @classmethod
    def all(cls) -> Dict[Tuple[ClassType, int, Optional[SubclassType]], ClassLevel]:
        return cls._class_levels

    @classmethod
    def clear(cls):
        cls._class_levels.clear()

    @classmethod
    def load_bulk(cls, class_levels: list[ClassLevel]):
        cls.clear()
        for cl in class_levels:
            cls.register(cl)
