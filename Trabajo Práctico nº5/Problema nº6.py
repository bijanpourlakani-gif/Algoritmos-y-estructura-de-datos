# 6). Crear una función que reciba como parámetro un número entero, y retorne la tabla de multiplicar de ese número. Imprimir tabla (por ejemplo, para el 3 deberá mostrar desde 3x0=0
#hasta  3x10 = 30).

def times_table(n):
    for i in range(11):
        print(f"{n} x {i} = {n * i}")


times_table(4)