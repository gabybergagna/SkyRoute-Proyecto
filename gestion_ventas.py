from conexion_base_datos import ejecutar_query
from datetime import datetime, timedelta

def registrar_venta(id_cliente, id_destino, fecha, costo):
    query = """
    INSERT INTO ventas (id_cliente, id_destino, fecha, costo, estado)
    VALUES (%s, %s, %s, %s, 'Activa')
    """
    ejecutar_query(query, (id_cliente, id_destino, fecha, costo))

def listar_ventas():
    query = "SELECT * FROM ventas"
    return ejecutar_query(query, fetch=True)

def anular_venta(id_venta):
    # Comprobar si la venta es anulable (últimos 15 minutos)
    query_check = "SELECT fecha FROM ventas WHERE id_venta = %s"
    resultado = ejecutar_query(query_check, (id_venta,), fetch=True)
    if not resultado:
        print("Venta no encontrada.")
        return
    fecha_venta = resultado[0]['fecha']
    ahora = datetime.now()
    if ahora - fecha_venta <= timedelta(minutes=15):
        query_update = """
        UPDATE ventas
        SET estado = 'Anulada', fecha_anulacion = %s
        WHERE id_venta = %s
        """
        ejecutar_query(query_update, (ahora, id_venta))
        print("Venta anulada correctamente.")
    else:
        print("La venta no puede ser anulada (excedió el plazo de 15 minutos).")