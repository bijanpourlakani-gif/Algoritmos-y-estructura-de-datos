# 33).Desarrollar un programa  que  permita  al usuario ingresar  una  serie  de  números, sumar todos
# los  pares  y  al  terminar mostrar  dicha  suma.  Si se  ingresó  algún  impar, mostrar un
# mensaje “Se ingresaron impares”. Para finalizar el ingreso, indicar la cantidad de números
# a ingresar al principio del programa, o interrumpir la carga cuando se ingrese el número 99.

pairs = 0
impairs = False

amount = int(input("¿Cuántos números deseas ingresar? (O escribe 99 para finalizar antes): "))

print("Ingresa los números (escribe 99 para finalizar anticipadamente):")
counter = 0

while counter < amount:
    number = int(input(f"Ingrese el número #{counter + 1}: "))

    if number == 99:
        break

    if number % 2 == 0:
        pairs += number
    else:
        impairs = True

    counter += 1

print(f"\nSuma de los números pares: {pairs}")
if impairs:
    print("Se ingresaron impares.")
