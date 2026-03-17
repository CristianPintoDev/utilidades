import re
import os
from docx import Document # instalar docx -  pip install docx

# Carpeta donde están los archivos de Word
carpeta = "C:/ruta/"  # Cambia esto por la ruta de la carpeta



# Utilizar una expresión regular para encontrar y guardar el nombre entre
# en este caso busca entre "del(la) Sr(a). " y ", RUT:"
patron_nombre = re.compile(r"del\(la\) Sr\(a\)\. (.+?), RUT:")

# For para recorrer todos los archivos en la carpeta
for nombre_archivo in os.listdir(carpeta):
    # Solo revisará los archivos que comienzan con "INFORME FIBROSCAN-" y terminan en ".docx"
    if nombre_archivo.startswith("INFORME FIBROSCAN-") and nombre_archivo.endswith(".docx"):
        # en ruta_archivo une el nombre completo de la ruta mas el nombre del archivo
        ruta_archivo = os.path.join(carpeta, nombre_archivo)
        
        # Carga el documento
        doc = Document(ruta_archivo)
        
        # Buscar el nombre en el documento
        nombre_extraido = None
        for parrafo in doc.paragraphs:
            texto = parrafo.text
            coincidencia = patron_nombre.search(texto)
            if coincidencia:
                nombre_extraido = coincidencia.group(1).strip()
                break  # Salir del bucle una vez que se encuentra el nombre
        
        # Si se encontró el nombre, renombrar el archivo
        if nombre_extraido:
            # Limpiar el nombre del archivo (eliminar caracteres no válidos)
            nombre_extraido = re.sub(r'[\\/:*?"<>|]', '-', nombre_extraido)
            
            # Crear la nueva ruta del archivo
            nueva_ruta = os.path.join(carpeta, f"{nombre_extraido}.docx")
            
            # Renombrar el archivo
            os.rename(ruta_archivo, nueva_ruta)
            #print(f"Archivo renombrado: {nombre_archivo} -> {nombre_extraido}.docx")
        else:
            # un print para ver que archivos no se renombraron y verificar el porqué
            print(f"No se encontró el nombre en el archivo: {nombre_archivo}")