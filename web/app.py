# app.py
import sys, os
from flask import Flask

# App
from config import VERSION
from blueprints.main import main_bp
from blueprints.resources import resources_bp

# Add the parent folder (char_tracker/) to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# Flask app initialization
app = Flask(__name__)

from registries import init_registries
init_registries()

# Register blueprints
app.register_blueprint(main_bp)
app.register_blueprint(resources_bp)


@app.context_processor
def inject_app_context():
    """Insert session lifetime into the app context"""
    return {
        "app_version": VERSION,
        # "session_lifetime": app.config['PERMANENT_SESSION_LIFETIME'].total_seconds()
    }


if __name__ == '__main__':
    print(app.url_map) # DEBUG

    with app.app_context():
        # Start Flask app
        app.run(
            host="0.0.0.0",
            port=os.environ.get("FLASK_PORT"),
            threaded=True, 
            debug=True,
            use_evalex=False
        )