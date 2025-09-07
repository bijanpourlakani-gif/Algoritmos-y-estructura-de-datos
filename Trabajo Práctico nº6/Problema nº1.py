#1). Crear un archivo de texto con el bloc de notas de Windows, y guardar una palabra por línea.
#Crear luego un programa que muestre en pantalla, una por una, las palabras que hay guardadas
#en ese archivo. Mostrar además, el total de líneas que había en el archivo.


file = open("New file.txt", "w")


words = ["pera", "bananas", "espinaca", "manzana"]


for word in words:
    file.write( f"{word} \n ")

file.close()

file= open("New file.txt", "r")

for line in file:

    print(line.strip())

