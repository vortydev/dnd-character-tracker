# app.py
import sys, os
from flask import Flask, render_template, jsonify

# Add the parent folder (char_tracker/) to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bin.feature_registry import FeatureRegistry
from bin.feature_io import load_features_from_file
from bin.feature_types import FeatureType
from bin.feature import Feature
from bin.race_feature import RaceFeature
from bin.class_feature import ClassFeature, SubclassFeature

# Flask app initialization
app = Flask(__name__)

# Load once at app start
FeatureRegistry.load_bulk(load_features_from_file())


@app.route('/features', methods=['GET'])
def page_features():
    return render_template('features.html')


@app.route('/api/features/get', methods=['GET'])
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


if __name__ == '__main__':
    with app.app_context():
        # Start Flask app
        app.run(
            host="0.0.0.0",
            port=os.environ.get("FLASK_PORT"),
            threaded=True, 
            debug=True,
            use_evalex=False
        )