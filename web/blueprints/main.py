# Common packages
from threading import Semaphore

# Flask packages
from flask import Blueprint, jsonify, render_template, redirect, send_from_directory, session

from config import ROOT


# Blueprint setup
main_bp = Blueprint('main_bp', __name__)


#%% Assets (static files)
@main_bp.route(ROOT+'/static/<path:path>')
def send_static(path):
    print(path)
    return send_from_directory('static', path)

@main_bp.route(ROOT+'/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)

@main_bp.route(ROOT+'/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)

@main_bp.route(ROOT+'/img/<path:path>')
def send_img(path):
    return send_from_directory('static/img', path)

@main_bp.route(ROOT+'/bs/<path:path>')
def send_bootstrap(path):
    return send_from_directory('static/bootstrap5', path)

@main_bp.route(ROOT+'/fa/<path:path>')
def send_fontawesome(path):
    return send_from_directory('static/fontawesome6', path)
#%%


# ===== Routes =====
@main_bp.route(ROOT+"/")
def redirect_index():
    """Redirects to the main menu."""
    return redirect(ROOT+'/index')


@main_bp.route(ROOT+"/index", methods=["GET"])
def index():
    """Renders the landing page"""
    return render_template("index.html", ROOT=ROOT)