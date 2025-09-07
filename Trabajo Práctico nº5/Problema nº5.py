# 5). Crear una función que reciba un número como parámetro el cual representa el lado de un cuadrado y muestre en pantalla el perímetro y la superficie del mismo.

def perimeter_surface(side):
    perimeter = 4 * side
    surface = side ** 2
    print(f"Perimetro: {perimeter}, Superficie: {surface}")


perimeter_surface(6)