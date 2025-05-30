# characters.py
from flask import Blueprint, render_template, jsonify

from config import ROOT

from registries import FeatureRegistry, SpellRegistry, RaceRegistry, ClassLevelRegistry, ClassRegistry
from bin.feature_types import FeatureType
from bin.spell import Spell

characters_bp = Blueprint('characters_bp', __name__)
root = ROOT

@characters_bp.route(root+'/characters', methods=['GET'])
def page_characters():
    return render_template('characters.html', root=root)