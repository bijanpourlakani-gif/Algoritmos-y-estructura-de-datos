# 23).Se deberán ingresar 8 notas a una lista. Se mostrará el promedio, redondeado a 2 decimales.


notes= []

for i in range(8):
    note = float(input(f"Ingresá la nota #{i+1}: "))
    notes.append(note)


average = sum(notes) / len(notes)

print(f"El promedio de las notas es: {round(average, 2)}")