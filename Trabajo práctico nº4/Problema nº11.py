# 11) Dada las siguientes notas almacenadas en un arreglo: [33, 11, 20, 2, 15, 1, 12, 11, 8, 14, 10]
#Elimine la nota más baja programáticamente sin usar la función (min) y escríbala en pantalla.
#Luego programáticamente calcule el promedio de notas descontando la nota eliminada.

scores = [33,11,20,2,15,1,12,11,8,14,10]
low_score = scores[0]
pos_score = 0

for i in range(1,len(scores)):

  if scores[i]<low_score:
   low_score = scores[i]
   pos_score =i

eliminate_score = scores.pop(pos_score)
print(f"la nota eliminada: {eliminate_score}")

average = sum(scores)/len(scores)
print("El proimedio de notas descontando la nota eliminada:",round(average,2))



