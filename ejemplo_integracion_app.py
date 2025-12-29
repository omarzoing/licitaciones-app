"""
EJEMPLO DE INTEGRACIÓN EN APP.PY
Este archivo muestra cómo modificar la función generar_empresas_y_logos()
para usar el nuevo sistema de generación de logos con IA
"""

# ============================================
# PASO 1: Añadir imports al inicio de app.py
# ============================================

# ANTES (línea ~17):
# from logo_image_generator import LogoImageGenerator

# DESPUÉS (línea ~17):
from logo_generator_multi_api import generar_logo_ia_simple
from logo_image_generator import LogoImageGenerator  # Mantener como fallback


# ============================================
# PASO 2: Reemplazar función generar_empresas_y_logos
# ============================================

def generar_empresas_y_logos_mejorado(cantidad=5):
    """
    Genera empresas y sus logos usando IA
    Con fallback automático al sistema anterior si falla
    """
    import streamlit as st
    from empresa_generator import EmpresaGenerator
    from logo_generator import LogoGenerator
    from api_config import get_api_config, is_dalle_configured, is_gemini_configured
    
    with st.spinner(f"🏗️ Generando {cantidad} opciones de constructoras con logos IA..."):
        api_config = get_api_config()
        
        # Detectar qué sistema de IA está disponible
        mostrar_info_sistema_ia(st)
        
        empresas = []
        logos = []
        
        for i in range(cantidad):
            # 1. Generar datos de empresa
            empresa = EmpresaGenerator.generar_empresa_completa()
            
            # 2. Intentar generar logo con IA
            logo_img = None
            concepto = ""
            metodo_usado = "placeholder"
            
            # OPCIÓN 1: Intentar con generador multi-API (Stable Diffusion, DALL-E, etc.)
            try:
                logo_img = generar_logo_ia_simple(
                    nombre_empresa=empresa['nombre'],
                    estilo="professional"  # o "minimalist", "traditional", "modern"
                )
                
                if logo_img:
                    concepto = "✨ Logo generado con IA (Stable Diffusion o DALL-E)"
                    metodo_usado = "ia"
                    print(f"✅ Logo {i+1} generado con IA")
                else:
                    raise Exception("IA no disponible")
                    
            except Exception as e:
                print(f"⚠️ IA no disponible para logo {i+1}: {e}")
                
                # OPCIÓN 2: Fallback - DALL-E configurado manualmente
                if is_dalle_configured() and not logo_img:
                    try:
                        logo_img_gen = LogoImageGenerator(
                            api_key=api_config['openai_key'], 
                            service="dalle"
                        )
                        prompt = f"Professional minimalist logo for construction company '{empresa['nombre']}'"
                        logo_img = logo_img_gen.generar_logo_dalle(prompt, empresa['nombre'])
                        concepto = "🎨 Logo generado con DALL-E"
                        metodo_usado = "dalle"
                    except:
                        pass
                
                # OPCIÓN 3: Fallback - Sistema clásico con código
                if not logo_img:
                    print(f"🔧 Usando sistema clásico para logo {i+1}")
                    logo_img_gen = LogoImageGenerator(service="placeholder")
                    
                    if is_gemini_configured():
                        # Con descripción de Gemini
                        logo_gen = LogoGenerator(api_config['gemini_key'])
                        concepto = logo_gen.generar_logo_texto_arte(empresa['nombre'])
                    else:
                        concepto = f"Logo corporativo minimalista"
                    
                    logo_img = logo_img_gen.generar_logo_placeholder(
                        empresa['nombre'], 
                        concepto
                    )
                    metodo_usado = "codigo"
            
            # 3. Guardar resultado
            empresas.append(empresa)
            logos.append({
                'empresa': empresa,
                'concepto': concepto,
                'imagen': logo_img,
                'metodo': metodo_usado  # Para debugging
            })
            
            # 4. Mostrar progreso
            porcentaje = (i + 1) / cantidad
            st.progress(porcentaje, text=f"Logo {i + 1}/{cantidad} - {metodo_usado.upper()}")
        
        # Mostrar estadísticas
        mostrar_estadisticas_generacion(st, logos)
        
        return empresas, logos


def mostrar_info_sistema_ia(st):
    """Muestra qué sistema de IA está configurado"""
    import os
    
    # Verificar qué servicios están disponibles
    tiene_hf = bool(os.getenv("HUGGINGFACE_TOKEN"))
    tiene_openai = bool(os.getenv("OPENAI_API_KEY"))
    tiene_replicate = bool(os.getenv("REPLICATE_API_TOKEN"))
    
    if tiene_hf:
        st.success("✅ Stable Diffusion (Hugging Face) - GRATIS")
    if tiene_openai:
        st.success("✅ DALL-E 3 (OpenAI) - De pago")
    if tiene_replicate:
        st.success("✅ Replicate - Créditos gratis")
    
    if not (tiene_hf or tiene_openai or tiene_replicate):
        st.warning("⚠️ No hay APIs de IA configuradas - Usando sistema clásico")
        st.info("💡 Configura HUGGINGFACE_TOKEN en .env para logos con IA (GRATIS)")


