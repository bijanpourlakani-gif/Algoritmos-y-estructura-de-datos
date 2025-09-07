
# 3).Pida una frase al usuario, controle que tenga una longitud total mayor a 5 caracteres. Muestre en pantalla los primeros 3 caracteres de la misma.



phrase = input('ingrese a una frase:')
if len(phrase)>=5:
    print(f"Los 3 caracteres son:",phrase[:3])

else:
    print("Debe tener más de cinco caracteres")