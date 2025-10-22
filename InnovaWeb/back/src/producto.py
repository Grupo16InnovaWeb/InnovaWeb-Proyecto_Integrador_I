class Producto:
    def __init__(self, id, nombre, descripcion, precio, stock, categoria_id, categoria_nombre=None, usuario_creador=None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.categoria_id = categoria_id
        self.categoria_nombre = categoria_nombre
        self.usuario_creador = usuario_creador

    def mostrar_datos(self):
        return f"ID: {self.id} | {self.nombre} | ${self.precio} | Stock: {self.stock} | Categoría: {self.categoria_nombre}"
    
    def mostrar_detalles(self):
        return f"""
=== DETALLES DEL PRODUCTO ===
ID: {self.id}
Nombre: {self.nombre}
Descripción: {self.descripcion}
Precio: ${self.precio}
Stock: {self.stock}
Categoría: {self.categoria_nombre}
Creado por: {self.usuario_creador}
        """
