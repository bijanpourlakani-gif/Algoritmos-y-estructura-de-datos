#Dado el siguiente diccionario diary = {"Juan": 47074963, "María": 46893258, "Pedro": 47123654}, elimina la entrada correspondiente a María.

diary = {
    "Juan": 47074963,
    "María": 46893258,
    "Pedro": 47123654
}


del diary["María"]

print("Diccionario actualizado:", diary)
