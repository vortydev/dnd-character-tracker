# spell.py
from enum import Enum
from typing import Optional, List
from common import ActionCost


class SpellSchool(Enum):
    ABJURATION = "Abjuration"
    CONJURATION = "Conjuration"
    DIVINATION = "Divination"
    ENCHANTMENT = "Enchantment"
    EVOCATION = "Evocation"
    ILLUSION = "Illusion"
    NECROMANCY = "Necromancy"
    TRANSMUTATION = "Transmutation"

class SpellComponent(Enum):
    V = "Verbal"     # The spell requires you to speak aloud
    S = "Somatic"    # The spell requires hand gestures
    M = "Material"   # The spell requires physical components
    

# LATER Add class spell lists
class Spell:
    """
    Represents a D&D 5e spell, including school, level, and description.
    """

    def __init__(
        self,
        name: str,
        level: int,
        school: SpellSchool,
        action_cost: ActionCost,
        description: str,
        higher_levels: Optional[str] = None,
        duration: Optional[str] = None,
        casting_time: Optional[str] = None,
        s_range: Optional[str] = None,
        components: Optional[List[SpellComponent]] = None,
        material_description: Optional[List[str]] = None,
    ):
        self.name = name
        self.level = level  # 0 for cantrips
        self.school = school
        self.action_cost = action_cost
        self.description = description
        self.higher_levels = higher_levels
        self.duration = duration
        self.casting_time = casting_time
        self.s_range = s_range
        self.components = components or []
        self.material_description = material_description or []

    def __str__(self):
        level_str = "Cantrip" if self.level == 0 else f"Level {self.level}"
        return f"{self.name} ({level_str} {self.school.value})"

    def to_dict(self):
        return {
            "name": self.name,
            "level": self.level,
            "school": self.school.value,
            "action_cost": self.action_cost.value,
            "description": self.description,
            "higher_levels": self.higher_levels,
            "duration": self.duration,
            "casting_time": self.casting_time,
            "range": self.s_range,
            "components": [c.value for c in self.components],
            "material_description": [m for m in self.material_description],
        }

    @staticmethod
    def from_dict(data: dict) -> "Spell":
        return Spell(
            name=data["name"],
            level=data["level"],
            school=SpellSchool(data["school"]),
            action_cost=ActionCost(data["action_cost"]),
            description=data["description"],
            higher_levels=data.get("higher_levels"),
            duration=data.get("duration"),
            casting_time=data.get("casting_time"),
            s_range=data.get("range"),
            components=[SpellComponent(c) for c in data.get("components", [])],
            material_description=[m for m in data.get("material_description", [])],
        )
