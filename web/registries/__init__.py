# web/registries/__init__.py
from bin.feature_registry import FeatureRegistry
from bin.feature_io import load_features_from_file
from bin.spell_registry import SpellRegistry
from bin.spell_io import load_spells_from_file
from bin.race_registry import RaceRegistry
from bin.race_io import load_races_from_file
from bin.class_level_registry import ClassLevelRegistry
from bin.class_level_io import load_class_levels_from_file
from bin.class_registry import ClassRegistry
from bin.character_registry import CharacterRegistry
from bin.character_io import load_characters_from_file


def init_registries():
    """Initialize and load all registries."""
    # === FeatureRegistry ===
    features = load_features_from_file()
    FeatureRegistry.load_bulk(features)

    # === SpellRegistry ===
    spells = load_spells_from_file()
    SpellRegistry.load_bulk(spells)

    # === RaceRegistry ===
    races = load_races_from_file(registries={"features": FeatureRegistry, "spells": SpellRegistry})
    RaceRegistry.load_bulk(races)

    # === ClassLevelRegistry ===
    cl = load_class_levels_from_file(registries={"features": FeatureRegistry, 
                                                 "spells": SpellRegistry})
    ClassLevelRegistry.load_bulk(cl)

    # === ClassRegistry ===
    ClassRegistry.register_defaults()

    # === Characters ===
    chars = load_characters_from_file(registries={"features": FeatureRegistry, 
                                                  "spells": SpellRegistry,
                                                  "classes": ClassRegistry})
    CharacterRegistry.load_bulk(chars)


# Re-export for consistency across the app
__all__ = [
    "FeatureRegistry",
    "SpellRegistry",
    "RaceRegistry",
    "ClassLevelRegistry",
    "ClassRegistry",
    "CharacterRegistry",
]