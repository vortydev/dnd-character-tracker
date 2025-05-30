# character.py
from collections import defaultdict
from typing import Dict, List, Optional, Any
from ability import Ability, AbilityType, Skill, SKILL_ABILITY_MAP

from race import Race
from race_types import RaceType
from race_registry import RaceRegistry

from class_base import ClassType
from character_class import CharacterClass
from class_level_registry import ClassLevelRegistry

from feature import Feature
from feature_types import FeatureType
from feature_registry import FeatureRegistry

from spell import Spell
from spell_registry import SpellRegistry


PROFICIENCY_BY_LEVEL = {
    range(1, 5): 2,
    range(5, 9): 3,
    range(9, 13): 4,
    range(13, 17): 5,
    range(17, 21): 6,
}


class Character:
    def __init__(self, name: str):
        self.name = name
        self.classes: List[CharacterClass] = []
        self.race: Race = None
        self.abilities: Dict[AbilityType, Ability] = {}
        self.proficient_skills: set[Skill] = set()

    @property
    def race(self) -> Optional[Race]:
        if self._race is None and self.race_type:
            self._race = RaceRegistry.get(self.race_type)
        return self._race
    
    # === Abilities ===
    def set_ability_score(self, ability_type: AbilityType, score: int):
        self.abilities[ability_type] = Ability(ability_type, score)

    def set_ability_scores(self, score_map: Dict[AbilityType, int]):
        for ab_type, score in score_map.items():
            self.set_ability_score(ab_type, score)

    def get_ability(self, ability_type: AbilityType) -> Optional[Ability]:
        return self.abilities.get(ability_type)

    def get_modifier(self, ability_type: AbilityType) -> Optional[int]:
        ab = self.get_ability(ability_type)
        return ab.modifier() if ab else None
    
    def get_effective_modifier(self, ability_type: AbilityType) -> Optional[int]:
        base_score = self.abilities.get(ability_type).score if ability_type in self.abilities else 0
        racial_bonus = 0

        if self.race:
            racial_bonus += self.race.ability_score_increase.get(ability_type, 0)
            if self.race.subrace:
                racial_bonus += self.race.subrace.ability_score_increase.get(ability_type, 0)

        total_score = base_score + racial_bonus
        return (total_score - 10) // 2
    
    @staticmethod
    def get_proficiency_bonus(level: int) -> int:
        for level_range, bonus in PROFICIENCY_BY_LEVEL.items():
            if level in level_range:
                return bonus
        raise ValueError("Invalid character level")


    # === Derived values ===
    def get_initiative(self) -> int:
        return self.get_effective_modifier(AbilityType.DEX) or 0
    
    def get_max_hp(self) -> int:
        hp = 0
        for char_class in self.classes:
            con_mod = self.get_effective_modifier(AbilityType.CON) or 0
            hd = char_class.base_class.hit_dice

            hp += hd  # Max for level 1
            if char_class.level > 1:
                avg = (hd // 2) + 1
                hp += (avg + con_mod) * (char_class.level - 1)

        return hp

    def get_skill_bonus(self, skill: Skill) -> int:
        ab_type = SKILL_ABILITY_MAP[skill]
        base_mod = self.get_effective_modifier(ab_type) or 0
        bonus = base_mod

        if hasattr(self, "proficient_skills") and skill in self.proficient_skills:
            bonus += self.get_proficiency_bonus(self.get_total_level())
        
        return bonus
    

    # === Skills ===
    def add_skill_proficiency(self, skill: Skill):
        self.proficient_skills.add(skill)

    def remove_skill_proficiency(self, skill: Skill):
        self.proficient_skills.discard(skill)

    def has_skill_proficiency(self, skill: Skill) -> bool:
        return skill in self.proficient_skills
    
    def set_skill_proficiencies(self, skills: List[Skill]):
        self.proficient_skills = set(skills)


    # === Race ===
    def set_race(self, race_type: RaceType):
        self.race_type = race_type
        self._race = RaceRegistry.get(race_type)

    def add_class(self, char_class: CharacterClass):
        self.classes.append(char_class)

    def get_class_levels(self) -> Dict[ClassType, int]:
        """Return a dict of {ClassType: level} for all classes."""
        return {c.class_type: c.level for c in self.classes}

    def get_total_level(self) -> int:
        return sum(c.level for c in self.classes)

    def get_level_in(self, class_type: ClassType) -> int:
        for c in self.classes:
            if c.class_type == class_type:
                return c.level
        return 0
    
    def get_main_class(self) -> Optional[CharacterClass]:
        """Returns the class with the highest level (or first in list if tied)."""
        if not self.classes:
            return None
        return max(self.classes, key=lambda c: c.level)
    
    def get_all_saving_throws(self) -> List[AbilityType]:
        """Get saving throws from all classes (duplicates removed)."""
        all_saves = []
        for char_class in self.classes:
            all_saves.extend(char_class.base_class.proficiency_saving_throws)
        return list(set(all_saves))  # Remove duplicates
    
    def get_all_features_and_spells(self) -> dict[str, dict[str, list[Feature | Spell]]]:
        """
        Return all features and spells, grouped by origin:
        - class
        - subclass
        - race
        """
        features_by_origin = defaultdict(list)
        spells_by_origin = defaultdict(list)

        total_level = self.get_total_level()

        # === Class & Subclass features ===
        for char_class in self.classes:
            for level in range(1, char_class.level + 1):
                # Get class-level features (not subclass-bound)
                try:
                    base_level = ClassLevelRegistry.get(char_class.class_type, level)
                    if base_level.subclass is None:
                        features_by_origin["class"].extend(base_level.features)
                        # Insert spell logic here if applicable
                except KeyError:
                    pass

                # Get subclass-level features for this level
                if char_class.subclass:
                    try:
                        subclass_level = ClassLevelRegistry.get(char_class.class_type, level)
                        if subclass_level.subclass == char_class.subclass:
                            features_by_origin["subclass"].extend(subclass_level.features)
                            # Insert subclass spell logic here if needed
                    except KeyError:
                        pass

        # === Race & Subrace features ===
        if self.race:
            for lvl, feats in self.race.feats.items():
                if lvl <= total_level:
                    features_by_origin["race"].extend(feats)

            for lvl, spells in self.race.spells.items():
                if lvl <= total_level:
                    spells_by_origin["race"].extend(spells)

            if self.race.subrace:
                for lvl, feats in self.race.subrace.feats.items():
                    if lvl <= total_level:
                        features_by_origin["race"].extend(feats)

                for lvl, spells in self.race.subrace.spells.items():
                    if lvl <= total_level:
                        spells_by_origin["race"].extend(spells)

        return {
            "features": dict(features_by_origin),
            "spells": dict(spells_by_origin)
        }

    # === IO ===
    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "race_type": self.race_type.value if self.race_type else None,
            "classes": [cc.to_dict() for cc in self.classes],
            "abilities": {ab_type.value: ab.score for ab_type, ab in self.abilities.items()},
            "proficient_skills": [s.value for s in self.proficient_skills],
        }

    @staticmethod
    def from_dict(data: Dict[str, Any], registries: Dict[str, Any] = None) -> "Character":
        char = Character(data["name"])
        if data.get("race_type"):
            from race_types import RaceType
            char.race_type = RaceType[data["race_type"]]
            char._race = RaceRegistry.get(char.race_type)

        char.classes = [CharacterClass.from_dict(c, registries) for c in data["classes"]]

        if "abilities" in data:
            for ab_name, score in data["abilities"].items():
                ab_type = AbilityType[ab_name]
                char.set_ability_score(ab_type, score)

        if "proficient_skills" in data:
            char.set_skill_proficiencies([Skill[s] for s in data["proficient_skills"]])

        return char
