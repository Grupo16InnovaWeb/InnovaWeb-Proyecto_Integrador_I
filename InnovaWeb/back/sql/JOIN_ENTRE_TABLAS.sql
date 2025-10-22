SELECT p.id, p.nombre, p.descripcion, p.precio, p.stock, 
       c.nombre as categoria_nombre, u.nombre_usuario
FROM productos p
JOIN categorias c ON p.categoria_id = c.id
JOIN usuarios u ON p.usuario_creador_id = u.id

