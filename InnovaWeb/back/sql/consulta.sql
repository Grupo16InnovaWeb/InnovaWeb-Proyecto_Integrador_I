-- Consulta con JOIN

SELECT 
    p.id AS id_producto,
    p.nombre AS producto,
    p.precio,
    c.nombre AS categoria
FROM productos p
JOIN categorias c ON p.categoria_id = c.id
ORDER BY c.nombre, p.nombre;
