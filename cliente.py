import requests

API_URL = "http://localhost:5000"

def login():
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    respuesta = requests.post(f"{API_URL}/login", json={
        "usuario": usuario,
        "contraseña": contraseña
    })

    if respuesta.status_code == 200:
        print("\n✅ ¡Login exitoso!")
        mostrar_tareas()
    else:
        print("\n❌ Error en el login:", respuesta.json().get("error", "Error desconocido"))
        if input("¿Deseás registrarte? (s/n): ").lower() == "s":
            registrar_usuario(usuario, contraseña)

def registrar_usuario(usuario=None, contraseña=None):
    if not usuario:
        usuario = input("Nuevo usuario: ")
    if not contraseña:
        contraseña = input("Nueva contraseña: ")

    respuesta = requests.post(f"{API_URL}/registro", json={
        "usuario": usuario,
        "contraseña": contraseña
    })

    if respuesta.status_code in [200, 201]:
        print("✅ Usuario registrado con éxito. Ahora podés iniciar sesión.")
    else:
        print("❌ No se pudo registrar:", respuesta.json().get("error", respuesta.text))

def mostrar_tareas():
    respuesta = requests.get(f"{API_URL}/tareas")
    if respuesta.status_code == 200:
        print("\n📋 TAREAS:")
        print(respuesta.text)
    else:
        print("❌ No se pudieron obtener las tareas.")

if __name__ == "__main__":
    login()