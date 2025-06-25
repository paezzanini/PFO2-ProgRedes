from flask import Flask
from .db import init_db
from .routes import app as rutas_blueprint

def create_app():
    app = Flask(__name__)
    init_db()
    app.register_blueprint(rutas_blueprint)
    return app