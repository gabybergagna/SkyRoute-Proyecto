from conexion_base_datos import ejecutar_query
from datetime import datetime, timedelta

def solicitar_arrepentimiento(id_venta, motivo, estado_arrepentimiento='Pendiente'):
    """
    Registra una solicitud de arrepentimiento para una venta.
    Esto activará un trigger en la DB para cambiar el estado de la venta.
    """
    fecha_solicitud = datetime.now().strftime('%Y-%m-%d')
    query = """
    INSERT INTO arrepentimientos (id_venta, fecha_solicitud, motivo, estado)
    VALUES (%s, %s, %s, %s)
    """
    ejecutar_query(query, (id_venta, fecha_solicitud, motivo, estado_arrepentimiento))
    print(f"Solicitud de arrepentimiento para venta {id_venta} registrada. Estado de venta actualizado a 'Arrepentimiento'.")

def actualizar_estado_arrepentimiento(id_arrepentimiento, nuevo_estado):
    """
    Actualiza el estado de una solicitud de arrepentimiento.
    Esto activará un trigger en la DB para cambiar el estado de la venta asociada.
    nuevo_estado: 'Aprobado', 'Rechazado', 'Pendiente'
    """
    if nuevo_estado not in ['Aprobado', 'Rechazado', 'Pendiente']:
        print("Estado de arrepentimiento inválido. Debe ser 'Aprobado', 'Rechazado' o 'Pendiente'.")
        return

    query = """
    UPDATE arrepentimientos
    SET estado = %s
    WHERE id_arrepentimiento = %s
    """
    ejecutar_query(query, (nuevo_estado, id_arrepentimiento))
    print(f"Estado de arrepentimiento {id_arrepentimiento} actualizado a '{nuevo_estado}'. Estado de venta asociado actualizado.")

