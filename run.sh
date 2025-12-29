#!/bin/bash

# Script de inicio para la aplicación
# Ejecuta: ./run.sh

echo "🚀 Iniciando Generador de Hojas Membretadas..."
echo ""

# Activar entorno virtual
echo "📦 Activando entorno virtual..."
source venv/bin/activate

# Configurar rutas de Homebrew para WeasyPrint (múltiples rutas)
export DYLD_LIBRARY_PATH="/opt/homebrew/lib:/opt/homebrew/Cellar/glib/2.86.2/lib:/opt/homebrew/Cellar/pango/1.57.0_1/lib:/opt/homebrew/Cellar/cairo/1.18.4/lib:$DYLD_LIBRARY_PATH"
export PKG_CONFIG_PATH="/opt/homebrew/lib/pkgconfig:/opt/homebrew/share/pkgconfig:$PKG_CONFIG_PATH"
export LDFLAGS="-L/opt/homebrew/lib"
export CPPFLAGS="-I/opt/homebrew/include"

# Verificar que la API key esté configurada
if grep -q "GOOGLE_API_KEY=.\+" .env; then
    echo "✅ API Key configurada"
else
    echo "⚠️  API Key no encontrada en .env"
    echo "   Por favor edita el archivo .env y añade tu API key"
    echo ""
fi

# Ejecutar Streamlit
echo "🌐 Abriendo aplicación..."
echo ""
streamlit run app.py
