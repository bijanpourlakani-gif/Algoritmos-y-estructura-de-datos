# 12).Se  le  pedirá  al  usuario  una  frase.  Se  mostrarán  en  pantalla,  una  palabra  por  línea  de  la misma. *no usar listas en este ejercicio

phrase = input('ingrese a una frase:')

word = ""
for character in phrase:
    if character != " ":

        word += character

    else:
        print(word)

        word= " "

if word:
            print(word)