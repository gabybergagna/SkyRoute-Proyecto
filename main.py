# Inicio del sistema
print("="*50)
print("         Bienvenidos al Sistema de SkyRoute")
print("="*50)

while True:
    print("\nMenú Principal:")
    print("1. Gestionar Clientes")
    print("2. Gestionar Destinos")
    print("3. Registrar Venta")
    print("4. Botón de Arrepentimiento")
    print("5. Consultas")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("\n--- Gestión de Clientes ---")
        print("1. Ver Clientes")
        print("2. Agregar Cliente")
        print("3. Modificar Cliente")
        print("4. Eliminar Cliente")
        input("Seleccione una opción (Simulación de acción): ")
        print("Acción simulada: operación realizada con éxito.")

    elif opcion == "2":
        print("\n--- Gestión de Destinos ---")
        print("1. Ver Destinos")
        print("2. Agregar Destino")
        print("3. Modificar Destino")
        print("4. Eliminar Destino")
        input("Seleccione una opción (Simulación de acción): ")
        print("Acción simulada: operación realizada con éxito.")

    elif opcion == "3":
        print("\n--- Registro de Venta ---")
        input("Ingrese datos de la venta (Simulación de ingreso): ")
        print("Venta registrada exitosamente (Simulado).")

    elif opcion == "4":
        print("\n--- Botón de Arrepentimiento ---")
        input("Ingrese número de venta a cancelar (Simulación): ")
        print("Venta cancelada exitosamente (Simulado).")

    elif opcion == "5":
        print("\n--- Consultas ---")
        print("1. Ver todas las ventas")
        print("2. Filtrar por cliente")
        print("3. Filtrar por destino")
        input("Seleccione una opción (Simulación de consulta): ")
        print("Resultados simulados: muestra de ventas filtradas.")

    elif opcion == "0":
        print("\nGracias por utilizar el sistema de SkyRoute. ¡Hasta pronto!")
        break

    else:
        print("Opción inválida. Intente nuevamente.")
