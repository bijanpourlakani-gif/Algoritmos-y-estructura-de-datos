# 34).Permitir ingresar 10 números al usuario. Determinar y mostrar el menor y el mayor.

numbers = []

print("Ingresa 10 números:")

for i in range(10):
    number= float(input(f"Ingrese el número #{i+1}: "))
    numbers.append(number)

bigger = min(numbers)
smaller = max(numbers)

print(f"\nEl número menor ingresado es: {smaller}")
print(f"El número mayor ingresado es: {bigger}")