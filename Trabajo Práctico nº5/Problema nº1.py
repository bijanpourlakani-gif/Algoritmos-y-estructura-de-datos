# 1). Crear una función llamada cuadrado que tome un número como parámetro e imprima en
#pantalla dicho número al cuadrado.

#a) Imprimir, desde dentro de la función, las variables locales que ésta posea. ¿Qué se
#imprime? * utilizar locals()

#b) Agregar dos o tres variables extras con valores inventados, y volver a mostrar todas
#las variables locales. ¿Hubo cambio alguno?

#a)
def square(x):

    results = x**2
    print(f"el cuadrado de {x} es {results}")
    print(f"Las variable locales",locals())

square(4)




#b)
def square(x):

    results = x**2
    description = "Cálculo al cuadrado"
    author = "james"
    print(f"el cuadrado de {x} es {results}")
    print(f"Las variable locales",locals())

square(3)