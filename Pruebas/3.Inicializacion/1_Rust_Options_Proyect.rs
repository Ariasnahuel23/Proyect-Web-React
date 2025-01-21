use std::env;
use std::fs;
use std::io::{self, Write};
use std::path::PathBuf;
use std::process::Command;

fn run_command(command: &str) -> io::Result<()> {
    if cfg!(target_os = "windows") {
        Command::new("cmd")
            .args(["/C", command])
            .status()?;
    } else {
        Command::new("sh")
            .arg("-c")
            .arg(command)
            .status()?;
    }
    Ok(())
}

fn create_project_folder(project_name: &str) -> io::Result<PathBuf> {
    let current_exe = env::current_exe()?;
    let base_path = current_exe.parent().unwrap();
    let project_path = base_path.join(project_name);

    if !project_path.exists() {
        fs::create_dir_all(&project_path)?;
        println!("Carpeta '{}' creada en: {:?}", project_name, project_path);
    } else {
        println!("La carpeta '{}' ya existe en: {:?}", project_name, project_path);
    }

    Ok(project_path)
}

fn main() -> io::Result<()> {
    println!("Configuración del proyecto Tauri con Bun\n");
    
    print!("Ingresa el nombre del proyecto: ");
    io::stdout().flush()?;
    
    let mut project_name = String::new();
    io::stdin().read_line(&mut project_name)?;
    let project_name = project_name.trim();

    let project_path = create_project_folder(project_name)?;
    env::set_current_dir(&project_path)?;

    println!("Creando el proyecto Tauri...");
    run_command("bun create tauri-app@latest .")?;

    println!("Inicializando el proyecto con bun init...");
    run_command("bun init -y")?;

    println!("Instalando las dependencias con Bun...");
    run_command("bun install")?;

    println!("Creando configuración de ESLint...");
    let eslint_config = r#"{
        "root": true,
        "parser": "@typescript-eslint/parser",
        "plugins": ["@typescript-eslint"],
        "extends": [
            "eslint:recommended",
            "plugin:@typescript-eslint/recommended"
        ]
    }"#;

    fs::write(".eslintrc.json", eslint_config)?;

    println!("Agregando scripts de ESLint al package.json...");
    run_command(r#"bun run json -I -f package.json -e 'this.scripts.lint="eslint . --ext .ts,.tsx"'"#)?;
    run_command(r#"bun run json -I -f package.json -e 'this.scripts["lint:fix"]="eslint . --ext .ts,.tsx --fix"'"#)?;

    println!("Ejecutando Tauri para desarrollo de escritorio...");
    run_command("bun run tauri dev")?;

    println!("\n¡Configuración y ejecución completada! Ahora puedes trabajar con tu proyecto Tauri.");
    
    Ok(())
}