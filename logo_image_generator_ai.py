"""
Generador de logos usando Google Gemini AI para crear imágenes PNG reales
Utiliza la API de Google Generative AI (Imagen 3)
"""

import os
import google.generativeai as genai
from PIL import Image
import requests
from io import BytesIO
import base64
import time

class LogoImageGeneratorAI:
    """
    Genera imágenes PNG de logos profesionales usando Google Gemini AI
    
    Ventajas:
    - Usa la misma API key que ya tienes (GOOGLE_API_KEY)
    - Gratis hasta 1,500 requests/día
    - Genera imágenes PNG reales de alta calidad
    - No requiere servicios adicionales
    """
    
    def __init__(self, api_key):
        """Inicializa el generador con la API key de Google"""
        genai.configure(api_key=api_key)
        # Usar el modelo Imagen 3 de Google
        self.model = genai.GenerativeModel('imagen-3.0-generate-001')
    
    def crear_prompt_profesional(self, nombre_empresa, descripcion_concepto=""):
        """
        Crea un prompt optimizado para generar logos profesionales de constructoras
        
        Args:
            nombre_empresa: Nombre de la constructora
            descripcion_concepto: Descripción adicional del concepto (opcional)
        
        Returns:
            Prompt optimizado para generación de logos
        """
        
        # Analizar si hay palabras clave en la descripción
        estilos_detectados = []
        if descripcion_concepto:
            concepto_lower = descripcion_concepto.lower()
            if "minimalista" in concepto_lower or "moderno" in concepto_lower:
                estilos_detectados.append("minimalist modern design")
            if "tradicional" in concepto_lower or "clásico" in concepto_lower:
                estilos_detectados.append("traditional elegant style")
            if "geométrico" in concepto_lower:
                estilos_detectados.append("geometric shapes")
            if "futurista" in concepto_lower or "contemporáneo" in concepto_lower:
                estilos_detectados.append("futuristic contemporary")
        
        estilo_str = ", ".join(estilos_detectados) if estilos_detectados else "professional corporate design"
        
        prompt = f"""Professional construction company logo for "{nombre_empresa}".

STYLE: {estilo_str}, clean, corporate

DESIGN REQUIREMENTS:
- Simple geometric shapes (triangles, hexagons, squares, circles)
- Solid professional colors (navy blue, dark green, orange, gray, black)
- Architectural elements (building silhouettes, construction lines, beams)
- Clean sans-serif typography
- White or transparent background
- Scalable vector-style design
- No text except company name "{nombre_empresa}"
- High contrast for readability
- Professional business logo aesthetic

TECHNICAL SPECS:
- Horizontal orientation
- Clean edges and shapes
- Suitable for letterhead and business cards
- Corporate professional look
- Construction industry themed

OUTPUT: A single centered logo on white background, professional quality, ready for business use."""

        return prompt
    
    def generar_logo_imagen3(self, nombre_empresa, descripcion_concepto="", timeout=120):
        """
        Genera un logo usando Google Imagen 3
        
        Args:
            nombre_empresa: Nombre de la empresa
            descripcion_concepto: Descripción del concepto de logo
            timeout: Tiempo máximo de espera en segundos
        
        Returns:
            PIL.Image: Imagen del logo generado o None si hay error
        """
        
        prompt = self.crear_prompt_profesional(nombre_empresa, descripcion_concepto)
        
        try:
            print(f"🎨 Generando logo para {nombre_empresa} con Imagen 3...")
            
            # Parámetros de generación
            generation_config = {
                "temperature": 0.4,  # Menos aleatorio, más consistente
                "top_p": 0.95,
                "top_k": 40,
                "max_output_tokens": 2048,
            }
            
            # Generar imagen
            response = self.model.generate_content(
                prompt,
                generation_config=generation_config
            )
            
            # Extraer la imagen de la respuesta
            if hasattr(response, 'candidates') and len(response.candidates) > 0:
                candidate = response.candidates[0]
                
                # Verificar si hay imagen en la respuesta
                if hasattr(candidate, 'content') and hasattr(candidate.content, 'parts'):
                    for part in candidate.content.parts:
                        # Buscar datos de imagen
                        if hasattr(part, 'inline_data'):
                            image_data = part.inline_data.data
                            # Convertir base64 a imagen PIL
                            img = Image.open(BytesIO(base64.b64decode(image_data)))
                            print(f"✅ Logo generado exitosamente: {img.size}")
                            return img
            
            print("⚠️ No se encontró imagen en la respuesta de Imagen 3")
            return None
            
        except Exception as e:
            print(f"❌ Error generando logo con Imagen 3: {e}")
            import traceback
            traceback.print_exc()
            return None
    
    def generar_logo_fallback_dalle_style(self, nombre_empresa, descripcion_concepto=""):
        """
        Método alternativo: Genera descripción con Gemini y sugiere usar DALL-E o similar
        
        Este método genera una descripción detallada que puede usarse con:
        - DALL-E 3 (OpenAI)
        - Stable Diffusion (Hugging Face, Replicate)
        - Midjourney
        """
        
        try:
            # Usar el modelo de texto para generar una descripción precisa
            text_model = genai.GenerativeModel('gemini-2.0-flash-exp')
            
            prompt = f"""Crea una descripción VISUAL detallada para un generador de imágenes AI (como DALL-E) 
que debe crear un logo profesional para la constructora "{nombre_empresa}".

La descripción debe incluir:
1. Forma geométrica principal (círculo, hexágono, triángulo, cuadrado, etc.)
2. Colores específicos (códigos hex o nombres precisos)
3. Elementos arquitectónicos concretos
4. Estilo de tipografía
5. Composición y layout

La descripción debe ser en inglés, concisa (máximo 100 palabras), y muy específica para que 
un modelo de generación de imágenes pueda crear el logo exacto.

FORMATO: Solo la descripción en inglés, sin explicaciones adicionales."""

            response = text_model.generate_content(prompt)
            descripcion_visual = response.text.strip()
            
            print(f"\n📝 Descripción generada para imagen AI:\n{descripcion_visual}\n")
            
            return descripcion_visual
            
        except Exception as e:
            print(f"Error generando descripción: {e}")
            return None
    
    def generar_multiples_logos(self, nombre_empresa, cantidad=5, delay=2):
        """
        Genera múltiples opciones de logos para que el usuario elija
        
        Args:
            nombre_empresa: Nombre de la empresa
            cantidad: Número de logos a generar
            delay: Segundos de espera entre generaciones
        
        Returns:
            Lista de imágenes PIL generadas
        """
        
        logos = []
        estilos = [
            "minimalist modern geometric",
            "traditional elegant corporate",
            "futuristic contemporary",
            "classic architectural",
            "clean simple professional"
        ]
        
        for i in range(cantidad):
            estilo = estilos[i % len(estilos)]
            descripcion = f"{estilo} design"
            
            print(f"\n🎨 Generando logo {i+1}/{cantidad} - Estilo: {estilo}")
            
            logo = self.generar_logo_imagen3(nombre_empresa, descripcion)
            
            if logo:
                logos.append({
                    'imagen': logo,
                    'numero': i + 1,
                    'estilo': estilo,
                    'nombre_empresa': nombre_empresa
                })
                print(f"✅ Logo {i+1} completado")
            else:
                print(f"⚠️ No se pudo generar logo {i+1}")
            
            # Pausa para no saturar la API
            if i < cantidad - 1:
                print(f"⏳ Esperando {delay} segundos...")
                time.sleep(delay)
        
        return logos


