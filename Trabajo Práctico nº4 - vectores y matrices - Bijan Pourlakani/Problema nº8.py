from random import random

# 8). Ídem anterior, pero debe mostrar el promedio de sus elementos.

#mport random


array = [random.randint(1,50) for _ in range(18)]

adding = sum(array)

average = sum(array)/len(array)

print(average)
print(f"El promedio total de todos los valores son:{average}")