# 2).Crear un programa que genere un archivo de texto llamado numeros.txt con 10 números
# enteros guardados en el mismo, uno por línea.

file = open("numeros.txt","w")
list_numbers = []

for i in range(1,11):
    list_numbers.append(i)

    file.write(f"{list_numbers} \n")

