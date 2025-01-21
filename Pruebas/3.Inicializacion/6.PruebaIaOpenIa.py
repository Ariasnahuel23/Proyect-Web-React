# Corrección del script para crear el archivo Python que automatice la configuración del proyecto
project_name = "my_tauri_project"

# Escribimos el script Python corregido
script_content = f"""
import os
import subprocess

def main():
    # Pedir el nombre del archivo que almacenará el proyecto
    script_file_name = input("Ingrese el nombre para el archivo Python de configuración: ")

    # Configurar la carpeta del proyecto
    project_folder = "{project_name}"
    if not os.path.exists(project_folder):
        os.makedirs(project_folder)
    os.chdir(project_folder)

    # Ejecutar los comandos para configurar el proyecto
    try:
        print("Creando proyecto Vite con React y TypeScript...")
        subprocess.run(["npm", "create", "vite@latest", project_folder, "--template", "react-ts"], check=True)
        
        os.chdir(project_folder)
        subprocess.run(["npm", "install"], check=True)

        print("Inicializando Tauri...")
        subprocess.run(["npx", "tauri", "init", "--force"], check=True)

        print("Configuración del proyecto completada exitosamente.")

    except subprocess.CalledProcessError as error:
        print(f"Error al ejecutar el comando: {{error}}")

if __name__ == "__main__":
    main()
"""

# Guardar el script en un archivo Python
file_path = "/mnt/data/setup_tauri_project.py"
with open(file_path, "w") as script_file:
    script_file.write(script_content)

file_path
