# 6).Crear una función que se encargue de crear un archivo de texto, con el nombre que se le dé
# como argumento. Y que lo llene con 250 números al azar entre 1 y 100.
import random

def crear_archivo_aleatorio(nombre_archivo):
    with open(nombre_archivo, "w") as archive:
        for _ in range(250):
            number= random.randint(1, 100)  # número al azar entre 1 y 100
            archive.write(str(number) + "\n")


crear_archivo_aleatorio("numeros_aleatorios.txt")
print("Archivo creado y lleno con 250 números al azar.")

