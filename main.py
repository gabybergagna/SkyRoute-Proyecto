from gestion_clientes import agregar_cliente, listar_clientes, modificar_cliente, eliminar_cliente
from gestion_destinos import agregar_destino, listar_destinos, modificar_destino, eliminar_destino
from gestion_ventas import registrar_venta, listar_ventas, agregar_detalle_venta, actualizar_total_venta
from gestion_arrepentimientos import solicitar_arrepentimiento, actualizar_estado_arrepentimiento
from conexion_base_datos import ejecutar_query
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
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            dni = input("DNI: ")
            email = input("Correo electrónico: ")
            telefono = input("Teléfono (opcional): ")
            try:
                agregar_cliente(nombre, apellido, dni, email, telefono)
                print("Cliente agregado correctamente.")
            except Exception as e:
                print(f"Error al agregar cliente: {e}")
        elif opcion == '2':
            print("\n--- Lista de Clientes ---")
            clientes = listar_clientes()
            if clientes:
                for c in clientes:
                    print(f"ID: {c['id_cliente']}, Nombre: {c['nombre']} {c['apellido']}, DNI: {c['dni']}, Email: {c['email']}, Teléfono: {c['telefono']}")
            else:
                print("No hay clientes registrados.")
        elif opcion == '3':
            try:
                id_c = int(input("ID cliente a modificar: "))
                nombre = input("Nuevo nombre: ")
                apellido = input("Nuevo apellido: ")
                dni = input("Nuevo DNI: ")
                email = input("Nuevo correo: ")
                telefono = input("Nuevo teléfono (opcional): ")
                modificar_cliente(id_c, nombre, apellido, dni, email, telefono)
                print("Cliente modificado correctamente.")
            except ValueError:
                print("ID de cliente inválido. Debe ser un número entero.")
            except Exception as e:
                print(f"Error al modificar cliente: {e}")
        elif opcion == '4':
            try:
                id_c = int(input("ID cliente a eliminar: "))
                confirm = input(f"¿Está seguro de eliminar al cliente con ID {id_c}? (s/n): ").lower()
                if confirm == 's':
                    eliminar_cliente(id_c)
                    print("Cliente eliminado correctamente.")
                else:
                    print("Eliminación cancelada.")
            except ValueError:
                print("ID de cliente inválido. Debe ser un número entero.")
            except Exception as e:
                print(f"Error al eliminar cliente: {e}")
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
            ciudad_origen = input("Ciudad de Origen: ")
            ciudad_destino = input("Ciudad de Destino: ")
            try:
                precio_base = float(input("Precio base: "))
                duracion_estimada = int(input("Duración estimada (días): "))
                agregar_destino(ciudad_origen, ciudad_destino, precio_base, duracion_estimada)
                print("Destino agregado correctamente.")
            except ValueError:
                print("Precio base o duración inválida. Deben ser números.")
            except Exception as e:
                print(f"Error al agregar destino: {e}")
        elif opcion == '2':
            print("\n--- Lista de Destinos ---")
            destinos = listar_destinos()
            if destinos:
                for d in destinos:
                    print(f"ID: {d['id_destino']}, Origen: {d['ciudad_origen']}, Destino: {d['ciudad_destino']}, Precio: {d['precio_base']:.2f}, Duración: {d['duracion_estimada']} días")
            else:
                print("No hay destinos registrados.")
        elif opcion == '3':
            try:
                id_d = int(input("ID destino a modificar: "))
                ciudad_origen = input("Nueva Ciudad de Origen: ")
                ciudad_destino = input("Nueva Ciudad de Destino: ")
                precio_base = float(input("Nuevo Precio base: "))
                duracion_estimada = int(input("Nueva Duración estimada (días): "))
                modificar_destino(id_d, ciudad_origen, ciudad_destino, precio_base, duracion_estimada)
                print("Destino modificado correctamente.")
            except ValueError:
                print("ID, precio base o duración inválida.")
            except Exception as e:
                print(f"Error al modificar destino: {e}")
        elif opcion == '4':
            try:
                id_d = int(input("ID destino a eliminar: "))
                confirm = input(f"¿Está seguro de eliminar el destino con ID {id_d}? (s/n): ").lower()
                if confirm == 's':
                    eliminar_destino(id_d)
                    print("Destino eliminado correctamente.")
                else:
                    print("Eliminación cancelada.")
            except ValueError:
                print("ID de destino inválido.")
            except Exception as e:
                print(f"Error al eliminar destino: {e}")
        elif opcion == '0':
            break
        else:
            print("Opción inválida, intente nuevamente.")

