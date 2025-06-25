from flask import Flask
from .db import init_db
from .routes import app as rutas_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(rutas_blueprint)
    init_db()
    return app