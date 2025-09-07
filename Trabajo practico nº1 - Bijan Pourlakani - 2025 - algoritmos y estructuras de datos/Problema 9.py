# 9).Mostrar en pantalla los resultados de calcular las siguientes expresiones (estas expresiones
# se encuentran  escritas  matemáticamente,  y  debería  reescribirlas  en  notación  de
# computadora  previamente;  cada  vez  que  encuentre  en  la  expresión  una  letra  minúscula,
# debe considerar  que  ese  dato  lo  debe  ingresar  el  usuario):
# • 5a + 10b
# • b2
# • 2x-y
#• 2n-1/2n-1





x = int(input('Ingrese al valor numérico:'))
y=  int(input('Ingrese al valor numérico:'))
a=  int(input('Ingrese al valor numérico:'))
b=  int(input('Ingrese al valor numérico:'))
n= int(input('Ingrese al valor numérico:'))

problem1= 5 * a + 10*b
problem2= b**2
problem3= 2*x-y
problem4= 2*n-1/2*n-1

print(f"El  resultado del punto 1 es:{problem1}")
print(f"El resultado del punto 2 es :{problem2}")
print(f"El resultado del punto 3 es :{problem3}")
print(f"El  resultado del punto 4  es:{problem4}")