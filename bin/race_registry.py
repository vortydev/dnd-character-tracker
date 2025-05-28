# race_registry.py
from typing import Dict
from race import Race, RaceType

class RaceRegistry:
    _races: Dict[str, Race] = {}

    @classmethod
    def register(cls, race: Race):
        key = cls._make_key(race.name, race.subrace.name if race.subrace else None)
        cls._races[key] = race

    @classmethod
    def get(cls, name: RaceType, subrace_name: str = None) -> Race:
        """
        Retrieve a race by its name and optional subrace name.
        """
        key = cls._make_key(name, subrace_name)
        return cls._races[key]

    @classmethod
    def all(cls) -> Dict[str, Race]:
        return cls._races

    @classmethod
    def clear(cls):
        cls._races.clear()

    @classmethod
    def load_bulk(cls, races: list[Race]):
        cls.clear()
        for race in races:
            cls.register(race)

    @staticmethod
    def _make_key(name: RaceType, subrace_name: str = None) -> str:
        """
        Generate a unique registry key from the race and optional subrace.
        Example: "Tiefling:Zariel" or "Human:None"
        """
        return f"{name.value}{':'+subrace_name if subrace_name else ''}"
