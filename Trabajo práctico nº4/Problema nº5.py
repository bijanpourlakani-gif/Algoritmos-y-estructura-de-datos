# 5) Crear un vector de 20 elementos. Luego lea por teclado una posición X y otra posición Y, e
#imprima el vector desde la posición X hasta la Y.

array = list(range(1,21))

x= int(input(f"ingrese desde la posicion X en (0-19):"))
y= int(input(f"ingrese  desde la posicion Y en (0-19):"))

if 0<=x<=y<=19:

 print(f"el vector desde la posición x a y son",array[x:y+1])

else:
    print("El vector no pertenece en la posicion X hasta la Y")