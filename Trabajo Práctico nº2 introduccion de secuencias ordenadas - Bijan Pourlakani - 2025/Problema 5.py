# 5).Pedir dos palabras al usuario y mostrarlas en pantalla concatenadas, es decir, una seguida de la otra.  ¿Cuales son todas las  maneras  en  que  se  pueden  mostrar  concatenadas  en pantalla,  cadenas  de  caracteres?  ¿Que diferencia hay entre mostrarlas una seguida de otra en pantalla, y en concatenarlas?

#¿Cuáles son todas las maneras de mostrar cadenas concatenadas en Python?

#Aquí tienes varias formas comunes de concatenar y mostrar cadenas en pantalla:

# 1). Usando el operador + (concatenación directa):

     #print(palabra1 + palabra2)

# 2).Usando una coma en print (muestra con espacio automáticamente):

    #print(palabra1, palabra2)
    #Esto no concatena, pero las muestra juntas separadas por espacio

# 3).Usando f-strings (formato literal):
     #print(f"{palabra1}{palabra2}")

# 4).Usando .format():

    #print("{}{}".format(palabra1, palabra2))

#5) Usando % (antiguo formato estilo C):

    # print("%s%s" % (palabra1, palabra2))


#¿Cuál es la diferencia entre mostrar las palabras una seguida de otra y concatenarlas?

#Mostrar una seguida de otra (por ejemplo con print(palabra1, palabra2)) significa que se imprimen en pantalla una al lado de la otra, separadas por un espacio (porque print() pone espacios entre los argumentos por defecto). No se crea una nueva cadena.

#Concatenar (como con palabra1 + palabra2) significa unir las dos cadenas en una sola nueva cadena. Esta nueva cadena puede ser guardada en una variable, usada para otros fines, etc.

#Ejemplo:

wordone = input('ingrese a una palabra:')

wordtwo = input('ingrese a una palabra:')

print(wordone+wordtwo)