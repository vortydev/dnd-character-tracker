# Common packages
import os
import secrets

CONTAINER_NAME = os.environ.get('CONTAINER_NAME')
VERSION = os.environ.get('APP_VERSION')

# Set the time zone to America/Toronto
os.environ['TZ'] = os.environ.get('TZ', 'UTC')

# Flask Server
secret_key = secrets.token_hex(64)
FLASK_SECRET_KEY = secret_key
FLASK_PORT = int(os.environ.get('FLASK_PORT', 8080))
LOGIN_ACTIVATED = int(os.environ.get('LOGIN_ACTIVATED', 30))    # Minutes idle before logout
ROOT = os.environ.get("API_ROOT", "")