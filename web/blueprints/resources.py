from flask import Blueprint, request, render_template, jsonify
from config import ROOT
from registries import FeatureRegistry, SpellRegistry, RaceRegistry, ClassLevelRegistry, ClassRegistry
from bin import ClassType, SubclassType, Spell, FeatureType

resources_bp = Blueprint('resources_bp', __name__)


# ===== Helper Functions =====
def build_spells_ref(spells_ref: dict[int, list[str]], spells: dict[int, list[Spell]]):
    for _, spell_list in spells.items():
        for s in spell_list:
            if s.level not in spells_ref.keys():
                spells_ref.update({s.level: []})
            if s.name not in spells_ref[s.level]:
                spells_ref[s.level].append(s.name)


# ===== Features =====
@resources_bp.route(ROOT+'/features', methods=['GET'])
def page_features():
    return render_template('features.html', ROOT=ROOT)

@resources_bp.route(ROOT+'/api/features/get', methods=['GET'])
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
@resources_bp.route(ROOT+'/spells', methods=['GET'])
def page_spells():
    return render_template('spells.html', ROOT=ROOT)

@resources_bp.route(ROOT+'/api/spells/get', methods=['GET'])
def api_get_spells():
    spell_list: list[dict[str]] = []
    for _, spell in SpellRegistry.all().items():
        spell_list.append(spell.to_dict())
    return jsonify({"spell_list": spell_list})


# ===== Races =====
@resources_bp.route(ROOT+'/races', methods=['GET'])
def page_races():
    return render_template('races.html', ROOT=ROOT)

@resources_bp.route(ROOT+'/api/races/get', methods=['GET'])
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

@resources_bp.route(ROOT+'/api/races/summary', methods=['GET'])
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
@resources_bp.route(ROOT+'/classes', methods=['GET'])
def page_classes():
    return render_template('classes.html', ROOT=ROOT)

@resources_bp.route(ROOT+'/api/classes/get', methods=['GET'])
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

@resources_bp.route(ROOT + '/api/classes/features/<class_name>', methods=['GET'])
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
        print("CLRegistry params:", class_type, level, subclass_type)
        levels = ClassLevelRegistry.get(class_type, level, subclass_type)
        print(l.to_dict() for l in levels)

        if not base:
            return jsonify({"status": "error", "message": "Class not found"}), 404

        # WIP Filter and flatten features/spells
        features = []
        spells = []
        for l in levels:
            if l.level <= level:
                features += [{"name": f.name, "level": l.level, "data": f.to_dict()} for f in l.features]
                # spells += [{"name": s, "level": entry["level"]} for s in entry.get("spells", [])]

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
            "features": sorted(features, key=lambda f: f["level"]),
            # "spells": spells,
            "requisite": base.requisite
        })

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"status": "error", "message": str(e)}), 400


@resources_bp.route(ROOT+"/api/races/features/<race_name>", methods=["GET"])
def get_race_features(race_name: str):
    from registries import RaceRegistry
    from bin import RaceType

    try:
        subrace_name = request.args.get("subrace", None)

        # === Validate and fetch Race ===
        try:
            race_type = RaceType(race_name)
        except ValueError:
            return jsonify({"status": "error", "message": f"Invalid race name: {race_name}"}), 400

        race = RaceRegistry.get(race_type)
        if not race:
            return jsonify({"status": "error", "message": f"Race not found: {race_name}"}), 404
        
        subrace = RaceRegistry.get(race_type, subrace_name) if subrace_name else None
        if subrace_name and not subrace:
            return jsonify({"status": "error", "message": f"Race+subrace not found: {race_name}"}), 404
        
        # === Name ===
        race_name = race.name.value.strip()
        subrace_name = None
        if subrace:
            subrace_name = subrace.subrace.name.strip() or ""

        # === Build description ===
        description = race.description.strip() or ""
        subrace_description = None
        if subrace:
            subrace_description = subrace.subrace.description.strip() or ""

        features: dict[str, list[dict[str, str]]] = {"race": []}
        seen_feats = set()

        # === Pass 1: Base race features ===
        for level, feat_list in race.feats.items():
            for f in feat_list:
                if f.name not in seen_feats:
                    features["race"].append({
                        "name": f.name,
                        "description": f.description
                    })
                    seen_feats.add(f.name)

        # === Pass 2: Subrace features (if valid match) ===
        if subrace:
            features.update({"subrace": []})
            for level, feat_list in subrace.feats.items():
                for f in feat_list:
                    if f.name not in seen_feats:
                        features["subrace"].append({
                            "name": f.name,
                            "description": f.description
                        })
                        seen_feats.add(f.name)

        # === Languages ===
        languages: list[str] = []
        seen_langs = set()

        for lang in race.languages:
            if lang.value not in seen_langs:
                languages.append(lang.value)
                seen_langs.add(lang.value)

        if subrace:
            for lang in subrace.subrace.languages:
                if lang.value not in seen_langs:
                    languages.append(lang.value)
                    seen_langs.add(lang.value)

        # === ASI ===
        asi = {}
        for a, s in race.ability_score_increase.items():
            asi[a.value] = s

        if subrace:
            for a, s in subrace.subrace.ability_score_increase.items():
                asi[a.value] = s

        # WIP === Info ===
        age_key = "Age"
        alignment_key = "Alignment"
        info = {
            "age": race.info.get(age_key),
            "alignment": race.info.get(alignment_key),
            "speed": race.speed,
            "size": race.size.value,
        }

        # TODO Spells

        return jsonify({
            "status": "success",
            "name": race_name,
            "sr_name": subrace_name,
            "description": description,
            "sr_description": subrace_description,
            "features": features,
            "languages": languages,
            "asi": asi,
            "info": info
        })

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"status": "error", "message": str(e)}), 400

    

# === Books ===
import os, json

@resources_bp.route(ROOT+"/library")
def book_index():
    pdf_dir = os.path.join("static", "pdf")
    # pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith(".pdf")]
    # print(pdf_files)

    json_path = os.path.join(pdf_dir, "pdf_index.json")
    with open(json_path, "r", encoding="utf-8") as f:
        pdf_files: list[dict] = json.load(f)

    for pdf in pdf_files:
        # Add full static-relative path to each PDF
        pdf["filepath"] = os.path.join("static", "pdf", pdf["filename"])

    return render_template("pdf_list.html", ROOT=ROOT, pdfs=pdf_files)