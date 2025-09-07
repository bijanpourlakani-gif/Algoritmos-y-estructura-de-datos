# 7). Desarrollar un programa de gestión de ventas que almacena sus datos en un archivo .txt. Cada
# producto se guarda en una línea del archivo de la siguiente manera:
# [nombre_producto], [cantidad_vendida], [precio]
# Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar, actualizar,
# eliminar productos y salir.  También debe poseer opciones para calcular la venta total y por
# producto. La opción salir borra el .txt.



import os

FILE = "ventas.txt"

def read():
    if not os.path.exists(FILE):
        return []
    with open(FILE) as f:
        return [line.strip().split(",") for line in f]

def save(products):
    with open(FILE, "w") as f:
        for p in products:
            f.write(",".join(p) + "\n")

while True:
    print("\n1.Agregar 2.Consultar 3.Actualizar 4.Eliminar 5.Total 6.Total Producto 7.Salir")
    option = input("Opción: ")

    products = read()

    if option == "1":
        name = input("Nombre: ")
        quantity = input("Cantidad vendida: ")
        price = input("Precio: ")
        products.append([name, quantity, price])
        save(products)
        print("Producto agregado.")

    elif option == "2":
        for p in products:
            print(f"Producto: {p[0]}, Cantidad: {p[1]}, Precio: {p[2]}")

    elif option == "3":
        name = input("Nombre a actualizar: ")
        for p in products:
            if p[0] == name:
                p[1] = input("Nueva cantidad: ")
                p[2] = input("Nuevo precio: ")
                save(products)
                print("Producto actualizado.")
                break
        else:
            print("Producto no encontrado.")

    elif option == "4":
        name = input("Nombre a eliminar: ")
        products = [p for p in products if p[0] != name]
        save(products)
        print("Producto eliminado si existía.")

    elif option == "5":
        total = 0
        for p in products:
            total += int(p[1]) * float(p[2])
        print(f"Venta total: ${total:.2f}")

    elif option == "6":
        name = input("Nombre del producto: ")
        for p in products:
            if p[0] == name:
                total_prod = int(p[1]) * float(p[2])
                print(f"Venta total de {name}: ${total_prod:.2f}")
                break
        else:
            print("Producto no encontrado.")

    elif option == "7":
        if os.path.exists(FILE):
            os.remove(FILE)
        print("Archivo borrado. Saliendo...")
        break

    else:
        print("Opción inválida.")

