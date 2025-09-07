#Dada la siguiente tupla numbers = (1, 2, 3, 4, 5), elimina el número 3 y crea una nueva tupla sin ese elemento.

tuple1 = (1,2,3,4,5)

new_tuple= list(tuple1)
new_tuple.remove(3)
all_new_tuple = tuple(new_tuple)

print(all_new_tuple)