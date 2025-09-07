# 8).El usuario deberá ingresar ingresar  una  frase  y  una letra. Determine  cuántas  veces  está esa  letra  en  dicha  frase, mostrar por pantalla.

phrase= input('ingrese a una frase:')
letter = input('ingrese a una letra:')

if len(letter) !=1:

    print('Solo ingresar a una sola letra')

else:

    amount = phrase.lower().count(letter.lower())

    print(f'la letra {letter} aparece {amount} de veces en la frase')