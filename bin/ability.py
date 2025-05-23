# ability.py
from enum import Enum
from collections import defaultdict

class AbilityType(Enum):
    """Enum representing the six core D&D ability types."""
    STR = 'str'
    DEX = 'dex'
    CON = 'con'
    INT = 'int'
    WIS = 'wis'
    CHA = 'cha'

    def full_name(self):
        """Return the full name of the ability."""
        return {
            AbilityType.STR: "Strength",
            AbilityType.DEX: "Dexterity",
            AbilityType.CON: "Constitution",
            AbilityType.INT: "Intelligence",
            AbilityType.WIS: "Wisdom",
            AbilityType.CHA: "Charisma"
        }[self]

class Ability:
    """Represents a single ability with a type and a numeric score."""
    def __init__(self, ability_type: AbilityType, score: int):
        """
        Initialize an Ability object.

        Args:
            ability_type (AbilityType): The type of ability (e.g., STR, DEX).
            score (int): The numeric value of the ability.
        """
        self.type = ability_type
        self.score = score

    def modifier(self) -> int:
        """
        Compute the ability modifier based on the score.

        Returns:
            int: The calculated modifier.
        """
        return (self.score - 10) // 2

    def __str__(self):
        """
        Return a readable string representation of the ability.

        Returns:
            str: The ability's name, key, score, and modifier.
        """
        return f"{self.type.full_name()} ({self.type.name}): {self.score} [mod: {self.modifier()}]"


class Skill(Enum):
    # Strength
    ATHLETICS = "Athletics"

    # Dexterity
    ACROBATICS = "Acrobatics"
    SLEIGHT_OF_HAND = "Sleight of Hand"
    STEALTH = "Stealth"

    # Intelligence
    ARCANA = "Arcana"
    HISTORY = "History"
    INVESTIGATION = "Investigation"
    NATURE = "Nature"
    RELIGION = "Religion"

    # Wisdom
    ANIMAL_HANDLING = "Animal Handling"
    INSIGHT = "Insight"
    MEDICINE = "Medicine"
    PERCEPTION = "Perception"
    SURVIVAL = "Survival"

    # Charisma
    DECEPTION = "Deception"
    INTIMIDATION = "Intimidation"
    PERFORMANCE = "Performance"
    PERSUASION = "Persuasion"

SKILL_ABILITY_MAP = {
    # Strength
    Skill.ATHLETICS: AbilityType.STR,

    # Dexterity
    Skill.ACROBATICS: AbilityType.DEX,
    Skill.SLEIGHT_OF_HAND: AbilityType.DEX,
    Skill.STEALTH: AbilityType.DEX,

    # Intelligence
    Skill.ARCANA: AbilityType.INT,
    Skill.HISTORY: AbilityType.INT,
    Skill.INVESTIGATION: AbilityType.INT,
    Skill.NATURE: AbilityType.INT,
    Skill.RELIGION: AbilityType.INT,

    # Wisdom
    Skill.ANIMAL_HANDLING: AbilityType.WIS,
    Skill.INSIGHT: AbilityType.WIS,
    Skill.MEDICINE: AbilityType.WIS,
    Skill.PERCEPTION: AbilityType.WIS,
    Skill.SURVIVAL: AbilityType.WIS,

    # Charisma
    Skill.DECEPTION: AbilityType.CHA,
    Skill.INTIMIDATION: AbilityType.CHA,
    Skill.PERFORMANCE: AbilityType.CHA,
    Skill.PERSUASION: AbilityType.CHA,
}

SKILLS_BY_ABILITY = defaultdict(list)
for skill, ability_type in SKILL_ABILITY_MAP.items():
    SKILLS_BY_ABILITY[ability_type].append(skill)
    