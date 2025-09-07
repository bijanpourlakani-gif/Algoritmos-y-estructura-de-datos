# 8) Ídem anterior, pero debe mostrar el promedio de sus elementos.

import random
array=[random.randint(1,50) for e in range (18)]
Adding = sum(array)
average = Adding/len(array)
print(f"El promedio total es:{average}")
