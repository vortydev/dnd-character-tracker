# character_registry.py
from typing import Dict
from character import Character
from character_io import save_characters_to_file

class CharacterRegistry:
    _characters: Dict[str, Character] = {}
    _archived: Dict[str, Character] = {}

    @classmethod
    def register(cls, char: Character, overwrite: bool = True):
        """Register a character. If overwrite is False and the character already exists, raise an error."""
        if not overwrite and char.name in cls._characters:
            raise ValueError(f"Character '{char.name}' already exists.")
        cls._characters[char.name] = char

    @classmethod
    def get(cls, name: str) -> Character:
        return cls._characters[name]

    @classmethod
    def exists(cls, name: str) -> bool:
        return name in cls._characters

    @classmethod
    def all(cls) -> Dict[str, Character]:
        return cls._characters

    @classmethod
    def clear(cls):
        cls._characters.clear()

    @classmethod
    def load_bulk(cls, characters: list[Character]):
        cls.clear()
        for char in characters:
            cls.register(char)

    @classmethod
    def save_to_file(cls, path: str = None):
        """Save all characters in the registry to file."""
        char_list = list(cls._characters.values())
        save_characters_to_file(char_list, path)

    @classmethod
    def delete(cls, name: str, archive: bool = True):
        """
        Delete (or archive) a character from the registry.
        """
        if name not in cls._characters:
            raise KeyError(f"Character '{name}' not found.")

        if archive:
            cls._archived[name] = cls._characters[name]

        del cls._characters[name]

    @classmethod
    def archived(cls) -> Dict[str, Character]:
        return cls._archived

    @classmethod
    def restore(cls, name: str):
        """
        Restore a previously archived character.
        """
        if name not in cls._archived:
            raise KeyError(f"Archived character '{name}' not found.")
        cls._characters[name] = cls._archived[name]
        del cls._archived[name]

    @classmethod
    def rename(cls, old_name: str, new_name: str):
        if old_name not in cls._characters:
            raise KeyError(f"Character '{old_name}' not found.")
        if new_name in cls._characters:
            raise ValueError(f"Character name '{new_name}' already exists.")

        char = cls._characters.pop(old_name)
        char.name = new_name
        cls._characters[new_name] = char
