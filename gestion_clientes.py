from conexion_base_datos import ejecutar_query

def agregar_cliente(nombre, apellido, dni, email, telefono):
    """
    Agrega un nuevo cliente a la base de datos.
    """
    query = """
    INSERT INTO clientes (nombre, apellido, dni, email, telefono)
    VALUES (%s, %s, %s, %s, %s)
    """
    ejecutar_query(query, (nombre, apellido, dni, email, telefono))

def listar_clientes():
    """
    Lista todos los clientes de la base de datos.
    Retorna una lista de diccionarios (o tuplas, dependiendo de ejecutar_query)
    con los datos de los clientes.
    """
    query = "SELECT * FROM clientes"
    return ejecutar_query(query, fetch=True)

def modificar_cliente(id_cliente, nombre, apellido, dni, email, telefono):
    """
    Modifica los datos de un cliente existente.
    """
    query = """
    UPDATE clientes
    SET nombre = %s, apellido = %s, dni = %s, email = %s, telefono = %s
    WHERE id_cliente = %s
    """
    ejecutar_query(query, (nombre, apellido, dni, email, telefono, id_cliente))

def eliminar_cliente(id_cliente):
    """
    Elimina un cliente de la base de datos por su ID.
    """
    query = "DELETE FROM clientes WHERE id_cliente = %s"
    ejecutar_query(query, (id_cliente,))