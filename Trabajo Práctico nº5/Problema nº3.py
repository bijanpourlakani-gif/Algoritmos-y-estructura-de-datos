# 3). ¿Qué imprimirá en pantalla el siguiente código? ¿Cuál es el alcance de la variable frase?

phrase = " Hola"

def f():
    phrase = "Es un lindo dia"
    print(phrase)  # Imprime "Es un lindo dia"


f()
print(phrase)

 # a) La primera línea imprime "Es un lindo dia" (valor de la frase local).La segunda línea imprime " Hola" (valor de la frase global, que no fue modificada).
 # b) La frase global: tiene alcance global, es accesible desde cualquier parte del código excepto cuando hay una variable local con el mismo nombre dentro de una función.
      #La frase dentro de f(): es local, existe sólo dentro de la función f().

