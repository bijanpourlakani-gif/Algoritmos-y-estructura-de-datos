# 25).Dada una lista de números, ingresada por el usuario o inventada por usted, cree otra lista con la cantidad de dígitos de cada número de la misma.

numbers = [3, 45, 789, 1024, -56, 0, 123456]

digits = [len(str(abs(num))) for num in numbers]

print("Números:", numbers)
print("Cantidad de dígitos:", digits)