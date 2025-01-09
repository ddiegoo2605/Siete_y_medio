#Creación de barajas, manejo de cartas, y usabilidad

#AQUÍ ES DÓNDE SE ENCUENTRAN TODOS LOS MENUS DEL PROGRAMA

menu00 = "1)Add/Remove/Show Players\n2)Settings\n3)Play Game\n4)Ranking\n5)Reports\n6)Exit"
menu02 = "1)Set Game Players\n2)Set Card's Deck\n3)Set Max Rounds (Default 5 Rounds)\n4)Go Back"
menu04 = "1)Players With More Earnings\n2)Players With More Games Played\n3)Players With More Minutes Played"

#AQUÍ SE ENCUENTRAN TODAS LA VARIBALES DEL JUEGO

baraja_española = {
 "OR01": {"literal": "As de Oros", "value": 1,  "priority": 4, "realValue": 1},
 "OR02": {"literal": "Dos de Oros", "value": 2,  "priority": 4, "realValue": 2},
 "OR03": {"literal": "Tres de Oros", "value": 3,  "priority": 4, "realValue": 3},
 "OR04": {"literal": "Cuatro de Oros", "value": 4, "priority": 4, "realValue": 4},
 "OR05": {"literal": "Cinco de Oros", "value": 5, "priority": 4, "realValue": 5},
 "OR06": {"literal": "Seis de Oros", "value": 6,  "priority": 4, "realValue": 6},
 "OR07": {"literal": "Siete de Oros", "value": 7,  "priority": 4, "realValue": 7},
 "OR08": {"literal": "Ocho de Oros", "value": 8,  "priority": 4, "realValue": 0.5},
 "OR09": {"literal": "Nueve de Oros", "value": 9,  "priority": 4, "realValue": 0.5},
 "OR10": {"literal": "Diez de Oros", "value": 10, "priority": 4, "realValue": 0.5},
 "OR11": {"literal": "Jota de Oros", "value": 11, "priority": 4, "realValue": 0.5},
 "OR12": {"literal": "Rey de Oros",  "value": 12, "priority": 4, "realValue": 0.5},

 "CP01": {"literal": "As de Copas",  "value": 1,  "priority": 3, "realValue": 1},
 "CP02": {"literal": "Dos de Copas", "value": 2,  "priority": 3, "realValue": 2},
 "CP03": {"literal": "Tres de Copas", "value": 3,  "priority": 3, "realValue": 3},
 "CP04": {"literal": "Cuatro de Copas", "value": 4, "priority": 3, "realValue": 4},
 "CP05": {"literal": "Cinco de Copas", "value": 5, "priority": 3, "realValue": 5},
 "CP06": {"literal": "Seis de Copas", "value": 6,  "priority": 3, "realValue": 6},
 "CP07": {"literal": "Siete de Copas", "value": 7,  "priority": 3, "realValue": 7},
 "CP08": {"literal": "Ocho de Copas", "value": 8,  "priority": 3, "realValue": 0.5},
 "CP09": {"literal": "Nueve de Copas", "value": 9,  "priority": 3, "realValue": 0.5},
 "CP10": {"literal": "Diez de Copas", "value": 10, "priority": 3, "realValue": 0.5},
 "CP11": {"literal": "Jota de Copas", "value": 11, "priority": 3, "realValue": 0.5},
 "CP12": {"literal": "Rey de Copas",  "value": 12, "priority": 3, "realValue": 0.5},

 "ES01": {"literal": "As de Espadas", "value": 1,  "priority": 2, "realValue": 1},
 "ES02": {"literal": "Dos de Espadas", "value": 2,  "priority": 2, "realValue": 2},
 "ES03": {"literal": "Tres de Espadas", "value": 3,  "priority": 2, "realValue": 3},
 "ES04": {"literal": "Cuatro de Espadas", "value": 4, "priority": 2, "realValue": 4},
 "ES05": {"literal": "Cinco de Espadas", "value": 5, "priority": 2, "realValue": 5},
 "ES06": {"literal": "Seis de Espadas", "value": 6,  "priority": 2, "realValue": 6},
 "ES07": {"literal": "Siete de Espadas", "value": 7,  "priority": 2, "realValue": 7},
 "ES08": {"literal": "Ocho de Espadas", "value": 8,  "priority": 2, "realValue": 0.5},
 "ES09": {"literal": "Nueve de Espadas", "value": 9,  "priority": 2, "realValue": 0.5},
 "ES10": {"literal": "Diez de Espadas", "value": 10, "priority": 2, "realValue": 0.5},
 "ES11": {"literal": "Jota de Espadas", "value": 11, "priority": 2, "realValue": 0.5},
 "ES12": {"literal": "Rey de Espadas",  "value": 12, "priority": 2, "realValue": 0.5},

 "BA01": {"literal": "As de Bastos",  "value": 1,  "priority": 1, "realValue": 1},
 "BA02": {"literal": "Dos de Bastos", "value": 2,  "priority": 1, "realValue": 2},
 "BA03": {"literal": "Tres de Bastos", "value": 3,  "priority": 1, "realValue": 3},
 "BA04": {"literal": "Cuatro de Bastos", "value": 4, "priority": 1, "realValue": 4},
 "BA05": {"literal": "Cinco de Bastos", "value": 5, "priority": 1, "realValue": 5},
 "BA06": {"literal": "Seis de Bastos", "value": 6,  "priority": 1, "realValue": 6},
 "BA07": {"literal": "Siete de Bastos", "value": 7,  "priority": 1, "realValue": 7},
 "BA08": {"literal": "Ocho de Bastos", "value": 8,  "priority": 1, "realValue": 0.5},
 "BA09": {"literal": "Nueve de Bastos", "value": 9,  "priority": 1, "realValue": 0.5},
 "BA10": {"literal": "Diez de Bastos", "value": 10, "priority": 1, "realValue": 0.5},
 "BA11": {"literal": "Jota de Bastos", "value": 11, "priority": 1, "realValue": 0.5},
 "BA12": {"literal": "Rey de Bastos",  "value": 12, "priority": 1, "realValue": 0.5}
 }

