# 24).Pedir al usuario una frase. Determinar de al menos dos modos diferentes (con y sin listas)  la cantidad de palabras que hay en dicha frase.

# con lista:
phrase = input("Ingresá una frase: ")

words = phrase.split()
amount_of_words = len(words)

print(f"Cantidad de palabras (con listas): {amount_of_words}")

# Sin lista:

phrase2 = input("Ingresá una frase: ")

in_word= False
count = 0

for character in phrase:
    if character != " " and not in_word:
        count += 1
        in_word = True
    elif character == " ":
        in_word = False

print(f"Cantidad de palabras (sin listas): {count}")



