from producto import Producto
from database import Database
import mysql.connector

class GestorProductos:
    def __init__(self):
        self.db = Database()
        self.conexion = self.db.conectar()

    def crear_producto(self, usuario_actual):
        print("\n--- CREAR NUEVO PRODUCTO ---")
        nombre = input("Nombre del producto: ")
        descripcion = input("Descripción: ")
        
        try:
            precio = float(input("Precio: "))
            stock = int(input("Stock: "))
        except ValueError:
            print("Error: Precio y stock deben ser números válidos.")
            return

        # Mostrar categorías disponibles
        categorias = self.obtener_categorias()
        if not categorias:
            print("No hay categorías disponibles. Contacta al administrador.")
            return

        print("\nCategorías disponibles:")
        for cat in categorias:
            print(f"{cat[0]}. {cat[1]}")

        try:
            categoria_id = int(input("ID de categoría: "))
        except ValueError:
            print("ID de categoría inválido.")
            return

        try:
            cursor = self.conexion.cursor()
            query = """INSERT INTO productos 
                      (nombre, descripcion, precio, stock, categoria_id, usuario_creador_id) 
                      VALUES (%s, %s, %s, %s, %s, %s)"""
            cursor.execute(query, (nombre, descripcion, precio, stock, categoria_id, usuario_actual.id))
            self.conexion.commit()
            cursor.close()
            print("✅ Producto creado exitosamente.")
        except mysql.connector.Error as e:
            print(f"❌ Error al crear producto: {e}")

    def listar_productos(self):
        try:
            cursor = self.conexion.cursor()
            # JOIN entre productos y categorías
            query = """SELECT p.id, p.nombre, p.descripcion, p.precio, p.stock, 
                              c.nombre as categoria_nombre, u.nombre_usuario
                       FROM productos p
                       JOIN categorias c ON p.categoria_id = c.id
                       JOIN usuarios u ON p.usuario_creador_id = u.id
                       ORDER BY p.id"""
            cursor.execute(query)
            resultados = cursor.fetchall()
            cursor.close()

            if not resultados:
                print("No hay productos registrados.")
                return

            print("\n--- LISTA DE PRODUCTOS ---")
            for resultado in resultados:
                producto = Producto(
                    resultado[0], resultado[1], resultado[2], resultado[3],
                    resultado[4], None, resultado[5], resultado[6]
                )
                print(producto.mostrar_datos())

        except mysql.connector.Error as e:
            print(f"Error al listar productos: {e}")

    def buscar_productos_por_categoria(self):
        try:
            cursor = self.conexion.cursor()
            # Obtener categorías
            cursor.execute("SELECT id, nombre FROM categorias")
            categorias = cursor.fetchall()

            print("\nCategorías disponibles:")
            for cat in categorias:
                print(f"{cat[0]}. {cat[1]}")

            categoria_id = input("Ingrese ID de categoría: ")

            # JOIN para productos por categoría
            query = """SELECT p.id, p.nombre, p.descripcion, p.precio, p.stock, 
                              c.nombre as categoria_nombre, u.nombre_usuario
                       FROM productos p
                       JOIN categorias c ON p.categoria_id = c.id
                       JOIN usuarios u ON p.usuario_creador_id = u.id
                       WHERE p.categoria_id = %s"""
            cursor.execute(query, (categoria_id,))
            resultados = cursor.fetchall()
            cursor.close()

            if not resultados:
                print("No hay productos en esta categoría.")
                return

            print(f"\n--- PRODUCTOS EN CATEGORÍA: {categorias[int(categoria_id)-1][1] if categorias else 'Desconocida'} ---")
            for resultado in resultados:
                producto = Producto(
                    resultado[0], resultado[1], resultado[2], resultado[3],
                    resultado[4], None, resultado[5], resultado[6]
                )
                print(producto.mostrar_datos())

        except mysql.connector.Error as e:
            print(f"Error al buscar productos: {e}")

    def actualizar_producto(self):
        self.listar_productos()
        try:
            producto_id = int(input("\nID del producto a actualizar: "))
            
            cursor = self.conexion.cursor()
            # Verificar que el producto existe
            cursor.execute("SELECT id FROM productos WHERE id = %s", (producto_id,))
            if not cursor.fetchone():
                print("❌ Producto no encontrado.")
                cursor.close()
                return

            print("\nDeje en blanco los campos que no desea cambiar:")
            nombre = input("Nuevo nombre: ")
            descripcion = input("Nueva descripción: ")
            precio = input("Nuevo precio: ")
            stock = input("Nuevo stock: ")

            # Construir query dinámicamente
            campos = []
            valores = []
            
            if nombre: 
                campos.append("nombre = %s")
                valores.append(nombre)
            if descripcion: 
                campos.append("descripcion = %s")
                valores.append(descripcion)
            if precio: 
                campos.append("precio = %s")
                valores.append(float(precio))
            if stock: 
                campos.append("stock = %s")
                valores.append(int(stock))

            if campos:
                valores.append(producto_id)
                query = f"UPDATE productos SET {', '.join(campos)} WHERE id = %s"
                cursor.execute(query, valores)
                self.conexion.commit()
                print("✅ Producto actualizado exitosamente.")
            else:
                print("⚠️ No se realizaron cambios.")

            cursor.close()

        except (ValueError, mysql.connector.Error) as e:
            print(f"❌ Error al actualizar producto: {e}")

    def eliminar_producto(self):
        self.listar_productos()
        try:
            producto_id = int(input("\nID del producto a eliminar: "))
            
            confirmacion = input("¿Está seguro de eliminar este producto? (s/n): ")
            if confirmacion.lower() != 's':
                print("Operación cancelada.")
                return

            cursor = self.conexion.cursor()
            cursor.execute("DELETE FROM productos WHERE id = %s", (producto_id,))
            self.conexion.commit()
            cursor.close()

            if cursor.rowcount > 0:
                print("✅ Producto eliminado exitosamente.")
            else:
                print("❌ Producto no encontrado.")

        except (ValueError, mysql.connector.Error) as e:
            print(f"❌ Error al eliminar producto: {e}")

    def obtener_categorias(self):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT id, nombre FROM categorias")
            categorias = cursor.fetchall()
            cursor.close()
            return categorias
        except mysql.connector.Error as e:
            print(f"Error al obtener categorías: {e}")
            return []

    def cerrar_conexion(self):
        self.db.desconectar()