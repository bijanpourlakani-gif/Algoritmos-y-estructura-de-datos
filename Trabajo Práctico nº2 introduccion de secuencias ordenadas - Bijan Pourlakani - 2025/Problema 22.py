# 22).El  usuario  deberá  poder  ingresar  varios  nombres  completos  (ejemplo:  ”Luis  Pérez”).  El programa deberá luego, colocar los nombres en una lista y los apellidos en otra.

names = []
surnames = []

print("Ingresá nombres completos (ejemplo: Luis Pérez). Escribí 'FIN' para terminar.")

while True:
    entrance = input("Nombre completo: ")

    if entrance.upper() == "FIN":
        break

    parts = entrance.split()

    # Verificamos que tenga al menos dos palabras
    if len(parts) >= 2:
        names.append(parts[0])  # Primer palabra: nombre
        surnames.append(" ".join(parts[1:]))  # Resto: apellido completo
    else:
        print("Por favor ingresá al menos nombre y apellido.")

# Mostramos los resultados
print("Lista de nombres:")
print(names)

print("Lista de apellidos:")
print(surnames)