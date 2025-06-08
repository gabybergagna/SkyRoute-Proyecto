from conexion_base_datos import ejecutar_query
from datetime import datetime, timedelta

def registrar_venta(id_cliente, fecha_venta=None):
    """
    Registra una nueva venta (solo el encabezado).
    El total se inicializa en 0 y debe ser actualizado posteriormente
    al agregar detalles de venta. El estado inicial es 'Confirmada'.
    Retorna el id_venta de la venta recién creada.
    """
    if fecha_venta is None:
        fecha_venta = datetime.now().strftime('%Y-%m-%d') # Formato 'YYYY-MM-DD' para DATE

    query = """
    INSERT INTO ventas (id_cliente, fecha_venta, total, estado)
    VALUES (%s, %s, %s, %s)
    """
    return ejecutar_query(query, (id_cliente, fecha_venta, 0.00, 'Confirmada'), return_id=True)


def listar_ventas():
    """
    Lista todas las ventas de la base de datos.
    Retorna una lista de diccionarios (o tuplas) con los datos de las ventas.
    """
    query = "SELECT * FROM ventas"
    return ejecutar_query(query, fetch=True)

def agregar_detalle_venta(id_venta, id_destino, cantidad):
    """
    Agrega un detalle a una venta existente.
    El subtotal será calculado automáticamente por el trigger `tr_calcular_subtotal`.
    Después de agregar el detalle, se debe actualizar el total de la venta.
    """
    query = """
    INSERT INTO detalle_venta (id_venta, id_destino, cantidad)
    VALUES (%s, %s, %s)
    """
    ejecutar_query(query, (id_venta, id_destino, cantidad))

    actualizar_total_venta(id_venta)


def actualizar_total_venta(id_venta):
    """
    Actualiza el campo 'total' en la tabla 'ventas' sumando los 'subtotal'
    de todos sus 'detalle_venta' asociados.
    """
    query = """
    UPDATE ventas
    SET total = (SELECT COALESCE(SUM(subtotal), 0) FROM detalle_venta WHERE id_venta = %s)
    WHERE id_venta = %s
    """
    ejecutar_query(query, (id_venta, id_venta))

