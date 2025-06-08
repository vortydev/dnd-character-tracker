# blueprints/admin.py
import subprocess
from flask import Blueprint, request, jsonify
from config import ROOT

from registries import FeatureRegistry, SpellRegistry, RaceRegistry, ClassLevelRegistry, ClassRegistry
from bin.feature_io import load_features_from_file
from bin.spell_io import load_spells_from_file
from bin.race_io import load_races_from_file
from bin.class_level_io import load_class_levels_from_file


root = ROOT
admin_bp = Blueprint("admin", __name__)


# === Routes ===
@admin_bp.route(root+"/admin/run-builder", methods=["POST"])
def run_builder():
    data = request.get_json()
    script_name = data.get("script")

    if not script_name or not script_name.startswith("build_") or not script_name.endswith(".py"):
        return jsonify({"status": "error", "message": "Invalid script name."}), 400

    script_path = f"/app/bin/builders/{script_name}"

    try:
        result = subprocess.run(["python", script_path], capture_output=True, text=True, check=True)

        # Reload corresponding registry
        reload_registry(script_name)

        return jsonify({
            "status": "success",
            "output": result.stdout
        })
    
    except subprocess.CalledProcessError as e:
        return jsonify({
            "status": "error",
            "message": e.stderr or str(e)
        }), 500

def reload_registry(script_name: str):
    registries = {
        "features": FeatureRegistry, 
        "spells": SpellRegistry
    }

    if script_name == "build_features.py":
        FeatureRegistry.load_bulk(load_features_from_file())
    elif script_name == "build_spells.py":
        SpellRegistry.load_bulk(load_spells_from_file())
    elif script_name == "build_races.py":
        RaceRegistry.load_bulk(load_races_from_file(registries=registries))
    elif script_name == "build_class_levels.py":
        ClassLevelRegistry.load_bulk(load_class_levels_from_file(registries=registries))
    elif script_name == "build_classes.py":
        ClassRegistry.register_defaults()
