from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def conectar():
    return sqlite3.connect('tienda.db')

# ---------------- CREATE ----------------
@app.route('/productos', methods=['POST'])
def crear_producto():
    data = request.get_json()
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO productos (nombre, precio, categoria_id) VALUES (?, ?, ?)",
        (data['nombre'], data['precio'], data['categoria_id'])
    )
    conexion.commit()
    conexion.close()
    return jsonify({'mensaje': 'Producto creado'}), 201

# ---------------- READ ---------------- (listado con JOIN)
@app.route('/productos', methods=['GET'])
def listar_productos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT p.id, p.nombre, p.precio, c.nombre as categoria
        FROM productos p
        LEFT JOIN categorias c ON p.categoria_id = c.id
    """)
    productos = [
        {'id': row[0], 'nombre': row[1], 'precio': row[2], 'categoria': row[3]}
        for row in cursor.fetchall()
    ]
    conexion.close()
    return jsonify(productos)

# ---------------- UPDATE ----------------
@app.route('/productos/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    data = request.get_json()
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "UPDATE productos SET nombre=?, precio=?, categoria_id=? WHERE id=?",
        (data['nombre'], data['precio'], data['categoria_id'], id)
    )
    conexion.commit()
    conexion.close()
    return jsonify({'mensaje': 'Producto actualizado'})

# ---------------- DELETE ----------------
@app.route('/productos/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM productos WHERE id=?", (id,))
    conexion.commit()
    conexion.close()
    return jsonify({'mensaje': 'Producto eliminado'})

# ---------------- RUN ----------------
if __name__ == '__main__':
    app.run(debug=True)
