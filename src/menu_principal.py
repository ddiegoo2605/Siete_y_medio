import Players
import random



def menu_principal():
    while True:
        titulo = "JUEGO SIETE Y MEDIO"
        largo_titulo = len(titulo)
        margen = 20 
        largo_linea = largo_titulo + margen * 2 
        espacio = " " * margen

        menu ="\n" + "-" * largo_linea+ "\n"+ "-" * margen + titulo.center(largo_linea - margen * 2) + "-" * margen + "\n" + "-" * largo_linea + "\n"+ espacio + "MENÚ PRINCIPAL" + "\n"

        print(menu)
        opciones = [
            "1. Add/Remove/Show Players",
            "2. Settings",
            "3. Play Game",
            "4. Ranking",
            "5. Reports",
            "6. Exit"
        ]
        
        for opcion in opciones:
            print(f"{espacio}{opcion}")
        

        seleccion = input("\n"+ espacio +"Selecciona una opción (1-6): ")

        if seleccion == '1':
           primera_opcion()
        elif seleccion == '2':
            print("Ajustes. Todavia falta por implementar")
        elif seleccion == '3':
            print("Jugar. Todavia falta por implementar")
        elif seleccion == '4':
            print("Estadísticas. Todavia falta por implementar")
        elif seleccion == '5':
            print("Reportes. Todavia falta por implementar")
        elif seleccion == '6':
            print("\n"+"Gracias por jugar, hasta la próxima")
            print("\n"+ "#" * largo_linea)
            break
        else:
            print("Error. Escoge una opción valida entre (1-6)")


#PRIMER OPCIÓN
def primera_opcion():
    flg00 = True
    while flg00:
        menu = "1)New Human Player\n2)New Boot\n3)Show/Remove Player\n4)Go Back"
        print(menu)
        correcto = False
        while correcto == False:
                option = input("Option:\n")
                if option.isdigit():
                    num_opcion = int(option)
                    if 1 <= num_opcion <= 4:
                        print(f"¡Número válido: {num_opcion}!")
                        correcto = True 
                    else:
                        print("El número no está entre 1 y 3. Inténtalo de nuevo.")
                else:
                    print("Por favor, introduce un número válido (entero).")
        if num_opcion == 1:
            new_human_player()
            
        elif num_opcion == 2:
            new_boot()
        elif num_opcion == 3:
            show_remove()
        elif num_opcion == 4:
            flg00 = False
            menu_principal()
            

def new_human_player():
    name = input("Name:\n")
    print(f"Name: \t\t{name}")
    nif = input("NIF:\n")
    print(f"NIF: \t\t{nif}")
    menu_juego_persona = "Select your Profile:\n\n1)Cautious\n\n2)Moderated\n\n3)Bold"
    print(menu_juego_persona)
    correcto = False
    while correcto == False:
            option = input("Option:\n")
            if option.isdigit():
                num_opcion = int(option)
                if 1 <= num_opcion <= 3:
                    print(f"¡Número válido: {num_opcion}!")
                    correcto = True 
                else:
                    print("El número no está entre 1 y 3. Inténtalo de nuevo.")
            else:
                print("Por favor, introduce un número válido (entero).")

    if num_opcion == 1:
        jugador = {"name": name , "human": True,"bank":False,"initialCard":"","priority":0,"type":50,"bet":0,"points":0,"cards":[],"roundPoints":0}
    elif num_opcion == 2:
        jugador = {"name": name , "human": True,"bank":False,"initialCard":"","priority":0,"type":40,"bet":0,"points":0,"cards":[],"roundPoints":0}

    elif num_opcion == 3:
        jugador = {"name": name , "human": True,"bank":False,"initialCard":"","priority":0,"type":30,"bet":0,"points":0,"cards":[],"roundPoints":0}
    
    correcto = False
    while correcto == False:    
        crear = input("Is ok ? Y/n:")
        if crear == 'Y':
            jugadores.jugadores[nif] = jugador
            #HAY QUE HACER QUE SE GUARDE EN EL DICCIONARIO
            primera_opcion()
            return
        elif crear == 'n':
            primera_opcion()
            correcto = True
            return
        else:
            print("Invalid option")

