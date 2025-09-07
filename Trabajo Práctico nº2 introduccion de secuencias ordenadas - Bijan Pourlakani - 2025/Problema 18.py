# 18).Crear dos listas del mismo tamaño,  y  luego  armar  una  tercer  lista,  a  la  cual  primero  se  le
# agregue  el  primer elemento de la lista 1, luego el primer elemento de la lista 2. Luego se le
# agregue el segundo elemento de la lista 1, luego el segundo elemento de la lista 2, y así
# sucesivamente.
# Ejemplo: Supongamos tenemos una lista de frutas y otra de verduras. La tercera quedará:

cake_list_ = ["frosting", "cream" , "butter"]

dinner_list= ["meat","cheese","onions"]

full_course_meal=[]

for e in range(len(cake_list_)):
    full_course_meal.append(cake_list_[e])
    full_course_meal.append(dinner_list[e])



print("Lista combinada:")
print(full_course_meal)
