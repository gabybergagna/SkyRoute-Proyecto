![Logo de SkyRoute](doc/logo.png)

# 🌐 Sistema de Ventas - SkyRoute S.R.L.

Bienvenidos al sistema de ventas secuencial de **SkyRoute S.R.L.**, una empresa dedicada a la comercialización de paquetes turísticos. Este proyecto fue desarrollado con fines educativos para modelar el registro de ventas de manera clara, segura y eficiente.

---

## Índice
<details>
  <summary>📂 Contenidos</summary>

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Integrantes del Equipo](#integrantes-del-equipo)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Funcionalidades](#funcionalidades)
  - [Gestión de Clientes](#gestión-de-clientes)
  - [Gestión de Destinos](#gestión-de-destinos)
  - [Gestión de Ventas](#gestión-de-ventas)
  - [Botón de Arrepentimiento](#botón-de-arrepentimiento)
- [Base de Datos](#base-de-datos)
  - [Estructura](#estructura)
  - [Datos de Ejemplo](#datos-de-ejemplo)
  - [Consultas Relevantes](#consultas-relevantes)
- [Instrucciones de Ejecución](#instrucciones-de-ejecución)
- [Ética y Ejercicio Profesional](#ética-y-ejercicio-profesional)
- [Conclusiones](#conclusiones)

</details>

---

## Descripción del Proyecto

SkyRoute es un sistema integral diseñado para gestionar clientes, destinos y ventas de una empresa de servicios turísticos. Implementa un módulo de arrepentimiento que permite anular ventas recientes, cumpliendo con las mejores prácticas en gestión de datos y protección legal. La arquitectura modular y el uso de MySQL garantizan escalabilidad, mantenibilidad y robustez en la gestión de la información.

---

## Integrantes del Equipo (Grupo 35)

| Nombre              | GitHub                                     |
|---------------------|--------------------------------------------|
| 👩‍💻 Ana Laura Giraudo  | [Lalygiraudo](https://github.com/Lalygiraudo)         |
| 👨‍💻 Fabricio Palacios  | [FabricioPalacios](https://github.com/FabricioPalacios) |
| 👩‍💻 Gabriela Bergagna  | [gabybergagna](https://github.com/gabybergagna)          |        
| 👨‍💻 Mariano Barboza    | [marianombarboza](https://github.com/marianombarboza)     |
| 👨‍💻 Patricio Henrry   | [PatricioHenrry](https://github.com/PatricioHenrry)      |

---

## Estructura del Proyecto

**skyroute/**
- `config.py` - Configuración de conexión a la base de datos
- `main.py` - Archivo principal con menú de opciones
- `conexion_base_datos.py` - Módulo para conexión y operaciones MySQL
- `gestion_clientes.py` - Funciones para CRUD de clientes
- `gestion_destinos.py` - Funciones para CRUD de destinos
- `gestion_ventas.py` - Registro de ventas y botón de arrepentimiento
- `README.md` - Documentación principal

**sql/**
- `schema.sql` - Sentencias DDL (creación de estructura)
- `inserts.sql` - Datos de ejemplo (DML)
- `consultas.sql` - Consultas SQL relevantes

---

## Tecnologías Utilizadas

- **Python 3.8+**
- **MySQL 8+**
- Biblioteca **mysql.connector** para conexión Python-MySQL
- Control de versiones con **Git** y hospedaje en **GitHub**
- Arquitectura modular basada en funciones para alta cohesión y bajo acoplamiento

---

## Funcionalidades

### Gestión de Clientes
- Agregar cliente con datos: razón social, CUIT y correo electrónico.
- Listar todos los clientes registrados.
- Modificar datos específicos de un cliente existente.
- Eliminar clientes.

### Gestión de Destinos
- Registrar destinos con ciudad, país y costo base.
- Listar destinos disponibles.
- Modificar información de destinos.
- Eliminar destinos.

### Gestión de Ventas
- Registrar ventas asociando cliente, destino, fecha y costo.
- Control de estado de la venta: "Activa" o "Anulada".

### Botón de Arrepentimiento
- Permitir anulación de una venta realizada dentro de los últimos 5 minutos.
- Cambiar estado de la venta a "Anulada".
- Registrar fecha y hora de anulación para trazabilidad.

---

## Base de Datos

### Estructura

Se ha implementado un esquema relacional en MySQL que incluye las tablas: 

- `clientes`
- `destinos`
- `ventas`

Cada tabla cuenta con sus claves primarias y relaciones foráneas que aseguran la integridad referencial.

### Datos de Ejemplo

Se insertaron al menos 3 registros por tabla para facilitar pruebas funcionales y demostraciones.

### Consultas Relevantes

Entre las consultas implementadas destacan:

- Listar todos los clientes.
- Mostrar ventas realizadas en una fecha específica.
- Obtener la última venta por cliente y su fecha.
- Listar destinos que comienzan con la letra "S".
- Mostrar cantidad de ventas agrupadas por país.

---

## Instrucciones de Ejecución

1. Clonar el repositorio:

```bash
git clone https://github.com/gabybergagna/skyroute.git
cd skyroute
