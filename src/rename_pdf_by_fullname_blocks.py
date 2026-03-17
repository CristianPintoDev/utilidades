import re, os
import fitz  # PyMuPDF

def rename_pdf_by_fullname_blocks(carpeta):

    # Expresión regular para detectar nombre y dos apellidos
    patron_nombre = re.compile(r"\b([A-ZÁÉÍÓÚÑ]{2,})\s*\n\s*([A-ZÁÉÍÓÚÑ]{2,})\s+([A-ZÁÉÍÓÚÑ]{2,})")

    # Recorrer archivos PDF
    for nombre_archivo in os.listdir(carpeta):
        if nombre_archivo.endswith(".pdf"):
            ruta_archivo = os.path.join(carpeta, nombre_archivo)
            doc = fitz.open(ruta_archivo)
            texto_completo = ""
            for pagina in doc:
                texto_completo += pagina.get_text()
            doc.close()

            # Buscar nombre + apellidos
            coincidencia = patron_nombre.search(texto_completo)
            if coincidencia:
                nombre = coincidencia.group(1).capitalize()
                apellido1 = coincidencia.group(2).capitalize()
                apellido2 = coincidencia.group(3).capitalize()

                nuevo_nombre = f"{nombre} {apellido1} {apellido2}"
                nuevo_nombre = re.sub(r'[\\/:*?"<>|]', '-', nuevo_nombre)  # Limpiar nombre

                nueva_ruta = os.path.join(carpeta, f"{nuevo_nombre}.pdf")

                # Verificar si ya existe un archivo con ese nombre
                if os.path.exists(nueva_ruta):
                    print(f"Archivo ya existe, saltando: {nuevo_nombre}.pdf")
                    continue  # Saltar al siguiente archivo

                # Renombrar el archivo
                os.rename(ruta_archivo, nueva_ruta)
                print(f"Archivo renombrado: {nombre_archivo} -> {nuevo_nombre}.pdf")
            else:
                print(f"No se encontró nombre completo en: {nombre_archivo}")
