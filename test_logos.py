"""
Script para probar los nuevos logos profesionales de constructora
"""
from logo_image_generator import LogoImageGenerator
import os

# Crear generador
generator = LogoImageGenerator()

# Crear directorio para logos de prueba
os.makedirs("test_logos", exist_ok=True)

# Lista de nombres de empresas de prueba
empresas = [
    "Constructora Atlas",
    "Edificaciones del Valle",
    "Construcciones Moderna",
    "Desarrollos Urbanos GDL",
    "Proyectos Arquitectónicos",
    "Grupo Constructor Premier",
    "Ingeniería y Obras",
    "Constructora Innovación"
]

print("🏗️  Generando logos profesionales de constructora...\n")

for i, empresa in enumerate(empresas, 1):
    print(f"Generando logo {i}/8: {empresa}")
    
    # Generar logo
    logo = generator.generar_logo_placeholder(empresa, "Logo profesional de constructora")
    
    if logo:
        # Guardar
        filename = f"test_logos/logo_{i}_{empresa.replace(' ', '_')}.png"
        logo.save(filename)
        print(f"  ✅ Guardado: {filename}\n")
    else:
        print(f"  ❌ Error generando logo\n")

print("🎉 ¡Logos generados! Revisa la carpeta test_logos/")
