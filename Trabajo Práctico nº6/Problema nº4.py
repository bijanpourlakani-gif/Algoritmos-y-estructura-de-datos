# 4).Crear un programa que dado un archivo de números con valores entre 1 y 10 (lo puede generar
#como ud. desee) determine cuántos números iguales a 5 hay en el archivo.


with open("numeros.txt", "w") as archive:
    for i in range(10):
        number = input(f"Ingrese el número {i+1}: ")
        archive.write(number + "\n")


counter = 0

with open("numeros.txt", "r") as archive:
    for line in archive:
        line = line.strip()
        if line.isdigit():
            if int(line) == 5:
                counter += 1

print("Cantidad de veces que aparece el número 5:", counter)
