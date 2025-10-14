import sqlite3

def crear_tablas():
    conexion = sqlite3.connect('tienda.db')
    cursor = conexion.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            categoria_id INTEGER,
            FOREIGN KEY (categoria_id) REFERENCES categorias(id)
        )
    ''')

    # Insertar categorías iniciales
    cursor.execute("INSERT OR IGNORE INTO categorias (id, nombre) VALUES (1, 'Electrónica')")
    cursor.execute("INSERT OR IGNORE INTO categorias (id, nombre) VALUES (2, 'Ropa')")
    cursor.execute("INSERT OR IGNORE INTO categorias (id, nombre) VALUES (3, 'Alimentos')")

    conexion.commit()
    conexion.close()
    print("Tablas creadas con éxito.")

if __name__ == '__main__':
    crear_tablas()
