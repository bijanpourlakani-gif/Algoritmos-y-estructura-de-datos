# 9). Permita al usuario ingresar una frase. Cambie las letras a por 4 y las letras e por 3

phrase = input('ingrese a una frase:')

replacementone = phrase.replace("a","4").replace("A","4")
replacementone = replacementone.replace("e","3").replace("E","3")

print("la frase modificada")
print (replacementone)

