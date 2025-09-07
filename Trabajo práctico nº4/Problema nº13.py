# Ingresar 20 valores al azar en un arreglo de 5x4 y mostrar las filas, por un lado, y luego las
#columnas por otro.

import random

matrix = [[random.randint(1,100) for _ in range(4)] for _ in range(5)]


print(f"Las filas de la matriz:")

for row in matrix:
    print(row)

print(f"Columnas de la matriz:")
for column in range(4):
    columns = [matrix[row][column] for row in range(5)]
    print(f"Columna {column + 1}:", columns)