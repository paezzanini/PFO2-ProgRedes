import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def registrar_usuario(usuario, contrasena):
    if not usuario and not contrasena:
        return {'error': 'Faltan datos'}, 400

    hash_contra = generate_password_hash(contrasena)

    try:
        conn = sqlite3.connect('tareas.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO usuarios (usuario, contrasena) VALUES (?, ?)', (usuario, hash_contra))
        conn.commit()
        conn.close()
        return {'mensaje': 'Usuario registrado correctamente'}, 201
    except sqlite3.IntegrityError:
        return {'error': 'El usuario ya existe'}, 409

def verificar_login(usuario, contrasena):
    if not usuario or not contrasena:
        return {'error': 'Faltan datos'}, 400

    conn = sqlite3.connect('tareas.db')
    cursor = conn.cursor()
    cursor.execute('SELECT contrasena FROM usuarios WHERE usuario = ?', (usuario,))
    resultado = cursor.fetchone()
    conn.close()

    if not resultado:
        return {'error': 'El usuario no existe'}, 404

    if check_password_hash(resultado[0], contrasena):
        return {'mensaje': 'Inicio de sesión exitoso'}, 200
    else:
        return {'error': 'Credenciales inválidas'}, 401