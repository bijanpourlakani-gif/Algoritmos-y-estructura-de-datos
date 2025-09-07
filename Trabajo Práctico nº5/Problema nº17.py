# 17). Desarrollar  una  función  que  retorne  la  posiciÓn  de  un  carácter  (la  primera  vez  que  apa-
# rezca) dentro de la cadena de N  caracteres de longitud, donde se reciben como parámetro
# la cadena  y el carácter respectivamente.

def position_character(chain, character):
    for i, c in enumerate(chain):
        if c == character:
            return i
    return -1


print("Posición del carácter:", position_character("American", "n"))
