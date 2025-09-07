#12) Ingresar 12 valores aleatorios en un arreglo (matriz) de 4x3 y mostrarlo en pantalla.

import random

matrix = [[random.randint(1,30)for rows in range (3)] for column in range(4)]

print(f"La matriz generado:")

for matrices in matrix:

 print(matrices)


