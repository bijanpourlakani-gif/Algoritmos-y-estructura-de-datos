 # 2). Crear una variable llamada n, que será global, en el código del ejercicio anterior y asignarle
#un valor inventado. Realizar las siguientes acciones:
#a) Mostrar el valor de n, elevado al cuadrado desde dentro del procedimiento.
#b) Modificar el valor de n, dentro del procedimiento. ¿Qué ocurre?
#c) Si necesitase modificar el valor de n, que es una variable global, dentro del
#procedimiento cuadrado, ¿Qué debería hacer?


global_n = 5

def square_global():
    global global_n
    print("Global al cuadrado:", global_n ** 2)
    global_n = 10  # Para modificar se usa 'global'

# Bloque de prueba del ejercicio 2
print("Antes de la función:", global_n)
square_global()
print("Después de la función:", global_n)

#a) Esto funciona correctamente, porque podemos leer una variable global desde una función sin problema, aunque no hayamos declarado global.
#b) sin la palabra global, Python crearía una nueva variable local llamada global_n dentro de la función, lo que puede causar confusión o errores.
# c) Se utiliza la palabra clave global dentro de la función antes de usar la variable.