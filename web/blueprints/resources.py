from flask import Blueprint, render_template, jsonify

from config import ROOT

from registries import FeatureRegistry, SpellRegistry, RaceRegistry, ClassLevelRegistry, ClassRegistry
from bin.feature_types import FeatureType
from bin.spell import Spell

resources_bp = Blueprint('resources_bp', __name__)
root = ROOT

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


def build_spells_ref(spells_ref: dict[int, list[str]], spells: dict[int, list[Spell]]):
    for _, spell_list in spells.items():
        for s in spell_list:
            if s.level not in spells_ref.keys():
                spells_ref.update({s.level: []})
            if s.name not in spells_ref[s.level]:
                spells_ref[s.level].append(s.name)


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
    for (_, _), cl in ClassLevelRegistry.all().items():
        level_list.append(cl.to_dict())

    return jsonify({
        "class_list": class_list,
        "level_list": level_list
    })