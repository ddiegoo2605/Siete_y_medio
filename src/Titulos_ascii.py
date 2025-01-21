import shutil

def centrar_titulo(titulo):
    ancho_terminal = shutil.get_terminal_size().columns
    lineas = titulo.splitlines()
    return "\n".join(line.center(ancho_terminal) for line in lineas)

def titulo_menu():
    titulo = r"""

  ______   ______  ________  ________  ________        __      __        __       __  ________  _______   ______   ______  
 /      \ |      \|        \|        \|        \      |  \    /  \      |  \     /  \|        \|       \ |      \ /      \ 
|  $$$$$$\ \$$$$$$| $$$$$$$$ \$$$$$$$$| $$$$$$$$       \$$\  /  $$      | $$\   /  $$| $$$$$$$$| $$$$$$$\ \$$$$$$|  $$$$$$\
| $$___\$$  | $$  | $$__       | $$   | $$__            \$$\/  $$       | $$$\ /  $$$| $$__    | $$  | $$  | $$  | $$  | $$
 \$$    \   | $$  | $$  \      | $$   | $$  \            \$$  $$        | $$$$\  $$$$| $$  \   | $$  | $$  | $$  | $$  | $$
 _\$$$$$$\  | $$  | $$$$$      | $$   | $$$$$             \$$$$         | $$\$$ $$ $$| $$$$$   | $$  | $$  | $$  | $$  | $$
|  \__| $$ _| $$_ | $$_____    | $$   | $$_____           | $$          | $$ \$$$| $$| $$_____ | $$__/ $$ _| $$_ | $$__/ $$
 \$$    $$|   $$ \| $$     \   | $$   | $$     \          | $$          | $$  \$ | $$| $$     \| $$    $$|   $$ \ \$$    $$
  \$$$$$$  \$$$$$$ \$$$$$$$$    \$$    \$$$$$$$$           \$$           \$$      \$$ \$$$$$$$$ \$$$$$$$  \$$$$$$  \$$$$$$ 
                                                                                                                           
"""
    print(centrar_titulo(titulo))
def titulo_ajustes():
    titulo = r"""
  ______      _____  __    __   ______   ________  ________   ______  
 /      \    |     \|  \  |  \ /      \ |        \|        \ /      \ 
|  $$$$$$\    \$$$$$| $$  | $$|  $$$$$$\ \$$$$$$$$| $$$$$$$$|  $$$$$$\
| $$__| $$      | $$| $$  | $$| $$___\$$   | $$   | $$__    | $$___\$$
| $$    $$ __   | $$| $$  | $$ \$$    \    | $$   | $$  \    \$$    \ 
| $$$$$$$$|  \  | $$| $$  | $$ _\$$$$$$\   | $$   | $$$$$    _\$$$$$$\
| $$  | $$| $$__| $$| $$__/ $$|  \__| $$   | $$   | $$_____ |  \__| $$
| $$  | $$ \$$    $$ \$$    $$ \$$    $$   | $$   | $$     \ \$$    $$
 \$$   \$$  \$$$$$$   \$$$$$$   \$$$$$$     \$$    \$$$$$$$$  \$$$$$$ 
                                                                              
"""
    print(centrar_titulo(titulo))
    
def titulo_jugadores():
    titulo = r"""

    _____  __    __   ______    ______   _______    ______   _______   ________   ______  
   |     \|  \  |  \ /      \  /      \ |       \  /      \ |       \ |        \ /      \ 
    \$$$$$| $$  | $$|  $$$$$$\|  $$$$$$\| $$$$$$$\|  $$$$$$\| $$$$$$$\| $$$$$$$$|  $$$$$$\
      | $$| $$  | $$| $$ __\$$| $$__| $$| $$  | $$| $$  | $$| $$__| $$| $$__    | $$___\$$
 __   | $$| $$  | $$| $$|    \| $$    $$| $$  | $$| $$  | $$| $$    $$| $$  \    \$$    \ 
|  \  | $$| $$  | $$| $$ \$$$$| $$$$$$$$| $$  | $$| $$  | $$| $$$$$$$\| $$$$$    _\$$$$$$\
| $$__| $$| $$__/ $$| $$__| $$| $$  | $$| $$__/ $$| $$__/ $$| $$  | $$| $$_____ |  \__| $$
 \$$    $$ \$$    $$ \$$    $$| $$  | $$| $$    $$ \$$    $$| $$  | $$| $$     \ \$$    $$
  \$$$$$$   \$$$$$$   \$$$$$$  \$$   \$$ \$$$$$$$   \$$$$$$  \$$   \$$ \$$$$$$$$  \$$$$$$ 
                                                                                                                                                                                    
"""
    print(centrar_titulo(titulo))

<<<<<<< HEAD
titulo_jugadores()
titulo_ajustes()
titulo_menu()
=======
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
>>>>>>> parent of fee0b66 (Merge pull request #54 from ddiegoo2605/Diego)
