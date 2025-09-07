# 7) Crear un vector de 18 valores aleatorios enteros entre 1 y 50, y mostrar por pantalla la suma
#de todos sus valores.

import random


array=[random.randint(1,50) for e in range (18)]


Adding = sum(array)
print(f"Suma total:{Adding}")