def menu_ventas():
    while True:
        print("\n--- Gestión de Ventas ---")
        print("1. Registrar nueva venta")
        print("2. Agregar destino a una venta (detalle de venta)")
        print("3. Listar todas las ventas (con detalles resumidos)")
        print("4. Solicitar Arrepentimiento / Cancelación de Venta")
        print("5. Gestionar estado de Arrepentimiento") # Para aprobar/rechazar
        print("0. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            try:
                print("\n--- Clientes disponibles ---")
                clientes_disp = listar_clientes()
                for c in clientes_disp:                    
                    print(f"ID: {c['id_cliente']}, Nombre: {c['nombre']} {c['apellido']}")
                id_cliente = int(input("ID del cliente para la venta: "))
                id_nueva_venta = registrar_venta(id_cliente)
                if id_nueva_venta:
                    print(f"Venta registrada con ID: {id_nueva_venta}. Ahora agregue los destinos a esta venta.")
                else:
                    print("No se pudo registrar la venta. Verifique el ID del cliente o la conexión.")
            except ValueError:
                print("ID de cliente inválido. Debe ser un número entero.")
            except Exception as e:
                print(f"Error al registrar venta: {e}")

        elif opcion == '2':
            try:
                print("\n--- Ventas disponibles para agregar detalles ---")
                ventas_disp = listar_ventas()
                for v in ventas_disp:
                    print(f"ID: {v['id_venta']}, Cliente: {v['id_cliente']}, Total: {v['total']:.2f}, Estado: {v['estado']}")
                print("\n--- Destinos disponibles ---")
                destinos_disp = listar_destinos()
                for d in destinos_disp:
                    print(f"ID: {d['id_destino']}, Destino: {d['ciudad_destino']}, Precio: {d['precio_base']:.2f}")

                id_venta = int(input("ID de la venta a la que desea agregar un destino: "))
                id_destino = int(input("ID del destino a agregar: "))
                cantidad = int(input("Cantidad de este destino (ej. número de pasajes): "))

                if cantidad <= 0:
                    print("La cantidad debe ser un número positivo.")
                    continue

                agregar_detalle_venta(id_venta, id_destino, cantidad)
                print(f"Destino {id_destino} (cantidad {cantidad}) agregado a la venta {id_venta}. Total de la venta actualizado.")
            except ValueError:
                print("ID de venta, ID de destino o cantidad inválida. Deben ser números enteros.")
            except Exception as e:
                print(f"Error al agregar detalle de venta: {e}")

        elif opcion == '3':
            print("\n--- Listado de Ventas ---")
            ventas = listar_ventas()
            if ventas:
                for v in ventas:
                    print(f"Venta ID: {v['id_venta']}, Cliente ID: {v['id_cliente']}, Fecha: {v['fecha_venta']}, Total: {v['total']:.2f}, Estado: {v['estado']}")
                    # OPCIONAL: Para mostrar los detalles de la venta, puedes descomentar y ajustar esto
                    try:
                        detalles = ejecutar_query(f"SELECT d.ciudad_destino, dv.cantidad, dv.subtotal FROM detalle_venta dv JOIN destinos d ON dv.id_destino = d.id_destino WHERE dv.id_venta = {v['id_venta']}", fetch=True)
                        if detalles:
                            print("  Detalles:")
                            for det in detalles:
                             print(f"    - {det['ciudad_destino']} (x{det['cantidad']}) - Subtotal: {det['subtotal']:.2f}")
                    except Exception as e:                                               
                     print(f"  Error al obtener detalles: {e}")
            else:
                print("No hay ventas registradas.")

        elif opcion == '4':
            try:
                id_venta = int(input("ID de la venta para solicitar arrepentimiento: "))
                motivo = input("Motivo de la solicitud de arrepentimiento: ")
                solicitar_arrepentimiento(id_venta, motivo)
            except ValueError:
                print("ID de venta inválido.")
            except Exception as e:
                print(f"Error al solicitar arrepentimiento: {e}")

        elif opcion == '5':
            print("\n--- Gestión de Estado de Arrepentimientos ---")
            arrepentimientos_query = """
            SELECT a.id_arrepentimiento, a.id_venta, v.fecha_venta, a.fecha_solicitud, a.motivo, a.estado
            FROM arrepentimientos a
            JOIN ventas v ON a.id_venta = v.id_venta
            ORDER BY a.fecha_solicitud DESC
            """
            arrepentimientos_todos = ejecutar_query(arrepentimientos_query, fetch=True)
            if arrepentimientos_todos:
                print("--- Listado de Solicitudes de Arrepentimiento ---")
                for arrep in arrepentimientos_todos:
                    print(f"  ID Arrep: {arrep['id_arrepentimiento']}, Venta ID: {arrep['id_venta']}, "
                          f"Fecha Venta: {arrep['fecha_venta']}, Solicitud: {arrep['fecha_solicitud']}, "
                          f"Motivo: '{arrep['motivo']}', Estado: {arrep['estado']}")
                try:
                    id_arrep = int(input("\nID del arrepentimiento a gestionar: "))
                    nuevo_estado = input("Nuevo estado ('Aprobado'/'Rechazado'/'Pendiente'): ").capitalize()
                    actualizar_estado_arrepentimiento(id_arrep, nuevo_estado)
                except ValueError:
                    print("ID de arrepentimiento inválido o estado no reconocido.")
                except Exception as e:
                    print(f"Error al actualizar estado del arrepentimiento: {e}")
            else:
                print("No hay solicitudes de arrepentimiento registradas.")

        elif opcion == '0':
            break
        else:
            print("Opción inválida, intente nuevamente.")

def main():
    while True:
        print("\n=== Sistema SkyRoute ===")
        print("1. Gestión de Clientes")
        print("2. Gestión de Destinos")
        print("3. Gestión de Ventas y Arrepentimientos")
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