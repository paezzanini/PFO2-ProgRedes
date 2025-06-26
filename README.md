
# PFO 2: Sistema de Gestión de Tareas (API Flask + SQLite)

Este proyecto implementa una API REST básica con Flask para registrar usuarios, iniciar sesión y mostrar una vista de tareas protegida. Incluye autenticación básica y almacenamiento de usuarios con contraseñas hasheadas usando SQLite.

---

## Funcionalidades del servidor

- Registro de usuarios (`POST /registro`)
- Inicio de sesión (`POST /login`)
- Visualización de bienvenida (`GET /tareas`)
- Contraseñas protegidas (hashed)
- Base de datos persistente (SQLite)

---

## Funcionalidades del cliente

- Iniciar sesión con usuario y contraseña (`POST /login`)
- Registrarse si el login falla (`POST /registro`)
- Ver tareas si el login fue exitoso (`GET /tareas`)

---

## Backlog de funcionalidades pendientes

- [X] Reorganizar la estructura del proyecto con carpetas (ej. `/app`)
- [X] Agregar confirmación de contraseña en el registro (validación mínima)
- [X] Mostrar una página HTML más personalizada en `/tareas` (usuario logueado)
- [ ] Agregar pruebas básicas con `curl` o `requests` para validar endpoints
- [ ] Documentar el uso del cliente en consola
- [ ] Revisar flujo en Error en el login: Credenciales inválidas


---

## Instalación y ejecución (Windows)

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/pfo2-gestion-tareas.git
cd pfo2-gestion-tareas
```

### 2. Crear entorno virtual (opcional pero recomendado)
```bash
python -m venv env
env\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar el servidor Flask
```bash
python servidor.py
```

### 5. Ejecutar el cliente en consola en otra consola
```bash
python cliente.py
```

#### Ejemplo de Uso

##### Usuario no registrado no deseo registrarme


##### Usuario no registrado deseo registrarme
Usuario: (vacio)
Contraseña: (vacio)

❌ Error en el login. ¿Deseás registrarte?
s/n: s
✅ Usuario registrado con éxito. Ahora podés iniciar sesión.

Se ejecuta nuevamente el cliente y ya permite loguearse con los datos de registro

##### Usuario no registrado confirmacion de pass erronea
ea

##### Usuario no registrado confirmacion de pass correcta

##### Usuario registrado - credenciales invalidas

##### Usuario registrado - login exitoso




## Capturas de pantalla

Falta Agregar
- Registro exitoso
- Login correcto/incorrecto
- Vista de bienvenida tras logueo

---

## Requisitos técnicos

- Python 3.8 o superior
- Flask
- SQLite3
- Werkzeug (para hashing de contraseñas)

---

## Respuestas conceptuales

### ¿Por qué hashear contraseñas?

Hashear contraseñas significa aplicar una función matemática que transforma la contraseña original en una cadena irreconocible. Es un proceso que no se puede revertir fácilmente, por eso se dice que es unidireccional.

Esto se hace para no guardar contraseñas en texto plano (es decir, tal como las escribe el usuario). Si alguien llegara a robar la base de datos, no podría ver directamente las contraseñas reales, porque solo tendría los valores ya hasheados.

Además, muchas veces se le agrega una “sal” (un valor aleatorio) antes de aplicar el hash, para hacer más difícil que alguien use ataques automáticos para adivinar las contraseñas.

En resumen, hashear sirve para proteger los datos de los usuarios y evitar que, si alguien accede a la base, pueda ver las contraseñas reales.

### Ventajas de usar SQLite

SQLite es una base de datos liviana que no necesita instalar un servidor aparte ni configuraciones complicadas. Todo se guarda en un solo archivo .db, lo que la hace muy práctica para proyectos chicos o medianos como este.

Una de las ventajas más grandes es que es fácil de usar y muy rápida para desarrollos locales o aplicaciones que no van a tener miles de usuarios al mismo tiempo.

También es ideal para practicar o hacer trabajos prácticos, porque no depende de conexiones externas ni servicios adicionales. Basta con importar la librería en Python y ya se puede empezar a guardar datos.

En resumen, SQLite es simple, funciona bien para este tipo de proyectos educativos o personales, y permite centrarse en la lógica del programa sin preocuparse por configurar un sistema de base de datos más complejo.

---
