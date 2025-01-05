#Registro de jugadores, creación de perfiles de juego
jugadores = []

def registrar_jugador():
    print("--- Registro de Jugador ---")
    nombre = input("Introduce tu nombre: ").strip()
    puntos_iniciales = 20

    # Selección del perfil
    print("Selecciona tu rango de atrevido:")
    print("1. Atrevido (Apuestas altas y arriesgadas)")
    print("2. Normal (Apuestas equilibradas)")
    print("3. Prudente (Apuestas bajas y seguras)")

    rango_opcion = input("Elige una opción (1, 2 o 3): ").strip()

    # Asignación del perfil según la opción seleccionada
    if rango_opcion == '1':
        rango = 'Atrevido'
    elif rango_opcion == '2':
        rango = 'Normal'
    elif rango_opcion == '3':
        rango = 'Prudente'
    else:
        print("Opción no válida. Registrando como 'Normal' por defecto.")
        rango = 'Normal'

    # Crea un diccionario para el jugador y lo añade a la lista
    jugador = {
        'nombre': nombre,
        'puntos': puntos_iniciales,
        'rango': rango
    }
    jugadores.append(jugador)
    print(f"Jugador {nombre} registrado con éxito con 20 puntos y rango '{rango}'.\n")


def mostrar_jugadores():
    if not jugadores:
        print("No hay jugadores registrados.")
        return

    print("\n--- Mostrando lista de jugadores ---")
    for i, jugador in enumerate(jugadores, start=1):
        print(f"Jugador {i}: {jugador['nombre']}, Puntos: {jugador['puntos']}, Perfil de riesgo: {jugador['rango']}")
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

def gestion_jugadores():
    while True:
        print("\n--- Gestión de jugadores ---")
        print("1. Registrar jugador")
        print("2. Mostrar jugadores registrados")
        print("3. Eliminar jugador")
        print("4. Volver al menú principal")

        opcion = input("Elige una opción: ").strip()

        if opcion == '1':
            registrar_jugador()
        elif opcion == '2':
            mostrar_jugadores()
        elif opcion == '3':
            eliminar_jugador()        
        elif opcion == '4':
            print("\n Volviendo al menú principal...")
            break
        else:
            print("Error. Escoge una opción(1-4)")


# Aquí evitamos la ejecución automática del código cuando se importa el módulo
if __name__ == "__main__":
   
    pass