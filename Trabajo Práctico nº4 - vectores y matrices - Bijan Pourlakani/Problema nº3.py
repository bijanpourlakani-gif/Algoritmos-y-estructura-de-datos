# Genere un vector con 20 valores aleatorios enteros entre 5 y 30. Luego leer un número por
# teclado y verificar si dicho valor está o no dentro del vector.

import random

array = [random.randint(5,30) for _ in range (20)]

print("el vector generado", array)

number = int(input(f"ingrese a un valor aleatorios:"))

if number in array:

  print(f"El valor {number} está dentro del vector")

else:

    print(f"el valor  ingresado {number} es inválido")