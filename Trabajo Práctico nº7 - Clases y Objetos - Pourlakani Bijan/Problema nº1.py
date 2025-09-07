# 1).Crear una clase llamada Alumno que tenga como atributo el nombre y la nota de alumno. Definir los
# métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si
# ha aprobado o no.

class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade

    def show_data (self):
        print(f"Nombre:{self.name}")
        print(f"Nota:{self.grade}")


    def show_results(self):
        if self.grade >=6:
            print(f"El alumno {self.name} aprobo con {self.grade} ")

        else:
            print(f"El alumno {self.name}  desaprobo con {self.grade} ")

student_one = Student ("Joeseph",9)
student_two = Student ("James",5)

student_one.show_data()
student_one.show_results()

student_two.show_data()
student_two.show_results()


