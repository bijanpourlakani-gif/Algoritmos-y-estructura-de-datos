# 7).Se le permitirá al usuario ingresar una frase. Se mostrarán en pantalla solamente las letras en posiciones pares de la misma.

phrase = input('ingrese a una frase:')

pairposition= phrase[::2]

print(pairposition)
print('Las letras en posiciones pares:')