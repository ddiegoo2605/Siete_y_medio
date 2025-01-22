import jugadores
import random
import titulos_ascii
import jugadores
from Utilidades import menu_settings
import random

import cartas

from juego import jugar_partida

#Funciones

import conexion
#Imports





def menu_principal():
    while True:
      
        
        opciones = [
            "\n",
            "\n",
            "1. Players",
            "2. Settings",
            "3. Play Game",
            "4. Ranking",
            "5. Reports",
            "6. Exit"
        ]
        
        for opcion in opciones:
            print(opcion)
        

        seleccion = input("\n"+"Selecciona una opción (1-6): ")

        if seleccion == '1':
            return primera_opcion()
        elif seleccion == '2':
            menu_settings()
            
        elif seleccion == '3':
            jugar_partida()
        elif seleccion == '4':
            cuarta_opcion()
        elif seleccion == '5':
            print("Reportes. Todavia falta por implementar")
        elif seleccion == '6':
            
            print("\n"+"Gracias por jugar, hasta la próxima")
            break
        else:
            print("Error. Escoge una opción valida entre (1-6)")


#PRIMER OPCIÓN
def primera_opcion():
    flg00 = True
    while flg00:
        


        menu = [
        "\n",
        "\n",
        "1)New Human Player",
        "2)New Boot",
        "3)Show/Remove Player",
        "4)Go Back",
        ]
        for opcion in menu:
            print(opcion) 
        
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
            id = ""
            while not id == "-1":    
                show_players()
                id = input(" Introduce -id para eliminar, -1 para retroceder:\n")
                eliminar_jugador(id)
                
        elif num_opcion == 4:
            flg00 = False
            menu_principal()
            

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
        if crear == 'Y' or crear == 'y':
            jugadores.jugadores[nif] = jugador
            agregar_jugador_bdd(jugador,nif,quien = "jugadores")
            #HAY QUE HACER QUE SE GUARDE EN EL DICCIONARIO

            primera_opcion()
            return
        elif crear == 'n' or crear == 'N':
            primera_opcion()

            return primera_opcion()
        elif crear == 'n':

            correcto = True
            return primera_opcion()
        else:
            print("Invalid option")

def new_boot():
    correcto = False
    while correcto == False:
        name = input("Name:\n")
        correcto = verificar_nombre(name)
    print(f"Name: \t\t{name}")
    es_unico = False
    while not es_unico:
        nif = nif_random()
        if nif not in jugadores.jugadores.keys() and nif not in jugadores.bots.keys():
            es_unico = True
        menu_juego_persona = "Select Profile For The New Boot:\n\n1)Cautious\n\n2)Moderated\n\n3)Bold"
        claves_nif = list(jugadores.jugadores.keys())
        existentes = 0
        for i in range(len(claves_nif)):
            if nif == claves_nif[i]:
                existentes += 1
        if existentes == 0:
            es_unico = True
    menu_juego_persona = "Select Profile For The New Boot:\n\n1)Cautious\n\n2)Moderated\n\n3)Bold"
    print(menu_juego_persona)
    while True:
        option = input("Option:\n")
        if option.isdigit():
            num_opcion = int(option)
            if 1 <= num_opcion <= 3:
                print(f"¡Número válido: {num_opcion}!")
                break
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
        if crear == 'Y' or crear == 'y':
            jugadores.bots[nif] = jugador
            agregar_jugador_bdd(jugador, nif, quien="bots")
            #HAY QUE HACER QUE SE GUARDE EN EL DICCIONARIO
            correcto = True

            primera_opcion()
            return
        elif crear == 'n' or crear == 'N':
            primera_opcion()

            return primera_opcion()
        elif crear == 'n':

            correcto = True
            return primera_opcion()
            
        else:
            print("opción no válida. Introduce 'y' o 'n'.")

