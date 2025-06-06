from gestion_clientes import agregar_cliente, listar_clientes, modificar_cliente, eliminar_cliente
from gestion_destinos import agregar_destino, listar_destinos, modificar_destino, eliminar_destino
from gestion_ventas import registrar_venta, listar_ventas, anular_venta
from datetime import datetime

def menu_clientes():
    while True:
        print("\n--- Gestión de Clientes ---")
        print("1. Agregar cliente")
        print("2. Listar clientes")
        print("3. Modificar cliente")
        print("4. Eliminar cliente")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            razon = input("Razón social: ")
            cuit = input("CUIT: ")
            correo = input("Correo electrónico: ")
            agregar_cliente(razon, cuit, correo)
            print("Cliente agregado.")
        elif opcion == '2':
            clientes = listar_clientes()
            for c in clientes:
                print(c)
        elif opcion == '3':
            id_c = int(input("ID cliente a modificar: "))
            razon = input("Nueva razón social: ")
            cuit = input("Nuevo CUIT: ")
            correo = input("Nuevo correo: ")
            modificar_cliente(id_c, razon, cuit, correo)
            print("Cliente modificado.")
        elif opcion == '4':
            id_c = int(input("ID cliente a eliminar: "))
            eliminar_cliente(id_c)
            print("Cliente eliminado.")
        elif opcion == '0':
            break
        else:
            print("Opción inválida, intente nuevamente.")

def menu_destinos():
    while True:
        print("\n--- Gestión de Destinos ---")
        print("1. Agregar destino")
        print("2. Listar destinos")
        print("3. Modificar destino")
        print("4. Eliminar destino")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            ciudad = input("Ciudad: ")
            pais = input("País: ")
            costo = float(input("Costo base: "))
            agregar_destino(ciudad, pais, costo)
            print("Destino agregado.")
        elif opcion == '2':
            destinos = listar_destinos()
            for d in destinos:
                print(d)
        elif opcion == '3':
            id_d = int(input("ID destino a modificar: "))
            ciudad = input("Nueva ciudad: ")
            pais = input("Nuevo país: ")
            costo = float(input("Nuevo costo base: "))
            modificar_destino(id_d, ciudad, pais, costo)
            print("Destino modificado.")
        elif opcion == '4':
            id_d = int(input("ID destino a eliminar: "))
            eliminar_destino(id_d)
            print("Destino eliminado.")
        elif opcion == '0':
            break
        else:
            print("Opción inválida, intente nuevamente.")

def menu_ventas():
    while True:
        print("\n--- Gestión de Ventas ---")
        print("1. Registrar venta")
        print("2. Listar ventas")
        print("3. Anular venta (botón arrepentimiento)")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_cliente = int(input("ID cliente: "))
            id_destino = int(input("ID destino: "))
            fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            costo = float(input("Costo: "))
            registrar_venta(id_cliente, id_destino, fecha, costo)
            print("Venta registrada.")
        elif opcion == '2':
            ventas = listar_ventas()
            for v in ventas:
                print(v)
        elif opcion == '3':
            id_venta = int(input("ID venta a anular: "))
            anular_venta(id_venta)
        elif opcion == '0':
            break
        else:
            print("Opción inválida, intente nuevamente.")

def main():
    while True:
        print("\n=== Sistema SkyRoute ===")
        print("1. Gestión de Clientes")
        print("2. Gestión de Destinos")
        print("3. Gestión de Ventas")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            menu_clientes()
        elif opcion == '2':
            menu_destinos()
        elif opcion == '3':
            menu_ventas()
        elif opcion == '0':
            print("Gracias por usar SkyRoute. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()