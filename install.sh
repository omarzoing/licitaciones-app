#!/bin/bash

# Script de instalación automática
# Generador de Hojas Membretadas para Constructoras

echo "🏗️  INSTALADOR - Generador de Hojas Membretadas"
echo "================================================"
echo ""

# Detectar sistema operativo
OS="$(uname -s)"
echo "📍 Sistema detectado: $OS"
echo ""

# Verificar Python
echo "🐍 Verificando Python..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo "✅ $PYTHON_VERSION encontrado"
else
    echo "❌ Python 3 no encontrado"
    echo "   Instala Python desde: https://www.python.org/downloads/"
    exit 1
fi
echo ""

# Verificar pip
echo "📦 Verificando pip..."
if command -v pip3 &> /dev/null; then
    PIP_VERSION=$(pip3 --version)
    echo "✅ pip encontrado"
else
    echo "❌ pip no encontrado"
    echo "   Instala pip siguiendo: https://pip.pypa.io/en/stable/installation/"
    exit 1
fi
echo ""

# Instalar dependencias del sistema según el OS
echo "🔧 Instalando dependencias del sistema..."
if [ "$OS" = "Darwin" ]; then
    # macOS
    echo "   Detectado: macOS"
    if command -v brew &> /dev/null; then
        echo "   Instalando dependencias con Homebrew..."
        brew install python3 cairo pango gdk-pixbuf libffi || {
            echo "⚠️  Advertencia: No se pudieron instalar todas las dependencias"
            echo "   Intenta manualmente: brew install python3 cairo pango gdk-pixbuf libffi"
        }
    else
        echo "⚠️  Homebrew no encontrado. Instálalo desde: https://brew.sh"
        echo "   Luego ejecuta: brew install python3 cairo pango gdk-pixbuf libffi"
    fi
elif [ "$OS" = "Linux" ]; then
    # Linux
    echo "   Detectado: Linux"
    if command -v apt-get &> /dev/null; then
        echo "   Instalando dependencias con apt-get..."
        sudo apt-get update
        sudo apt-get install -y python3 python3-pip libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info
    elif command -v yum &> /dev/null; then
        echo "   Instalando dependencias con yum..."
        sudo yum install -y python3 python3-pip cairo pango gdk-pixbuf2 libffi-devel
    else
        echo "⚠️  Gestor de paquetes no reconocido"
        echo "   Instala manualmente: cairo, pango, gdk-pixbuf, libffi"
    fi
else
    echo "⚠️  Sistema operativo no reconocido: $OS"
    echo "   Instala manualmente las dependencias de WeasyPrint"
fi
echo ""

# Instalar dependencias de Python
echo "📦 Instalando dependencias de Python..."
pip3 install -r requirements.txt || {
    echo "❌ Error instalando dependencias de Python"
    exit 1
}
echo "✅ Dependencias de Python instaladas"
echo ""

# Configurar archivo .env
echo "🔑 Configurando archivo .env..."
if [ -f ".env" ]; then
    echo "✅ Archivo .env ya existe"
else
    if [ -f ".env.example" ]; then
        cp .env.example .env
        echo "✅ Archivo .env creado desde .env.example"
    else
        cat > .env << 'EOF'
# Google Gemini API Key
GOOGLE_API_KEY=
EOF
        echo "✅ Archivo .env creado"
    fi
fi
echo ""

# Verificar API key
echo "🔐 Verificando configuración de API Key..."
if grep -q "GOOGLE_API_KEY=.\+" .env; then
    echo "✅ API Key encontrada en .env"
else
    echo "⚠️  API Key no configurada en .env"
    echo ""
    echo "   📝 ACCIÓN REQUERIDA:"
    echo "   1. Ve a: https://makersuite.google.com/app/apikey"
    echo "   2. Crea una API key de Google Gemini"
    echo "   3. Edita el archivo .env y añade tu API key:"
    echo "      GOOGLE_API_KEY=tu_api_key_aqui"
    echo ""
fi

# Ejecutar pruebas
echo "🧪 Ejecutando pruebas del sistema..."
python3 test_sistema.py
TEST_RESULT=$?
echo ""

# Resumen final
echo "================================================"
if [ $TEST_RESULT -eq 0 ]; then
    echo "✅ ¡INSTALACIÓN COMPLETADA EXITOSAMENTE!"
    echo ""
    echo "🚀 Para ejecutar la aplicación:"
    echo "   streamlit run app.py"
    echo ""
    echo "📚 Documentación:"
    echo "   - Inicio rápido: INICIO_RAPIDO.md"
    echo "   - Guía completa: GUIA_CONFIGURACION.md"
    echo ""
else
    echo "⚠️  Instalación completada con advertencias"
    echo ""
    echo "🔍 Revisa los errores arriba y:"
    echo "   1. Asegúrate de configurar tu API key en .env"
    echo "   2. Instala las dependencias faltantes"
    echo "   3. Ejecuta nuevamente: python3 test_sistema.py"
    echo ""
fi
echo "================================================"
