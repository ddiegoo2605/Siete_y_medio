#Registro de jugadores, creación de perfiles de juego
jugadores = []

def imprimir_titulo(titulo):
    largo_titulo = len(titulo)
    margen = 20
    largo_linea = largo_titulo + margen * 2
    espacio = " " * margen

    print("\n" + "-" * largo_linea)
    print("-" * margen + titulo.center(largo_linea - margen * 2) + "-" * margen)
    print("-" * largo_linea)

def registrar_jugador():
    imprimir_titulo("Registro de jugador")
    nombre = input("Introduce tu nombre: ").strip()
    puntos_iniciales = 20

    # Selección del perfil
    print("Selecciona tu perfil de riesgo:")
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

        opcion = input(f"\n{espacio}Elige una opción: ").strip()

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