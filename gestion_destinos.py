from conexion_base_datos import ejecutar_query

def agregar_destino(ciudad, pais, costo_base):
    query = """
    INSERT INTO destinos (ciudad, pais, costo_base)
    VALUES (%s, %s, %s)
    """
    ejecutar_query(query, (ciudad, pais, costo_base))

def listar_destinos():
    query = "SELECT * FROM destinos"
    return ejecutar_query(query, fetch=True)

def modificar_destino(id_destino, ciudad, pais, costo_base):
    query = """
    UPDATE destinos
    SET ciudad = %s, pais = %s, costo_base = %s
    WHERE id_destino = %s
    """
    ejecutar_query(query, (ciudad, pais, costo_base, id_destino))

def eliminar_destino(id_destino):
    query = "DELETE FROM destinos WHERE id_destino = %s"
    ejecutar_query(query, (id_destino,))