# race_registry.py
from typing import Dict, Optional
from race import Race, RaceType

class RaceRegistry:
    _races: Dict[tuple[str, Optional[str]], Race] = {}

    @classmethod
    def register(cls, race: Race):
        subrace_name = race.subrace.name if race.subrace else None
        key = cls._make_key(race.name, subrace_name)
        cls._races[key] = race

    @classmethod
    def get(cls, race_type: RaceType, subrace_name: Optional[str] = None) -> Race:
        key = cls._make_key(race_type, subrace_name)
        try:
            return cls._races[key]
        except KeyError:
            raise KeyError(f"Missing key: '{key}'")

    @classmethod
    def all(cls) -> Dict[tuple[str, Optional[str]], Race]:
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
    def _make_key(name: RaceType, subrace_name: Optional[str] = None) -> tuple[str, Optional[str]]:
        return (name.value, subrace_name)
