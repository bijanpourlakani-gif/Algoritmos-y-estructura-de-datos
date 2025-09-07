# 29).Pedirle al usuario la cantidad de notas que desea ingresar. Luego pedir cada nota, y
# guardarlas.

notes = int(input("¿Cuántas notas deseas ingresar? "))


grades = []

for i in range(notes):
    note = float(input(f"Ingrese la nota #{i+1}: "))
    grades.append(note)


print("Las notas que ingresaste son:", grades)