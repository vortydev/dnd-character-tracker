# class_level_registry.py
from typing import Dict
from class_level import ClassLevel
from class_ import ClassType

# WIP A way to get the class level
class ClassLevelRegistry:
    _class_levels: Dict[tuple[ClassType, int], ClassLevel] = {}

    @classmethod
    def register(cls, cl: ClassLevel):
        cls._class_levels[(cl.class_type, cl.level)] = cl

    @classmethod
    def get(cls, ct: ClassType, lvl: int) -> ClassLevel:
        return cls._class_levels[(ct, lvl)]

    @classmethod
    def all(cls) -> Dict[tuple[ClassType, int], ClassLevel]:
        return cls._class_levels

    @classmethod
    def clear(cls):
        cls._class_levels.clear()

    @classmethod
    def load_bulk(cls, class_levels: list[ClassLevel]):
        cls.clear()
        for cl in class_levels:
            cls.register(cl)