# ============== FUNCIÓN AUXILIAR PARA USAR EN APP.PY ==============

def generar_logo_con_ia(api_key, nombre_empresa, descripcion_concepto=""):
    """
    Función auxiliar simplificada para integrar en app.py
    
    Args:
        api_key: Google API Key
        nombre_empresa: Nombre de la constructora
        descripcion_concepto: Descripción opcional del concepto
    
    Returns:
        PIL.Image o None
    """
    try:
        generator = LogoImageGeneratorAI(api_key)
        return generator.generar_logo_imagen3(nombre_empresa, descripcion_concepto)
    except Exception as e:
        print(f"Error en generación de logo: {e}")
        return None


# ============== TESTING ==============

if __name__ == "__main__":
    # Prueba del generador
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        print("❌ ERROR: No se encontró GOOGLE_API_KEY en las variables de entorno")
        print("Por favor configura tu .env con: GOOGLE_API_KEY=tu_api_key_aqui")
        exit(1)
    
    print("🚀 INICIANDO GENERADOR DE LOGOS CON IA")
    print("=" * 60)
    
    # Test 1: Generar un solo logo
    print("\n📋 TEST 1: Generar un logo individual")
    print("-" * 60)
    
    generator = LogoImageGeneratorAI(api_key)
    
    logo = generator.generar_logo_imagen3(
        nombre_empresa="Constructora Atlas",
        descripcion_concepto="minimalist modern geometric design"
    )
    
    if logo:
        logo.save("test_logo_individual.png")
        print(f"✅ Logo guardado como 'test_logo_individual.png'")
        print(f"   Tamaño: {logo.size}")
    else:
        print("❌ No se pudo generar el logo")
    
    # Test 2: Generar múltiples logos
    print("\n📋 TEST 2: Generar múltiples logos (3 opciones)")
    print("-" * 60)
    
    logos = generator.generar_multiples_logos("Edificaciones Minerva", cantidad=3, delay=3)
    
    if logos:
        print(f"\n✅ Se generaron {len(logos)} logos exitosamente:")
        for logo_data in logos:
            filename = f"test_logo_{logo_data['numero']}_{logo_data['estilo'].replace(' ', '_')}.png"
            logo_data['imagen'].save(filename)
            print(f"   - {filename} ({logo_data['imagen'].size})")
    else:
        print("❌ No se pudieron generar logos múltiples")
    
    print("\n" + "=" * 60)
    print("✨ PRUEBAS COMPLETADAS")
