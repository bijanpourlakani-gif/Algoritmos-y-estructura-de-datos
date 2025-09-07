# 15) . Cargar 12 valores al azar en un arreglo llamado “a” de 4x3, y cargar la suma de las filas en un
# arreglo llamado “b” y luego la suma de las columnas en otro arreglo llamado “c”. Luego
# recorrer y mostrar ambos arreglos.

import random

a = [[random.randint(1, 50) for _ in range(3)] for _ in range(4)]

b = [sum(row) for row in a]


c = [sum(a[row][column] for row in range(4)) for column in range(3)]


print("Matriz 'a' (4x3):")
for row in a:
    print(row)


print("\nArreglo 'b' (suma de filas):", b)

# Mostrar el arreglo c (suma de columnas)
print("Arreglo 'c' (suma de columnas):", c)
