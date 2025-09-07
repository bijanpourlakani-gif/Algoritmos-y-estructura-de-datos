# 15).Realizar un programa que permita ingresar dos palabras, y determine si tienen la misma
# longitud o no. Mostrar un mensaje en pantalla en cada caso. Misma longitud, una menor, o
# una mayor.


variable1 = input("Ingrese a una palabra: ")
variable2 = input("Ingrese a una palabra: ")

lenone=len(variable1)
lentwo=len(variable1)
if lenone > lentwo:
    print(f"Su longitud es  {lenone}, Esto  nos indica que la primera palabra es mayor que la segunda")
elif len(variable2) > len(variable1):
    print(f"Su longitud es {lentwo}, Esto nos indica que la segunda palabra es mayor que la primera")
else:
    print(f"Las dos palabras tienen igual longitud de {lenone} en {lentwo}")
