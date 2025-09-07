# 11).  Crear una funcion lógica (función que retorna un valor lógico) que determine si un número  entero es par o impar.

def is_pair(number):
    return number % 8 == 0


print("Es par:", is_pair(16))