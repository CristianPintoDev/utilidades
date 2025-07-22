import re
import os
import fitz  # PyMuPDF. Instálalo con: pip install PyMuPDF

# Carpeta donde están los archivos PDF
carpeta = "C:/Users/Cristian/OneDrive - Universidad Católica de Chile/Escritorio/Nueva carpeta"  # Cambia esto por la ruta real

# Expresión regular para extraer el nombre
patron_nombre = re.compile(r"NOMBRE LEGAL:\s*(.+)")

# Recorrer todos los archivos en la carpeta
for nombre_archivo in os.listdir(carpeta):
    # Solo revisar los archivos que terminan en ".pdf"
    if nombre_archivo.endswith(".pdf"):
        ruta_archivo = os.path.join(carpeta, nombre_archivo)

        # Abrir el PDF
        doc = fitz.open(ruta_archivo)
        texto_completo = ""

        # Leer el texto de todas las páginas
        for pagina in doc:
            texto_completo += pagina.get_text()

        doc.close()

        # Buscar el nombre en el texto
        coincidencia = patron_nombre.search(texto_completo)
        if coincidencia:
            nombre_extraido = coincidencia.group(1).strip()

            # Limpiar caracteres no válidos en nombres de archivo
            nombre_extraido = re.sub(r'[\\/:*?"<>|]', '-', nombre_extraido)

            # Crear la nueva ruta con el nuevo nombre
            nueva_ruta = os.path.join(carpeta, f"{nombre_extraido}.pdf")

            # Renombrar el archivo
            os.rename(ruta_archivo, nueva_ruta)
            # print(f"Archivo renombrado: {nombre_archivo} -> {nombre_extraido}.pdf")
        else:
            print(f"No se encontró el nombre en el archivo: {nombre_archivo}")
