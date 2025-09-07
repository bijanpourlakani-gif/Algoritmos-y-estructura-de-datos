#  Leer nombres y cargarlos en un vector, donde la lectura finaliza con “zzz”. Las zzz no deben
# estar dentro del vector. Luego mostrar los nombres por pantalla.


names = []


while True:
    name = input("Ingrese un nombre (o 'zzz' para finalizar): ")
    if name.lower() == "zzz":
        break
    names.append(name)

print(f"Nombres ingresados:")
for name in names:
    print(name)