def show_players():
    botardo = {}
    jugadorazos = {}
    cursor = conexion.conexion.cursor()
    cursor.execute("SELECT id, nombre,tipo FROM bots")
    usuarios = cursor.fetchall()
    for id, nombre, tipo in usuarios:
        if tipo == 50:
            tipo = "Ambicious"
        elif tipo == 40:
            tipo = "Moderated"
        elif tipo == 30:
            tipo = "Bold"
        botardo[id] = {"nombre":nombre , "tipo": tipo}
    cursor.execute("SELECT id, nombre, tipo FROM jugadores")
    usuarios = cursor.fetchall()
    for id, nombre, tipo in usuarios:
        if tipo == 50:
            tipo = "Ambicious"
        elif tipo == 40:
            tipo = "Moderated"
        elif tipo == 30:
            tipo = "Bold"
        
        jugadorazos[id] = {"nombre":nombre , "tipo": tipo}
    lista_nif_jugadores = list(jugadorazos.keys())
    lista_nif_botardo = list(botardo.keys())
    if len(jugadorazos) > len(botardo):
        for i in range(len(jugadorazos)):
            if i <= len(botardo) - 1:
                print(f"{lista_nif_botardo[i]}".ljust(10) + f"{botardo[lista_nif_botardo[i]]['nombre']}".ljust(10) + f"{botardo[lista_nif_botardo[i]]['tipo']}".ljust(10) + " || " +f"{lista_nif_jugadores[i]}".ljust(10) + f"{jugadorazos[lista_nif_jugadores[i]]['nombre']}".ljust(10) + f"{jugadorazos[lista_nif_jugadores[i]]['tipo']}".ljust(10))
            else:
                print(f"|| {lista_nif_jugadores[i]}".rjust(43) + f"{jugadorazos[lista_nif_jugadores[i]]['nombre']}".ljust(10) + f"{jugadorazos[lista_nif_jugadores[i]]['tipo']}".ljust(10))
    elif len(jugadorazos) < len(botardo):
        for i in range(len(botardo)):
            if i <= len(jugadorazos) - 1:
                print(f"{lista_nif_botardo[i]}".ljust(10) + f"{botardo[lista_nif_botardo[i]]['nombre']}".ljust(10) + f"{botardo[lista_nif_botardo[i]]['tipo']}".ljust(10) + " || " +f"{lista_nif_jugadores[i]}".ljust(10) + f"{jugadorazos[lista_nif_jugadores[i]]['nombre']}".ljust(10) + f"{jugadorazos[lista_nif_jugadores[i]]['tipo']}".ljust(10))
            else:
                print(f"{lista_nif_botardo[i]} {botardo[lista_nif_botardo[i]]['nombre']}  {botardo[lista_nif_botardo[i]]['tipo']}  ||")
    elif len(jugadorazos) == len(botardo):
        for i in range(len(botardo)):
            print(f"{lista_nif_botardo[i]}".ljust(10) + f"{botardo[lista_nif_botardo[i]]['nombre']}".ljust(10) + f"{botardo[lista_nif_botardo[i]]['tipo']}".ljust(10) + " || " +f"{lista_nif_jugadores[i]}".ljust(10) + f"{jugadorazos[lista_nif_jugadores[i]]['nombre']}".ljust(10) + f"{jugadorazos[lista_nif_jugadores[i]]['tipo']}".ljust(10))

#FALTA IMPLEMENTAR UNA FUNCION QUE ELIMINE LOS JUGADORES

#    SEGUNDA OPCIÓN

def set_game_players():
    show_seted_players()
    jugadores.imprimir_titulo("SET PLAYERS")
    show_players()
    option = input("Option (id to add to game, -id to remove player, sh to show actual players in game, -1 to go back:")
    if option == "-1":
        return menu_settings()
    elif verificar_nif(option) == True or verificar_nif(option[1:]) == True:
        lista_dnis = list(jugadores.jugadores.keys())
        for i in range(len(list(lista_dnis))):
            if lista_dnis[i] == option or lista_dnis[i] == option[1:]:
                if option[0] == "-":
                    del jugadores.player_game[option[1:]]
                    print(f"Player {jugadores.jugadores[lista_dnis[i]]['name']} has been removed from the game")
                else:
                    name = jugadores.jugadores[option]["name"]
                    human = jugadores.jugadores[option]["human"]
                    type = jugadores.jugadores[option]["type"]
                    jugador = {"name":name , "human":human , "type":type }
                    jugadores.player_game[option] = jugador
                    print(f"Player {name} has been added to the game")
                    show_seted_players()
                break
        
def eliminar_jugador(nif):
    if verificar_nif(nif[1:]) == True:
        cursor = conexion.conexion.cursor() 

        cursor.execute("SELECT id FROM jugadores")
        usuarios = cursor.fetchall()
        dni_humano = []
        dni_bots = [] 
        for id, in usuarios:
            dni_humano.append(id)
        cursor.execute("SELECT id FROM bots")
        usuarios = cursor.fetchall()
        eliminar_humano = False
        eliminar_bot = False
        for id, in usuarios:
            dni_bots.append(id)
        if len(dni_humano) > len(dni_bots):
            for i in range(len(dni_humano)):
                if dni_humano[i] == nif[1:]:
                    eliminar_humano = True
                if i <= len(dni_bots) - 1:
                    if dni_bots[i] == nif[1:]:
                        eliminar_bot = True
        elif len(dni_humano) < len(dni_bots):
            for i in range(len(dni_bots)):
                if dni_bots[i] == nif[1:]:
                    eliminar_bot = True
                if i <= len(dni_humano) - 1:
                    if dni_humano[i] == nif[1:]:
                        eliminar_humano = True
        elif len(dni_humano) == len(dni_bots):
            for i in range(len(dni_bots)):
                if dni_bots[i] == nif[1:]:
                    eliminar_bot = True
                elif dni_humano[i] == nif[1:]:
                    eliminar_humano = True
        if eliminar_humano == True:
            nif = nif[1:]
            consulta = "DELETE FROM jugadores WHERE id= %s"
            valor = (nif,)
            cursor.execute(consulta, valor)
            conexion.conexion.commit()
            return
        elif eliminar_bot == True:
            nif = nif[1:]
            consulta = "DELETE FROM bots WHERE id= %s"
            valor = (nif,)
            cursor.execute(consulta, valor)
            conexion.conexion.commit()
            return
        else:
            print("No se ha encontrado el jugador")
            return
            
    else:
        print("NIF incorrecto")
        return
            

