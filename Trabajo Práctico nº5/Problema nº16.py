# 16). Dado un número entero formado sólo por los dígitos 0 (cero) y 1 (uno), diseñe una función
# que compruebe si el número tiene o no la misma cantidad  de ceros que de unos.

def same_numbers_zeros_ones(n):
    chain = str(n)
    return chain.count('0') == chain.count('1')
print("Ceros y unos iguales:", same_numbers_zeros_ones(1010))