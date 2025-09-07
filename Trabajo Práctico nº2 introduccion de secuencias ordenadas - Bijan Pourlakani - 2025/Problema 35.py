# 35).Número  Invertido:  Se  requiere  mostrar  en  pantalla  un  nu ´mero  invertido  de  6  cifras,  al
# que fuera ingresado por teclado. (Ejemplo:  en  pantalla  se  verá:  “El  número  ingresado  es
# 140975, invertido es: 579041”)

number = input("Ingrese un número de 6 cifras: ")

if len(number) == 6 and number.isdigit():
    number_inverted = number[::-1]  # Invertir el número usando slicing
    print(f"El número ingresado es {number}, invertido es: {number_inverted}")
else:
    print("Por favor, ingrese un número válido de 6 cifras.")
