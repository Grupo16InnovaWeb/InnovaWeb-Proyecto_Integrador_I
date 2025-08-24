SRS – Especificación de Requisitos de Software
 (IEEE 830)
 Proyecto: InnovaWeb – E-commerce de Tecnología\ Repositorio:
 https://nnovaWeb-Proyecto_Integrador_I
 <org>/<repo> \ Versión del documento: v1.1.0\ Estado: Entrega académica\ Fecha: 2025-08-24
 0. Historial de cambios
 Versión
 Fecha
 Autor
 Descripción
 v1.0.0
 2025-08-24
 Johana
 Acosta
 Documento inicial IEEE 830
 v1.1.0
 2025-08-24
 Johana
 Acosta
 Se agregaron criterios de aceptación, matriz de trazabilidad y
 detalle de BD
 1. Introducción
 1.1 Propósito
 El propósito de este documento es especificar de manera clara y estructurada los requisitos funcionales y
 no funcionales del sistema InnovaWeb, un proyecto en Python para la gestión de usuarios en un E
commerce de tecnología. El SRS será utilizado por el equipo de desarrollo, docentes y revisores académicos
 para comprender los objetivos, limitaciones y características del sistema.
 1.2 Alcance
 InnovaWeb permitirá:
 • 
• 
• 
• 
• 
• 
Registrar e iniciar sesión de usuarios.
 Validar contraseñas con criterios de seguridad.
 Controlar el acceso mediante roles (administrador y usuario estándar).
 Mostrar menús personalizados según el rol.
 Administrar usuarios: cambiar roles, eliminar usuarios (solo admin).
 Diseñar y documentar una base de datos relacional en tercera forma normal (3FN), con conexión
 simulada en consola y scripts SQL ejecutables en MySQL.
 1.3 Definiciones, acrónimos y abreviaturas
 • 
• 
• 
POO: Programación Orientada a Objetos.
 3FN: Tercera Forma Normal, modelo de normalización en bases de datos.
 CRUD: Create, Read, Update, Delete.
 1
• 
• 
Regex: Expresiones regulares.
 Admin: Usuario con privilegios de administrador.
 1.4 Referencias
 • 
• 
• 
Documentación IEEE 830: Estándar de especificación de requisitos de software.
 Diagramas de clases y entidad-relación (
 Base de datos.png ).
 docs/Diagrama de Clases.png , 
Archivos de base de datos: 
database/Creacion de tablas.txt y 
Usuarios.txt .
 1.5 Visión general del documento
 docs/Diagrama de 
database/CRUD para 
El documento está organizado en: Introducción, Descripción general, Requisitos específicos y Apéndices,
 siguiendo el estándar IEEE 830.
 2. Descripción general
 2.1 Perspectiva del producto
 El sistema es una aplicación en Python 3.x. Funciona de manera independiente, pero incluye el diseño de
 una base de datos en MySQL para almacenar y administrar los datos. Se proveen scripts SQL para crear las
 tablas y realizar operaciones CRUD.
 2.2 Funciones principales
 • 
• 
• 
• 
• 
Registro de usuario con validaciones (regex, duplicados).
 Inicio de sesión con control de roles.
 Menú dinámico según rol.
 Funciones exclusivas para administradores (gestión de usuarios).
 Ejecución de scripts SQL para crear tablas y CRUD.
 2.3 Características de los usuarios
 • 
• 
Usuario estándar: puede registrarse, iniciar sesión y consultar sus propios datos.
 Administrador: además de lo anterior, puede listar usuarios, cambiar roles y eliminar cuentas.
 2.4 Restricciones
 • 
• 
• 
El sistema debe conectarse a MySQL 
Contraseñas: mínimo 6 caracteres, con letras y números.
 Proyecto académico (no apto para producción).
 2.5 Suposiciones y dependencias
 • 
• 
Se asume que Python 3.x está instalado.
 Se requiere MySQL Server para ejecutar los scripts SQL.
 2
