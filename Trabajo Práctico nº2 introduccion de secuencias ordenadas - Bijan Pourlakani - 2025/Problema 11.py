# 11).Permitir ingresar al usuario un número de un dígito. Controlando se haya ingresado dicho número  de  no  más  de  1  dígito  de  longitud,  pasarlo  a  letras  y  mostrarlo  en  pantalla. (Ejemplo:  Si  ingresa  3,  se  ver´ a  como  resultado  ”tres”).

number_in_letters = { "0": "cero", "1": "uno","2": "dos", "3": "tres","4": "cuatro", "5": "cinco", "6": "seis", "7": "siete", "8": "ocho", "9":"nueve"}

number = input("Ingresa un número de un solo dígito (0-9): ")

if number.isdigit() and len(number) == 1:
      print("En letras:", number_in_letters[number])
else:
    print("Entrada inválida. Debes ingresar solo un número de un dígito (0-9).")