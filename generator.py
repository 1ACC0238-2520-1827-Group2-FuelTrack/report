import os
import re

def generate_readme_with_content(start_path, readme_filename="README.md"):
    with open(readme_filename, 'w', encoding='utf-8') as readme_file:

        # 1. Agregar la carátula primero
        add_cover_section(start_path, readme_file)

        # 2. Agregar los registros de versiones e información de colaboración
        add_versions_and_collaboration(start_path, readme_file)

        # 3. Escribir la tabla de contenidos (sin indentación innecesaria y sin formato de código)
        readme_file.write("## Table of Contents\n\n")
        toc = generate_table_of_contents(start_path)
        readme_file.write(toc)
        
        # 4. Espacio entre la tabla de contenidos y el contenido real
        readme_file.write("\n---\n\n")
        
        # 5. Agregar el contenido de los archivos `.md` respetando la jerarquía
        add_content_to_readme(start_path, readme_file)

def add_cover_section(start_path, readme_file):
    """
    Agrega el archivo 'a.1.cover.md' como la carátula del informe.
    """
    preliminary_dir = os.path.join(start_path, "A.Preliminary")
    cover_file = os.path.join(preliminary_dir, "a.1. cover.md")
    
    if os.path.exists(cover_file):
        with open(cover_file, 'r', encoding='utf-8') as f:
            content = f.read()
            readme_file.write("# Informe de Trabajo Final\n\n")
            readme_file.write(content)
            readme_file.write("\n\n")
    else:
        print("Advertencia: El archivo 'a.1.cover.md' no existe en el directorio.")

def add_versions_and_collaboration(start_path, readme_file):
    """
    Agrega los archivos que contienen versiones y colaboración antes de la tabla de contenidos.
    """
    preliminary_dir = os.path.join(start_path, "A.Preliminary")
    version_file = os.path.join(preliminary_dir, "a.2. versions.md")
    collaboration_file = os.path.join(preliminary_dir, "a.3. Collaborations Insights.md")

    # Agregar el archivo de versiones si existe
    if os.path.exists(version_file):
        with open(version_file, 'r', encoding='utf-8') as f:
            content = f.read()
            readme_file.write(f"## Registro de Versiones del Informe\n\n")
            readme_file.write(content)
            readme_file.write("\n\n")
    
    # Agregar el archivo de colaboración si existe
    if os.path.exists(collaboration_file):
        with open(collaboration_file, 'r', encoding='utf-8') as f:
            content = f.read()
            readme_file.write(f"## Project Report Collaboration Insights\n\n")
            readme_file.write(content)
            readme_file.write("\n\n")

def generate_table_of_contents(directory, level=1):
    toc = ""
    
    # Iterar sobre los archivos y directorios en el directorio
    for item in sorted(os.listdir(directory)):
        item_path = os.path.join(directory, item)
        
        if os.path.isdir(item_path):
            # Ignorar directorios como 'A', 'B', 'C' (carpetas especiales)
            if item.lower() in ['a', 'b', 'c']:
                continue
            
            # Recursivamente generar TOC de los archivos dentro del directorio
            toc += generate_table_of_contents(item_path, level + 1)
        elif item.endswith(".md"):
            # Solo agregar archivos .md a la tabla de contenido
            section_name = item.replace(".md", "").replace("-", " ")
            toc += f"- [{section_name}](#{section_name.replace(' ', '-').lower()})\n"

    return toc


def add_content_to_readme(directory, readme_file, level=1):
    for item in sorted(os.listdir(directory)):
        item_path = os.path.join(directory, item)

        if os.path.isdir(item_path):
            # Ignorar directorios como 'A', 'B', 'C' (carpetas especiales)
            if item.lower() in ['a', 'b', 'c']:
                continue
            
            # Recursivamente agregar contenido de los archivos dentro del directorio
            add_content_to_readme(item_path, readme_file, level)
        elif item.endswith(".md"):
            # Agregar contenido de archivos .md
            section_name = item.replace(".md", "").replace("-", " ")
            readme_file.write(f"## {section_name}\n\n")
            
            # Leer el contenido del archivo .md
            with open(item_path, 'r', encoding='utf-8') as md_file:
                content = md_file.read()
                readme_file.write(content)
                readme_file.write("\n\n")


# Ruta a la carpeta principal donde se encuentra la carpeta 'structure'
project_dir = "structure"  # Cambia esta ruta al directorio correcto

# Llamar la función para generar el README.md
generate_readme_with_content(project_dir)
