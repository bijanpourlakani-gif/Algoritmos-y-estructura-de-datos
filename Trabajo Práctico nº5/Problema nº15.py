# 15). Desarrollar  una  función  que  dados  cinco  números,  recibidos  por  parámetro,  devuelva  el
# promedio  de  ellos.  Se puede  generalizar  para  n  parámetros  devolviendo  el  promedio  de
# los mismos.

def average(*numbers):
    return sum(numbers) / len(numbers)


print("Promedio:", average(6, 7, 8, 9, 10))