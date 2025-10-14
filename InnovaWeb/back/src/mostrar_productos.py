import sqlite3

conexion = sqlite3.connect('tienda.db')
cursor = conexion.cursor()

# Consulta con JOIN para mostrar productos y su categoría
cursor.execute("""
    SELECT p.id, p.nombre, p.precio, c.nombre AS categoria
    FROM productos p
    LEFT JOIN categorias c ON p.categoria_id = c.id
""")

productos = cursor.fetchall()

print("Listado de productos:\n")
for prod in productos:
    print(f"ID: {prod[0]}, Nombre: {prod[1]}, Precio: ${prod[2]:,.2f}, Categoría: {prod[3]}")

conexion.close()
