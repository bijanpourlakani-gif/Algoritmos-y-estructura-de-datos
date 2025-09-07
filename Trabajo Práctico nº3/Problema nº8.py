#. Utilizando el diccionario ages = {"Juan": 30, "María": 25, "Pedro": 35}, agrega la entrada "Ana" con un valor de edad de 28 al diccionario. Imprime cada nombre seguido por su respectiva edad en una línea separada. Luego pedirle al usuario que ingrese un nombre y verificar si el nombre ingresado existe en el diccionario edades e imprime un mensaje apropiado en consecuencia.


ages = {"Juan": 30, "María": 25, "Pedro": 35}


print("Listado de edades:")
for name, edad in ages.items():
    print(f"{name}: {edad} años")


user_name = input("\nIngresa un nombre para verificar si está en el diccionario: ")

# Verificar si el nombre está en el diccionario
if user_name in ages:
    print(f"{user_name} tiene {ages[user_name]} años.")
else:
    print(f"{user_name} no se encuentra en el diccionario.")