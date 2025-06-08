USE skyroute_db;

-- 1. Listar todos los clientes
SELECT * FROM clientes;

-- 2. Mostrar ventas realizadas en una fecha específica
SELECT * FROM ventas WHERE fecha_venta = '2025-06-01';

-- 3. Obtener la última venta de cada cliente y su fecha
SELECT v1.id_cliente, v1.fecha_venta, v1.total, v1.estado
FROM ventas v1
INNER JOIN (
    SELECT id_cliente, MAX(fecha_venta) AS ultima_fecha_venta
    FROM ventas
    GROUP BY id_cliente
) v2 ON v1.id_cliente = v2.id_cliente AND v1.fecha_venta = v2.ultima_fecha_venta;

-- 4. Listar todos los destinos que empiezan con “S”
SELECT * FROM destinos WHERE ciudad_destino LIKE 'S%';

-- 5. Mostrar cuántas ventas se realizaron por ciudad de destino
SELECT d.ciudad_destino, COUNT(DISTINCT dv.id_venta) AS total_ventas -- Usamos DISTINCT id_venta para contar ventas únicas
FROM ventas v
JOIN detalle_venta dv ON v.id_venta = dv.id_venta
JOIN destinos d ON dv.id_destino = d.id_destino
GROUP BY d.ciudad_destino;
