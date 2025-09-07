# 2).Crear la clase Triangulo que almacene la longitud de cada uno de sus lados. Deberá contener los
# siguientes métodos:
# a) area(): devuelve el área del triángulo
# b) forma(): indica si se trata de un triángulo equilátero, isósceles o irregular.
# c) perímetro(): devuelve el perímetro del triángulo.
# Se deben crear dos triángulos, mostrar los valores de sus atributos en pantalla, su área, forma y
# perímetro.

import math

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def form(self):
        if self.side1 == self.side2 == self.side3:
            return "Equilátero"
        elif (self.side1 == self.side2 or
              self.side1 == self.side3 or
              self.side2 == self.side3):
            return "Isósceles"
        else:
            return "Escaleno (Irregular)"

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

# ---- Uso del programa ----

tri1 = Triangle(3, 3, 3)  # Triángulo equilátero
tri2 = Triangle(3, 4, 5)  # Triángulo escaleno (clásico)

for i, t in enumerate([tri1, tri2], start=1):
    print(f"\nTriángulo {i}:")
    print(f"Lados: {t.side1}, {t.side2}, {t.side3}")
    print(f"Perímetro: {t.perimeter()}")
    print(f"Forma: {t.form()}")
    print(f"Área: {t.area():.2f}")







