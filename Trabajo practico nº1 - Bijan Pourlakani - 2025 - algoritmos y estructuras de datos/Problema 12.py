# 12).Leer dos  números  y  determinar  cuál  de  ellos  es  el  mayor,  mostrando  por  pantalla  “El
# valor mayor es:” y el correspondiente número.


message1= int(input('ingrese a un numero:'))
message2= int(input('ingrese a un numero:'))

if message2>message1:

    print(f"El valor mayor es: {message2}")

elif message2<message1:

    print(f"el valor mayor es : {message1}")

else:
        print(f"los valores ingresados son inguales")
