-- Creación de la base de datos
CREATE DATABASE IF NOT EXISTS skyroute_db;
USE skyroute_db;

-- Tabla clientes
CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    razon_social VARCHAR(100) NOT NULL,
    cuit VARCHAR(20) NOT NULL UNIQUE,
    correo VARCHAR(100)
);

-- Tabla destinos
CREATE TABLE IF NOT EXISTS destinos (
    id_destino INT AUTO_INCREMENT PRIMARY KEY,
    ciudad VARCHAR(50) NOT NULL,
    pais VARCHAR(50) NOT NULL,
    costo_base DECIMAL(10,2) NOT NULL
);

-- Tabla ventas
CREATE TABLE IF NOT EXISTS ventas (
    id_venta INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_destino INT NOT NULL,
    fecha DATETIME NOT NULL,
    costo DECIMAL(10,2) NOT NULL,
    estado ENUM('Activa', 'Anulada') DEFAULT 'Activa',
    fecha_anulacion DATETIME NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_destino) REFERENCES destinos(id_destino)
);