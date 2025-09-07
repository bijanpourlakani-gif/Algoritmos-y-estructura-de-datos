# 36).Pedirle al usuario dos números positivos, a y b. Controlar que a < b. Mostrar en pantalla los números del intervalo cerrado [a, b] La computadora deberá ahora seleccionar al azar un número de ese intervalo. Y el usuario deberá adivinar cuál número ha sido seleccionado por  la  computadora,  obteniendo  un  mensaje  de éxito  en  caso  de  acertar.  El  usuario  solo tendrá 10 vidas (número de intentos) y en caso de no acertar, deberá obtener un mensaje de pucha.

import random

# Paso 1: Pedir los números a y b
while True:
    a = int(input("Ingrese el primer número (a): "))
    b = int(input("Ingrese el segundo número (b): "))

    if a < b and a > 0 and b > 0:
        break
    else:
        print("Asegúrese de que a < b y ambos sean números positivos.")


print(f"Los números del intervalo cerrado [{a}, {b}] son:", list(range(a, b + 1)))

selected_number = random.randint(a, b)

lives = 10
while lives > 0:
    trys = int(input(f"Intenta adivinar el número (Tienes {lives} intentos): "))

    if trys == selected_number:
        print("¡Felicidades! Has adivinado el número.")
        break
    else:
        lives -= 1
        if lives > 0:
            print("¡Pucha! No es el número, intenta de nuevo.")
        else:
            print(f"Te quedaste sin vidas. El número era {selected_number}.")
