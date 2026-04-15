# 🐾 PySide Mascotas - Sistema de Adopción

![Versión](https://img.shields.io/badge/PySide6-v6.x-green)
![Python](https://img.shields.io/badge/Python-3.13-blue)
![Database](https://img.shields.io/badge/MySQL-8.0-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

**PySide Mascotas** es una aplicación de escritorio profesional desarrollada con **Python** y **PySide6**. El sistema permite gestionar el catálogo de mascotas de un refugio digital mediante un CRUD completo, utilizando un diseño moderno en **Modo Oscuro** y una arquitectura escalable por capas.

---

## ✨ Características Principales
* **Interfaz Moderna:** Implementación de **QDarkStyle** para una experiencia visual "Dark Mode" nativa.
* **Arquitectura Profesional:** Separación de responsabilidades en Capas (Vistas, Servicios, Modelos).
* **Persistencia Robusta:** Uso de **SQLAlchemy (ORM)** para interactuar con MySQL.
* **Control de Versiones de BD:** Gestión de esquema mediante migraciones con **Alembic**.
* **Diseño Adaptable:** Ventanas con Layouts dinámicos que se ajustan a cualquier resolución (1280x720 base).

## 🛠️ Stack Tecnológico
* **GUI:** PySide6 (Qt for Python)
* **Estilo:** QDarkStyle
* **ORM:** SQLAlchemy
* **Migraciones:** Alembic
* **Base de Datos:** MySQL
* **Entorno:** Python 3.13 + Dotenv para variables de entorno

---

## 📁 Estructura del Proyecto
```text
pyside_mascotas/
├── models/          # Modelos de SQLAlchemy (Tablas)
│   └── mascota.py
├── services/        # Lógica de negocio y consultas a BD
│   └── mascota_service.py
├── views/           # Interfaz de usuario (Widgets y Ventanas)
│   ├── home_view.py
│   └── form_view.py
├── alembic/         # Historial de migraciones
├── app.py           # Punto de entrada de la aplicación
├── database.py      # Configuración de conexión y motor
├── migrate.py       # Script de automatización de migraciones
└── .env             # Variables de entorno (Configuración local)
```
## 🚀 Instalación y Configuración
1. Clonar el repositorio
```Bash
git clone [https://github.com/Valduz-Jose/pyside_mascotas.git](https://github.com/Valduz-Jose/pyside_mascotas.git)
cd pyside_mascotas
```
2. Crear y activar entorno virtual
```Bash
python -m venv .venv1
# En Windows:
.venv1\Scripts\activate
```
3. Instalar dependencias
```Bash
pip install PySide6 qdarkstyle SQLAlchemy Alembic python-dotenv PyMySQL cryptography
```
4. Configurar Base de Datos
Crea un archivo .env en la raíz del proyecto con tus credenciales (asegúrate de tener MySQL corriendo):

```Fragmento de código
DB_USER=tu_usuario
DB_PASS=tu_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=pyside_mascotas_db
```
5. Ejecutar Migraciones
Este paso creará automáticamente la tabla mascotas en tu base de datos:

```Bash
python migrate.py
```
6. Iniciar la aplicación
```Bash
python app.py
```

## 📸 Funcionalidades
* **Dashboard Principal: Listado dinámico de mascotas con QTableView.**
* **Registro de Mascotas: Formulario validado para ingresar nombre, especie y peso.**
* **Edición Inteligente: Activación de edición mediante doble clic en la fila de la tabla.**
* **Eliminación Segura: Sistema de borrado con ventana de confirmación.**

👤 Autor
José Alejandro Valduz Contreras - https://github.com/Valduz-Jose


## Inicio
<img width="1128" height="437" alt="Captura de pantalla 2026-04-15 163120" src="https://github.com/user-attachments/assets/7aecbd08-7e25-48c1-823e-78408c4a8c5f" />

## Navbar
<img width="1171" height="476" alt="Captura de pantalla 2026-04-15 163148" src="https://github.com/user-attachments/assets/f26fdcdb-4c4b-4eba-a56c-02c31a568703" />

## Agregar
<img width="1542" height="922" alt="Captura de pantalla 2026-04-15 163157" src="https://github.com/user-attachments/assets/ae712360-1ccf-4563-8bb2-8391d22ee4a0" />

## Editar
<img width="1581" height="918" alt="Captura de pantalla 2026-04-15 163133" src="https://github.com/user-attachments/assets/77d35127-81d5-40af-808d-fd8ce9e2625a" />

## Eliminar
<img width="1591" height="918" alt="Captura de pantalla 2026-04-15 163210" src="https://github.com/user-attachments/assets/92733d48-7be3-4f01-87ba-a67eb2834598" />
