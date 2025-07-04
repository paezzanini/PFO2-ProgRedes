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
    respuesta, status = verificar_login(datos.get("usuario"), datos.get("contraseña"))
    return jsonify(respuesta), status


@app.route("/tareas", methods=["GET"])
def tareas():
    usuario = request.args.get("usuario", "usuario anónimo")
    return render_template("tareas.html", usuario=usuario)
