import os
import subprocess

def initialize_project():
    # Obtener la ubicación actual del script
    current_directory = os.getcwd()

    # Solicitar al usuario el nombre del proyecto
    project_name = input("¿Cómo se llamará el proyecto? ")

    # Crear la ruta completa del proyecto
    project_path = os.path.join(current_directory, project_name)

    # Verificar si la carpeta ya existe
    if os.path.exists(project_path):
        print(f"La carpeta '{project_name}' ya existe. Por favor, elige otro nombre.")
        return

    # Crear la carpeta del proyecto
    os.makedirs(project_path)
    print(f"Carpeta creada: {project_path}")

    # Cambiar al directorio del proyecto
    os.chdir(project_path)

    # Inicializar un proyecto con Vite
    print("Inicializando proyecto con Vite...")
    try:
        subprocess.run(["npm", "create", "vite@latest", "./", "--", "--template", "react-ts"], check=True)
    except FileNotFoundError:
        print("Error: No se encontró el comando 'npm'. Asegúrate de que Node.js y npm estén instalados y configurados correctamente en tu sistema.")
        return

    # Cambiar al directorio del proyecto y añadir Tauri
    print("Agregando Tauri al proyecto...")
    try:
        subprocess.run(["npm", "install"], check=True)
        subprocess.run(["npm", "install", "@tauri-apps/cli", "@tauri-apps/api"], check=True)
    except FileNotFoundError:
        print("Error: No se encontró el comando 'npm'. Asegúrate de que Node.js y npm estén instalados y configurados correctamente en tu sistema.")
        return

    # Configurar Tauri
    print("Configurando Tauri...")
    try:
        subprocess.run(["npx", "tauri", "init"], check=True)
    except FileNotFoundError:
        print("Error: No se encontró el comando 'npx'. Asegúrate de que Node.js y npm estén instalados y configurados correctamente en tu sistema.")
        return

    print(f"¡El proyecto '{project_name}' ha sido inicializado con éxito con React, Tauri y TypeScript!")

if __name__ == "__main__":
    try:
        initialize_project()
    except subprocess.CalledProcessError as e:
        print(f"Se produjo un error durante la ejecución del comando: {e}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
