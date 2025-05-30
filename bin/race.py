# race.py
from typing import Optional, Dict, List
from enum import Enum
from ability import AbilityType
from common import Size, Language, DamageType
from spell import Spell
from spell_registry import SpellRegistry
from feature_types import FeatureType
from feature_registry import FeatureRegistry
from race_types import RaceType
from race_feature import RaceFeature
    

class Subrace:
    """
    Represents a specific subrace variation tied to a parent race.
    """

    def __init__(
        self,
        name: str,
        parent_race: RaceType,
        description: str = None,
        ability_score_increase: Optional[Dict[AbilityType, int]] = None,
        feats: Optional[Dict[int, List[RaceFeature]]] = None,
        spells: Optional[Dict[int, List[Spell]]] = None,
        info: Optional[Dict[str, str]] = None,
        languages: Optional[List[Language]] = None
    ):
        self.name = name
        self.parent_race = parent_race
        self.description = description
        self.ability_score_increase = ability_score_increase or {}
        self.feats = feats or {}
        self.spells = spells or {}
        self.info = info or {}
        self.languages = languages or []

    def to_dict(self):
        return {
            "name": self.name,
            "parent_race": self.parent_race.value,
            "description": self.description,
            "ability_score_increase": {k.value: v for k, v in self.ability_score_increase.items()},
            "feats": {
                str(level): [f.name for f in feat_list] for level, feat_list in self.feats.items()
            },
            "spells": {
                str(level): [spell.name for spell in spell_list]
                for level, spell_list in self.spells.items()
            },
            "info": self.info,
            "languages": [l.value for l in self.languages],
        }

    @staticmethod
    def from_dict(data: dict, registries: dict[str]=None) -> "Subrace":
        registries = registries or {}
        spell_registry: SpellRegistry = registries.get("spells", SpellRegistry)
        feature_registry: FeatureRegistry = registries.get("features", FeatureRegistry)

        spells_dict = {
            int(k): [
                spell_registry.get(s["name"]) if isinstance(s, dict) else spell_registry.get(s)
                for s in v
            ]
            for k, v in data.get("spells", {}).items()
        }
        features_dict = {
            int(k): [feature_registry.get(f, FeatureType.RACE, RaceType(data["parent_race"])) for f in v]
            for k, v in data.get("feats", {}).items()
        }
        langs = [Language(l) for l in data.get("languages", [])]

        return Subrace(
            name=data["name"],
            parent_race=RaceType(data["parent_race"]),
            description=data.get("description", None),
            ability_score_increase={AbilityType(k): v for k, v in data.get("ability_score_increase", {}).items()},
            feats=features_dict,
            spells=spells_dict,
            info=data.get("info", {}),
            languages=langs,
        )


class Race:
    """
    Represents a playable race and optional subrace.

    Attributes:
        name: The main race (e.g., Tiefling, Elf).
        subrace: Optional subrace (e.g., Zariel, High Elf).
        speed: Base movement speed in feet.
        size: Size category (usually "Medium").
        ability_score_increase: Dict of AbilityType → bonus score.
        feats: Dict of level → list of feats gained at that level.
        spells: Dict of level → list of spells gained at that level.
        info: Other string-based traits like vision, languages, etc.
    """

    def __init__(
        self,
        name: RaceType,
        description: str = None,
        subrace: Optional[Subrace] = None,
        speed: int = 30,
        size: Size = Size.MEDIUM,
        ability_score_increase: Optional[Dict[AbilityType, int]] = None,
        feats: Optional[Dict[int, List[RaceFeature]]] = None,
        spells: Optional[Dict[int, List[Spell]]] = None,
        info: Optional[Dict[str, str]] = None,
        languages: Optional[List[Language]] = None,
    ):
        self.name = name
        self.description = description
        self.subrace = subrace
        self.speed = speed
        self.size = size
        self.ability_score_increase = ability_score_increase or {}
        self.feats = feats or {}
        self.spells = spells or {}
        self.info = info or {}  # Contains explicit text details from books
        self.languages = languages or []

    def describe(self) -> str:
        """
        Return a human-readable string for this race/subrace.
        Returns:
            str: e.g., "Tiefling (Zariel)" or "Elf"
        """
        desc = f"{self.name.value}"
        if self.subrace:
            desc += f" ({getattr(self.subrace, 'name', str(self.subrace))})"
        return desc

    def to_dict(self):
        """
        Serialize this Race into a dictionary for JSON output.
        Returns:
            dict: The serialized representation.
        """
        return {
            "name": self.name.value,
            "description": self.description,
            "subrace": self.subrace.to_dict() if self.subrace else None,
            "speed": self.speed,
            "size": self.size.value,
            "ability_score_increase": {k.value: v for k, v in self.ability_score_increase.items()},
            "feats": {
                str(level): [f.name for f in feat_list] for level, feat_list in self.feats.items()
            },
            "spells": {
                str(level): [spell.name for spell in spell_list]
                for level, spell_list in self.spells.items()
            },
            "info": self.info,
            "languages": [l.value for l in self.languages],
        }

    @staticmethod
    def from_dict(data: dict, registries: dict[str] = None):
        """
        Deserialize a Race object from a saved dictionary.
        Args:
            data (dict): Serialized race dictionary.
        Returns:
            Race: A new Race instance.
        """
        registries = registries or {}
        spell_registry: SpellRegistry = registries.get("spells", SpellRegistry)
        feature_registry: FeatureRegistry = registries.get("features", FeatureRegistry)

        spells_dict = {
            int(k): [
                spell_registry.get(s["name"]) if isinstance(s, dict) else spell_registry.get(s)
                for s in v
            ]
            for k, v in data.get("spells", {}).items()
        }
        features_dict = {
            int(k): [
                feature_registry.get(f, FeatureType.RACE, RaceType(data["name"])) 
                for f in v
            ]
            for k, v in data.get("feats", {}).items()
        }
        langs = [Language(l) for l in data.get("languages", [])]

        return Race(
            name=RaceType(data["name"]),
            description=data.get("description", None),
            subrace=Subrace.from_dict(data["subrace"], registries) if data.get("subrace") else None,
            speed=data.get("speed", 30),
            size=Size(data.get("size", "Medium")),
            ability_score_increase={
                AbilityType(k): v for k, v in data.get("ability_score_increase", {}).items()
            },
            feats=features_dict,
            spells=spells_dict,
            info=data.get("info", {}),
            languages=langs
        )

    def __str__(self):
        """
        Return a readable string representation of the race.
        Returns:
            str
        """
        return self.describe()
