# characters.py
from flask import Blueprint, render_template, jsonify, request, redirect
from config import ROOT, CHAR_EDITOR_ENABLED
from registries import CharacterRegistry, RaceRegistry
from bin.character import Character

characters_bp = Blueprint('characters_bp', __name__, url_prefix=ROOT)
# TODO Add semaphore and security

@characters_bp.route(ROOT+'/characters', methods=['GET'])
def page_characters():
    if not CHAR_EDITOR_ENABLED:
        redirect(ROOT+'/index')
    return render_template('characters.html', root=ROOT)


@characters_bp.route(ROOT+'/api/characters/get', methods=['GET'])
def get_all_characters():
    """
    Return all characters from the CharacterRegistry.
    """
    characters = CharacterRegistry.all().values()
    return jsonify({"characters": [char.to_dict() for char in characters]})


@characters_bp.route(ROOT+'/api/characters/<name>', methods=['GET'])
def get_character(name: str):
    try:
        char = CharacterRegistry.get(name)
        return jsonify(char.to_dict())
    except KeyError:
        return jsonify({"error": f"Character '{name}' not found."}), 404
    

@characters_bp.route(ROOT+'/api/characters/save', methods=['POST'])
def save_character():
    data = request.get_json()
    try:
        char = Character.from_dict(data, registries={"races": RaceRegistry})
        CharacterRegistry.register(char, overwrite=True)
        CharacterRegistry.save_to_file()
        return jsonify({"status": "success", "message": f"Character '{char.name}' saved."})
    
    except KeyError as ke:
        return jsonify({"status": "error", "message": f"Missing key: {ke}"}), 400
    
    except ValueError as ve:
        return jsonify({"status": "error", "message": f"Value error: {ve}"}), 400
    
    except TypeError as te:
        return jsonify({"status": "error", "message": f"Type error: {te}"}), 400
    
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"status": "error", "message": f"Unhandled error: {str(e)}"}), 400


@characters_bp.route(ROOT+'/api/characters/delete/<name>', methods=['DELETE'])
def delete_character(name):
    try:
        CharacterRegistry.delete(name, archive=True)
        return jsonify({"status": "success", "message": f"Character '{name}' archived."})
    except KeyError:
        return jsonify({"status": "error", "message": f"Character '{name}' not found."}), 404
    

# === Editor ===
@characters_bp.route(ROOT+'/characters/editor', methods=['GET'])
def page_character_editor():
    if not CHAR_EDITOR_ENABLED:
        redirect(ROOT+'/index')
    return render_template('character_editor.html', root=ROOT)


@characters_bp.route(ROOT+'/api/characters/check-name/<name>', methods=['GET'])
def check_character_name(name: str):
    """
    Check if a character with the given name already exists.
    """
    exists = CharacterRegistry.exists(name)
    return jsonify({"exists": exists})

# WIP
@characters_bp.route(ROOT+'/characters/sheet', methods=['GET'])
def page_character_sheet():
    return render_template('character_sheet.html', root=ROOT)