import os
import subprocess

def run_command(command):
    """Helper function to run a shell command."""
    process = subprocess.Popen(command, shell=True)
    process.communicate()

def create_project_folder(project_name):
    """Creates a project folder at the same level as this script."""
    # Obtener la ruta actual del archivo
    base_path = os.path.dirname(os.path.abspath(__file__))
    # Crear la ruta completa para la carpeta del proyecto
    project_path = os.path.join(base_path, project_name)

    # Crear la carpeta si no existe
    if not os.path.exists(project_path):
        os.makedirs(project_path)
        print(f"Carpeta '{project_name}' creada en: {project_path}")
    else:
        print(f"La carpeta '{project_name}' ya existe en: {project_path}")

    return project_path

def main():
    # Preguntar por el nombre del proyecto
    print("Configuración del proyecto Tauri con Bun y ESLint\n")
    project_name = input("Ingresa el nombre del proyecto: ")

    # Crear la carpeta del proyecto y navegar dentro de ella
    project_path = create_project_folder(project_name)
    os.chdir(project_path)

    # 1. Crear proyecto Tauri en la carpeta creada
    print("Creando el proyecto Tauri...")
    run_command("bun create tauri-app@latest .")

    # 2. Inicializar el proyecto con configuración predeterminada
    print("Inicializando el proyecto con bun init...")
    run_command("bun init -y")  # Inicia el proyecto con configuración predeterminada

    # 3. Ejecutar bun install para instalar las dependencias
    print("Instalando las dependencias con Bun...")
    run_command("bun install")  # Instala las dependencias del proyecto

    # 4. Instalar ESLint
    print("Instalando ESLint...")
    run_command("bun add eslint --dev")  # Instalar ESLint como dependencia de desarrollo

    # 5. Crear archivo de configuración para ESLint
    print("Creando archivo de configuración de ESLint...")
    run_command("bun run eslint --init")  # Ejecuta la configuración interactiva de ESLint

    # 6. Ejecutar el entorno de desarrollo de Tauri
    print("Ejecutando Tauri para desarrollo de escritorio...")
    run_command("bun run tauri dev")  # Ejecuta el desarrollo de escritorio con Tauri

    # Confirmación final
    print("\n¡Configuración y ejecución completada! Ahora puedes trabajar con tu proyecto Tauri y ESLint.")

if __name__ == "__main__":
    main()