#   TERCERA OPCIÓN

def playGame():
    ask_card = False
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
            print("Aún no implementado")
        elif num_opcion == 2:
            print("Aún no implementado")
        elif num_opcion == 3:
            print("Aún no implementado")
        elif num_opcion == 4:
            ask_card = True
            if ask_card:
                print("You're not allowed to change the bet if you have ordered some card.")
                input("Enter to continue")
            else:
                apuesta_personalizada = int(input("Set the new Bet: "))
                if 1 <= apuesta_personalizada <= jugadores.jugadores["puntos"]:
                    jugadores.jugadores["apuesta"] = apuesta_personalizada
                    input("Enter to continue")
                else:
                    print(f"The New Bet has to be a number between 1 and {jugadores.jugadores['puntos']}.")
        elif num_opcion == 5:
            print("Aún no implementado")
        elif num_opcion == 6:
            return menu_principal()

#def humanRound(id, mazo):
    
#def playGame():
    #ask_card = False
    #set_cards = False
   # if set_cards == False:
  #      print("Set cards first")
 #       return menu_principal
#    else:
      #  jugadores.imprimir_titulo("PLAY GAME")
     #   menu = ("1)View Stats\n2)View Game Stats\n3)Set Bet\n4)Order Card\n5)Automatic Play\n6)Stand")
    #    correcto = False
   #     while correcto == False:
          #  option = input("Option:\n")
         #   if option.isdigit():
        #        num_opcion = int(option)
       #         if 1 <= num_opcion <= 6:
      #              print(f"Número válido: {num_opcion}!")
     #               correcto = True 
    #            else:
   #                 print("El número no está entre 1 y 6. Inténtalo de nuevo.")
  #          else:
 #               print("Por favor, introduce un número válido (entero).")
        #if num_opcion == 1:
        
        #elif num_opcion == 2:

        #if ask_card:
                #print("You're not allowed to change the bet if you have ordered some card.")
                #input("Enter to continue")
            #else:
             #   apuesta_personalizada = int(input("Set the new Bet: "))
              #  if 1 <= apuesta_personalizada <= jugador["puntos"]:
               #     jugador["apuesta"] = apuesta_personalizada
                #    input("Enter to continue")
                #else:
                 #   print(f"The New Bet has to be a number between 1 and {jugador['puntos']}.")
        #elif num_opcion == 4:
         #   ask_card = True
        #elif num_opcion == 5:
        
        #elif num_opcion == 6:
#            return menu_principal()

#def humanRound(id, mazo):
   

#   CUARTA OPCIÓN

def cuarta_opcion():

    menu =[ 
        "\n",
        "\n",
        "1)Players With More Earnings",
        "2)Players With More Gmes Played",
        "3)Players With More Minutes Played",
        "4)Go back",
    ]
    for opcion in menu:
        print(opcion)
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

def show_seted_players():
    if len(jugadores.player_game) == 0:
        print("There is no players in game")
        input("Enter to continue")
    else:
        for i in range(len(jugadores.player_game)):
            nif = list(jugadores.player_game.keys())[i]
            nif_jugadoresInGame = list(jugadores.player_game.keys())
            name = jugadores.jugadores[nif_jugadoresInGame[i]]["name"]
            if jugadores.jugadores[nif_jugadoresInGame[i]]["human"] == True:
                human_boot = "Human"
            else:
                human_boot = "Boot"
            if jugadores.jugadores[nif_jugadoresInGame[i]]["type"] == 50:
                type = "Ambicious"
            elif jugadores.jugadores[nif_jugadoresInGame[i]]["type"] == 40:
                type = "Moderated"
            elif jugadores.jugadores[nif_jugadoresInGame[i]]["type"] == 30:
                type = "Bold"
            print(f"{nif}     {name}    {human_boot}    {type}  ")
        input("Enter to continue")
    return 

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

                
def agregar_jugador_bdd(jugador,nif,quien = ""):
    lista_valores = list(jugador.values())
    cursor = conexion.conexion.cursor()
    consulta_instert = f"""
        INSERT INTO {quien} (id, nombre, human, bank, initialCard, priority, tipo, bet, points, card, roundPoints)
        VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
""" 
    valores = (nif,)
    for i in range(len(lista_valores)):
        if type(lista_valores[i]) == list:
            valores += (str(lista_valores[i]),)            
        else:
            valores += (lista_valores[i],)
    cursor.execute(consulta_instert, valores)
    conexion.conexion.commit()
    cursor.close()



    
menu_principal()

