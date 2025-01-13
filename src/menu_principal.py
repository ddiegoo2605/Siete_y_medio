import jugadores
import random
#Imports


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
            print("Jugar. Todavia falta por implementar")
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
            return menu_principal()
            

def new_human_player():
    correcto = False
    while correcto == False:
        name = input("Name:\n")
        correcto = verificar_nombre(name)
    print(f"Name: \t\t{name}")
    correcto = False
    es_unico = False
    while correcto == False or es_unico == False:
        nif = input("NIF:\n")
        correcto = verificar_nif(nif)
        claves_nif = list(jugadores.jugadores.keys())
        existentes = 0
        for i in range(len(claves_nif)):
            if nif == claves_nif[i]:
                print(f"NIF:\t\t{nif} already exists")
                existentes += 1
        if existentes == 0:
            es_unico = True

        
    nif = nif.upper()
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
    correcto = False
    while correcto == False:
        name = input("Name:\n")
        correcto = verificar_nombre(name)
    print(f"Name: \t\t{name}")
    es_unico = False
    while es_unico == False:
        nif = nif_random
        claves_nif = list(jugadores.jugadores.keys())
        existentes = 0
        for i in range(len(claves_nif)):
            if nif == claves_nif[i]:
                existentes += 1
        if existentes == 0:
            es_unico = True
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
        jugadores.jugadores_rankings[nif] = {"earnings": 0 , "games": 0, "minutes":0 }
    elif num_opcion == 2:
        jugador = {"name": name , "human": False,"bank":False,"initialCard":"","priority":0,"type":40,"bet":0,"points":0,"cards":[],"roundPoints":0}
        jugadores.jugadores_rankings[nif] = {"earnings": 0 , "games": 0, "minutes":0 }
    elif num_opcion == 3:
        jugador = {"name": name , "human": False,"bank":False,"initialCard":"","priority":0,"type":30,"bet":0,"points":0,"cards":[],"roundPoints":0}
        jugadores.jugadores_rankings[nif] = {"earnings": 0 , "games": 0, "minutes":0 }
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



#   TERCERA OPCIÓN

def playGame():
    set_cards = False
    if set_cards == False:
        print("Set cards first")
        return menu_principal
    else:
        jugadores.imprimir_titulo("PLAY GAME")
        menu = ("1)View Stats\n2)View Game Stats\n3)Set Bet\n4)Order Card\n5)Automatic Play\n6)Stand")
        correcto = False
        while correcto == False:
            option = input("Option:\n")
            if option.isdigit():
                num_opcion = int(option)
                if 1 <= num_opcion <= 6:
                    print(f"Número válido: {num_opcion}!")
                    correcto = True 
                else:
                    print("El número no está entre 1 y 6. Inténtalo de nuevo.")
            else:
                print("Por favor, introduce un número válido (entero).")
        if num_opcion == 1:
        
        elif num_opcion == 2:

        elif num_opcion == 3:
        
        elif num_opcion == 4:
        
        elif num_opcion == 5:
        
        elif num_opcion == 6:
            return menu_principal()

def humanRound(id, mazo):
    

#   CUARTA OPCIÓN

def cuarta_opcion():
    menu = "1)Players With More Earnings\n2)Players With More Gmes Played\n3)Players With More Minutes Played\4)Go back"
    print(menu)
    correcto = False
    while correcto == False:
        option = input("Option:\n")
        if option.isdigit():
            num_opcion = int(option)
            if 1 <= num_opcion <= 4:
                print(f"Número válido: {num_opcion}!")
                correcto = True 
            else:
                print("El número no está entre 1 y 4. Inténtalo de nuevo.")
        else:
            print("Por favor, introduce un número válido (entero).")
    if num_opcion == 1:
       return players_with_more_earnigns()
    elif num_opcion == 2:
        return players_with_more_earnigns()
    elif num_opcion == 3:
        return players_with_more_minutes()
    elif num_opcion == 4:
        return menu_principal()
    
def players_with_more_earnigns():
    claves = ordenar_diccionario(jugadores.jugadores_rankings,criterio="earnings",orden="desc")
    jugadores.imprimir_titulo("RANKING")
    for i in range(len(claves)):
        print(f"{claves[i]}  {jugadores.jugadores[claves[i]]["name"]}   {jugadores.jugadores_rankings[claves[i]]["earnings"]}  {jugadores.jugadores_rankings[claves[i]]["games"]}    {jugadores.jugadores_rankings[claves[i]]["minutes"]}")

    
