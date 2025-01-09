from cartas import baraja_española, baraja_poker
def mostrar_titulo_settings():
    print("""
     ███████╗███████╗████████╗████████╗██╗███╗   ██╗ ██████╗ ███████╗
     ██╔════╝██╔════╝╚══██╔══╝╚══██╔══╝██║████╗  ██║██╔════╝ ██╔════╝
     ███████╗█████╗     ██║      ██║   ██║██╔██╗ ██║██║  ███╗█████╗  
     ╚════██║██╔══╝     ██║      ██║   ██║██║╚██╗██║██║   ██║██╔══╝  
     ███████║███████╗   ██║      ██║   ██║██║ ╚████║╚██████╔╝███████╗
     ╚══════╝╚══════╝   ╚═╝      ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
    """)


def elegir_baraja():
    print("Elige una baraja, Española o de Poker")
    eleccion = int(input("1 para Baraja Española \n2 para Baraja de Poker: "))

    if eleccion == 1:
        print("Has elegido la Baraja Española.")
        return baraja_española
    elif eleccion == 2:
        print("Has elegido la Baraja de Poker.")
        return baraja_poker
    else:
        raise ValueError 
    


    

    


    
    

jugadores = { "11115555A":{"name":"Mario","human":True,"bank":False,"initialCard":"","priority":0,"type":40,"bet":4,"points":0,"cards":[],"roundPoints":0},
 "22225555A":{"name":"Pedro","human":True,"bank":False,"initialCard":"","priority":0,"type":40,"bet":4,"points":0,"cards":[],"roundPoints":0}
 }
mostrar_titulo_settings()
elegir_baraja()
