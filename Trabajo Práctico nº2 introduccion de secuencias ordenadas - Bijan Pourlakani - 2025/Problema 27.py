# 27).Tirar ahora, 2500 veces un dado de 6 caras. Mostrar el promedio de esas tiradas. Comparar
# con el promedio del ejercicio anterior. ¿Nota una diferencia sustancial habiendo cambiado
# la cantidad de tiradas?

import random

throws = [random.randint(1, 6) for _ in range(2500)]

print("Tiradas:", throws)

average= sum(throws) / len(throws)
print(f"Promedio de las tiradas: {round(average, 2)}")

# Comparación:

#Con 20 tiradas, el promedio puede variar bastante por azar (por ejemplo, 3.6, 2.9, 4.2…).
# Con 2500 tiradas, el promedio se acerca mucho más a 3.5, porque el azar se compensa con más repeticiones.