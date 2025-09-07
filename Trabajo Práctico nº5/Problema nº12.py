# 12). Crear  una  función  que  reciba  un  carácter  y  un  número  como  parámetros  e  imprima  en
#pantalla  un  triángulo  formado  por  ese  caracter  que  tenga  como  ancho  inicial  el  número
#recibido como parámetro. Por ejemplo, si el carácter es * y el ancho es 4, debería escribir:


def triangle_inverse(character, width):
    for i in range(width, 0, -1):
        print(character * i)


triangle_inverse("*", 4)