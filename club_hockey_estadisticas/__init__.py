#3. Conocer el nombre del jugador o jugadora más influyente, esto se consigue
#sumando goles a favor, goles evitados y cantidad de asistencias. La particularidad
#es que los goles a favor, evitados y las asistencias NO valen lo mismo

#4. Conocer el promedio de goles por partido del equipo en general. Dato: Se jugaron 25 partidos en la temporada.

#5. Conocer el promedio de goles por partido del goleador o goleadora.


#1. Generar una estructura todas las estadísticas asociadas a cada jugador.
def generate_list_player (names, goals, goals_avoid, assists):
    """ 
        Genera una lista de diccionarios con las estadísticas de cada jugador
        
        Recibe como argumentos 4 listas de:
        - nombres de jugadores
        - goles a favor
        - goles evitados
        - asistencias realizadas
    """
    list_players = []
    
    for name, goal, goal_av, assist in zip(names, goals, goals_avoid, assists):
        player = {
            "Name": name,
            "Goals": goal,
            "Goals_avoid": goal_av,
            "Assists": assist
        }
        list_players.append(player)
    
    return list_players


#2. Conocer el nombre y la cantidad de goles del goleador o goleadora.
