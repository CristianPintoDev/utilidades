import os
import re

# Carpeta con los archivos PDF
carpeta = "C:/ruta/"  # Cambia esto por la ruta de la carpeta

# Recorrer archivos PDF
for nombre_archivo in os.listdir(carpeta):
    if nombre_archivo.endswith(".pdf"):
        nombre_sin_extension = os.path.splitext(nombre_archivo)[0]
        partes = nombre_sin_extension.strip().split()

        # Verificar que tiene al menos 4 partes (nombre1, nombre2, apellido1, apellido2)
        if len(partes) >= 4:
            nombre1 = partes[0]
            apellido1 = partes[2]
            apellido2 = partes[3]

            nuevo_nombre = f"{nombre1} {apellido1} {apellido2}.pdf"
            nueva_ruta = os.path.join(carpeta, nuevo_nombre)
            ruta_original = os.path.join(carpeta, nombre_archivo)

            # Si ya existe un archivo con el nuevo nombre, saltar
            if os.path.exists(nueva_ruta):
                print(f"Archivo ya existe, saltando: {nuevo_nombre}")
                continue

            # Renombrar archivo
            os.rename(ruta_original, nueva_ruta)
            print(f"Renombrado: {nombre_archivo} -> {nuevo_nombre}")
        else:
            print(f"No se puede procesar (nombre muy corto): {nombre_archivo}")
