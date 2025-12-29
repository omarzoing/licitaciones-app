#!/bin/bash

# Script para ejecutar Streamlit con las librerías de Homebrew configuradas
# Soluciona el problema de "cannot load library 'libgobject-2.0-0'"

# Detectar arquitectura (Apple Silicon o Intel)
if [ -d "/opt/homebrew" ]; then
    # Apple Silicon
    export HOMEBREW_PREFIX="/opt/homebrew"
else
    # Intel Mac
    export HOMEBREW_PREFIX="/usr/local"
fi

# Configurar variables de entorno para las librerías
export DYLD_LIBRARY_PATH="$HOMEBREW_PREFIX/lib:${DYLD_LIBRARY_PATH}"
export LDFLAGS="-L$HOMEBREW_PREFIX/lib"
export CPPFLAGS="-I$HOMEBREW_PREFIX/include"
export PKG_CONFIG_PATH="$HOMEBREW_PREFIX/lib/pkgconfig"

echo "🔧 Configurando rutas de librerías..."
echo "   Homebrew: $HOMEBREW_PREFIX"
echo "   Librerías: $HOMEBREW_PREFIX/lib"
echo ""

# Verificar que las librerías existen
if [ ! -f "$HOMEBREW_PREFIX/lib/libgobject-2.0.dylib" ]; then
    echo "⚠️  Advertencia: No se encontró libgobject-2.0.dylib"
    echo "   Ejecuta: brew install glib"
    echo ""
fi

echo "🚀 Iniciando Streamlit..."
echo "   URL: http://localhost:8501"
echo ""
echo "   Presiona Ctrl+C para detener"
echo ""

# Activar entorno virtual y ejecutar Streamlit
source venv/bin/activate
streamlit run app.py
