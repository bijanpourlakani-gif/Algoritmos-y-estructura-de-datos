# 9) Ídem anterior, pero debe mostrar el valor máximo y el mínimo del vector.

import random
array=[random.randint(1,50) for e in range (18)]
Adding = sum(array)
average = Adding/len(array)
maximum = max(array)
minimum = min(array)
print(Adding)
print(average)
print(f"El vector máximo  es:{maximum}")
print(f"el vector mínimo es:{minimum}")
