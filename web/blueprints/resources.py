from flask import Blueprint, render_template, jsonify

from config import ROOT

from registries import FeatureRegistry, SpellRegistry, RaceRegistry
from bin.feature_types import FeatureType

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
    for _, race in RaceRegistry.all().items():
        race_list.append(race.to_dict())
    return jsonify({"race_list": race_list})