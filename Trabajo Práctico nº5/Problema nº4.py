# 4). ¿Què imprimirá en pantalla el siguiente código? Determine el alcance de cada variable.

x = 3

def f2():
    y = x + 1
    print(x)

def g():
    f2()
    # y no está definida en este ámbito

g()
x = 1
print("x:", x)
# print(y)  # Esto daría error porque y no existe fuera de f2

# rta: se imprime la función x:3 en el ámbito global. Después, la variable y no existe en g(), porque fue declarada solo dentro de f2(), Reasigna el valor de x global a 1 y se imprime "x: 1".
# Alcance de variables:

#x: variable global, visible en todo el código (incluidas las funciones, mientras no se reasigne dentro).

#y: variable local, solo existe dentro de f2().