def players_with_more_games():
    claves = ordenar_diccionario(jugadores.jugadores_rankings,criterio="games",orden="desc")
    jugadores.imprimir_titulo("RANKING")
    for i in range(len(claves)):
        print(f"{claves[i]}  {jugadores.jugadores[claves[i]]["name"]}   {jugadores.jugadores_rankings[claves[i]]["earnings"]}  {jugadores.jugadores_rankings[claves[i]]["games"]}    {jugadores.jugadores_rankings[claves[i]]["minutes"]}")

def players_with_more_minutes():
    claves = ordenar_diccionario(jugadores.jugadores_rankings,criterio="minutes",orden="desc")
    jugadores.imprimir_titulo("RANKING")
    for i in range(len(claves)):
        print(f"{claves[i]}  {jugadores.jugadores[claves[i]]["name"]}   {jugadores.jugadores_rankings[claves[i]]["earnings"]}  {jugadores.jugadores_rankings[claves[i]]["games"]}    {jugadores.jugadores_rankings[claves[i]]["minutes"]}")


#   QUINTA OPCIÓN   


#    GENERADOR DE NIF'S
def nif_random():
    
    letrasDni = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
    num = random.randrange(10000000,99999999)
    dni_num = num
    num = num%23
    nif = str(dni_num) + letrasDni[num]
    return nif

def verificar_nif(nif):
    if len(nif) == 9:
        if nif[:8].isdigit():
            letrasDni = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
            num = int(nif[:8])
            num = num%23
            if letrasDni[num] == nif[8].upper():
                return True
            else:
                print("Wrong NIF")
                return False

        else:
            print("Wrong NIF")
            return False

    else:
        print("Wrong NIF")
        return False
def verificar_nombre(name):
    if name.isalpha():
        return True
    else:
        print("Wrong Name. please, enter a name no empty with only letters")
        return False

def ordenar_diccionario(diccionario,criterio ="",orden="asc",):
    claves = list(jugadores.jugadores_rankings.keys())
    if criterio == "":
        for pasadas in range(len(claves)-1):
            cambios = False
            for i in range(len(claves)-1-pasadas):
                if orden == "asc":
                    if claves[i] > claves[i+1]:
                        cambios = True
                        aux = claves[i]
                        claves[i] = claves[i+1]
                        claves[i+1] = aux
                else:
                    if claves[i] < claves[i+1]:
                        cambios = True
                        aux = claves[i]
                        claves[i] = claves[i+1]
                        claves[i+1] = aux
            if not cambios:
                return claves
    elif criterio == "earnings":
        if type(diccionario[claves[0]][criterio]) in (int,float,str):
            for pasadas in range(len(claves) - 1):
                cambios = False
                for i in range(len(claves) - 1 - pasadas):
                    if orden == "asc":
                        if diccionario[claves[i]][criterio] > diccionario[claves[i + 1]][criterio]:
                            cambios = True
                            aux = claves[i]
                            claves[i] = claves[i + 1]
                            claves[i + 1] = aux
                    else:
                        if diccionario[claves[i]][criterio] < diccionario[claves[i + 1]][criterio]:
                            cambios = True
                            aux = claves[i]
                            claves[i] = claves[i + 1]
                            claves[i + 1] = aux
                if not cambios:
                    return claves
    elif criterio == "games":
        if type(diccionario[claves[0]][criterio]) in (int,float,str):
            for pasadas in range(len(claves) - 1):
                cambios = False
                for i in range(len(claves) - 1 - pasadas):
                    if orden == "asc":
                        if diccionario[claves[i]][criterio] > diccionario[claves[i + 1]][criterio]:
                            cambios = True
                            aux = claves[i]
                            claves[i] = claves[i + 1]
                            claves[i + 1] = aux
                    else:
                        if diccionario[claves[i]][criterio] < diccionario[claves[i + 1]][criterio]:
                            cambios = True
                            aux = claves[i]
                            claves[i] = claves[i + 1]
                            claves[i + 1] = aux
                if not cambios:
                    return claves
    elif criterio == "minutes":
        if type(diccionario[claves[0]][criterio]) in (int,float,str):
            for pasadas in range(len(claves) - 1):
                cambios = False
                for i in range(len(claves) - 1 - pasadas):
                    if orden == "asc":
                        if diccionario[claves[i]][criterio] > diccionario[claves[i + 1]][criterio]:
                            cambios = True
                            aux = claves[i]
                            claves[i] = claves[i + 1]
                            claves[i + 1] = aux
                    else:
                        if diccionario[claves[i]][criterio] < diccionario[claves[i + 1]][criterio]:
                            cambios = True
                            aux = claves[i]
                            claves[i] = claves[i + 1]
                            claves[i + 1] = aux
                if not cambios:
                    return claves
    
menu_principal()