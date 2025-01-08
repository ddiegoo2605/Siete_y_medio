import jugadores
def menu_principal():
    print("""
    ********************************************************************************************************************************************
                                     _____                         ___              __   __  __      ______
                                    / ___/___ _   _____  ____     /   |  ____  ____/ /  / / / /___ _/ / __/
                                    \__ \/ _ \ | / / _ \/ __ \   / /| | / __ \/ __  /  / /_/ / __ `/ / /_
                                   ___/ /  __/ |/ /  __/ / / /  / ___ |/ / / / /_/ /  / __  / /_/ / / __/
                                  /____/\___/|___/\___/_/ /_/  /_/  |_/_/ /_/\__,_/  /_/ /_/\__,_/_/_/
                     
                       ____ ___
                       \      /
                        \    /
                         /  / 
                        /__/   


     ********************************************************************************************************************************************
    """)
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
if __name__ == "__main__":
    menu_principal()