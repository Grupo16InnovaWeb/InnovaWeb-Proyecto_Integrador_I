-- Crear base de datos
CREATE DATABASE IF NOT EXISTS sistema_usuarios;
USE sistema_usuarios;

-- Tabla de usuarios (existente)
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(50) UNIQUE NOT NULL,
    contrasenia VARCHAR(100) NOT NULL,
    rol ENUM('admin', 'usuario') NOT NULL DEFAULT 'usuario',
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Nueva tabla de categorías
CREATE TABLE IF NOT EXISTS categorias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Nueva tabla de productos
CREATE TABLE IF NOT EXISTS productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(200) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL DEFAULT 0,
    categoria_id INT,
    usuario_creador_id INT,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id),
    FOREIGN KEY (usuario_creador_id) REFERENCES usuarios(id)
);

-- Insertar datos iniciales
INSERT INTO usuarios (nombre_usuario, contrasenia, rol) 
VALUES 
('admin', 'admin123', 'admin'),
('usuario1', 'clave123', 'usuario'),
('usuario2', 'clave123', 'usuario');

-- Insertar categorías de tecnología
INSERT INTO categorias (nombre, descripcion) VALUES
('Laptops', 'Computadoras portátiles y notebooks'),
('Smartphones', 'Teléfonos inteligentes y accesorios'),
('Tablets', 'Tablets y dispositivos táctiles'),
('Periféricos', 'Teclados, mouse, monitores'),
('Componentes', 'Hardware interno para PC');

-- Insertar productos de ejemplo
INSERT INTO productos (nombre, descripcion, precio, stock, categoria_id, usuario_creador_id) VALUES
('Laptop Dell XPS 13', 'Laptop ultrabook con procesador Intel i7, 16GB RAM, 512GB SSD', 1299.99, 15, 1, 1),
('iPhone 15 Pro', 'Smartphone Apple con cámara triple 48MP, 256GB almacenamiento', 1199.99, 25, 2, 1),
('Samsung Galaxy Tab S9', 'Tablet Android con S-Pen incluido, 128GB almacenamiento', 799.99, 10, 3, 1),
('Teclado Mecánico Razer', 'Teclado gaming mecánico switches verde RGB', 149.99, 30, 4, 1),
('Mouse Logitech MX Master', 'Mouse ergonómico para productividad', 99.99, 40, 4, 1);