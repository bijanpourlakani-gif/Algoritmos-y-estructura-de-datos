# 18). Realizar un procedimiento que tome como parámetro una longitud e imprima en pantalla
# un  rectángulo  de  numerales,  hueco  por  dentro.  Por  ejemplo,  si  se  ingresó  4,  se  verá en
# pantalla:  Tip:  Puede  ser  útil  pensarlo  por  línea  horizontal
# Generalizarlo,  luego,  en una versión  2,  para  un parámetro  extra:  el  carácter  que  se  usará
# para dibujar el rectángulo, en vez de usar siempre un numeral.

def hollow_rectangle(side, character='#'):
    print(character * side)
    for _ in range(side - 2):
        print(character + ' ' * (side - 2) + character)
    print(character * side)


hollow_rectangle(4)