# spell_registry.py
from typing import Dict
from spell import Spell

class SpellRegistry:
    _spells: Dict[str, Spell] = {}

    @classmethod
    def register(cls, spell: Spell):
        cls._spells[spell.name.lower()] = spell

    @classmethod
    def get(cls, name: str) -> Spell:
        return cls._spells[name.lower()]

    @classmethod
    def all(cls) -> Dict[str, Spell]:
        return cls._spells

    @classmethod
    def clear(cls):
        cls._spells.clear()

    @classmethod
    def load_bulk(cls, spells: list[Spell]):
        cls.clear()
        for spell in spells:
            cls.register(spell)
