# 16)  Crear una matriz de 5 filas y 6 columnas, llenarla con valores numéricos enteros, al azar entre
# 1 y 6. Luego, reemplazar todos los valores en la fila 5, por el valor 0.

import random


matrix = [[random.randint(1, 6) for _ in range(6)] for _ in range(5)]


print("Matriz original:")
for row in matrix:
    print(row)


matrix[4] = [0] * 6

print("\nMatriz con la fila 5 reemplazada por ceros:")
for row in matrix:
    print(row)
