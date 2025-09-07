#Dado el siguiente diccionario movie = {"titulo": "El padrino", "director": "Francis Ford Coppola", "año": 1972}, accede al valor del director e imprímelo. Luego actualiza el valor del año de lanzamiento a 1974.

movie = {
    "titulo": "El padrino",
    "director": "Francis Ford Coppola",
    "año": 1972
}


print("Director:", movie["director"])

movie["año"] = 1974


print("Diccionario actualizado:", movie)
