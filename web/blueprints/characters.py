# characters.py
from flask import Blueprint, render_template, jsonify, request
from config import ROOT
from registries import CharacterRegistry
from bin.character import Character

characters_bp = Blueprint('characters_bp', __name__)
root = ROOT


@characters_bp.route(root+'/characters', methods=['GET'])
def page_characters():
    return render_template('characters.html', root=root)


@characters_bp.route(root+'/api/characters/get', methods=['GET'])
def get_all_characters():
    """
    Return all characters from the CharacterRegistry.
    """
    characters = CharacterRegistry.all().values()
    return jsonify({"characters": [char.to_dict() for char in characters]})


@characters_bp.route(root + '/api/characters/<name>', methods=['GET'])
def get_character(name: str):
    try:
        char = CharacterRegistry.get(name)
        return jsonify(char.to_dict())
    except KeyError:
        return jsonify({"error": f"Character '{name}' not found."}), 404
    

@characters_bp.route(root + '/api/characters/save', methods=['POST'])
def save_character():
    data = request.get_json()
    try:
        char = Character.from_dict(data)
        CharacterRegistry.register(char, overwrite=True)
        return jsonify({"status": "success", "message": f"Character '{char.name}' saved."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400


@characters_bp.route(root + '/api/characters/delete/<name>', methods=['DELETE'])
def delete_character(name):
    try:
        CharacterRegistry.delete(name, archive=True)
        return jsonify({"status": "success", "message": f"Character '{name}' archived."})
    except KeyError:
        return jsonify({"status": "error", "message": f"Character '{name}' not found."}), 404