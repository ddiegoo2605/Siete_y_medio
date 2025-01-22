#Lógica de apuestas
def establecer_apuestas(jugadores, puntos_banca):

    # Establece las apuestas de los jugadores automáticamente según su perfil de riesgo.

    apuestas = {}
    for id_jugador, datos_jugador in jugadores.items():
        if datos_jugador["puntos"] <= 0:
            apuestas[id_jugador] = 0
            continue
        perfil_riesgo = datos_jugador["tipo"]
        apuesta_maxima = min(datos_jugador["puntos"], puntos_banca)
        apuesta = int(apuesta_maxima * (perfil_riesgo / 100))
        apuesta = max(1, apuesta)
        apuestas[id_jugador] = apuesta
    return apuestas
