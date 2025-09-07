# 20). Crear una función que reciba dos array, un booleano y retorne un array.
# - Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
# - Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
# - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.

def operate_arrays(arr1, arr2, common):
    results = []
    for x in arr1:
        if (x in arr2) == common:
            results.append(x)
    for x in arr2:
        if (x in arr1) == common and x not in results:
            results.append(x)
    return results

print("Elementos comunes:", operate_arrays([1,2,3], [2,3,4], True))
print("Elementos no comunes:", operate_arrays([1,2,3], [2,3,4], False))