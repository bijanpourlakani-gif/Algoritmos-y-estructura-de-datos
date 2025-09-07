# 3) Genere un vector con 20 valores aleatorios enteros entre 5 y 30. Luego leer un número por
#teclado y verificar si dicho valor está o no dentro del vector.
import random


array=[random.randint(5,30) for e in range (20)]

print(array)
print("El vector generado")

number = int(input("ingrese a un valor numerico:"))

if number in array:

 print(f"el numero {number} si aparece en el vector ")

else:
  print(f"el numero {number} no aparece en el vector ")



