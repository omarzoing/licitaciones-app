"""
Configuración de APIs para generación de logos
"""

import os

# ==================== CONFIGURACIÓN DE APIs ====================

# OPCIÓN 1: Google Gemini (ACTUAL - Gratuita con límites)
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', 'AIzaSyBdCVeU5bWZQG4UDWzEdr-3zCx-62Ua7cg')
USE_GEMINI = True  # Cambiar a False si prefieres DALL-E

# OPCIÓN 2: OpenAI ChatGPT/DALL-E (Requiere API key de pago)
# Para usar DALL-E:
# 1. Ve a https://platform.openai.com/api-keys
# 2. Crea una API key
# 3. Pégala aquí abajo
# 4. Cambia USE_GEMINI = False arriba
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', '')  # ← Pega tu API key aquí entre las comillas
USE_DALLE = False  # Cambiar a True para usar DALL-E

# ==================== CONFIGURACIÓN DE LOGOS ====================

# Si ambas APIs fallan, usar placeholder
USE_PLACEHOLDER_FALLBACK = True

# Calidad de logos generados
LOGO_SIZE = "1024x1024"  # Para DALL-E: "1024x1024", "512x512", "256x256"
LOGO_QUALITY = "high"     # Para generación: "high", "medium", "low"

# ==================== INSTRUCCIONES ====================
"""
CÓMO USAR TU API DE CHATGPT (DALL-E):

1. Obtén tu API key:
   - Ve a: https://platform.openai.com/api-keys
   - Crea una nueva API key
   - Copia la key

2. Configura la API key:
   OPCIÓN A - Directamente en este archivo:
   OPENAI_API_KEY = 'sk-tu-api-key-aqui'
   
   OPCIÓN B - Variable de entorno (más segura):
   export OPENAI_API_KEY='sk-tu-api-key-aqui'

3. Activa DALL-E:
   USE_GEMINI = False
   USE_DALLE = True

4. Reinicia la aplicación:
   ./run.sh

NOTA: DALL-E es de pago. Cada imagen generada consume créditos.
      Gemini es gratuito con límites mensuales.
"""

def get_api_config():
    """Retorna la configuración actual de APIs"""
    return {
        'use_gemini': USE_GEMINI,
        'use_dalle': USE_DALLE,
        'gemini_key': GEMINI_API_KEY,
        'openai_key': OPENAI_API_KEY,
        'fallback': USE_PLACEHOLDER_FALLBACK
    }

def is_dalle_configured():
    """Verifica si DALL-E está configurado correctamente"""
    return USE_DALLE and OPENAI_API_KEY and OPENAI_API_KEY.startswith('sk-')

def is_gemini_configured():
    """Verifica si Gemini está configurado correctamente"""
    return USE_GEMINI and GEMINI_API_KEY and len(GEMINI_API_KEY) > 20
