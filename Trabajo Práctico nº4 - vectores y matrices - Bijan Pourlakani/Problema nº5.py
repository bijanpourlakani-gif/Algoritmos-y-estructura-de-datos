#Crear un vector de 20 elementos. Luego lea por teclado una posición X y otra posición Y, e
#imprima el vector desde la posición X hasta la Y.

array = list(range(1,21))

x = int(input("ingrese a la posicion x en (0-19):"))
y = int(input("ingrese a la posicion y en (0-19):"))

if 0 <=x<=y<=19 :

  print(f"el vector desde la posicion x hasta y",array [x:y:1])

else:

    print(f"el vector es inválido")