def mostrar_estadisticas_generacion(st, logos):
    """Muestra estadísticas de cómo se generaron los logos"""
    
    # Contar métodos usados
    metodos = {}
    for logo in logos:
        metodo = logo.get('metodo', 'desconocido')
        metodos[metodo] = metodos.get(metodo, 0) + 1
    
    # Mostrar con emojis
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if metodos.get('ia', 0) > 0:
            st.metric("✨ Con IA", metodos['ia'])
    
    with col2:
        if metodos.get('dalle', 0) > 0:
            st.metric("🎨 DALL-E", metodos['dalle'])
    
    with col3:
        if metodos.get('codigo', 0) > 0:
            st.metric("🔧 Código", metodos['codigo'])


# ============================================
# PASO 3: Versión con Caché (Opcional - RECOMENDADO)
# ============================================

def generar_empresas_y_logos_con_cache(cantidad=5):
    """
    Versión mejorada con sistema de caché
    Los logos generados se guardan para no regenerarlos
    """
    import streamlit as st
    from pathlib import Path
    from PIL import Image
    import json
    
    # Crear carpeta de caché
    cache_dir = Path("logos_cache")
    cache_dir.mkdir(exist_ok=True)
    cache_json = cache_dir / "logos_metadata.json"
    
    # Cargar metadata de caché si existe
    if cache_json.exists():
        with open(cache_json, 'r') as f:
            cache_metadata = json.load(f)
    else:
        cache_metadata = {}
    
    with st.spinner(f"🏗️ Generando {cantidad} opciones..."):
        empresas = []
        logos = []
        
        for i in range(cantidad):
            empresa = EmpresaGenerator.generar_empresa_completa()
            nombre = empresa['nombre']
            
            # Crear ID único
            cache_id = f"{nombre.replace(' ', '_').lower()}_professional"
            cache_file = cache_dir / f"{cache_id}.png"
            
            # Verificar si existe en caché
            if cache_file.exists() and cache_id in cache_metadata:
                print(f"📦 Logo {i+1} desde caché: {nombre}")
                logo_img = Image.open(cache_file)
                concepto = cache_metadata[cache_id].get('concepto', 'Logo en caché')
                metodo = 'cache'
            else:
                # Generar nuevo logo con IA
                print(f"🎨 Generando nuevo logo {i+1}: {nombre}")
                logo_img = generar_logo_ia_simple(nombre, "professional")
                
                if logo_img:
                    # Guardar en caché
                    logo_img.save(cache_file)
                    concepto = "✨ Logo generado con IA"
                    cache_metadata[cache_id] = {
                        'nombre': nombre,
                        'concepto': concepto,
                        'timestamp': str(datetime.now())
                    }
                    metodo = 'ia'
                else:
                    # Fallback
                    logo_img_gen = LogoImageGenerator()
                    logo_img = logo_img_gen.generar_logo_placeholder(nombre, "")
                    concepto = "Logo clásico"
                    metodo = 'codigo'
            
            empresas.append(empresa)
            logos.append({
                'empresa': empresa,
                'concepto': concepto,
                'imagen': logo_img,
                'metodo': metodo
            })
            
            st.progress((i + 1) / cantidad)
        
        # Guardar metadata actualizada
        with open(cache_json, 'w') as f:
            json.dump(cache_metadata, f, indent=2)
        
        return empresas, logos


# ============================================
# PASO 4: Configuración de Estilos por Diseño
# ============================================

# Mapa de estilos de logo según el diseño de hoja seleccionado
ESTILOS_POR_DISEÑO = {
    'minimalista': 'minimalist',
    'tradicional': 'traditional',
    'moderno': 'modern',
    'geometrico': 'geometric',
    # Mapear tus 18 diseños nuevos:
    'azul_amarillo_bold': 'modern',
    'verde_minimalista': 'minimalist',
    'negro_naranja': 'geometric',
    'azul_rosa_isometrico': 'modern',
    'marron_simple': 'traditional',
    'negro_rojo': 'geometric',
    'blanco_naranja_clean': 'minimalist',
    'blanco_negro_simple': 'minimalist',
    'morado_minimalista': 'minimalist',
    'negro_amarillo_industrial': 'geometric',
    # ... resto de diseños
}

def generar_logo_matched_diseño(nombre_empresa, diseño_hoja):
    """Genera logo que coincide con el estilo del diseño de hoja"""
    estilo = ESTILOS_POR_DISEÑO.get(diseño_hoja, 'professional')
    return generar_logo_ia_simple(nombre_empresa, estilo)


# ============================================
# INSTRUCCIONES DE USO
# ============================================

"""
CÓMO INTEGRAR EN TU APP.PY:

1. REEMPLAZO COMPLETO (Más simple):
   - Busca la función actual generar_empresas_y_logos() en app.py
   - Reemplázala con generar_empresas_y_logos_mejorado()
   - Listo!

2. CON CACHÉ (Recomendado):
   - Usa generar_empresas_y_logos_con_cache()
   - Los logos se guardan y no se regeneran
   - Ahorra tiempo y llamadas a la API

3. INTEGRACIÓN MÍNIMA (Sin cambiar mucho):
   - Solo añade el import:
     from logo_generator_multi_api import generar_logo_ia_simple
   
   - En la línea ~129-138, reemplaza:
     logo_img = logo_img_gen.generar_logo_placeholder(...)
     
     Por:
     logo_img = generar_logo_ia_simple(empresa['nombre'], "professional")
     if not logo_img:
         # Fallback original
         logo_img = logo_img_gen.generar_logo_placeholder(...)

TESTING:

1. Asegúrate de tener configurado HUGGINGFACE_TOKEN en .env
2. Ejecuta: streamlit run app.py
3. Genera logos y verifica la calidad
4. Si hay problemas, el sistema usa automáticamente el fallback (código)

"""
