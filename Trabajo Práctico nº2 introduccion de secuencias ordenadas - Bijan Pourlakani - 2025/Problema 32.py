# 32).Permitir  ingresar  números  enteros  hasta  que  se  ingrese  la  opción  ”s” de  salir.  Luego mostrar por pantalla los número ingresados.

numbers = []

print("Ingresa números enteros. Escribe 's' para salir.")

while True:
    entrance = input("Ingrese un número (o 's' para salir): ")

    if entrance.lower() == 's':
        break

    try:
        number = int(entrance)
        numbers.append(number)
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número entero o 's' para salir.")

print("\nNúmeros ingresados:")
print(numbers)
