
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)

# Inicialización de la base de datos
def init_db():
    conn = sqlite3.connect('tareas.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE NOT NULL,
            contrasena TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Registro de usuario
@app.route('/registro', methods=['POST'])
def registro():
    datos = request.json
    usuario = datos.get('usuario')
    contrasena = datos.get('contraseña')

    if not usuario or not contrasena:
        return jsonify({'error': 'Faltan datos'}), 400

    hash_contra = generate_password_hash(contrasena)

    try:
        conn = sqlite3.connect('tareas.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO usuarios (usuario, contrasena) VALUES (?, ?)', (usuario, hash_contra))
        conn.commit()
        conn.close()
        return jsonify({'mensaje': 'Usuario registrado correctamente'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'El usuario ya existe'}), 409

# Login de usuario
@app.route('/login', methods=['POST'])
def login():
    datos = request.json
    usuario = datos.get('usuario')
    contrasena = datos.get('contraseña')

    conn = sqlite3.connect('tareas.db')
    cursor = conn.cursor()
    cursor.execute('SELECT contrasena FROM usuarios WHERE usuario = ?', (usuario,))
    resultado = cursor.fetchone()
    conn.close()

    if resultado and check_password_hash(resultado[0], contrasena):
        return jsonify({'mensaje': 'Inicio de sesión exitoso'})
    else:
        return jsonify({'error': 'Credenciales inválidas'}), 401

# Endpoint de bienvenida
@app.route('/tareas', methods=['GET'])
def tareas():
    return '''
    <html>
        <body>
            <h1>Bienvenido al sistema de gestión de tareas</h1>
        </body>
    </html>
    '''

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
