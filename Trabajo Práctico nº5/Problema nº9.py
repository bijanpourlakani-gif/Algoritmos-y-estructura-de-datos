# 9). Crear una función  que  reciba  una  cadena  de  caracteres  y  una  letra  como  parámetros,  y
# devuelva la cantidad de veces que dicha letra aparece en la cadena.
# Por  ejemplo,  si  la  cadena  es  ’Barcelona’  y  la  letra  es  ’a’,  debería  devolver  2  (aparece  2
# veces).

def counter_letter(chain, letter):
    counter = 0
    for c in chain:
        if c == letter:
            counter += 1
    return counter


print("Cantidad de letras:", counter_letter("America", "e"))