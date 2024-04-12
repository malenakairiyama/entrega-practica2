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
def get_scorer (players_info):
    """Recorre la lista de jugadores, calcula el maximo entre las claves "Goals" y 
    retorna el nombre junto con la cantidad de goles corespondiente al maximo"""
    max = 0
    name_max = ""
    for player in players_info:
        goals = player["Goals"]
        if goals > max:
            max = goals 
            name_max = player["Name"]
    
    return name_max, max

#3. Conocer el nombre del jugador o jugadora más influyente, esto se consigue
#sumando goles a favor, goles evitados y cantidad de asistencias. La particularidad
#es que los goles a favor, evitados y las asistencias NO valen lo mismo

def get_influencer (players_info):
    """Encuentra al jugador más influyente según un promedio ponderado de goles a favor, goles evitados y asistencias.
    
    Argumento: lista de diccionarios que contienen las estadísticas de cada jugador.

    Retorna: 
        str: El nombre del jugador más influyente."""
    

    list_influence = []
    for player in players_info:
        influence = player["Goals"] * 1.5 + player["Goals_avoid"] * 1.25 + player["Assists"]
        list_influence.append((player["Name"], influence))
    name_max = max(list_influence, key=lambda x: x[1])[0]
    
    return name_max

#4. Conocer el promedio de goles por partido del equipo en general.
def team_goals_average (players_info, matches):
    """
    Calcula el promedio de goles por partido del equipo en general.

    Parametros:
    players_info (list): Lista de diccionarios que contienen las estadísticas de cada jugador
    matches (int): Número total de partidos jugados en la temporada.

    Retorna:
    float: El promedio de goles por partido del equipo."""
    
    total = sum(player["Goals"] for player in players_info)
    average = total / matches
    
    return average

#5. Conocer el promedio de goles por partido del goleador o goleadora.
def max_scorer_average (players_info, matches):
    """Calcula el promedio de goles por partido del goleador o goleadora.

    Argumentos:
    players_info (list): Lista de diccionarios que contienen las estadísticas de cada jugador.
    partidos_jugados (int): Cantidad de partidos jugados en la temporada.

    Retorna:
    float: Promedio de goles por partido del goleador o goleadora.
    """
    max_scorer_name, max_scores = get_scorer(players_info)
    average = max_scores / matches
    
    return average


