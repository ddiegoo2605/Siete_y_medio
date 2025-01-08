import jugadores

def menu_principal():
    while True:
        titulo = "JUEGO SIETE Y MEDIO"
        largo_titulo = len(titulo)
        margen = 20 
        largo_linea = largo_titulo + margen * 2 
        espacio = " " * margen

        print("\n" + "-" * largo_linea)
        print("-" * margen + titulo.center(largo_linea - margen * 2) + "-" * margen)
        print("-" * largo_linea)
        print("\n"+ espacio + "MENÚ PRINCIPAL")
        print("\n")
        opciones = [
            "1. Gestión de jugadores",
            "2. Ajustes",
            "3. Jugar",
            "4. Estadísticas",
            "5. Reportes",
            "6. Salir"
        ]
        
        for opcion in opciones:
            print(f"{espacio}{opcion}")
        

        seleccion = input("\n"+ espacio +"Selecciona una opción (1-6): ")

        if seleccion == '1':
           jugadores.gestion_jugadores()
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
<<<<<<< Updated upstream
=======

#PRIMER OPCIÓN
def primera_opcion():
    menu = "1)New Human Player\n2)New Boot\n3)Show/Remove Player\n4)Go Back"
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

    elif num_opcion == 3:

    elif num_opcion == 4:
        menu_principal()

def new_human_player():
    name = input("Name:\n")
    print(f"Name: \t\t{name}")
    nif = input("NIF:\n")
    print(f"NIF: \t\t\{nif}")
    menu_juego_persona = "Select your Profile:\n\n1)Cautious\n\n2)Moderated\n\n3)Bold"
    print(menu_juego_persona)
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
        jugador = {nif: {"name": name , "human": True,"bank":False,"initialCard":"","priority":0,"type":50,"bet":0,"points":0,"cards":[],"roundPoints":0}}
    elif num_opcion == 2:
        jugador = {nif: {"name": name , "human": True,"bank":False,"initialCard":"","priority":0,"type":40,"bet":0,"points":0,"cards":[],"roundPoints":0}}

    elif num_opcion == 3:
        jugador = {nif: {"name": name , "human": True,"bank":False,"initialCard":"","priority":0,"type":30,"bet":0,"points":0,"cards":[],"roundPoints":0}}


    while correcto == False:    
        crear = input("Is ok ? Y/n:")
        if crear == 'Y':
            jugadores.append(jugador)
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
        jugador = {nif: {"name": name , "human": False,"bank":False,"initialCard":"","priority":0,"type":50,"bet":0,"points":0,"cards":[],"roundPoints":0}}
    elif num_opcion == 2:
        jugador = {nif: {"name": name , "human": False,"bank":False,"initialCard":"","priority":0,"type":40,"bet":0,"points":0,"cards":[],"roundPoints":0}}

    elif num_opcion == 3:
        jugador = {nif: {"name": name , "human": False,"bank":False,"initialCard":"","priority":0,"type":30,"bet":0,"points":0,"cards":[],"roundPoints":0}}

    while correcto == False:    
        crear = input("Is ok ? Y/n:")
        if crear == 'Y':
            bots.append(jugador)
            #HAY QUE HACER QUE SE GUARDE EN EL DICCIONARIO
            primera_opcion()
            return
        elif crear == 'n':
            primera_opcion()
            correcto = True
            return
        else:
            print("Invalid option")

def show_remove_minecraft():
    pass
#    SEGUNDA OPCIÓN



#    GENERADOR DE NIF'S
def nif_random():
    
    letrasDni = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
    num = random.randrange(10000000,99999999)
    dni_num = num
    num = num%23
    nif = str(dni_num) + letrasDni[num]
    return nif

>>>>>>> Stashed changes
if __name__ == "__main__":
    menu_principal()
