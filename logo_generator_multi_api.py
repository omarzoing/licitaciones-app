"""
Generador de logos PNG usando múltiples APIs de IA
Soporta: DALL-E 3, Stable Diffusion, y Google Imagen
"""

import os
import requests
from PIL import Image
from io import BytesIO
import base64
import time

class LogoGeneratorMultiAPI:
    """
    Generador de logos que soporta múltiples servicios de IA
    """
    
    def __init__(self, openai_key=None, hf_token=None, google_key=None):
        """
        Inicializa con las API keys disponibles
        
        Args:
            openai_key: API Key de OpenAI (para DALL-E 3)
            hf_token: Token de Hugging Face (para Stable Diffusion)
            google_key: API Key de Google (para Imagen/Gemini)
        """
        self.openai_key = openai_key
        self.hf_token = hf_token
        self.google_key = google_key
    
    def crear_prompt_optimizado(self, nombre_empresa, estilo="professional"):
        """Crea un prompt optimizado para cualquier generador de imágenes"""
        
        estilos_map = {
            "minimalist": "minimalist, clean geometric shapes, simple",
            "traditional": "traditional, elegant, classic corporate",
            "modern": "modern, contemporary, sleek",
            "geometric": "geometric, angular, structural",
            "professional": "professional, corporate, business"
        }
        
        estilo_desc = estilos_map.get(estilo, estilos_map["professional"])
        
        prompt = f"""Professional construction company logo for "{nombre_empresa}". 
{estilo_desc} design. Features: solid colors (navy blue, dark gray, orange), 
geometric shapes (hexagon, triangle, square), architectural elements, 
clean sans-serif typography, white background, vector style, 
corporate branding, high quality, centered composition, 
suitable for letterhead and business cards. 
Construction industry aesthetic. Simple and memorable."""
        
        return prompt
    
    def generar_con_dalle3(self, nombre_empresa, estilo="professional"):
        """
        Genera logo usando DALL-E 3 de OpenAI
        
        Costo: ~$0.04 por imagen (1024x1024)
        Calidad: ⭐⭐⭐⭐⭐ (Excelente)
        Velocidad: ~10-20 segundos
        
        Requiere: pip install openai
        """
        
        if not self.openai_key:
            print("⚠️ No se proporcionó OpenAI API key")
            return None
        
        try:
            from openai import OpenAI
            
            client = OpenAI(api_key=self.openai_key)
            prompt = self.crear_prompt_optimizado(nombre_empresa, estilo)
            
            print(f"🎨 Generando con DALL-E 3: {nombre_empresa}...")
            
            response = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                quality="standard",  # o "hd" para mejor calidad (+$0.04)
                n=1
            )
            
            # Descargar la imagen
            image_url = response.data[0].url
            img_response = requests.get(image_url, timeout=30)
            img = Image.open(BytesIO(img_response.content))
            
            print(f"✅ Logo generado con DALL-E 3: {img.size}")
            return img
            
        except Exception as e:
            print(f"❌ Error con DALL-E 3: {e}")
            return None
    
    def generar_con_stable_diffusion(self, nombre_empresa, estilo="professional"):
        """
        Genera logo usando Stable Diffusion XL en Hugging Face
        
        Costo: GRATIS (con límites)
        Calidad: ⭐⭐⭐⭐ (Muy buena)
        Velocidad: ~15-30 segundos
        Límite: ~100-200 requests/día gratis
        
        Obtén token gratis en: https://huggingface.co/settings/tokens
        """
        
        if not self.hf_token:
            print("⚠️ No se proporcionó Hugging Face token")
            return None
        
        try:
            # Nueva API de Hugging Face (actualizada 2024) - Usando FLUX.1-schnell
            # Es más rápido y de mejor calidad que SDXL
            API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell"
            
            headers = {
                "Authorization": f"Bearer {self.hf_token}",
                "Content-Type": "application/json"
            }
            
            prompt = self.crear_prompt_optimizado(nombre_empresa, estilo)
            
            
            payload = {
                "inputs": prompt,
                "parameters": {
                    "num_inference_steps": 4,
                    "guidance_scale": 0.0
                }
            }
            
            print(f"🎨 Generando con Stable Diffusion: {nombre_empresa}...")
            
            response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
            
            if response.status_code == 200:
                img = Image.open(BytesIO(response.content))
                print(f"✅ Logo generado con Stable Diffusion: {img.size}")
                return img
            elif response.status_code == 503:
                print("⏳ Modelo cargándose... Espera 20 segundos y reintenta")
                time.sleep(20)
                # Reintentar una vez
                response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
                if response.status_code == 200:
                    img = Image.open(BytesIO(response.content))
                    return img
            
            print(f"❌ Error Stable Diffusion: {response.status_code}")
            print(f"   Respuesta: {response.text[:200]}")
            return None
            
        except Exception as e:
            print(f"❌ Error con Stable Diffusion: {e}")
            return None
    
    def generar_con_replicate(self, nombre_empresa, estilo="professional"):
        """
        Genera logo usando Replicate (SDXL o Flux)
        
        Costo: Créditos gratis limitados, luego ~$0.005-0.01/imagen
        Calidad: ⭐⭐⭐⭐⭐ (Excelente)
        Velocidad: ~5-15 segundos
        
        Requiere: pip install replicate
        Obtén API token en: https://replicate.com/account/api-tokens
        """
        
        try:
            import replicate
            
            if not os.getenv("REPLICATE_API_TOKEN"):
                print("⚠️ No se encontró REPLICATE_API_TOKEN")
                return None
            
            prompt = self.crear_prompt_optimizado(nombre_empresa, estilo)
            
            print(f"🎨 Generando con Replicate (SDXL): {nombre_empresa}...")
            
            output = replicate.run(
                "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
                input={
                    "prompt": prompt,
                    "negative_prompt": "text, words, watermark, low quality",
                    "width": 1024,
                    "height": 1024,
                    "num_outputs": 1,
                    "scheduler": "K_EULER",
                    "num_inference_steps": 50,
                    "guidance_scale": 7.5
                }
            )
            
            # Descargar imagen
            if output and len(output) > 0:
                img_url = output[0]
                img_response = requests.get(img_url, timeout=30)
                img = Image.open(BytesIO(img_response.content))
                print(f"✅ Logo generado con Replicate: {img.size}")
                return img
            
            return None
            
        except Exception as e:
            print(f"❌ Error con Replicate: {e}")
            return None
    
    def generar_logo_auto(self, nombre_empresa, estilo="professional", preferencia=None):
        """
        Genera logo intentando múltiples servicios automáticamente
        
        Args:
            nombre_empresa: Nombre de la constructora
            estilo: Estilo del logo (minimalist, traditional, modern, etc.)
            preferencia: Lista de servicios preferidos ['dalle', 'sd', 'replicate']
        
        Returns:
            PIL.Image o None
        """
        
        # Orden de preferencia por defecto (basado en calidad/precio)
        if not preferencia:
            servicios = []
            
            # Si hay Hugging Face token (GRATIS), intentar primero
            if self.hf_token:
                servicios.append('sd')
            
            # Si hay Replicate (casi gratis)
            if os.getenv("REPLICATE_API_TOKEN"):
                servicios.append('replicate')
            
            # DALL-E al final (de pago)
            if self.openai_key:
                servicios.append('dalle')
        else:
            servicios = preferencia
        
        print(f"\n🔄 Intentando generar logo con servicios disponibles: {servicios}")
        print(f"   Empresa: {nombre_empresa}")
        print(f"   Estilo: {estilo}\n")
        
        for servicio in servicios:
            if servicio == 'dalle':
                img = self.generar_con_dalle3(nombre_empresa, estilo)
                if img:
                    return img
            
            elif servicio == 'sd':
                img = self.generar_con_stable_diffusion(nombre_empresa, estilo)
                if img:
                    return img
            
            elif servicio == 'replicate':
                img = self.generar_con_replicate(nombre_empresa, estilo)
                if img:
                    return img
            
            # Pequeña pausa entre intentos
            time.sleep(1)
        
        print("❌ No se pudo generar el logo con ningún servicio")
        return None


