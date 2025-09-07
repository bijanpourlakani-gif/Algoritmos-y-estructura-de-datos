# 10).Permita al usuario ingresar el nombre de un archivo, genere un nuevo nombre donde los espacios sean reemplazados por gui´on bajo y la extensi´on por numerales.

archive = input("Ingresa el nombre del archivo (con su extensión): ")

archive_upgrade = archive.replace(" ", "_")

archive_upgrade = archive_upgrade.rsplit(".", 1)
if len(archive_upgrade) == 2:
    new_name = archive_upgrade[0] + "#" + archive_upgrade[1]
else:
    new_name = archive_upgrade[0]

print("Nombre modificado del archivo:")
print(new_name)