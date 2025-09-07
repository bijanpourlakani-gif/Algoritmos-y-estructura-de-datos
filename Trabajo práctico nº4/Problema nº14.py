# Ingresar 12 valores en un arreglo de 4x3 y mostrar la suma de las filas y luego la suma de las columnas.

import random

matrix = [[random.randint(1,100) for _ in range(3)] for _ in range(4)]


print(f" Matriz de 4x3:")

for row in matrix:
    print(row)

print(f"La suma de cada fila:")
for i,row in enumerate(matrix):

    print(f"fila{i+1}:{sum(row)}")



print(f"La suma de cada Columna:")
for column in range(3):
   sum_of_columns = sum([matrix[row][column] for row in range(4)])
   print(f"Columna {column+1}:{sum_of_columns}")