# ============== FUNCIÓN SIMPLIFICADA PARA APP.PY ==============

def generar_logo_ia_simple(nombre_empresa, estilo="professional"):
    """
    Función simplificada que detecta automáticamente qué servicios están disponibles
    y genera el logo con el mejor servicio posible
    
    Uso en app.py:
        from logo_generator_multi_api import generar_logo_ia_simple
        logo = generar_logo_ia_simple("Constructora Atlas", "minimalist")
    
    Variables de entorno necesarias (al menos una):
        - OPENAI_API_KEY (para DALL-E 3)
        - HUGGINGFACE_TOKEN (para Stable Diffusion - GRATIS)
        - REPLICATE_API_TOKEN (para Replicate)
    """
    
    openai_key = os.getenv("OPENAI_API_KEY")
    hf_token = os.getenv("HUGGINGFACE_TOKEN")
    
    generator = LogoGeneratorMultiAPI(
        openai_key=openai_key,
        hf_token=hf_token
    )
    
    return generator.generar_logo_auto(nombre_empresa, estilo)


# ============== TESTING ==============

if __name__ == "__main__":
    print("🚀 GENERADOR DE LOGOS CON IA - MULTI API")
    print("=" * 70)
    
    # Verificar qué servicios están disponibles
    openai_key = os.getenv("OPENAI_API_KEY")
    hf_token = os.getenv("HUGGINGFACE_TOKEN")
    replicate_token = os.getenv("REPLICATE_API_TOKEN")
    
    print("\n📋 API Keys detectadas:")
    print(f"   OpenAI (DALL-E 3):      {'✅ Disponible' if openai_key else '❌ No configurada'}")
    print(f"   Hugging Face (SD):      {'✅ Disponible' if hf_token else '❌ No configurada'}")
    print(f"   Replicate:              {'✅ Disponible' if replicate_token else '❌ No configurada'}")
    
    if not any([openai_key, hf_token, replicate_token]):
        print("\n⚠️ ADVERTENCIA: No hay API keys configuradas")
        print("\n📝 Para configurar:")
        print("   1. Copia .env.example a .env")
        print("   2. Añade al menos una de estas líneas:")
        print("      HUGGINGFACE_TOKEN=tu_token_aqui        # GRATIS - Recomendado")
        print("      OPENAI_API_KEY=tu_key_aqui             # De pago")
        print("      REPLICATE_API_TOKEN=tu_token_aqui      # Créditos gratis")
        print("\n🔗 Obtener tokens gratis:")
        print("   Hugging Face: https://huggingface.co/settings/tokens")
        print("   Replicate: https://replicate.com/account/api-tokens")
        exit(1)
    
    # Crear generador
    generator = LogoGeneratorMultiAPI(
        openai_key=openai_key,
        hf_token=hf_token
    )
    
    # Test: Generar un logo
    print("\n" + "=" * 70)
    print("📋 TEST: Generar logo con auto-detección de servicios")
    print("=" * 70 + "\n")
    
    logo = generator.generar_logo_auto(
        nombre_empresa="Constructora Atlas",
        estilo="minimalist"
    )
    
    if logo:
        filename = "test_logo_multi_api.png"
        logo.save(filename)
        print(f"\n✅ ¡ÉXITO! Logo guardado como '{filename}'")
        print(f"   Tamaño: {logo.size}")
        print(f"   Formato: {logo.format}")
    else:
        print("\n❌ No se pudo generar el logo")
        print("   Verifica que al menos una API key esté configurada correctamente")
    
    print("\n" + "=" * 70)
    print("✨ TEST COMPLETADO")
    print("=" * 70)
