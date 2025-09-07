# 6).Realizar un programa para calcular la liquidación de sueldo:
#a. Crear una clase llamada “Empleado”
#b. La clase debe contener los atributos: nombre, horas-trabajadas y tarifa-hora.
#c. Crear el método:calculo-salario.
#d. Pedir al usuario que ingrese todos los empleados que son parte de la empresa en una lista para
# que luego el programa calcule el sueldo que le corresponde cobrar en función de las horas
#trabajadas y el valor de la hora trabajada para cada empleado que figure en la lista. Mostrar en
#pantalla el nombre del empleado y el sueldo que le corresponde cobrar.

class Employee:
    def __init__(self, name, hours_worked, hourly_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):

        return self.hours_worked * self.hourly_rate


if __name__ == "__main__":
    employees = []

    while True:
        print("\n--- Ingreso de datos del empleado ---")
        name = input("Nombre: ")
        hours = float(input("Horas trabajadas: "))
        rate = float(input("Tarifa por hora: "))

   
        employee = Employee(name, hours, rate)
        employees.append(employee)

        another = input("¿Desea ingresar otro empleado? (s/n): ")
        if another.lower() != "s":
            break

    # Calculate and show salaries
    print("\n=== Sueldos de los empleados ===")
    for emp in employees:
        print(f"Empleado: {emp.name} - Sueldo: ${emp.calculate_salary():.2f}")
