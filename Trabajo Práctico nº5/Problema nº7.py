# 7).  Escriba una función denominada cuadrante(x, y), dónde x e y son valores enteros recibidos
# como parámetros los cuales representan un punto, y que retorne un valor entre 1, 2, 3 o 4
# de  acuerdo  al  cuadrante  que  se  encuentre  el  punto  (x, y),  ingresado  como  parámetro,  en  los ejes cartesianos.

def quadrant(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    else:
        return 0  # sobre ejes

print("Cuadrante:", quadrant(-3, 4)) # Nos indica que se encuentra en el segundo cuadrante