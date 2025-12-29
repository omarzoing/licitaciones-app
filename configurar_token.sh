#!/bin/bash

# Script para configurar fácilmente tu token de Hugging Face

echo "🎨 Configurador de Token de Hugging Face"
echo "========================================"
echo ""
echo "Instrucciones:"
echo "1. Ve a: https://huggingface.co/settings/tokens"
echo "2. Inicia sesión (puedes usar Google)"
echo "3. Haz clic en 'New token'"
echo "4. Ponle un nombre (ej: logos_constructora)"
echo "5. Selecciona tipo 'Read'"
echo "6. Copia el token que se genera"
echo ""
echo "========================================"
echo ""

# Pedir el token al usuario
read -p "Pega tu token de Hugging Face aquí: " HUGGINGFACE_TOKEN

# Verificar que no esté vacío
if [ -z "$HUGGINGFACE_TOKEN" ]; then
    echo "❌ Error: El token está vacío"
    exit 1
fi

# Verificar formato básico (debe empezar con hf_)
if [[ ! $HUGGINGFACE_TOKEN == hf_* ]]; then
    echo "⚠️ Advertencia: El token normalmente empieza con 'hf_'"
    read -p "¿Estás seguro que es correcto? (s/n): " confirm
    if [[ $confirm != "s" && $confirm != "S" ]]; then
        echo "❌ Cancelado"
        exit 1
    fi
fi

# Verificar si .env existe
if [ ! -f .env ]; then
    echo "📝 Creando archivo .env desde .env.example..."
    cp .env.example .env
fi

# Verificar si ya existe HUGGINGFACE_TOKEN en .env
if grep -q "HUGGINGFACE_TOKEN=" .env; then
    echo "⚠️ Ya existe una línea HUGGINGFACE_TOKEN en .env"
    read -p "¿Quieres reemplazarla? (s/n): " replace
    if [[ $replace == "s" || $replace == "S" ]]; then
        # Reemplazar en macOS (compatibilidad con sed de BSD)
        sed -i '' "s|HUGGINGFACE_TOKEN=.*|HUGGINGFACE_TOKEN=$HUGGINGFACE_TOKEN|" .env
        echo "✅ Token actualizado en .env"
    else
        echo "❌ Cancelado - No se modificó .env"
        exit 1
    fi
else
    # Añadir al final
    echo "" >> .env
    echo "# Token de Hugging Face para generación de logos con IA" >> .env
    echo "HUGGINGFACE_TOKEN=$HUGGINGFACE_TOKEN" >> .env
    echo "✅ Token añadido a .env"
fi

echo ""
echo "========================================"
echo "✨ ¡Listo! Token configurado correctamente"
echo "========================================"
echo ""
echo "Ahora puedes probar el generador:"
echo "  source venv/bin/activate"
echo "  python3 logo_generator_multi_api.py"
echo ""
