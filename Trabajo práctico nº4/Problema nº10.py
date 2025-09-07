# 10) Arreglo de valores lógicos (Booleanos)
#Crear un algoritmo que recorra las butacas de una sala de cine y determine cuántas butacas
#desocupadas hay en la sala. Suponga que inicialmente tiene un vector con valores booleanos
#que si es verdadero (true) implica que está ocupada y si es falso (falso) la butaca está
#desocupada. Tenga en cuenta que el arreglo deberá ser creado e inicializado al principio del
#algoritmo.

import random

seats =[random.choice([True,False]) for _ in range(40)]
print(f"El estado de las butacas (True = ocupado , False = desocupado):")
print(seats)

unoccupied = seats.count(False)


print(f"Cantidad de butacas desocupados:,{unoccupied}")



