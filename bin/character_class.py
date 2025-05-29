# character_class.py
from typing import Optional, List, Dict
from class_base import ClassType, Class
from class_registry import ClassRegistry
from ability import Skill


class CharacterClass:
    def __init__(self, class_type: ClassType, level: int):
        self.class_type = class_type
        self.level = level
        self._base_class: Optional[Class] = None  # Lazy-loaded reference

        # Optional character-specific data (extend later)
        self.chosen_skills: List[Skill] = []  # Filled after creation
    
    def get_class_name(self):
        return self.class_type.value
    
    @property
    def base_class(self) -> Class:
        if self._base_class is None:
            self._base_class = ClassRegistry.get(self.class_type)
        return self._base_class
    
    def to_dict(self) -> Dict[str]:
        return {
            "class_type": self.class_type.value,
            "level": self.level,
            "chosen_skills": [skill for skill in self.chosen_skills],
        }

    @staticmethod
    def from_dict(data: Dict[str]) -> "CharacterClass":
        cc = CharacterClass(
            class_type=ClassType(data["class_type"]),
            level=data["level"]
        )
        # Assuming Skill is an Enum or has a from_name method
        cc.chosen_skills = [Skill[s] for s in data.get("chosen_skills", [])]
        return cc
