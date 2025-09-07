# 8). Escriba una función que calcule la enésima potencia de un número, recibiendo como
#parámetro un número real base y otro entero llamado exponente.
#La definición de la funcion es: y = xn donde x representa la base y n representa el exponente.
#Nota:  tener en  cuenta  que  n  puede  ser  un  número  negativo. Ejemplo: 23 = 8 y 2−3 = 0.125

def potency(x,n):
    return x**n

print(f"Su siguiente potencia:",potency(3,2))