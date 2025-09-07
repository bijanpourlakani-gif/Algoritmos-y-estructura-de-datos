# 31).Suma de Números Positivos y Negativos: Se requiere un programa que permita el ingreso
# de 10 números y al finalizar muestre en pantalla la cantidad números positivos y por otra
# parte la cantidad de números negativos que fueron ingresados.

positives = 0
negatives = 0

print("Ingresa 10 números (positivos o negativos):")
for i in range(10):
    number= float(input(f"Ingrese el número #{i+1}: "))
    if number > 0:
        positives += 1
    elif number < 0:
        negatives += 1
    # Los ceros no se cuentan como positivos ni negativos

print(f"\nCantidad de números positivos: {positives}")
print(f"Cantidad de números negativos: {negatives}")
