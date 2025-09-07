# 19). Pedir el nombre al usuario, y corroborar si ese nombre existe entre los nombres de usuarios válidos guardados en una lista.

optional = ["Charles","Clifford","Bruce","Vanessa","James"]

Name = input("Ingrese una de las nombres del usuario:")

if Name in optional:


    print("¡Acceso permitdo!")
    print(optional)
else:

    print("¡Acceso inválido!")
