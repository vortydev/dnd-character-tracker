from flask import Blueprint, request, render_template, jsonify

from config import ROOT

from registries import FeatureRegistry, SpellRegistry, RaceRegistry, ClassLevelRegistry, ClassRegistry
from bin.feature_types import FeatureType
from bin.spell import Spell
from bin.class_base import ClassType
from bin.subclass_ import SubclassType

resources_bp = Blueprint('resources_bp', __name__)
root = ROOT


# ===== Helper Functions =====
def build_spells_ref(spells_ref: dict[int, list[str]], spells: dict[int, list[Spell]]):
    for _, spell_list in spells.items():
        for s in spell_list:
            if s.level not in spells_ref.keys():
                spells_ref.update({s.level: []})
            if s.name not in spells_ref[s.level]:
                spells_ref[s.level].append(s.name)


# ===== Features =====
@resources_bp.route(root+'/features', methods=['GET'])
def page_features():
    return render_template('features.html', root=root)

@resources_bp.route(root+'/api/features/get', methods=['GET'])
def api_get_features():
    base_feats = []
    race_feats = []
    class_feats = []
    subclass_feats = []

    for (_, typ, _), feat in FeatureRegistry.all().items():
        feat_dict = {
            "html": feat.get_html(),
            "name": feat.name,
            "type": typ,
            "context": feat.get_context()
        }

        if typ == FeatureType.CLASS.value:
            class_feats.append(feat_dict)
        elif typ == FeatureType.SUBCLASS.value:
            subclass_feats.append(feat_dict)
        elif typ == FeatureType.RACE.value:
            race_feats.append(feat_dict)
        else:
            base_feats.append(feat_dict)
        
    def sort_by_context(feats): return sorted(feats, key=lambda f: f["context"].lower())

    return jsonify({
        "base_feats": sort_by_context(base_feats),
        "race_feats": sort_by_context(race_feats),
        "class_feats": sort_by_context(class_feats),
        "subclass_feats": sort_by_context(subclass_feats),
    })


# ===== Spells =====
@resources_bp.route(root+'/spells', methods=['GET'])
def page_spells():
    return render_template('spells.html', root=root)

@resources_bp.route(root+'/api/spells/get', methods=['GET'])
def api_get_spells():
    spell_list: list[dict[str]] = []
    for _, spell in SpellRegistry.all().items():
        spell_list.append(spell.to_dict())
    return jsonify({"spell_list": spell_list})


# ===== Races =====
@resources_bp.route(root+'/races', methods=['GET'])
def page_races():
    return render_template('races.html', root=root)

@resources_bp.route(root+'/api/races/get', methods=['GET'])
def api_get_races():
    race_list: list[dict[str]] = []
    spells_ref: dict[int, list[str]] = {}

    # Load the list of races
    for _, race in RaceRegistry.all().items():
        race_list.append(race.to_dict())
        build_spells_ref(spells_ref, race.spells)
        if race.subrace:
            build_spells_ref(spells_ref, race.subrace.spells)

    return jsonify({"race_list": race_list, "spells_ref": spells_ref})

@resources_bp.route(root + '/api/races/summary', methods=['GET'])
def api_get_race_summaries():
    """
    Return a simplified list of race names and their subraces.
    """
    summaries = []

    for _, race in RaceRegistry.all().items():
        summaries.append({
            "name": race.name.value,
            "subraces": [race.subrace.name] if race.subrace else []
        })

    return jsonify({"races": summaries})



# ===== Classes =====
@resources_bp.route(root+'/classes', methods=['GET'])
def page_classes():
    return render_template('classes.html', root=root)

@resources_bp.route(root+'/api/classes/get', methods=['GET'])
def api_get_classes():
    class_list: list[dict] = []
    level_list: list[dict] = []

    # === Fetch base class definitions ===
    for _, c in ClassRegistry.all().items():
        class_list.append(c.to_dict())

    # === Fetch all class/subclass levels ===
    for (_, _, _), cl in ClassLevelRegistry.all().items():
        level_list.append(cl.to_dict())

    return jsonify({
        "class_list": class_list,
        "level_list": level_list
    })

@resources_bp.route(root + '/api/classes/features/<class_name>', methods=['GET'])
def get_class_full_features(class_name: str):
    """Return class base info (HP, proficiencies) and level-based features/spells up to given level."""
    # from registries import ClassLevelRegistry, ClassRegistry

    try:
        subclass = request.args.get("subclass")
        level = int(request.args.get("level", 1))

        try:
            class_type = ClassType(class_name)
        except ValueError:
            return jsonify({"status": "error", "message": f"Invalid class name: {class_name}"}), 400

        subclass_type = SubclassType(subclass) if subclass else None
        base = ClassRegistry.get(class_type)
        levels = ClassLevelRegistry.get(class_type, level, subclass_type)
        print(levels)

        if not base:
            return jsonify({"status": "error", "message": "Class not found"}), 404

        # Filter and flatten features/spells
        features = []
        spells = []
        for entry in levels:
            if entry.get("level") <= level and entry.get("type") == "Base":
                features += [{"name": f, "level": entry["level"]} for f in entry.get("features", [])]
                spells += [{"name": s, "level": entry["level"]} for s in entry.get("spells", [])]

        return jsonify({
            "status": "success",
            "class_name": class_name,
            "level": level,
            "hit_points": {
                "dice": base.hit_dice,
                "per_level": base.fixed_hp_per_level,
                "at_1st_level": base.hp_1st_level,
                "ability_mod": base.hp_ability_mod.value
            },
            "proficiencies": {
                "armor": [a.value for a in base.proficiency_armor],
                "weapons": [w.value for w in base.proficiency_weapons],
                "tools": [t.to_dict() for t in base.proficiency_tools],  # if ToolItem is a custom class
                "saving_throws": [s.value for s in base.proficiency_saving_throws],
                "specific_weapons": [w.value for w in base.proficiency_specific_weapons],
                "skill_pool": [s.value for s in base.proficiency_skill_pool],
                "skill_choices": base.skill_choices
            },
            "features": features,
            "spells": spells,
            "requisite": base.requisite
        })

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"status": "error", "message": str(e)}), 400
