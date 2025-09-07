#Crear un vector de 18 valores aleatorios enteros entre 1 y 50, y mostrar por pantalla la suma
#de todos sus valores.

import random


array = [random.randint(1, 50) for _ in range(18)]

adding = sum(array)

print(adding)
print(f"La suma de todos los valores son:{adding}")