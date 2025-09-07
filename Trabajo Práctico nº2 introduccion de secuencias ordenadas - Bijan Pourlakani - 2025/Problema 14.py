# 14).Dada la siguiente lista de compras de ingredientes para preparar una torta, mostrarla enpantalla, un ingrediente por límea. Luego corregir el último a ”Canela en polvo”[”Chocolate”, ”Huevos”, ”Manteca”, ”Crema de leche”, ”Frutillas”]

list_ingredients = ["Chocolate","Huevos","Manteca","Crema de leche","Frutillas"]

straight = list_ingredients
list_ingredients[4] = "Canela en polvo"
for ingredient in list_ingredients:
    print(ingredient)

