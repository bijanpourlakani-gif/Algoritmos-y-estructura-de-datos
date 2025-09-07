# 21). Crear un programa que calcule quien gana más partidas al piedra, papel, tijera.
# • El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
# • La función recibe un listado que contiene pares, representando cada jugada.
# • El par puede contener combinaciones de "R" (piedra), "P" (papel)  o "S" (tijera). Ejemplo.
# Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".

def game_winner(plays):
    rules = {'R': 'S', 'S': 'P', 'P': 'R'}
    p1 = p2 = 0
    for j1, j2 in plays:
        if j1 == j2:
            continue
        elif rules[j1] == j2:
            p1 += 1
        else:
            p2 += 1
    if p1 > p2:
        return "Player 1"
    elif p2 > p1:
        return "Player 2"
    else:
        return "Tie"


print("Ganador:", game_winner([("R","S"), ("P","S"), ("S","P")]))
