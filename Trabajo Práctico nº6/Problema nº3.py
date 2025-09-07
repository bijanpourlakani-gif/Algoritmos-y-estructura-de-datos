# 3). Crear un programa que le pida al usuario 5 colores, y los guarde en un archivo de texto llamado
# colores.txt.

file = open("colores.txt","w")



for i in range(5):

   colours = input(f"ingrese una color {i+1}:")

   file.write(f"{colours} \n")

file.close()