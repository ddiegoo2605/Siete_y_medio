import os 
def calcular_ancho_terminal():
    try:
        columnas, _= os.get_terminal_size()
        return columnas
    except OSError:
        return 80

def titulo_menu_principal():
    titulo_menu = r""" 
  ______   ______  ________  ________  ________        __      __        __       __  ________  _______   ______   ______  
 /      \ |      \|        \|        \|        \      |  \    /  \      |  \     /  \|        \|       \ |      \ /      \ 
|  $$$$$$\ \$$$$$$| $$$$$$$$ \$$$$$$$$| $$$$$$$$       \$$\  /  $$      | $$\   /  $$| $$$$$$$$| $$$$$$$\ \$$$$$$|  $$$$$$ 
| $$___\$$  | $$  | $$__       | $$   | $$__            \$$\/  $$       | $$$\ /  $$$| $$__    | $$  | $$  | $$  | $$  | $$
 \$$    \   | $$  | $$  \      | $$   | $$  \            \$$  $$        | $$$$\  $$$$| $$  \   | $$  | $$  | $$  | $$  | $$
 _\$$$$$$\  | $$  | $$$$$      | $$   | $$$$$             \$$$$         | $$\$$ $$ $$| $$$$$   | $$  | $$  | $$  | $$  | $$
|  \__| $$ _| $$_ | $$_____    | $$   | $$_____           | $$          | $$ \$$$| $$| $$_____ | $$__/ $$ _| $$_ | $$__/ $$
 \$$    $$|   $$ \| $$     \   | $$   | $$     \          | $$          | $$  \$ | $$| $$     \| $$    $$|   $$ \ \$$    $$
  \$$$$$$  \$$$$$$ \$$$$$$$$    \$$    \$$$$$$$$           \$$           \$$      \$$ \$$$$$$$$ \$$$$$$$  \$$$$$$  \$$$$$$ 
                                                                                                                           
"""
    ancho_terminal = calcular_ancho_terminal()
    lineas = titulo_menu.splitlines()
    titulo_centrado = "\n".join([Linea.center(ancho_terminal) for Linea in lineas])
    return titulo_centrado

def titulo_players():
    titulo_players = r"""
 _______   __         ______   __      __  ________  _______    ______  
|       \ |  \       /      \ |  \    /  \|        \|       \  /      \ 
| $$$$$$$\| $$      |  $$$$$$\ \$$\  /  $$| $$$$$$$$| $$$$$$$\|  $$$$$$\
| $$__/ $$| $$      | $$__| $$  \$$\/  $$ | $$__    | $$__| $$| $$___\$$
| $$    $$| $$      | $$    $$   \$$  $$  | $$  \   | $$    $$ \$$    \ 
| $$$$$$$ | $$      | $$$$$$$$    \$$$$   | $$$$$   | $$$$$$$\ _\$$$$$$\
| $$      | $$_____ | $$  | $$    | $$    | $$_____ | $$  | $$|  \__| $$
| $$      | $$     \| $$  | $$    | $$    | $$     \| $$  | $$ \$$    $$
 \$$       \$$$$$$$$ \$$   \$$     \$$     \$$$$$$$$ \$$   \$$  \$$$$$$ 
"""
    ancho_terminal = calcular_ancho_terminal()
    lineas = titulo_players.splitlines()
    titulo_centrado = "\n".join([Linea.center(ancho_terminal) for Linea in lineas])
    return titulo_centrado

