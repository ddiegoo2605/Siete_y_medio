#Carpeta de pruebas para ejecutar cualquiera de las carpetas previas
from random import choice, randint
from cartas import baraja_española, baraja_poker
from jugadores import mostrar_jugadores  # Importamos mostrar_jugadores() del archivo jugadores.py
from titulos_ascii import calcular_ancho_terminal, titulo_settings



def elegir_baraja():
    print("\nElige una baraja:\n1) Baraja Española\n2) Baraja de Poker\n3) Go back")
    correcto = False
    while correcto == False:    
        eleccion = input("\nOpción: ")
        if eleccion.isdigit():
            eleccion = int(eleccion)
            if 1 >= eleccion <= 3:
                correcto = True
        else:
            print("Por favor, introduce un número.")
    if eleccion == 1:
        print("\nHas elegido la Baraja Española.")
        input("Pulsa para continuar: ")
        return baraja_española
    elif eleccion == 2:
        print("\nHas elegido la Baraja de Poker.")
        input()
        return baraja_poker
    else:
        raise ValueError 
        
    
    

#def elegir_dificultad():

def crear_set_jugadores():
    perfiles = ['Cautious', 'Moderated', 'Bold']
    jugadores_partida = {}

    # Mostrar jugadores existentes y seleccionar uno
    print("\nSelecciona un jugador humano para la partida:")
    jugador_humano = mostrar_jugadores()  # Debe devolver un diccionario con los datos del jugador seleccionado
    jugadores_partida[jugador_humano["id"]] = jugador_humano

    # Crear dos bots
    for i in range(1, 3):
        bot = {
            "id": f"BOT{randint(1000, 9999)}",  # ID único
            "name": f"Bot {i}",
            "human": False,
            "perfil": choice(perfiles)
        }
        jugadores_partida[bot["id"]] = bot

    return jugadores_partida

def set_max_rondas():
    while True:
        try:
            rondas = int(input("\nIntroduce el número máximo de rondas (mínimo 5): "))
            if rondas >= 5:
                print(f"Se han establecido {rondas} rondas máximas para la partida.")
                return rondas
            else:
                print("El número de rondas debe ser al menos 5. Inténtalo de nuevo.")
        except ValueError:
            print("Por favor, introduce un número válido.")

def menu_settings():
    while True:
        ancho_terminal = calcular_ancho_terminal()
        print(titulo_settings())
        
        opciones = [
            "\n",
            "\n",
            "1) Set Game Players",
            "2) Set Card's Deck",
            "3) Set Max Rounds (Default 5 Rounds)",
            "4) Go back"
        ]

        for opcion in opciones:
            print(opcion.center(ancho_terminal))
        
        correcto = False
        while not correcto:
            eleccion = input("\n"+"Option: ".center(ancho_terminal))
            if eleccion.isdigit():
                eleccion = int(eleccion)
                if 1 <= eleccion <= 4:
                    correcto = True
                    print(f"¡Número válido: {eleccion}!")
                else:
                    print("El número no está entre 1 y 4. Inténtalo de nuevo.")
                jugadores = crear_set_jugadores()
                print("\nJugadores creados para la partida:".center(ancho_terminal))
                for jugador_id, jugador in jugadores.items():
                    tipo = "Humano" if jugador["human"] else "Bot"
                    print(f"{jugador_id}: {jugador['name']} ({tipo}, {jugador['perfil']})")
            elif eleccion == 2:
                elegir_baraja()
            elif eleccion == 3:
                max_rondas = set_max_rondas()
            elif eleccion == 4:
                print("Volviendo al menú principal...\n".center(ancho_terminal))
            return
                
            
if __name__ == "__main__":
    menu_settings()

