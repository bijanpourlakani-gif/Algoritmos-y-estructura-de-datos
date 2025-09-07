# 6) Crear un vector de 30 valores aleatorios enteros entre 1 y 100. Luego leer dos valores x e y
#(entre 1 y 30) e intercambiar los valores de las posiciones x e y respectivamente.

import random


array = [random.randint(1, 100) for _ in range(30)]


print("Vector original:")
print(array)


x = int(input("Ingrese posición x (1-30): ")) - 1
y = int(input("Ingrese posición y (1-30): ")) - 1


if 0 <= x < 30 and 0 <= y < 30:

    array[x], array[y] = array[y], array[x]


    print("\nVector después del intercambio:")
    print(array)
else:
    print("Las posiciones deben estar entre 1 y 30.")

