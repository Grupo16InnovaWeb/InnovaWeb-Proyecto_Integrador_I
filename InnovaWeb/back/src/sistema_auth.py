from user import Usuario
from database import Database
import re
import mysql.connector

class SistemaAuth:
    def __init__(self):
        self.db = Database()
        self.conexion = self.db.conectar()

    def validar_contrasenia(self, contrasenia):
        return (
            len(contrasenia) >= 6 and
            re.search(r"[A-Za-z]", contrasenia) and
            re.search(r"[0-9]", contrasenia)
        )

    def buscar_usuario(self, nombre):
        try:
            cursor = self.conexion.cursor()
            query = "SELECT id, nombre_usuario, contrasenia, rol FROM usuarios WHERE nombre_usuario = %s"
            cursor.execute(query, (nombre,))
            resultado = cursor.fetchone()
            cursor.close()
            
            if resultado:
                return Usuario(resultado[1], resultado[2], resultado[3], resultado[0])
            return None
        except mysql.connector.Error as e:
            print(f"Error al buscar usuario: {e}")
            return None

    def registrar_usuario(self):
        nombre = input("Ingrese nombre de usuario: ")
        
        if self.buscar_usuario(nombre):
            print("Ya existe un usuario con ese nombre.")
            return

        contrasenia = input("Ingrese contraseña: ")
        if not self.validar_contrasenia(contrasenia):
            print("Contraseña inválida. Debe tener al menos 6 caracteres con letras y números.")
            return

        try:
            cursor = self.conexion.cursor()
            query = "INSERT INTO usuarios (nombre_usuario, contrasenia, rol) VALUES (%s, %s, %s)"
            cursor.execute(query, (nombre, contrasenia, "usuario"))
            self.conexion.commit()
            cursor.close()
            print("Usuario registrado exitosamente.")
        except mysql.connector.Error as e:
            print(f"Error al registrar usuario: {e}")

    def iniciar_sesion(self):
        nombre = input("Usuario: ")
        contrasenia = input("Contraseña: ")
        
        usuario = self.buscar_usuario(nombre)
        if usuario and usuario.contrasenia == contrasenia:
            print(f"Bienvenido, {usuario.nombre_usuario} ({usuario.rol})")
            return usuario
        
        print("Credenciales incorrectas.")
        return None

    def obtener_todos_usuarios(self):
        try:
            cursor = self.conexion.cursor()
            query = "SELECT id, nombre_usuario, contrasenia, rol FROM usuarios"
            cursor.execute(query)
            resultados = cursor.fetchall()
            cursor.close()
            
            usuarios = []
            for resultado in resultados:
                usuarios.append(Usuario(resultado[1], resultado[2], resultado[3], resultado[0]))
            return usuarios
        except mysql.connector.Error as e:
            print(f"Error al obtener usuarios: {e}")
            return []

    def actualizar_rol_usuario(self, nombre, nuevo_rol):
        try:
            cursor = self.conexion.cursor()
            query = "UPDATE usuarios SET rol = %s WHERE nombre_usuario = %s"
            cursor.execute(query, (nuevo_rol, nombre))
            self.conexion.commit()
            cursor.close()
            return True
        except mysql.connector.Error as e:
            print(f"Error al actualizar rol: {e}")
            return False

    def eliminar_usuario(self, nombre):
        try:
            cursor = self.conexion.cursor()
            query = "DELETE FROM usuarios WHERE nombre_usuario = %s"
            cursor.execute(query, (nombre,))
            self.conexion.commit()
            cursor.close()
            return True
        except mysql.connector.Error as e:
            print(f"Error al eliminar usuario: {e}")
            return False

    def cerrar_conexion(self):
        self.db.desconectar()