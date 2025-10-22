class Usuario:
    def __init__(self, nombre_usuario, contrasenia, rol="usuario", id=None):
        self.id = id
        self.nombre_usuario = nombre_usuario
        self.contrasenia = contrasenia
        self.rol = rol

    def mostrar_datos(self):
        return f"ID: {self.id} | Usuario: {self.nombre_usuario} | Rol: {self.rol}"