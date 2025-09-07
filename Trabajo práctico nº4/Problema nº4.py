 # 4) Leer nombres y cargarlos en un vector, donde la lectura finaliza con “zzz”. Las zzz no deben
#estar dentro del vector. Luego mostrar los nombres por pantalla.

names = [ ]

while True:
    name= input("ingrese a una vector(o zzz en palabras):")
    if name.lower() == "zzz":
     break

    names.append(name)


for name in names:
 print(name)
