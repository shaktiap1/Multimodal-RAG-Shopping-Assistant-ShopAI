import os
from flask import Flask
from flask_cors import CORS
from pathlib import Path
from .routes import register_routes

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Load default config or environment variables
    app.config["UPLOAD_FOLDER"] = os.environ.get("UPLOAD_FOLDER", "/tmp")

    # Automatically register all blueprints in app/routes
    register_routes(app)
    return app
