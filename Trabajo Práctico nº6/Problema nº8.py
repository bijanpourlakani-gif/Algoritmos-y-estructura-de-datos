# 8)Desarrollar un programa que gestione una agenda de contactos usando un archivo de texto
# (agenda.txt). Cada línea del archivo debe contener un contacto en el siguiente formato:
# [nombre],[teléfono],[email]
# El programa debe ofrecer un menú en consola con las siguientes opciones:
# a) Agregar contacto: Pedir nombre, teléfono y email, y agregarlo al archivo.
# b) Mostrar todos los contactos: Leer el archivo línea por línea y mostrar los contactos uno
# por uno.
# c) Buscar contacto por nombre: Pedir un nombre y mostrar si existe en la agenda (mostrar
# también sus datos).
# d) Eliminar contacto: Pedir un nombre, y si existe, eliminar esa línea del archivo.
# e) Actualizar contacto: Pedir nombre, y si existe, permitir modificar su teléfono o email.
# f) Contar contactos totales: Mostrar cuántos contactos hay guardados en el archivo.
# g) Salir del programa: Terminar la ejecución.

import os
import sys

FILE = "agenda.txt"
LOG_FILE = "log_agenda.txt"

# Función para imprimir en pantalla y guardar en archivo
def print_log(text):
    print(text)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")

def read_contacts():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as f:
        return [line.strip().split(",") for line in f]

def save_contacts(contacts):
    with open(FILE, "w", encoding="utf-8") as f:
        for c in contacts:
            f.write(",".join(c) + "\n")

while True:
    print_log("\n--- Menú Agenda ---")
    print_log("a) Agregar contacto")
    print_log("b) Mostrar todos los contactos")
    print_log("c) Buscar contacto por nombre")
    print_log("d) Eliminar contacto")
    print_log("e) Actualizar contacto")
    print_log("f) Contar contactos totales")
    print_log("g) Salir")

    option = input("Opción: ").lower()
    contacts = read_contacts()

    if option == "a":
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        contacts.append([nombre, telefono, email])
        save_contacts(contacts)
        print_log("Contacto agregado.")

    elif option == "b":
        if contacts:
            for c in contacts:
                print_log(f"Nombre: {c[0]}, Teléfono: {c[1]}, Email: {c[2]}")
        else:
            print_log("No hay contactos.")

    elif option == "c":
        nombre = input("Nombre a buscar: ")
        for c in contacts:
            if c[0].lower() == nombre.lower():
                print_log(f"Encontrado: Nombre: {c[0]}, Teléfono: {c[1]}, Email: {c[2]}")
                break
        else:
            print_log("Contacto no encontrado.")

    elif option == "d":
        nombre = input("Nombre a eliminar: ")
        new_contacts = [c for c in contacts if c[0].lower() != nombre.lower()]
        if len(new_contacts) != len(contacts):
            save_contacts(new_contacts)
            print_log("Contacto eliminado.")
        else:
            print_log("Contacto no encontrado.")

    elif option == "e":
        nombre = input("Nombre a actualizar: ")
        for c in contacts:
            if c[0].lower() == nombre.lower():
                nuevo_tel = input(f"Nuevo teléfono (actual: {c[1]}): ")
                nuevo_email = input(f"Nuevo email (actual: {c[2]}): ")
                if nuevo_tel.strip():
                    c[1] = nuevo_tel
                if nuevo_email.strip():
                    c[2] = nuevo_email
                save_contacts(contacts)
                print_log("Contacto actualizado.")
                break
        else:
            print_log("Contacto no encontrado.")

    elif option == "f":
        print_log(f"Total de contactos: {len(contacts)}")

    elif option == "g":
        print_log("Saliendo del programa...")
        break

    else:
        print_log("Opción inválida.")
