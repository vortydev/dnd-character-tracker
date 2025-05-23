# character.py
from typing import Dict
from ability import Ability, AbilityType
from race import Race

PROFICIENCY_BY_LEVEL = {
    range(1, 5): 2,
    range(5, 9): 3,
    range(9, 13): 4,
    range(13, 17): 5,
    range(17, 21): 6,
}

def get_proficiency_bonus(level: int) -> int:
    for level_range, bonus in PROFICIENCY_BY_LEVEL.items():
        if level in level_range:
            return bonus
    raise ValueError("Invalid character level")


class Character:
    def __init__(self, name: str, health: int, ability_scores: Dict[AbilityType, int], race: Race):
        self.name = name
        self.race = race
        self.health = {
            "max": health,
            "cur": health,
            "temp": 0
        }
        self.abilities = {
            key: Ability(key, ability_scores.get(key, 10))
            for key in AbilityType
        }

    def to_dict(self):
        return {
            "name": self.name,
            "health": self.health,
            "abilities": {k.value: v.score for k, v in self.abilities.items()},
            "race": self.race.to_dict()
        }

    @staticmethod
    def from_dict(data: dict):
        from race import Race  # avoid circular import
        ability_scores = {AbilityType(k): v for k, v in data["abilities"].items()}
        race = Race.from_dict(data["race"])
        char = Character(data["name"], data["health"]["max"], ability_scores, race)
        char.health = data["health"]
        return char

    def __str__(self):
        abilities = "\n".join(str(a) for a in self.abilities.values())
        return (
            f"{self.name} [{self.race.describe()}]\n"
            f"HP: {self.health['cur']}/{self.health['max']} (+{self.health['temp']} temp)\n"
            f"Abilities:\n{abilities}"
        )
