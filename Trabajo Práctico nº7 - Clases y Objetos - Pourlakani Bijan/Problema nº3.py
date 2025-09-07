# 3).Crear una clase llamada Persona. Sus atributos son: nombre, apellido, edad y DNI. Construye los
# siguientes métodos para la clase:
# a. Un constructor, donde los datos pueden estar vacíos.
# b. mostrar(): Muestra los datos de la persona.
# c. esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.


class Person:
    def __init__(self, first_name="", last_name="", age=0, id_number=""):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.id_number = id_number

    def show(self):

        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"ID number: {self.id_number}")

    def is_adult(self):

        return self.age >= 18



person1 = Person("John", "Smith", 25, "12345678")
person1.show()
print("Is adult?", person1.is_adult())




