# 28).Pedirle al usuario sus 10 marcas favoritas. Mostrar una marca al azar de la lista.

import random

marks = []
for i in range(10):
    mark = input(f"Ingrese su marca favorita #{i+1}: ")
    marks.append(mark)


mark_aleatorial = random.choice(marks)
print(f"Una de tus marcas favoritas al azar es: {mark_aleatorial}")