#Registro de jugadores, creación de perfiles de juego
jugadores = {}
bots = {}
jugadores_rankings = {}
cardgame = {}
player_game = {}
player_game_round = {}
id_game = 0
seted_player = []
def imprimir_titulo(titulo):
    largo_titulo = len(titulo)
    margen = 20
    largo_linea = largo_titulo + margen * 2
    espacio = " " * margen

    print("\n" + "-" * largo_linea + "\n" + "-" * margen + titulo.center(largo_linea - margen * 2) + "-" * margen + "\n" + "-" * largo_linea)

def registrar_jugador():
    imprimir_titulo("Registro de jugador")
    nombre = input("Introduce tu nombre: ")
    puntos_iniciales = 20

    # Selección del perfil
    print("Selecciona tu perfil de riesgo:" + "\n" + "1. Atrevido (Apuestas altas y arriesgadas)" + "\n" + "2. Normal (Apuestas equilibradas)" + "\n" + "3. Prudente (Apuestas bajas y seguras)")
 
    #COMPROBACIÓN DE QUE SEA UN NÚMERA ADEMÁS DE CORRECTO
    correcto = False
    while correcto == False:
        rango_opcion = input("Elige una opción (1, 2 o 3): ")
        if rango_opcion.isdigit():
            num_opcion = int(rango_opcion)
            if 1 <= num_opcion <= 3:
                print(f"¡Número válido: {num_opcion}!")
                correcto = True 
            else:
                print("El número no está entre 1 y 3. Inténtalo de nuevo.")
        else:
            print("Por favor, introduce un número válido (entero).")


    

    # Asignación del perfil según la opción seleccionada
    if num_opcion == 1:
        rango = 'Atrevido'
    elif num_opcion == 2:
        rango = 'Normal'
    elif num_opcion == 3:
        rango = 'Prudente'

    # Crea un diccionario para el jugador y lo añade a la lista
    jugador = {
        'nombre': nombre,
        'puntos': puntos_iniciales,
        'rango': rango
    }
    jugadores.append(jugador)
    print(f"Jugador {nombre} registrado con éxito con 20 puntos y rango '{rango}'.\n")


def mostrar_jugadores():
    indice = 0
    if not jugadores:
        print("No hay jugadores registrados.")
        return

    print("\n--- Mostrando lista de jugadores ---")
    for jugador in jugadores:
        indice +=1
        print(f"Jugador {indice}: {jugador['nombre']}, Puntos: {jugador['puntos']}, Perfil de riesgo: {jugador['rango']}")
    print()

def eliminar_jugador():
    if not jugadores:
        print("No hay jugadores registrados para eliminar.")
        return

    mostrar_jugadores()

    try:
        # Preguntar al usuario por el índice del jugador a eliminar
        seleccion = int(input("Selecciona el número del jugador a eliminar: "))

        if seleccion < 1 or seleccion > len(jugadores):
            print("Número de jugador no válido. No se puede eliminar.")
            return

        jugador_eliminado = jugadores.pop(seleccion - 1)  # Eliminar al jugador
        print(f"Jugador '{jugador_eliminado['nombre']}' eliminado.")
    except ValueError:
        print("Por favor ingresa un número válido.")
    except IndexError:
        print("No has seleccionado un numero de los jugadores mostrados. No se puede eliminar.")

def imprimir_opciones():
    opciones = [
        "1. Registrar jugador",
        "2. Mostrar jugadores registrados",
        "3. Eliminar jugador",
        "4. Volver al menú principal"
    ]
    espacio = " " * 20
    for opcion in opciones:
        print(f"{espacio}{opcion}")

def gestion_jugadores():
    while True:
        titulo = "Gestión de jugadores"
        largo_titulo = len(titulo)
        margen = 20
        largo_linea = largo_titulo + margen * 2 
        espacio = " " * margen

        print("\n"+"-"* margen + titulo.center(largo_linea - margen * 2) +"-"* margen)
        
        imprimir_opciones()

        correcto = False
        while correcto == False:
            opcion = input("Elige una opción (1, 2 o 3): ")
            if opcion.isdigit():
                num_opcion = int(opcion)
                if 1 <= num_opcion <= 3:
                    print(f"¡Número válido: {num_opcion}!")
                    correcto = True 
                else:
                    print("El número no está entre 1 y 3. Inténtalo de nuevo.")
            else:
                print("Por favor, introduce un número válido (entero).")

        if num_opcion == 1:
            registrar_jugador()
        elif num_opcion == 2:
            mostrar_jugadores()
        elif num_opcion == 3:
            eliminar_jugador()        
        elif num_opcion == 4:
            print("\n Volviendo al menú principal...")
            break

def cabecera_game_over():
    print("""
    *******************************************************************************************************************
                    .d8888b.                                       .d88888b.
                   d88P  Y88b                                     d88P" "Y88b
                   888    888                                     888     888
                   888         8888b.  88888b.d88b.    .d88b.     888     888 888  888  .d88b.  888d888
                   888  88888     "88b 888 "888 "88b d8P   Y8b    888     888 888  888 d8P  Y8b 888P"
                   888    888 .d888888 888  888  888 888888888    888     888 Y88  88P 88888888 888 
                   Y88b  d88P 888  888 888  888  888 Y8b.         Y88b. .d88P  Y8bd8P  Y8b.     888
                    "Y8888P88 "Y888888 888  888  888  "Y888888     "Y88888P"    Y88P    "Y88888 888

    *******************************************************************************************************************   
""")



