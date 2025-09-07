#18).Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si
#el divisor es cero el programa debe mostrar un mensaje de error.

Divisionone= float(input('Ingresar al valor numérico:'))
Divisiontwo= float(input('Ingresar al valor numérico:'))

if Divisiontwo != 0 :
    Division = Divisionone / Divisiontwo

    print(f"El resultado de la division es :{Division}")
else:
    print("ERROR")
