#15).Dada la  siguiente  lista  de  valores  numéricos  [56, 7, 34, 19, 3, 1, 76, 2, 81, 4, 2, 8]  muestre  en pantalla solo los elementos de la misma que están ubicados en posiciones pares, como 0, 2, 4, etc (¿Cómo puede determinar si un nro es par o no? ¿Deberá escribir cada print de  a  uno,  o  deberá  considerar  realizar  un  recorrido  por  la  lista,  usando  un  bucle?)
# Buena pregunta. Para resolver esto, lo ideal es usar un bucle que recorra la lista y muestre solo los elementos en índices pares (0, 2, 4, etc.).

# En este caso utilice el slicing para indicar a los elementos de las posiciones pares utilizando y el 2 nos indica que estamos saltamos cada vez en la posicion de los elementos


list_ = [56,7,34,19,3,1,76,2,81,4,2,8]

pairlist = list_[::2]

for pair in pairlist:

 print(pair)


