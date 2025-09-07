# 17). Pida  10  nombres  de  pelÍculas  al  usuario.  Guardelos  en  una  lista.  Luego  pida  al  usuario
# que  ingrese  un  número  n del  1  al  10.  Controle  que  n esté  en  el  rango  correcto,  es  decir
# entre  1  y  10.  Muestre  en  pantalla  cuál  es  la  película  n-ésima.  Por  ejemplo,  si  el  usuario
# me ingresa 1, debo mostrar la primer película de la lista.

movies = []
for e in range(10):

 best = input(f"Ingrese a los nombres de las peliculas {e+1}: ")

 movies.append(best)

select_ = int(input("ingrese a un numero de la lista:"))

if 1<=select_<= 10 :

    print(f"La pelicula seleccionada {select_} es:{movies[select_ -1]}")

else:

    print("Un numero inválido")
