# 10). Con  la  función  creada  en  el  ejercicio  anterior,  elabore  un  programa  en  donde  se  ingresa
#un  caracter  y  10  palabras;  y  muestre  la  cantidad  total  de  veces  que  apareció  el  carácter
#en las 10 palabras.

def counter_letter(chain, letter):
    counter = 0
    for c in chain:
        if c == letter:
            counter += 1
    return counter

def counter_letter_in_10_words(character,words):
    total = 0
    for word in words:
        total += counter_letter(word, character)
    return total
words_one = ["foods","drinks","teeth","dices","Argentina","Empanadas","frijoles","Hola","Cereza","Negro"]
print("Total de apariciones:",counter_letter_in_10_words("e",words_one))