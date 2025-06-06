import mysql.connector
from config import DB_CONFIG
from mysql.connector import Error

def conectar():
    """Establece conexión con la base de datos y devuelve el objeto conexión."""
    try:
        conexion = mysql.connector.connect(**DB_CONFIG)
        return conexion
    except Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None

def ejecutar_query(query, params=None, fetch=False):
    """Ejecuta sentencias SQL, opcionalmente devuelve resultados."""
    conexion = conectar()
    if conexion is None:
        return None
    cursor = conexion.cursor(dictionary=True)
    try:
        cursor.execute(query, params)
        if fetch:
            resultados = cursor.fetchall()
        else:
            conexion.commit()
            resultados = None
        cursor.close()
        conexion.close()
        return resultados
    except Error as e:
        print(f"Error ejecutando query: {e}")
        cursor.close()
        conexion.close()
        return None
