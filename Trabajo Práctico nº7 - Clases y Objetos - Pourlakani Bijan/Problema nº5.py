# 5).Realizar un programa que permita ingresar al usuario todos los vehículos que tienen en su familia.
# a. Crear una clase llamada Vehiculo.
# b. La clase debe contener los atributos: marca, modelo, patente, color.
# Guardar los vehículos en una lista. Finalmente, se deberán mostrar en pantalla todas las marcas de
# vehículos que la familia tiene. Con un conteo de cuántos en total vehículos de cada marca tienen.



class Vehicle:
    def __init__(self, brand, model, plate, color):
        self.brand = brand
        self.model = model
        self.plate = plate
        self.color = color
if __name__ == "__main__":
    vehicles = []

    while True:
        print("\n--- Enter Family Vehicles ---")
        brand = input("Marca: ")
        model = input("Modelo: ")
        plate = input("Patente: ")
        color = input("Color: ")


        vehicle = Vehicle(brand, model, plate, color)
        vehicles.append(vehicle)

        another = input("¿Desea ingresar otro vehículo? (s/n):: ")
        if another.lower() != "s":
            break


    print("\n=== Marcas de vehículos en la familia  ===")

    brand_count = {}
    for v in vehicles:
        if v.brand in brand_count:
            brand_count[v.brand] += 1
        else:
            brand_count[v.brand] = 1

    for brand, count in brand_count.items():
        print(f"Marca: {brand} - Cantidad: {count}")
