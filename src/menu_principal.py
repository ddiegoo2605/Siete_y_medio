import jugadores

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
if __name__ == "__main__":
    menu_principal()