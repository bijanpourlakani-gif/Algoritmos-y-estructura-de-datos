# 13). Crear  una  función que  reciba  un  número  entero  como  parámetro  y retorne verdadero si
#es un número primo o falso en caso contrario.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


print("¿Es primo?:", is_prime(8))