def new_boot():
    name = input("Name:\n")
    print(f"Name: \t\t{name}")
    nif = nif_random()
    menu_juego_persona = "Select Profile For The New Boot:\n\n1)Cautious\n\n2)Moderated\n\n3)Bold"
    print(menu_juego_persona)
    correcto = False
    while correcto == False:
            option = input("Option:\n")
            if option.isdigit():
                num_opcion = int(option)
                if 1 <= num_opcion <= 3:
                    print(f"¡Número válido: {num_opcion}!")
                    correcto = True 
                else:
                    print("El número no está entre 1 y 3. Inténtalo de nuevo.")
            else:
                print("Por favor, introduce un número válido (entero).")

    if num_opcion == 1:
        jugador = {"name": name , "human": False,"bank":False,"initialCard":"","priority":0,"type":50,"bet":0,"points":0,"cards":[],"roundPoints":0}
    elif num_opcion == 2:
        jugador = {"name": name , "human": False,"bank":False,"initialCard":"","priority":0,"type":40,"bet":0,"points":0,"cards":[],"roundPoints":0}

    elif num_opcion == 3:
        jugador = {"name": name , "human": False,"bank":False,"initialCard":"","priority":0,"type":30,"bet":0,"points":0,"cards":[],"roundPoints":0}
    correcto = False
    while correcto == False:    
        crear = input("Is ok ? Y/n:")
        if crear == 'Y':
            jugadores.bots[nif] = jugador
            #HAY QUE HACER QUE SE GUARDE EN EL DICCIONARIO
            correcto = True
            primera_opcion()
            return
        elif crear == 'n':
            primera_opcion()
            correcto = True
            return
        else:
            print("Invalid option")

def show_remove():
    jugadores.imprimir_titulo("SHOW REMOVE")
    dnis_bots = list(jugadores.bots.keys())
    dnis = list(jugadores.jugadores.keys())
    for i in range(len(jugadores.bots)):
        print(i)
        if jugadores.bots[dnis_bots[i]]["type"] == 50:
            type_bot = "Ambicious"
        elif jugadores.bots[dnis_bots[i]]["type"] == 40:
            type_bot = "Moderated"
        elif jugadores.bots[dnis_bots[i]]["type"] == 30:
            type_bot = "Bold"
        if jugadores.jugadores[dnis[i]]["type"] == 50:
            type = "Ambicious"
        elif jugadores.jugadores[dnis[i]]["type"] == 40:
            type = "Moderated"
        elif jugadores.jugadores[dnis[i]]["type"] == 30:
            type = "Bold"
        if len(jugadores.bots) > len(jugadores.jugadores):
            if i >= len(jugadores.jugadores) + 1:
                print(f"{dnis_bots[i]} {jugadores.bots[dnis_bots[i]]['name']} {type_bot} ||")
            else:
                print(f"{dnis_bots[i]} {jugadores.bots[dnis_bots[i]]['name']} {type_bot} || {dnis[i]} {jugadores.jugadores[dnis[i]]['name']} {type} ")

        elif len(jugadores.bots) < len(jugadores.jugadores):
            if i >= len(jugadores.bots) + 1:
                print(f"{dnis[i]} {jugadores.jugadores[dnis[i]]['name']} {type}")
            else:
                print(f"{dnis_bots[i]} {jugadores.bots[dnis_bots[i]]['name']} {type_bot} || {dnis[i]} {jugadores.jugadores[dnis[i]]['name']} {type} ")
        else:
            print(f"{dnis_bots[i]} {jugadores.bots[dnis_bots[i]]['name']} {type_bot} || {dnis[i]} {jugadores.jugadores[dnis[i]]['name']} {type} ")



#    SEGUNDA OPCIÓN



#    GENERADOR DE NIF'S
def nif_random():
    
    letrasDni = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
    num = random.randrange(10000000,99999999)
    dni_num = num
    num = num%23
    nif = str(dni_num) + letrasDni[num]
    return nif

menu_principal()

if __name__ == "__main__":
    menu_principal()

