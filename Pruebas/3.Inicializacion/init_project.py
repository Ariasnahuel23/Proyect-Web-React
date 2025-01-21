import os
import subprocess
import json
import time

def run_command(command):
    """Ejecuta comandos del sistema y espera a que terminen"""
    process = subprocess.Popen(command, shell=True)
    process.wait()
    return process.returncode

def create_project_folder(project_name):
    """Crea la carpeta del proyecto en la ubicación actual"""
    base_path = os.path.dirname(os.path.abspath(__file__))
    project_path = os.path.join(base_path, project_name)
    
    if not os.path.exists(project_path):
        os.makedirs(project_path)
        print(f"✓ Carpeta creada: {project_path}")
    return project_path

def check_requirements():
    """Verifica que estén instalados los requisitos necesarios"""
    requirements = {
        "rust": "rustc --version",
        "bun": "bun --version"
    }
    
    for req, cmd in requirements.items():
        if subprocess.run(cmd, shell=True).returncode != 0:
            print(f"❌ Error: {req} no está instalado")
            return False
    return True

def update_package_json():
    """Actualiza los scripts en package.json"""
    try:
        with open('package.json', 'r') as f:
            package_data = json.load(f)
        
        # Actualizar scripts
        package_data['scripts'] = {
            "dev": "bun run tauri dev",
            "build": "bun run tauri build",
            "preview": "bun run vite preview",
            "lint": "eslint . --ext .ts,.tsx"
        }
        
        with open('package.json', 'w') as f:
            json.dump(package_data, f, indent=2)
    except Exception as e:
        print(f"Error actualizando package.json: {str(e)}")

def main():
    """Función principal que ejecuta la inicialización del proyecto"""
    print("🚀 Iniciando configuración del proyecto Vite + React + Tauri + TypeScript\n")
    
    # 1. Verificar requisitos
    if not check_requirements():
        return
    
    # 2. Crear proyecto
    project_name = input("📂 Nombre del proyecto: ")
    project_path = create_project_folder(project_name)
    os.chdir(project_path)
    
    # 3. Crear proyecto Tauri con template React + TypeScript
    print("\n📦 Creando proyecto con Tauri...")
    run_command("bun create tauri-app@latest . --template react-ts --package-manager bun --typescript")
    
    # 4. Instalar dependencias
    print("\n📥 Instalando dependencias...")
    dependencies = [
        "bun add react react-dom",
        "bun add -D @tauri-apps/cli",
        "bun add -D @types/react @types/react-dom",
        "bun add -D typescript",
        "bun add -D eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin"
    ]
    
    for cmd in dependencies:
        print(f"Ejecutando: {cmd}")
        run_command(cmd)
        time.sleep(1)
    
    # 5. Configurar ESLint
    print("\n🔧 Configurando ESLint...")
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
        json.dump(eslint_config, f, indent=2)
    
    # 6. Actualizar package.json
    print("\n📝 Actualizando package.json...")
    update_package_json()
    
    # 7. Iniciar el proyecto
    print("\n🚀 Iniciando el proyecto...")
    run_command("bun run tauri dev")  # Cambiado de 'bun run dev' a 'bun run tauri dev'
    
    print("\n✅ ¡Proyecto inicializado correctamente!")
    print(f"📁 Ubicación: {project_path}")
    print("💻 Comandos disponibles:")
    print("   - bun run tauri dev   : Iniciar en modo desarrollo")
    print("   - bun run tauri build : Compilar para producción")
    print("   - bun run lint        : Ejecutar ESLint")

if __name__ == "__main__":
    main()