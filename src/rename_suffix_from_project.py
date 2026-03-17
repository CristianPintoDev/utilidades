import os

def rename_suffix_from_project(carpeta, extension_proyecto):

    for nombre_archivo in os.listdir(carpeta):
        ruta_completa = os.path.join(carpeta, nombre_archivo)

        if os.path.isfile(ruta_completa):
            nombre, extension = os.path.splitext(nombre_archivo)

            if ' _' in nombre:
                nuevo_nombre_base = nombre.rsplit(' _', 1)[0]
                nuevo_nombre = nuevo_nombre_base + extension 
                nueva_ruta = os.path.join(carpeta, nuevo_nombre)

                # Evitar sobreescribir archivos existentes
                contador = 1
                while os.path.exists(nueva_ruta):
                    nuevo_nombre = f"{nuevo_nombre_base}_{contador}{extension}"
                    nueva_ruta = os.path.join(carpeta, nuevo_nombre)
                    contador += 1

                os.rename(ruta_completa, nueva_ruta)
                print(f"Renombrado: {nombre_archivo} -> {nuevo_nombre}")
            
            elif '_' in nombre:
                nuevo_nombre_base = nombre.rsplit('_', 1)[0]
                nuevo_nombre = nuevo_nombre_base + extension
                nueva_ruta = os.path.join(carpeta, nuevo_nombre)

                # Evitar sobreescribir archivos existentes
                contador = 1
                while os.path.exists(nueva_ruta):
                    nuevo_nombre = f"{nuevo_nombre_base}_{contador}{extension}"
                    nueva_ruta = os.path.join(carpeta, nuevo_nombre)
                    contador += 1

                os.rename(ruta_completa, nueva_ruta)
                print(f"Renombrado: {nombre_archivo} -> {nuevo_nombre}")
            

    for nombre_archivo in os.listdir(carpeta):
        ruta_completa = os.path.join(carpeta, nombre_archivo)  
        nombre, extension = os.path.splitext(nombre_archivo)  
        nuevo_nombre = nombre + extension_proyecto + extension
        nueva_ruta = os.path.join(carpeta, nuevo_nombre)

        # Evitar sobreescribir archivos existentes
        contador = 1
        while os.path.exists(nueva_ruta):
            nuevo_nombre = f"{nombre}_{contador}{extension}"
            nueva_ruta = os.path.join(carpeta, nuevo_nombre)
            contador += 1

        os.rename(ruta_completa, nueva_ruta)
        print(f"Renombrado: {nombre_archivo} -> {nuevo_nombre}")

