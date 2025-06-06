USE skyroute_db;

-- Clientes de ejemplo
INSERT INTO clientes (razon_social, cuit, correo) VALUES
('Empresa Alpha', '20-12345678-9', 'contacto@alpha.com'),
('Beta S.A.', '27-98765432-1', 'info@beta.com'),
('Gamma SRL', '30-11223344-5', 'ventas@gamma.com');

-- Destinos de ejemplo
INSERT INTO destinos (ciudad, pais, costo_base) VALUES
('Salta', 'Argentina', 5000.00),
('Santiago', 'Chile', 7000.00),
('São Paulo', 'Brasil', 8000.00);

-- Ventas de ejemplo
INSERT INTO ventas (id_cliente, id_destino, fecha, costo, estado) VALUES
(1, 1, '2025-06-01 10:00:00', 5000.00, 'Activa'),
(2, 2, '2025-06-02 14:30:00', 7200.00, 'Activa'),
(3, 3, '2025-06-03 09:15:00', 8500.00, 'Anulada');