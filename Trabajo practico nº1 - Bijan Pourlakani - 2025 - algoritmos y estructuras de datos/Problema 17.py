# 17).Realizar un programa que permita al usuario ingresar 3 números, ordenarlos y mostrarlos
# luego en pantalla de menor a mayor.


number1= int(input('ingrese al valor númerico:'))
number2= int(input('ingrese al valor númerico:'))
number3= int(input('ingrese al valor númerico:'))

numbers = [number1,number2,number3]

numbers.sort()

print(f"Los numeros ordenados de menor a mayor son:")

for num in numbers:
    print(num)
