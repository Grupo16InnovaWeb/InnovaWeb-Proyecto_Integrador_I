# InnovaWeb

# InnovaWeb - Proyecto Integrador I

## Descripción
Este proyecto es un **sistema de e-Commerce** desarrollado como parte del Proyecto Integrador I.  
Permite gestionar usuarios con roles (`admin` y `usuario`), controlar el registro e inicio de sesión, y mostrar menús personalizados según el rol.  
El sistema está pensado para ser escalable, con posibilidad de integrarse a una base de datos MySQL.

---

## Funcionalidades
- Registro e inicio de sesión de usuarios.
- Gestión de roles: `admin` o `usuario`.
- Menús dinámicos según rol.
- Validación de usuarios y contraseñas.
- Integración opcional con base de datos MySQL.
- Posibilidad de CRUD de usuarios (con BaseDatos).

---

## Estructura del proyecto
- **Usuario**: representa a cada usuario del sistema, con atributos como nombre, email, contraseña y rol.
- **SistemaAuth**: controla registro, login y validaciones de usuarios.
- **MenuSistema**: muestra opciones según el rol del usuario.
- **BaseDatos** (opcional): conexión y consultas a la base de datos MySQL.

---


### Diagrama de Clases
![Diagrama de Clases](docs/imagenes/diagrama_clases.png)  

> Representa las clases principales y sus relaciones.

---

## Tecnologías
- Python 3.x
- MySQL (opcional)
- PlantUML (para diagramas)
- Visual Studio Code (recomendado)

---

##  Instala
