from conexion_base_datos import ejecutar_query

def agregar_destino(ciudad_origen, ciudad_destino, precio_base, duracion_estimada):
    """
    Agrega un nuevo destino a la base de datos.
    """
    query = """
    INSERT INTO destinos (ciudad_origen, ciudad_destino, precio_base, duracion_estimada)
    VALUES (%s, %s, %s, %s)
    """
    ejecutar_query(query, (ciudad_origen, ciudad_destino, precio_base, duracion_estimada))

def listar_destinos():
    """
    Lista todos los destinos de la base de datos.
    Retorna una lista de diccionarios (o tuplas) con los datos de los destinos.
    """
    query = "SELECT * FROM destinos"
    return ejecutar_query(query, fetch=True)

def modificar_destino(id_destino, ciudad_origen, ciudad_destino, precio_base, duracion_estimada):
    """
    Modifica los datos de un destino existente.
    """
    query = """
    UPDATE destinos
    SET ciudad_origen = %s, ciudad_destino = %s, precio_base = %s, duracion_estimada = %s
    WHERE id_destino = %s
    """
    ejecutar_query(query, (ciudad_origen, ciudad_destino, precio_base, duracion_estimada, id_destino))

def eliminar_destino(id_destino):
    """
    Elimina un destino de la base de datos por su ID.
    """
    query = "DELETE FROM destinos WHERE id_destino = %s"
    ejecutar_query(query, (id_destino,))