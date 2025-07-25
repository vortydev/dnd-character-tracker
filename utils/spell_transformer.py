# utils/spell_transformer.py
from bin.spell import Spell, SpellSchool, SpellComponent, SpellTag
from bin.common import ActionCost, Source
from bin.class_base import ClassType

def transform_api_spell(api_spell: dict) -> Spell:
    """Convert an API spell dict into your custom Spell object."""
    school_map = {
        "abjuration": SpellSchool.ABJURATION,
        "conjuration": SpellSchool.CONJURATION,
        "divination": SpellSchool.DIVINATION,
        "enchantment": SpellSchool.ENCHANTMENT,
        "evocation": SpellSchool.EVOCATION,
        "illusion": SpellSchool.ILLUSION,
        "necromancy": SpellSchool.NECROMANCY,
        "transmutation": SpellSchool.TRANSMUTATION
    }

    raw_school = api_spell.get("school", "").strip().lower()
    school = school_map.get(raw_school, SpellSchool.UNKNOWN)

    components = []
    for comp in api_spell.get("components", "").upper():
        try:
            components.append(SpellComponent(comp))
        except ValueError:
            pass

    tags = [SpellTag.RITUAL] if api_spell.get("ritual") == "yes" else []

    spell_lists = []
    for cls in api_spell.get("dnd_class", "").split(","):
        cls_clean = cls.strip().lower().capitalize()
        if cls_clean in ClassType.__members__:
            spell_lists.append(ClassType[cls_clean])

    return Spell(
        name=api_spell["name"],
        level=parse_level(api_spell["level"]),
        school=school,
        action_cost=ActionCost.ACTION,  # Default/fallback for now
        description=api_spell["desc"],
        higher_levels=api_spell.get("higher_level"),
        duration=api_spell.get("duration"),
        casting_time=api_spell.get("casting_time"),
        s_range=api_spell.get("range"),
        components=components,
        material_description=[api_spell["material"]] if api_spell.get("material") else [],
        tags=tags,
        source=Source.PHB,  # All open5e spells are from SRD/PHB
        spell_lists=spell_lists
    )


def parse_level(value: str) -> int:
    """Extracts the numeric level from strings like '4th-level', 'Cantrip', etc."""
    value = value.lower().strip()
    if value == "cantrip":
        return 0
    if value[0].isdigit():
        return int(value[0])  # Assumes only 1–9-level
    raise ValueError(f"Unrecognized level format: {value}")
