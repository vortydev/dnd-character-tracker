# class_level_registry.py
from typing import Dict, Optional, Tuple
from bin.class_level import ClassLevel
from bin.class_base import ClassType
from subclass_ import SubclassType

class ClassLevelRegistry:
    _class_levels: Dict[Tuple[ClassType, int, Optional[SubclassType]], ClassLevel] = {}

    @classmethod
    def register(cls, cl: ClassLevel):
        subclass = cl.subclass if cl.subclass else None
        cls._class_levels[(cl.class_type, cl.level, subclass)] = cl

    @classmethod
    def get(cls, class_type: ClassType, max_level: int, subclass: SubclassType=None):
        results = []

        for (ct, lvl, sub), data in cls._class_levels.items():
            if ct == class_type and lvl <= max_level and sub == subclass:
                results.append(data)

        return sorted(results, key=lambda x: x["level"])

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
