# 4).Pida un número al usuario, mayor que 1 y menor a 50. Muestre en pantalla los números de 1 hasta ese número ingresado, uno por línea.

number = int (input('ingrese a un numero mayor que 1 y menor a 50:'))

if 1 < number < 50:

 for i in range (1, number+1):

    print(i)

else:
    print('Numero inválido. Debe ser mayor que 1 y menor que 50')