baraja_poker ={
 "PI01": {"literal": "As de Picas", "value": 1,  "priority": 4, "realValue": 1},
 "PI02": {"literal": "Dos de Picas", "value": 2,  "priority": 4, "realValue": 2},
 "PI03": {"literal": "Tres de Picas", "value": 3,  "priority": 4, "realValue": 3},
 "PI04": {"literal": "Cuatro de Picas", "value": 4, "priority": 4, "realValue": 4},
 "PI05": {"literal": "Cinco de Picas", "value": 5, "priority": 4, "realValue": 5},
 "PI06": {"literal": "Seis de Picas", "value": 6,  "priority": 4, "realValue": 6},
 "PI07": {"literal": "Siete de Picas", "value": 7,  "priority": 4, "realValue": 7},
 "PI08": {"literal": "Ocho de Picas", "value": 8,  "priority": 4, "realValue": 0.5},
 "PI09": {"literal": "Nueve de Picas", "value": 9,  "priority": 4, "realValue": 0.5},
 "PI10": {"literal": "Diez de Picas", "value": 10, "priority": 4, "realValue": 0.5},
 "PI11": {"literal": "Jota de Picas", "value": 11, "priority": 4, "realValue": 0.5},
 "PI12": {"literal": "Rey de Picas",  "value": 12, "priority": 4, "realValue": 0.5},

 "CR01": {"literal": "As de Corazones", "value": 1,  "priority": 3, "realValue": 1},
 "CR02": {"literal": "Dos de Corazones", "value": 2,  "priority": 3, "realValue": 2},
 "CR03": {"literal": "Tres de Corazones", "value": 3,  "priority": 3, "realValue": 3},
 "CR04": {"literal": "Cuatro de Corazones", "value": 4, "priority": 3, "realValue": 4},
 "CR05": {"literal": "Cinco de Corazones", "value": 5, "priority": 3, "realValue": 5},
 "CR06": {"literal": "Seis de Corazones", "value": 6,  "priority": 3, "realValue": 6},
 "CR07": {"literal": "Siete de Corazones", "value": 7,  "priority": 3, "realValue": 7},
 "CR08": {"literal": "Ocho de Corazones", "value": 8,  "priority": 3, "realValue": 0.5},
 "CR09": {"literal": "Nueve de Corazones", "value": 9,  "priority": 3, "realValue": 0.5},
 "CR10": {"literal": "Diez de Corazones", "value": 10, "priority": 3, "realValue": 0.5},
 "CR11": {"literal": "Jota de Corazones", "value": 11, "priority": 3, "realValue": 0.5},
 "CR12": {"literal": "Rey de Corazones",  "value": 12, "priority": 3, "realValue": 0.5},

 "TR01": {"literal": "As de Tréboles", "value": 1,  "priority": 2, "realValue": 1},
 "TR02": {"literal": "Dos de Tréboles", "value": 2,  "priority": 2, "realValue": 2},
 "TR03": {"literal": "Tres de Tréboles", "value": 3,  "priority": 2, "realValue": 3},
 "TR04": {"literal": "Cuatro de Tréboles", "value": 4, "priority": 2, "realValue": 4},
 "TR05": {"literal": "Cinco de Tréboles", "value": 5, "priority": 2, "realValue": 5},
 "TR06": {"literal": "Seis de Tréboles", "value": 6,  "priority": 2, "realValue": 6},
 "TR07": {"literal": "Siete de Tréboles", "value": 7,  "priority": 2, "realValue": 7},
 "TR08": {"literal": "Ocho de Tréboles", "value": 8,  "priority": 2, "realValue": 0.5},
 "TR09": {"literal": "Nueve de Tréboles", "value": 9,  "priority": 2, "realValue": 0.5},
 "TR10": {"literal": "Diez de Tréboles", "value": 10, "priority": 2, "realValue": 0.5},
 "TR11": {"literal": "Jota de Tréboles", "value": 11, "priority": 2, "realValue": 0.5},
 "TR12": {"literal": "Rey de Tréboles",  "value": 12, "priority": 2, "realValue": 0.5},

 "DI01": {"literal": "As de Diamantes", "value": 1,  "priority": 1, "realValue": 1},
 "DI02": {"literal": "Dos de Diamantes", "value": 2,  "priority": 1, "realValue": 2},
 "DI03": {"literal": "Tres de Diamantes", "value": 3,  "priority": 1, "realValue": 3},
 "DI04": {"literal": "Cuatro de Diamantes", "value": 4, "priority": 1, "realValue": 4},
 "DI05": {"literal": "Cinco de Diamantes", "value": 5, "priority": 1, "realValue": 5},
 "DI06": {"literal": "Seis de Diamantes", "value": 6,  "priority": 1, "realValue": 6},
 "DI07": {"literal": "Siete de Diamantes", "value": 7,  "priority": 1, "realValue": 7},
 "DI08": {"literal": "Ocho de Diamantes", "value": 8,  "priority": 1, "realValue": 0.5},
 "DI09": {"literal": "Nueve de Diamantes", "value": 9,  "priority": 1, "realValue": 0.5},
 "DI10": {"literal": "Diez de Diamantes", "value": 10, "priority": 1, "realValue": 0.5},
 "DI11": {"literal": "Jota de Diamantes", "value": 11, "priority": 1, "realValue": 0.5},
 "DI12": {"literal": "Rey de Diamantes",  "value": 12, "priority": 1, "realValue": 0.5},

}

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
    


    
    

players = { "11115555A":{"name":"Mario","human":True,"bank":False,"initialCard":"","priority":0,"type":40,"bet":4,"points":0,"cards":[],"roundPoints":0},
 "22225555A":{"name":"Pedro","human":True,"bank":False,"initialCard":"","priority":0,"type":40,"bet":4,"points":0,"cards":[],"roundPoints":0}
 }

elegir_baraja()