# 19). Crear una función que reciba un String y se encargue de poner en mayúscula la primera
# letra de cada palabra. No se pueden utilizar operaciones del lenguaje que lo resuelvan
# directamente.

def capitalize_words(text):
    results = ''
    new_word = True
    for c in text:
        if new_word and c.isalpha():
            results += c.upper()
            new_word = False
        else:
            results += c
        if c == ' ':
            new_word = True
    return results


print("Capitalizado:", capitalize_words("hola mundo cruel"))