def titulo_settings():
    titulo_settings = r"""
  _____    ______  ________  ________  ______  __    __   ______    ______  
 /      \ |        \|        \|        \|      \|  \  |  \ /      \  /      \ 
|  $$$$$$\| $$$$$$$$ \$$$$$$$$ \$$$$$$$$ \$$$$$$| $$\ | $$|  $$$$$$\|  $$$$$$\
| $$___\$$| $$__       | $$      | $$     | $$  | $$$\| $$| $$ __\$$| $$___\$$
 \$$    \ | $$  \      | $$      | $$     | $$  | $$$$\ $$| $$|    \ \$$    \ 
 _\$$$$$$\| $$$$$      | $$      | $$     | $$  | $$\$$ $$| $$ \$$$$ _\$$$$$$\
|  \__| $$| $$_____    | $$      | $$    _| $$_ | $$ \$$$$| $$__| $$|  \__| $$
 \$$    $$| $$     \   | $$      | $$   |   $$ \| $$  \$$$ \$$    $$ \$$    $$
  \$$$$$$  \$$$$$$$$    \$$       \$$    \$$$$$$ \$$   \$$  \$$$$$$   \$$$$$$  
                                                                                                                                                       
"""
    ancho_terminal = calcular_ancho_terminal()
    lineas = titulo_settings.splitlines()
    titulo_centrado = "\n".join([Linea.center(ancho_terminal) for Linea in lineas])
    return titulo_centrado

def titulo_ranking():
    titulo_ranking = r"""
 _______    ______   __    __  __    __  ______  __    __   ______  
|       \  /      \ |  \  |  \|  \  /  \|      \|  \  |  \ /      \ 
| $$$$$$$\|  $$$$$$\| $$\ | $$| $$ /  $$ \$$$$$$| $$\ | $$|  $$$$$$\
| $$__| $$| $$__| $$| $$$\| $$| $$/  $$   | $$  | $$$\| $$| $$ __\$$
| $$    $$| $$    $$| $$$$\ $$| $$  $$    | $$  | $$$$\ $$| $$|    \
| $$$$$$$\| $$$$$$$$| $$\$$ $$| $$$$$\    | $$  | $$\$$ $$| $$ \$$$$
| $$  | $$| $$  | $$| $$ \$$$$| $$ \$$\  _| $$_ | $$ \$$$$| $$__| $$
| $$  | $$| $$  | $$| $$  \$$$| $$  \$$\|   $$ \| $$  \$$$ \$$    $$
 \$$   \$$ \$$   \$$ \$$   \$$ \$$   \$$ \$$$$$$ \$$   \$$  \$$$$$$ 
"""
    ancho_terminal = calcular_ancho_terminal()
    lineas = titulo_ranking.splitlines()
    titulo_centrado = "\n".join([Linea.center(ancho_terminal) for Linea in lineas])
    return titulo_centrado

def titulo_goodbye():
    titulo_goodbye = r"""

  ______    ______    ______   _______           _______   __      __  ________ 
 /      \  /      \  /      \ |       \         |       \ |  \    /  \|        \
|  $$$$$$\|  $$$$$$\|  $$$$$$\| $$$$$$$\        | $$$$$$$\ \$$\  /  $$| $$$$$$$$
| $$ __\$$| $$  | $$| $$  | $$| $$  | $$ ______ | $$__/ $$  \$$\/  $$ | $$__    
| $$|    \| $$  | $$| $$  | $$| $$  | $$|      \| $$    $$   \$$  $$  | $$  \   
| $$ \$$$$| $$  | $$| $$  | $$| $$  | $$ \$$$$$$| $$$$$$$\    \$$$$   | $$$$$   
| $$__| $$| $$__/ $$| $$__/ $$| $$__/ $$        | $$__/ $$    | $$    | $$_____ 
 \$$    $$ \$$    $$ \$$    $$| $$    $$        | $$    $$    | $$    | $$     \
  \$$$$$$   \$$$$$$   \$$$$$$  \$$$$$$$          \$$$$$$$      \$$     \$$$$$$$$
                                                                                                                                                                                                                                              
"""
    ancho_terminal = calcular_ancho_terminal()
    lineas = titulo_goodbye.splitlines()
    titulo_centrado = "\n".join([Linea.center(ancho_terminal) for Linea in lineas])
    return titulo_centrado