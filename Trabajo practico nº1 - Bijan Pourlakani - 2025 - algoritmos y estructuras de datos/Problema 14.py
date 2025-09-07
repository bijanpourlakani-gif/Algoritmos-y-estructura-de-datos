# 14).Realizar un programa que lea dos números enteros desde teclado e informe en pantalla cuál
# de los dos números es el mayor. Si son iguales debe informar en pantalla lo siguiente: “Los
# números leídos son iguales”


number1 = int(input("Ingrese el primer número entero: "))
number2 = int(input("Ingrese el segundo número entero: "))

if number1 > number2:
    print(f"El número mayor es: {number1}")
elif number2 > number1:
    print(f"El número mayor es: {number2}")
else:
    print("Los números leídos son iguales")

