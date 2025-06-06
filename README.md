
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
- Agregar cliente con datos: razón social, CUIT y correo electrónico
- Listar todos los clientes registrados
- Modificar datos específicos de un cliente existente
- Eliminar clientes

### Gestión de Destinos
- Registrar destinos con ciudad, país y costo base
- Listar destinos disponibles
- Modificar información de destinos
- Eliminar destinos

### Gestión de Ventas
- Registrar ventas asociando cliente, destino, fecha y costo
- Control de estado de la venta: "Activa" o "Anulada"

### Botón de Arrepentimiento
- Permitir anulación de una venta realizada dentro de los últimos 5 minutos
- Cambiar estado de la venta a "Anulada"
- Registrar fecha y hora de anulación para trazabilidad

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
- Listar todos los clientes
- Mostrar ventas realizadas en una fecha específica
- Obtener la última venta por cliente y su fecha
- Listar destinos que comienzan con la letra "S"
- Mostrar cantidad de ventas agrupadas por país

---

## Instrucciones de Ejecución

1. Clonar el repositorio:
```bash
git clone https://github.com/gabybergagna/skyroute.git
cd skyroute
