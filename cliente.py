import requests

API_URL = "http://localhost:5000"



def login():
    usuario = input("Usuario: ")
    intentos = 0
    while intentos < 3:
        contraseña = input("Contraseña: ")
        respuesta = requests.post(
            f"{API_URL}/login", json={"usuario": usuario, "contraseña": contraseña}
        )

        if respuesta.status_code == 200:
            print("\n✅ ¡Login exitoso!")
            mostrar_tareas(usuario)
            return
        elif respuesta.status_code == 401:
            print("❌ Contraseña incorrecta.")
            intentos += 1
            if intentos < 3:
                print(f"Intento {intentos}/3. Intente nuevamente.\n")
            else:
                print("❌ Demasiados intentos fallidos. Cerrando.")
                return
        elif respuesta.status_code == 404:
            print("❌ El usuario no existe.")
            if input("¿Deseás registrarte? (s/n): ").lower() == "s":
                registrar_usuario(usuario, contraseña)
            return
        else:
            print(
                "\n❌ Error en el login:",
                respuesta.json().get("error", "Error desconocido"),
            )


def registrar_usuario(usuario=None, contraseña=None):
    if not usuario:
        usuario = input("Nuevo usuario: ")
    if not contraseña:
        contraseña = input("Nueva contraseña: ")

    confirmacion = input("Confirmá la contraseña: ")

    if contraseña != confirmacion:
        print("❌ Las contraseñas no coinciden.")
        return

    respuesta = requests.post(
        f"{API_URL}/registro", json={"usuario": usuario, "contraseña": contraseña}
    )

    if respuesta.status_code in [200, 201]:
        print("✅ Usuario registrado con éxito. Ahora podés iniciar sesión.")
    else:
        print("❌ No se pudo registrar:", respuesta.json().get("error", respuesta.text))


def mostrar_tareas(usuario=None):
    params = {"usuario": usuario} if usuario else {}
    respuesta = requests.get(f"{API_URL}/tareas", params=params)

    if respuesta.status_code == 200:
        print("\nTAREAS:")
        print(respuesta.text)
    else:
        print("❌ No se pudieron obtener las tareas.")


if __name__ == "__main__":
    login()
