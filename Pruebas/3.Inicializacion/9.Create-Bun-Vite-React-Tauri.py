import os
import subprocess
import json
import time

def run_command(command):
    """Ejecuta un comando del sistema."""
    process = subprocess.Popen(command, shell=True)
    process.communicate()

def create_project_folder(project_name):
    """Crea una carpeta para el proyecto."""
    base_path = os.path.dirname(os.path.abspath(__file__))
    project_path = os.path.join(base_path, project_name)

    if not os.path.exists(project_path):
        os.makedirs(project_path)
        print(f"Carpeta '{project_name}' creada en: {project_path}")
    else:
        print(f"La carpeta '{project_name}' ya existe en: {project_path}")

    return project_path

def create_eslint_config():
    """Crea la configuración de ESLint."""
    eslint_config = {
        "root": True,
        "parser": "@typescript-eslint/parser",
        "plugins": ["@typescript-eslint"],
        "extends": [
            "eslint:recommended",
            "plugin:@typescript-eslint/recommended"
        ]
    }
    
    with open(".eslintrc.json", "w") as f:
        json.dump(eslint_config, f, indent=4)

def check_rust_installation():
    """Verifica que Rust esté instalado"""
    result = subprocess.run(['rustc', '--version'], capture_output=True, text=True)
    return result.returncode == 0

def install_dependencies():
    """Instala las dependencias necesarias"""
    commands = [
        "bun install",
        "bun add @tauri-apps/api",
        "bun add -D @tauri-apps/cli",
        "cargo install tauri-cli",
    ]
    for cmd in commands:
        print(f"Ejecutando: {cmd}")
        run_command(cmd)
        time.sleep(2)

def main():
    print("Configuración del proyecto Tauri con Bun\n")
    project_name = input("Ingresa el nombre del proyecto: ")

    if not check_rust_installation():
        print("Error: Rust no está instalado. Por favor, instala Rust desde https://rustup.rs/")
        return

    project_path = create_project_folder(project_name)
    os.chdir(project_path)

    print("Instalando dependencias principales...")
    install_dependencies()

    print("Creando el proyecto Tauri...")
    run_command("bun create tauri-app@latest . --template react-ts --package-manager bun --typescript")
    time.sleep(2)

    print("Inicializando el proyecto con bun init...")
    run_command("bun init -y")

    print("Instalando las dependencias con Bun...")
    run_command("bun install")

    print("Instalando ESLint y dependencias...")
    run_command("bun add -D eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin json")

    print("Creando configuración de ESLint...")
    create_eslint_config()

    print("Agregando scripts de ESLint al package.json...")
    run_command('bun run json -I -f package.json -e \'this.scripts.lint="eslint . --ext .ts,.tsx"\'')
    run_command('bun run json -I -f package.json -e \'this.scripts["lint:fix"]="eslint . --ext .ts,.tsx --fix"\'')

    print("Ejecutando Tauri...")
    run_command("cargo tauri dev")  # Usar cargo tauri en lugar de bun tauri

    print("\n¡Configuración completada!")

if __name__ == "__main__":
    main()