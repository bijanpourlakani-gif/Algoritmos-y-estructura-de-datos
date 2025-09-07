# 10).Escribir un programa que solicite al usuario ingresar un número con decimales y almacenarlo
# en una variable. A continuación, el programa debe solicitar al usuario que ingrese un número
# entero y guardarlo en otra variable. En una tercera variable se deberá guardar el resultado
# de la suma de los dos números ingresados por el usuario. Por último, se debe mostrar en
# pantalla el texto “El resultado de la suma es [suma]”, donde “[suma]” se reemplazará por el
# resultado de la operación.

float = float(input("ingrese  a un número decimal:"))
int = int(input("ingrese  a un número entero:"))

sum = float+int

print(f"El resultado de la suma entre los dos numero ingresados por el usuario es: {sum} ")