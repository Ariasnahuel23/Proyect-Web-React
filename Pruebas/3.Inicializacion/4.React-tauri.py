import os
import subprocess
import socket

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

def find_free_port(start_port=3000, max_port=4000):
    """Finds a free port starting from `start_port`."""
    for port in range(start_port, max_port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            result = s.connect_ex(('127.0.0.1', port))
            if result != 0:  # The port is free
                return port
    return None  # If no port is available in the range

def main():
    # Preguntar por el nombre del proyecto
    print("Configuración del proyecto Tauri\n")
    project_name = input("Ingresa el nombre del proyecto: ")

    # Crear la carpeta del proyecto y navegar dentro de ella
    project_path = create_project_folder(project_name)
    os.chdir(project_path)

    # 1. Crear proyecto Tauri en la carpeta creada
    print("Creando el proyecto Tauri...")
    run_command("npm create tauri-app@latest .")

    # 2. Inicializar el proyecto con configuración predeterminada
    print("Inicializando el proyecto con npm init...")
    run_command("npm init -y")  # Inicia el proyecto con configuración predeterminada

    # 3. Ejecutar npm install para instalar las dependencias
    print("Instalando las dependencias...")
    run_command("npm install")  # Instala las dependencias del proyecto

    # 4. Detectar puerto libre y mostrarlo
    print("\nDetectando un puerto libre...")
    free_port = find_free_port()
    if free_port:
        print(f"Puerto libre encontrado: {free_port}. Puedes acceder a tu proyecto en: http://localhost:{free_port}")
    else:
        print("No se pudo encontrar un puerto libre en el rango especificado.")

    # 5. Ejecutar el entorno de desarrollo de Tauri
    print("Ejecutando Tauri para desarrollo de escritorio...")
    run_command("npm run tauri dev")  # Ejecuta el desarrollo de escritorio con Tauri

    # Confirmación final
    print("\n¡Configuración y ejecución completada! Ahora puedes trabajar con tu proyecto Tauri.")

if __name__ == "__main__":
    main()
