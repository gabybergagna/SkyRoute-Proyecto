-- Creación de la base de datos
CREATE DATABASE IF NOT EXISTS skyroute_db;
USE skyroute_db;

-- Tabla CLIENTES 
CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    dni VARCHAR(20) NOT NULL UNIQUE,
    email VARCHAR(150) NOT NULL UNIQUE,
    telefono VARCHAR(20)
);

-- Tabla DESTINOS 
CREATE TABLE destinos (
    id_destino INT AUTO_INCREMENT PRIMARY KEY,
    ciudad_origen VARCHAR(100) NOT NULL,
    ciudad_destino VARCHAR(100) NOT NULL,
    precio_base DECIMAL(10,2) NOT NULL,
    duracion_estimada INT NOT NULL
);

-- Tabla VENTAS 
CREATE TABLE ventas (
    id_venta INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,		
    fecha_venta DATE NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    estado ENUM('Confirmada', 'Cancelada', 'Arrepentimiento') DEFAULT 'Confirmada',
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

-- Tabla DETALLE_VENTA 
CREATE TABLE detalle_venta (
    id_detalle INT AUTO_INCREMENT PRIMARY KEY,
    id_venta INT NOT NULL,
    id_destino INT NOT NULL,
    cantidad INT NOT NULL,
    subtotal DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (id_venta) REFERENCES ventas(id_venta),
    FOREIGN KEY (id_destino) REFERENCES destinos(id_destino)
);

-- Tabla ARREPENTIMIENTOS 
CREATE TABLE arrepentimientos (
    id_arrepentimiento INT AUTO_INCREMENT PRIMARY KEY,
    id_venta INT NOT NULL,
    fecha_solicitud DATE NOT NULL,
    motivo TEXT,
    estado ENUM('Aprobado', 'Rechazado', 'Pendiente') DEFAULT 'Pendiente',
    FOREIGN KEY (id_venta) REFERENCES ventas(id_venta)
);

-- Índices básicos para optimizar consultas
CREATE INDEX idx_clientes_dni ON clientes(dni);
CREATE INDEX idx_ventas_cliente ON ventas(id_cliente);
CREATE INDEX idx_detalle_venta ON detalle_venta(id_venta);
CREATE INDEX idx_arrepentimientos_venta ON arrepentimientos(id_venta);

-- Trigger para calcular subtotal automáticamente
DELIMITER //
CREATE TRIGGER tr_calcular_subtotal
BEFORE INSERT ON detalle_venta
FOR EACH ROW
BEGIN
    DECLARE v_precio_base DECIMAL(10,2);
    SELECT precio_base INTO v_precio_base FROM destinos WHERE id_destino = NEW.id_destino;
    SET NEW.subtotal = NEW.cantidad * v_precio_base;
END//

CREATE TRIGGER tr_actualizar_subtotal
BEFORE UPDATE ON detalle_venta
FOR EACH ROW
BEGIN
    DECLARE v_precio_base DECIMAL(10,2);
    SELECT precio_base INTO v_precio_base FROM destinos WHERE id_destino = NEW.id_destino;
    SET NEW.subtotal = NEW.cantidad * v_precio_base;
END//

CREATE TRIGGER tr_arrepentimiento_insert
AFTER INSERT ON arrepentimientos
FOR EACH ROW
BEGIN
    UPDATE ventas
    SET estado = 'Arrepentimiento' 
    WHERE id_venta = NEW.id_venta;
END//

CREATE TRIGGER tr_arrepentimiento_update
AFTER UPDATE ON arrepentimientos
FOR EACH ROW
BEGIN
    IF NEW.estado = 'Aprobado' AND OLD.estado != 'Aprobado' THEN
        UPDATE ventas
        SET estado = 'Cancelada'
        WHERE id_venta = NEW.id_venta;
    ELSEIF NEW.estado = 'Rechazado' AND OLD.estado != 'Rechazado' THEN
        UPDATE ventas
        SET estado = 'Confirmada' 
        WHERE id_venta = NEW.id_venta;
    
    END IF;
END//
DELIMITER ;
