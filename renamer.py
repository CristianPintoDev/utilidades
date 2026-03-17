import argparse

def remove_middle_name_docx(folder):
    print("Quitando segundo nombre en DOCX en:", folder)

def remove_middle_name_pdf(folder):
    print("Quitando segundo nombre en PDF en:", folder)

def rename_suffix_from_project(folder, extension_project):
    print("Renombrando PDF según contenido en:", folder)

def rename_docx_by_content(folder):
    print("Renombrando DOCX según contenido en:", folder)

def rename_pdf_by_content(folder):
    print("Renombrando PDF según contenido en:", folder)

def rename_pdf_by_fullname_blocks(folder):
    print("Renombrando PDF con nombre completo segun contenido en:", folder)

def rename_to_uppercase(folder):
    print("Renombrando a mayusculas en:", folder)

def main():
    parser = argparse.ArgumentParser(
        description="Herramienta para renombrar archivos automáticamente"
    )

    parser.add_argument(
        "accion",
        choices=[
            "remove_middle_name_docx",
            "remove_middle_name_pdf",
            "rename_suffix_from_project",
            "rename_docx_by_content",
            "rename_pdf_by_content",
            "rename_pdf_by_fullname_blocks",
            "rename_to_uppercase"
        ],
        help="Tipo de renombrado a realizar"
    )

    parser.add_argument(
        "carpeta",
        help="Carpeta donde están los archivos"
    )
    parser.add_argument(
        "--extension_project",
        help="Extensión que se agregará al archivo"
    )

    args = parser.parse_args()

    if args.accion == "remove_middle_name_docx":
        remove_middle_name_docx(args.carpeta)

    elif args.accion == "remove_middle_name_pdf-name-pdf":
        remove_middle_name_pdf(args.carpeta)

    elif args.accion == "rename_suffix_from_project":

        if not args.extension_project:
            print("Debes indicar --extension-project")
            return

        rename_suffix_from_project(args.carpeta, args.extension_project)
    
    elif args.accion == "rename_docx_by_content":
        rename_docx_by_content(args.carpeta)
    
    elif args.accion == "rename_pdf_by_content":
        rename_pdf_by_content(args.carpeta)
    
    elif args.accion == "rename_pdf_by_fullname_blocks":
        rename_pdf_by_fullname_blocks(args.carpeta)

    elif args.accion == "rename_to_uppercase":
        rename_to_uppercase(args.carpeta)


if __name__ == "__main__":
    main()