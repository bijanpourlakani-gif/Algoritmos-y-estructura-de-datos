# 26).Tirar 20 veces un dado de 6 caras. Mostrar el promedio de esas 20 tiradas.


import random

throws = [random.randint(1, 6) for _ in range(20)]

print("Tiradas:", throws)

average = sum(throws) / len(throws)
print(f"Promedio de las tiradas: {round(average, 2)}")