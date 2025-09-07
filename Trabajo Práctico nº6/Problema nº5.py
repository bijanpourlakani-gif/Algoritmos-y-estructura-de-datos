# 5).  Crear un programa que dado un archivo de texto, que contiene números (lo puede generar
# como ud. desee) determine el valor promedio y la suma de todos ellos.

entrance = input("Ingrese números separados por espacios: ")


with open("numeros.txt", "w") as archive:
    for num in entrance.split():
        archive.write(num + "\n")


with open("numeros.txt", "r") as archive:
    numbers = []
    for line in archive:
        line = line.strip()
        if line.isdigit():
            numbers.append(int(line))

if numbers:
    adding = sum(numbers)
    average = adding / len(numbers)
    print("Suma:", adding)
    print("Promedio:", average)
else:
    print("No hay números válidos en el archivo.")


