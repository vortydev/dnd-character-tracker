# class_level.py
from enum import Enum
from typing import Optional, Dict, List
from class_ import ClassType, SubclassType
from class_feature import ClassFeature
from feature_registry import FeatureRegistry
from spell_slots_tables import get_class_level_spell_slots


class ClassLevelType(Enum):
    BASE = "Base"
    SPELLCASTER = "Spellcaster"
    # WIP
    SORCERER = "Sorcerer"



# TODO Add ability score improvement logic
class ClassLevel():
    """Base ClassLevel object for any class."""
    def __init__(self, lvl: int, class_type: ClassType,
                 features: List[ClassFeature] = [], subclass: Optional[SubclassType] = None):
        self.level = lvl
        self.class_type = class_type
        self.features = features
        self.subclass = subclass
    
    def to_dict(self):
        return {
            "type": ClassLevelType.BASE,
            "level": self.level,
            "class_type": self.class_type.value,
            "features": [f.name for f in self.features],
            "subclass": self.subclass.value if self.subclass else None,
        }
    
    @staticmethod
    def from_dict(data: dict) -> "ClassLevel":
        features = [FeatureRegistry.get(name) for name in data.get("features", [])]
        subclass_val = data.get("subclass")
        return ClassLevel(
            lvl=data["level"],
            class_type=ClassType(data["class_type"]),
            features=features,
            subclass=SubclassType(subclass_val) if subclass_val else None,
        )


class ClassLevelSpellcaster(ClassLevel):
    """Base ClassLevel object for spellcasting classes."""
    def __init__(self, lvl: int, class_type: ClassType,
                 features: List[ClassFeature] = [], subclass: Optional[SubclassType] = None,
                 known_cantrips: int=0, known_spells: int=0):
        super().__init__(lvl, class_type, features, subclass)
        self.known_cantrips = known_cantrips
        self.known_spells = known_spells
        self.spell_slots = get_class_level_spell_slots(self.class_type, self.level)

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "type": ClassLevelType.SPELLCASTER.value,
            "known_cantrips": self.known_cantrips,
            "known_spells": self.known_spells,
            "spell_slots": self.spell_slots,
        })
        return data
    
    @staticmethod
    def from_dict(data: dict) -> "ClassLevelSpellcaster":
        base = ClassLevel.from_dict(data)
        return ClassLevelSpellcaster(
            lvl=base.level,
            class_type=ClassType(base.class_type.value),
            features=base.features,
            subclass=base.subclass,
            known_cantrips=data.get("known_cantrips", 0),
            known_spells=data.get("known_spells", 0),
            spell_slots=data.get("spell_slots", {}),
        )
    

class ClassLevelSorcerer(ClassLevelSpellcaster):
    """ClassLevel object for the Sorcerer class."""
    def __init__(self, lvl: int, class_type: ClassType = ClassType.SORCERER,
                 features: List[ClassFeature] = [], subclass: Optional[SubclassType] = None,
                 known_cantrips: int=0, known_spells: int=0, sorcery_points: int=None):
        super().__init__(lvl, class_type, features, subclass, known_cantrips, known_spells)
        self.known_spells = min(self.level + 1, 15)
        self.sorcery_points = self.level if self.level > 1 else 0
        if sorcery_points:
            self.sorcery_points = sorcery_points

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "type": ClassLevelType.SORCERER.value,
            "sorcery_points": self.sorcery_points,
        })
        return data
    
    @staticmethod
    def from_dict(data: dict) -> "ClassLevelSorcerer":
        base = ClassLevelSpellcaster.from_dict(data)
        return ClassLevelSorcerer(
            lvl=base.level,
            class_type=ClassType(base.class_type.value),
            features=base.features,
            subclass=base.subclass,
            known_cantrips=base.known_cantrips,
            known_spells=base.known_spells,
            spell_slots=base.spell_slots,
            sorcery_points=data.get("sorcery_points", 0),
        )
    