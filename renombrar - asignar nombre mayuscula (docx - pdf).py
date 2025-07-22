import os

# Carpeta con los archivos
carpeta = "C:/Users/Cristian/OneDrive - Universidad Católica de Chile/Escritorio/Nueva carpeta"

# Recorrer todos los archivos en la carpeta
for nombre_archivo in os.listdir(carpeta):
    ruta_actual = os.path.join(carpeta, nombre_archivo)

    if os.path.isfile(ruta_actual):
        nombre, extension = os.path.splitext(nombre_archivo)
        nuevo_nombre = f"{nombre.upper()}{extension}"
        nueva_ruta = os.path.join(carpeta, nuevo_nombre)

        try:
            # Intentar renombrar el archivo
            os.rename(ruta_actual, nueva_ruta)
            print(f"Renombrado: {nombre_archivo} -> {nuevo_nombre}")
        except Exception as e:
            print(f"No se pudo renombrar {nombre_archivo} -> {nuevo_nombre}. Error: {e}")
