#Crea un programa que permita al usuario ingresar el nombre y la puntuación
#obtenida en un examen de varios estudiantes. Almacena esta información en un
#diccionario donde el nombre del estudiante sea la clave y su puntuación sea el valor.
#Luego, permite al usuario consultar la puntuación de un estudiante específico.



scores = {}


print("Ingresa los datos de los estudiantes (escribe 'fin' para terminar):")
while True:
    name = input("Nombre del estudiante: ")
    if name.lower() == 'fin':
        break
    try:
        score = float(input(f"Puntuación obtenida por {name}: "))

        scores[name] = score
    except ValueError:
        print("Por favor, ingresa una puntuación válida (número).")


print("\nListado de estudiantes y sus puntuaciones:")
for name, score in scores.items():
    print(f"{name}: {score}")


print("\nConsulta de puntuación:")
consulting = input("Ingresa el nombre del estudiante que deseas consultar: ")
if consulting in scores:
    print(f"{consulting} obtuvo una puntuación de {scores[score]}")
else:
    print(f"No se encontró a ningún estudiante llamado {consulting}.")
