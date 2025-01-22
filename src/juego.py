import random
from cartas import baraja_española, baraja_poker
from jugadores import jugadores, bots, player_game
from Utilidades import set_max_rondas

def seleccionar_jugadores(jugadores_disponibles=None, bots_disponibles=None):
    """
    Permite al usuario seleccionar jugadores del sistema para la partida.
    """
    jugadores_disponibles = jugadores_disponibles if jugadores_disponibles is not None else jugadores
    bots_disponibles = bots_disponibles if bots_disponibles is not None else bots

    print("Seleccionando jugadores para la partida...")
    print("Lista de jugadores humanos disponibles:")
    for nif, jugador in jugadores_disponibles.items():
        
        print(f"{nif}: {jugador['name']} (humano)")

    print("\nLista de bots disponibles:")
    for nif, bot in bots_disponibles.items():
        print(f"{nif}: {bot['name']} (bot)")

    while True:
        seleccion = input("Introduce el NIF del jugador o bot que deseas añadir (-1 para terminar): ")
        if seleccion == "-1":
            if player_game:
                print("Selección de jugadores completada.")
                break
            else: 
                print("Debes seleccionar al menos un jugador o bot para jugar.")

        elif seleccion in jugadores_disponibles:
            if seleccion in player_game:
                print(f"{jugadores_disponibles[seleccion]['name']} ya está en la partida.")
            else:
                player_game[seleccion] = jugadores_disponibles[seleccion]

                print(f"{jugadores_disponibles[seleccion]['name']} añadido a la partida.")
        elif seleccion in bots_disponibles:
            if seleccion in player_game:
                print(f"{bots_disponibles[seleccion]['name']} ya está en la partida.")
            else:
                player_game[seleccion] = bots_disponibles[seleccion]
                print(f"{bots_disponibles[seleccion]['name']} añadido a la partida.")
        else:
            print("NIF no válido. Inténtalo de nuevo.")
    
    if not player_game:
        print("No se seleccionaron jugadores. Configura al menos uno para jugar.")
        return False
    return True

def repartir_cartas_iniciales(jugadores, mazo):
    """
    Reparte una carta inicial a cada jugador y asigna la banca.
    """
    print("Repartiendo cartas iniciales...\n")
    cartas_asignadas = {}
    for jugador_id, jugador in jugadores.items():
        carta = random.choice(list(mazo.keys()))
        jugador["initialCard"] = carta
        jugador["priority"] = mazo[carta]["priority"]
        print(f"{jugador['name']} recibió {mazo[carta]['literal']}")
        cartas_asignadas[jugador_id] = mazo[carta]["priority"]
    
    # Determinar la banca
    banca_id = max(cartas_asignadas, key=cartas_asignadas.get)  # Jugador con mayor prioridad
    jugadores[banca_id]["bank"] = True
    print(f"\nLa banca es: {jugadores[banca_id]['name']} (con {mazo[jugadores[banca_id]['initialCard']]['literal']})")
    return banca_id

def jugar_partida():
    """
    Lógica principal del juego.
    """
    print("Iniciando configuración del juego...\n")

    # Seleccionar jugadores
    if not seleccionar_jugadores(jugadores, bots):
        return  # Salir si no hay jugadores
    rondas= set_max_rondas()
    if rondas < 5:
        print("El número de rondas debe ser al menos 5. Configurando 5 rondas por defecto.")
        rondas = 5

    # Seleccionar el mazo
    print("Selecciona el mazo con el que jugar:")
    print("1) Baraja Española\n2) Baraja de Póker")
    while True:
        seleccion = input("Opción (1-2): ")
        if seleccion == "1":
            mazo = baraja_española
            break
        elif seleccion == "2":
            mazo = baraja_poker
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")

    # Repartir cartas iniciales y determinar la banca
    banca_id = repartir_cartas_iniciales(player_game, mazo)

    # Inicio del juego
    rondas = 5
    for ronda in range(1, rondas + 1):
        print(f"\n--- Ronda {ronda} ---")

        # Turnos de los jugadores (excluyendo la banca inicialmente)
        for jugador_id, jugador in player_game.items():
            if jugador_id != banca_id:
                print(f"Turno de {jugador['name']}...")
                # Implementa la lógica de turnos de cada jugador aquí

        # Turno de la banca
        print(f"Turno de la banca ({player_game[banca_id]['name']})...")
        # Implementa la lógica específica de la banca aquí

    print("\nJuego terminado.")