Se asume conocimiento básico de consola y SQL.
 • 
3. Requisitos específicos
 3.1 Requisitos funcionales
 • 
• 
• 
• 
• 
• 
• 
REQ-001. El sistema debe permitir el registro de usuarios con validación de contraseña.
 REQ-002. El sistema debe validar que no se registren usuarios duplicados.
 REQ-003. El sistema debe permitir iniciar sesión con credenciales válidas.
 REQ-004. El sistema debe mostrar menús distintos según el rol del usuario.
 REQ-005. El sistema debe permitir que un administrador cambie el rol de otro usuario.
 REQ-006. El sistema debe permitir que un administrador elimine usuarios.
 REQ-007. El sistema debe ejecutar scripts SQL para crear y administrar la base de datos.
 3.2 Requisitos no funcionales
 • 
• 
• 
• 
• 
• 
• 
NFR-001. El sistema debe estar desarrollado en Python 3.x.
 NFR-002. El código debe cumplir con modularidad y separación de responsabilidades.
 NFR-003. Las contraseñas deben validarse mediante expresiones regulares.
 NFR-004. El sistema debe mostrar mensajes claros de error y validación.
 NFR-005. La base de datos debe estar normalizada hasta 3FN.
 NFR-006. El sistema debe aplicar principios de POO (encapsulamiento, clases y métodos).
 NFR-007. La conexión a la base de datos debe manejar errores y excepciones correctamente.
 3.3 Interfaces
 • 
• 
• 
Usuario: Consola de comandos.
 Base de datos: MySQL (scripts SQL incluidos).
 Archivos: Documentación y diagramas en carpeta 
3.4 Restricciones de diseño
 • 
• 
• 
Lenguaje obligatorio: Python 3.x.
 Modelo relacional: MySQL, normalizado a 3FN.
 Editor recomendado: Visual Studio Code.
 docs/ .
 4. Criterios de aceptación
 • 
• 
• 
UAT-001. Dado un usuario nuevo, cuando se registre con contraseña válida, entonces debe
 guardarse correctamente en la base de datos.
 UAT-002. Dado un usuario existente, cuando intente registrarse con el mismo email, entonces el
 sistema debe mostrar error de duplicado.
 UAT-003. Dado un usuario registrado, cuando inicie sesión con credenciales correctas, entonces
 debe acceder al menú correspondiente a su rol.
 3
• 
• 
• 
UAT-004. Dado un administrador, cuando seleccione la opción de listar usuarios, entonces debe
 visualizar todos los registros de la base de datos.
 UAT-005. Dado un administrador, cuando cambie el rol de un usuario, entonces el cambio debe
 reflejarse en la base de datos.
 UAT-006. Dado un administrador, cuando elimine un usuario, entonces el registro debe eliminarse
 de la base de datos.
 5. Matriz de trazabilidad
 REQ
 Descripción
 Caso de uso
 Script BD
 Test
 REQ-001 Registro de
 usuario
 CU-01 Registro
 INSERT INTO usuarios...
 TC-001
 REQ-002 Validar
 duplicados
 SELECT * FROM usuarios 
CU-01 Registro
 WHERE email=?
 TC-002
 REQ-003 Inicio de sesión
 CU-02 Login
 SELECT * FROM usuarios...
 TC-003
 REQ-004 Menú por rol
 CU-03 Gestión de
 menú
 N/A
 TC-004
 REQ-005 Cambiar rol
 CU-04 Gestión de
 usuarios
 UPDATE usuarios SET rol=?
 TC-005
 REQ-006 Eliminar usuario
 CU-04 Gestión de
 usuarios
 DELETE FROM usuarios...
 TC-006
 REQ-007 Scripts de BD
 CU-05 Administración
 BD
 CREATE TABLE...
 TC-007
 6. Apéndices
 • 
• 
• 
Diagramas del proyecto (
 Glosario ampliado.
 docs/ ).
 Ejemplos de ejecución en consola