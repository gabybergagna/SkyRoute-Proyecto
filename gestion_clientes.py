from conexion_base_datos import ejecutar_query

def agregar_cliente(razon_social, cuit, correo):
    query = """
    INSERT INTO clientes (razon_social, cuit, correo)
    VALUES (%s, %s, %s)
    """
    ejecutar_query(query, (razon_social, cuit, correo))

def listar_clientes():
    query = "SELECT * FROM clientes"
    return ejecutar_query(query, fetch=True)

def modificar_cliente(id_cliente, razon_social, cuit, correo):
    query = """
    UPDATE clientes
    SET razon_social = %s, cuit = %s, correo = %s
    WHERE id_cliente = %s
    """
    ejecutar_query(query, (razon_social, cuit, correo, id_cliente))

def eliminar_cliente(id_cliente):
    query = "DELETE FROM clientes WHERE id_cliente = %s"
    ejecutar_query(query, (id_cliente,))