import jugadores

def menu_principal():
    while True:
        print("\n ---------- MENÚ PRINCIPAL ----------")
        print("1. Gestión de jugadores")
        print("2. Ajustes")
        print("3. Jugar")
        print("4. Estadísticas")
        print("5. Reportes")
        print("6. Salir")

        seleccion = input("Selecciona una opción (1-6): ")

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
            print("Gracias por jugar, hasta la proxima")
            break
        else:
            print("Error. Escoge una opción valida entre (1-6)")
if __name__ == "__main__":
    menu_principal()