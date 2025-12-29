#!/usr/bin/env python3
"""
Script de prueba simplificado para generar un logo con IA
Carga automáticamente las variables de entorno desde .env
"""

import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Verificar que el token esté cargado
print("🔍 Verificando configuración...")
print("=" * 70)

hf_token = os.getenv("HUGGINGFACE_TOKEN")
openai_key = os.getenv("OPENAI_API_KEY")
replicate_token = os.getenv("REPLICATE_API_TOKEN")

print(f"Hugging Face: {'✅ Configurado' if hf_token else '❌ No configurado'}")
print(f"OpenAI:       {'✅ Configurado' if openai_key else '❌ No configurado'}")
print(f"Replicate:    {'✅ Configurado' if replicate_token else '❌ No configurado'}")
print("=" * 70)

if not any([hf_token, openai_key, replicate_token]):
    print("\n❌ ERROR: No hay ninguna API configurada")
    print("Por favor verifica tu archivo .env")
    exit(1)

# Importar el generador
print("\n📦 Importando generador de logos...")
from logo_generator_multi_api import LogoGeneratorMultiAPI

# Crear instancia del generador
print("🎨 Creando generador...")
generator = LogoGeneratorMultiAPI(
    openai_key=openai_key,
    hf_token=hf_token
)

# Generar logo de prueba
print("\n" + "=" * 70)
print("🎨 Generando logo de prueba con IA...")
print("Empresa: Constructora Atlas")
print("Estilo: Profesional")
print("=" * 70)
print()

logo = generator.generar_logo_auto(
    nombre_empresa="Constructora Atlas",
    estilo="professional"
)

if logo:
    filename = "test_logo_ia.png"
    logo.save(filename)
    print(f"\n{'=' * 70}")
    print(f"✅ ¡ÉXITO! Logo generado correctamente")
    print(f"{'=' * 70}")
    print(f"📁 Archivo: {filename}")
    print(f"📐 Tamaño: {logo.size}")
    print(f"🎨 Formato: {logo.format}")
    print()
    print("💡 Ahora puedes:")
    print(f"   1. Abrir '{filename}' para ver el logo")
    print(f"   2. Integrar el generador en tu app.py")
    print(f"   3. Revisar la documentación en MEJORA_LOGOS_IA.md")
    print()
else:
    print("\n❌ No se pudo generar el logo")
    print("Revisa los mensajes de error arriba")
    exit(1)
