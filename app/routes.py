from flask import Blueprint, request, jsonify, render_template
from .auth import registrar_usuario, verificar_login

app = Blueprint("rutas", __name__)


@app.route("/registro", methods=["POST"])
def registro():
    datos = request.json
    return jsonify(*registrar_usuario(datos.get("usuario"), datos.get("contraseña")))


@app.route("/login", methods=["POST"])
def login():
    datos = request.json
    return jsonify(*verificar_login(datos.get("usuario"), datos.get("contraseña")))


@app.route("/tareas", methods=["GET"])
def tareas():
    return render_template("tareas.html")
