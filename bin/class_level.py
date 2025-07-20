# class_level.py
from enum import Enum
from typing import Optional, Dict, List
from class_base import ClassType, SubclassType
from class_feature import ClassFeature
from feature_registry import FeatureRegistry
from feature_types import FeatureType
from spell_slots_tables import get_class_level_spell_slots


class ClassLevelType(Enum):
    BASE = "Base"
    SPELLCASTER = "Spellcaster"
    ARTIFICER = "Artificer" # Infusions
    BARD = "Bard" # Bardic inspiration
    MONK = "Monk" # Ki points
    SORCERER = "Sorcerer" # Sorcery points
    ROGUE = "Rogue" # Sneak attack
    # TODO Add other classes



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
            "type": ClassLevelType.BASE.value,
            "level": self.level,
            "class_type": self.class_type.value,
            "features": [f.name for f in self.features],
            "subclass": self.subclass.value if self.subclass else None,
        }
    
    @staticmethod
    def from_dict(data: dict, registries: dict[str] = None) -> "ClassLevel":
        class_type = ClassType(data["class_type"])
        subclass_val = data.get("subclass", None)

        registries = registries or {}
        feature_registry: FeatureRegistry = registries.get("features", FeatureRegistry)

        features = [feature_registry.get(name, FeatureType.SUBCLASS if subclass_val else FeatureType.CLASS, class_type) for name in data.get("features", [])]
        return ClassLevel(
            lvl=data["level"],
            class_type=class_type,
            features=features,
            subclass=SubclassType(subclass_val) if subclass_val and subclass_val != "None" else None
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
    def from_dict(data: dict, registries: dict[str] = None) -> "ClassLevelSpellcaster":
        base = ClassLevel.from_dict(data, registries)
        return ClassLevelSpellcaster(
            lvl=base.level,
            class_type=ClassType(base.class_type.value),
            features=base.features,
            subclass=base.subclass,
            known_cantrips=data.get("known_cantrips", 0),
            known_spells=data.get("known_spells", 0),
        )
    
# Sorcerer
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
    def from_dict(data: dict, registries: dict[str] = None) -> "ClassLevelSorcerer":
        base = ClassLevelSpellcaster.from_dict(data, registries)
        return ClassLevelSorcerer(
            lvl=base.level,
            class_type=ClassType(base.class_type.value),
            features=base.features,
            subclass=base.subclass,
            known_cantrips=base.known_cantrips,
            known_spells=base.known_spells,
            sorcery_points=data.get("sorcery_points", 0),
        )
    
class ClassLevelArtificer(ClassLevelSpellcaster):
    """ClassLevel object for the Artificer class."""
    def __init__(self, lvl: int, class_type: ClassType = ClassType.ARTIFICER,
                 features: List[ClassFeature] = [], subclass: Optional[SubclassType] = None,
                 known_cantrips: int=0, known_spells: int=0,
                 infusions_known: int=0, infused_items: int=0):
        super().__init__(lvl, class_type, features, subclass, known_cantrips, known_spells)
        self.infusions_known = infusions_known
        self.infused_items = infused_items

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "type": ClassLevelType.ARTIFICER.value,
            "infusions_known": self.infusions_known,
            "infused_items": self.infused_items,
        })
        return data
    
    @staticmethod
    def from_dict(data: dict, registries: dict[str] = None) -> "ClassLevelArtificer":
        base = ClassLevelSpellcaster.from_dict(data, registries)
        return ClassLevelArtificer(
            lvl=base.level,
            class_type=ClassType(base.class_type.value),
            features=base.features,
            subclass=base.subclass,
            known_cantrips=base.known_cantrips,
            known_spells=base.known_spells,
            infusions_known=data.get("infusions_known", 0),
            infused_items=data.get("infused_items", 0),
        )

# Rogue
class ClassLevelRogue(ClassLevel):
    """ClassLevel object for the Rogue class."""
    def __init__(self, lvl: int, class_type: ClassType,
                 features: List[ClassFeature] = [], subclass: Optional[SubclassType] = None,
                 sneak_attack_dice: int=1, sneak_attack_dmg:int=6):
        super().__init__(lvl, class_type, features, subclass)
        self.sneak_attack_dice = sneak_attack_dice
        self.sneak_attack_dmg = sneak_attack_dmg
        
    def to_dict(self):
        data = super().to_dict()
        data.update({
            "type": ClassLevelType.ROGUE.value,
            "sneak_attack_dice": self.sneak_attack_dice,
            "sneak_attack_dmg": self.sneak_attack_dmg,
        })
        return data
    
    @staticmethod
    def from_dict(data: dict, registries: dict[str] = None) -> "ClassLevelRogue":
        base = ClassLevel.from_dict(data, registries)
        return ClassLevelRogue(
            lvl=base.level,
            class_type=ClassType(base.class_type.value),
            features=base.features,
            subclass=base.subclass,
            sneak_attack_dice=data.get("sneak_attack_dice", 1),
            sneak_attack_dmg=data.get("sneak_attack_dmg", 6),
        )
    