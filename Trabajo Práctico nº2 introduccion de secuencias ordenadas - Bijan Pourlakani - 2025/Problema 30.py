# 30).Cuenta Regresiva: Se requiere un programa que permita el ingreso de un número positivo
# y  muestre  en  pantalla  la  cuenta  regresiva  desde  el  número  ingresado  hasta  llegar  a  0.
# Realizar diferentes versiones del programa, utilizando en cada una, una estructura de bucle
# diferente de las que tiene disponibles en Python.

# Versión 1: Usando un bucle for:

number = int(input("Ingrese un número positivo: "))

print("Cuenta regresiva con FOR:")
for i in range(number, -1, -1):
    print(i)

#Versión 2: while

number2 = int(input("Ingrese un número positivo: "))  # Usuario escribe: 5

print("Cuenta regresiva con WHILE:")
while number2 >= 0:
    print(number2)
    number2 -= 1

#Versión 3: Simulando do-while

number3 = int(input("Ingrese un número positivo: "))  # Usuario escribe: 5

print("Cuenta regresiva simulando DO-WHILE:")
while True:
    print(number3)
    number3 -= 1
    if number3 < 0:
        break