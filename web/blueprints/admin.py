# blueprints/admin.py
import subprocess
from flask import Blueprint, request, jsonify
from config import ROOT

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
        return jsonify({
            "status": "success",
            "output": result.stdout
        })
    except subprocess.CalledProcessError as e:
        return jsonify({
            "status": "error",
            "message": e.stderr or str(e)
        }), 500
