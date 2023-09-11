from lista_piezas import lista_piezas
mi_tablero = lista_piezas()


def configuracion_tablero():
    print("")
    print("")
    print("-----------------------Coloréalo-----------------------")
    print("Por favor ingrese el ancho del tablero")
    print("-----------------------Guatematel-----------------------")
    filas = input(">")
    print("-----------------------Coloréalo-----------------------")
    print("Por favor ingrese el alto del tablero")
    print("-----------------------Guatematel-----------------------")
    columnas = input(">")
    print("-----------------------Coloréalo-----------------------")
    # Creo todas las piezas de mi tablero
    mi_tablero.inicializar_tablero(int(filas), int(columnas))
    mi_tablero.filas = int(filas)
    mi_tablero.columnas = int(columnas)
    # Verificamos que mi tablero se haya creado correctamente
    mi_tablero.imprimir_tablero_en_consola()

    # Sentinela de agregar nueva pieza
    nueva_pieza = True
    while nueva_pieza:
        print("-----------------------Coloréalo-----------------------")
        print("Por favor elija su color")
        print("AZUL")
        print("ROJO")
        print("VERDE")
        print("PÚRPURA")
        print("NARANJA")
        print("-----------------------Guatematel-----------------------")
        color = input(">")
        print("-----------------------Coloréalo-----------------------")
        print("Por favor ingrese la fila en que desea colocar la pieza")
        print("Rango: 1 - "+ filas)
        print("-----------------------Guatematel-----------------------")
        fila = input(">")
        print("-----------------------Coloréalo-----------------------")
        print("Por favor ingrese la columna en que desea colocar la pieza")
        print("Rango: 1 - "+ filas)
        print("-----------------------Guatematel-----------------------")
        columna = input(">")
        mi_tablero.actualizar_pieza(int(fila), int(columna), color)
        print("")
        print("")
        mi_tablero.imprimir_tablero_en_consola()
        # Preguntamos si desea agregar otra pieza
        respuesta = input("Desea agregar otra pieza S/N: ")
        print("")
        print("")
        if respuesta == "N" or respuesta == "n":
            nueva_pieza = False
    print("=============================FIN CONFIGURACIÓN PIEZAS=================================")
    mi_tablero.imprimir_tablero_en_consola()
    print("=============================FIN CONFIGURACIÓN TABLERO=================================")
    print("")
    print("")
    # Deberiamos graficar
    mi_tablero.graficar()


def mostrar_menu():
    print("")
    print("")
    print("-----------------------Coloréalo-----------------------")
    print("1. Configurar tablero")
    print("2. Mostrar datos del Estudiante")
    print("3. Salir")
    print("-----------------------Guatematel-----------------------")
    opcion = input(">")
    while True:
        if opcion == "1":
            print("")
            configuracion_tablero()
            break
        elif opcion == "3":
            print("Hasta la próxima")
            break
        elif opcion == "2":
            print("Andrés Emilio Peñate Hernández")
            print("201708550")
            print("Introduccion a la programacion y computación 2 'D'")
            print("Ingenieria en Ciencias y Sistemas")
            print("Tercer y Cuarto Semestre")
        else:
            print("Indique una opción válida")
            mostrar_menu()


mostrar_menu()