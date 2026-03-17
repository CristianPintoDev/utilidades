# File Renamer CLI

Herramienta en Python para automatizar el renombrado de archivos **PDF y DOCX** utilizando distintas reglas.

Este proyecto reúne varias utilidades que originalmente estaban separadas en scripts independientes y las integra en una **interfaz de línea de comandos (CLI)** fácil de usar.

---

## Funcionalidades

La herramienta permite realizar diferentes tipos de renombrado:

* Convertir nombres de archivos a **MAYÚSCULAS**
* Eliminar el **segundo nombre** de archivos
* Renombrar archivos **PDF según su contenido**
* Renombrar archivos **DOCX según su contenido**
* Extraer **nombre completo desde el contenido de un PDF**
* Limpiar o modificar **sufijos en nombres de archivo**

---

## Requisitos

* Python 3.10 o superior

Instalar dependencias:

```
pip install -r requirements.txt
```

Dependencias utilizadas:

* PyMuPDF
* python-docx

---

## Uso

Ejecutar el script desde la terminal:

```
python renamer.py <accion> <carpeta>
```

Ejemplo:

```
python renamer.py rename_to_uppercase C:/documentos
```

---

## Acciones disponibles

| Acción                          | Descripción                                                 |
| ------------------------------- | ----------------------------------------------------------- |
| `rename_to_uppercase`           | Convierte el nombre de los archivos a mayúsculas            |
| `remove_middle_name_pdf`        | Elimina el segundo nombre en archivos PDF                   |
| `remove_middle_name_docx`       | Elimina el segundo nombre en archivos DOCX                  |
| `rename_pdf_by_content`         | Renombra PDF usando información encontrada en el contenido  |
| `rename_docx_by_content`        | Renombra DOCX usando información encontrada en el contenido |
| `rename_pdf_by_fullname_blocks` | Extrae nombre completo desde bloques de texto en PDF        |
| `rename_suffix_from_project`    | Modifica o agrega sufijos al nombre del archivo             |

---

## Ejemplos

Convertir nombres a mayúsculas:

```
python renamer.py rename_to_uppercase C:/archivos
```

Eliminar segundo nombre en PDFs:

```
python renamer.py remove_middle_name_pdf C:/archivos
```

Renombrar archivos según contenido:

```
python renamer.py rename_pdf_by_content C:/archivos
```

---

## Estructura del proyecto

```
file-renamer
│
├── renamer.py
├── requirements.txt
├── README.md
│
└── src
```

---

## Autor

Cristian Pinto


## License

This project is licensed under the MIT License.