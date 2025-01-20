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

def replace_eslint_config(project_path):
    """Replaces the content of eslint.config.js with the specified content."""
    eslint_config_path = os.path.join(project_path, "eslint.config.js")

    # Código para el nuevo archivo eslint.config.js
    eslint_content = '''import globals from "globals";
import pluginJs from "@eslint/js";
import tseslint from "typescript-eslint";
import pluginReact from "eslint-plugin-react";

export default [
  {files: ["**/*.{js,mjs,cjs,ts,jsx,tsx}"]},
  {files: ["**/*.js"], languageOptions: {sourceType: "script"}},
  {languageOptions: { globals: globals.browser }},
  pluginJs.configs.recommended,
  ...tseslint.configs.recommended,
  pluginReact.configs.flat.recommended,
];'''

    # Escribe el nuevo contenido en el archivo eslint.config.js
    with open(eslint_config_path, "w") as file:
        file.write(eslint_content)
    print(f"Archivo eslint.config.js reemplazado en: {eslint_config_path}")

def main():
    # Preguntar por el nombre del proyecto
    print("Configuración del proyecto Tauri\n")
    project_name = input("Ingresa el nombre del proyecto: ")

    # Crear la carpeta del proyecto y navegar dentro de ella
    project_path = create_project_folder(project_name)
    os.chdir(project_path)

    # 1. Crear proyecto Tauri en la carpeta creada
    run_command("npm create tauri-app@latest .")

    # 2. Seleccionar configuración
    print("Seleccionando configuración: TypeScript, npm, React, TypeScript\n")
    run_command("npm init -y")  # Inicia el proyecto con configuración predeterminada
    run_command("npm install --save-dev eslint")  # Instala ESLint
    
    # 3. Inicializar ESLint
    print("\nInicializando ESLint...")
    run_command("npm init @eslint/config@latest")  # Inicializa ESLint con configuración interactiva

    # 4. Instalar eslint-plugin-react
    print("\nInstalando eslint-plugin-react para soporte de React...")
    run_command("npm install eslint-plugin-react --save-dev")

    # 5. Instalar Prettier y su configuración para ESLint y TypeScript
    print("\nInstalando Prettier y configuraciones para ESLint y TypeScript...")
    run_command("npm install eslint prettier eslint-config-prettier eslint-plugin-prettier @typescript-eslint/eslint-plugin @typescript-eslint/parser --save-dev")

    # 6. Reemplazar el archivo eslint.config.js
    replace_eslint_config(project_path)

    # 7. Instrucciones finales
    print("\nConfiguración completa. Para continuar:")
    print("1. Ejecuta `npm install` para instalar dependencias")
    print("2. Ejecuta `npm run tauri dev` para desarrollo de escritorio")
    print("3. Ejecuta `npm run tauri android dev` para desarrollo en Android")

if __name__ == "__main__":
    main()
