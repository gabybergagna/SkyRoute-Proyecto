USE skyroute_db;

-- 1. Listar todos los clientes
SELECT * FROM clientes;

-- 2. Mostrar ventas realizadas en una fecha específica
SELECT * FROM ventas WHERE DATE(fecha) = '2025-06-01';

-- 3. Obtener la última venta de cada cliente y su fecha
SELECT v1.id_cliente, v1.fecha, v1.costo, v1.estado
FROM ventas v1
INNER JOIN (
    SELECT id_cliente, MAX(fecha) AS ultima_fecha
    FROM ventas
    GROUP BY id_cliente
) v2 ON v1.id_cliente = v2.id_cliente AND v1.fecha = v2.ultima_fecha;

-- 4. Listar todos los destinos que empiezan con “S”
SELECT * FROM destinos WHERE ciudad LIKE 'S%';

-- 5. Mostrar cuántas ventas se realizaron por país
SELECT d.pais, COUNT(*) AS total_ventas
FROM ventas v
JOIN destinos d ON v.id_destino = d.id_destino
GROUP BY d.pais;
