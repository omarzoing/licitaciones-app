"""
Generador de logos usando Hugging Face Inference Client (2024)
Usa la librería oficial huggingface_hub
"""

import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from PIL import Image
from io import BytesIO
import time

class LogoGeneratorIA:
    """Generador de logos profesionales usando IA de Hugging Face"""
    
    def __init__(self, hf_token):
        self.client = InferenceClient(token=hf_token)
        # FLUX.1-schnell: Modelo público, rápido y de alta calidad
        self.model = "black-forest-labs/FLUX.1-schnell"
    
    def crear_prompt(self, nombre_empresa, estilo="professional"):
        """Crea un prompt optimizado para logos con paletas de colores variadas"""
        
        import random
        
        # Paletas de colores para constructoras (profesionales y atractivas)
        paletas_colores = [
            "navy blue and orange",           # Clásico industrial
            "dark green and gold",            # Elegante y premium
            "charcoal gray and red",          # Moderno y dinámico
            "royal blue and silver",          # Corporativo profesional
            "forest green and brown",         # Natural y sólido
            "burgundy and cream",             # Sofisticado
            "teal and gray",                  # Contemporáneo
            "black and amber orange",         # Industrial moderno
            "slate blue and yellow",          # Energético
            "dark brown and turquoise",       # Único y memorable
            "indigo and white",               # Limpio y confiable
            "olive green and tan",            # Terroso y estable
            "crimson and black",              # Fuerte y audaz
            "steel gray and cyan",            # Tech y moderno
            "warm brown and orange",          # Acogedor y profesional
        ]
        
        # Seleccionar paleta aleatoria
        colores = random.choice(paletas_colores)
        
        # Bases de prompts por estilo
        prompts_base = {
            "minimalist": "minimalist geometric logo",
            "traditional": "elegant classic corporate logo",
            "modern": "modern sleek contemporary logo",
            "geometric": "geometric architectural logo",
            "professional": "professional corporate logo"
        }
        
        base = prompts_base.get(estilo, "professional corporate logo")
        
        # Prompt mejorado con colores variados
        prompt = f"""{base} for construction company "{nombre_empresa}", 
simple geometric shape, {colores} color scheme, 
white background, clean design, vector style, minimalist, 
high quality, professional branding, modern aesthetic"""
        
        return prompt
    
    def generar(self, nombre_empresa, estilo="professional"):
        """
        Genera un logo PNG
        
        Returns:
            PIL.Image o None
        """
        
        prompt = self.crear_prompt(nombre_empresa, estilo)
        
        print(f"🎨 Generando logo: {nombre_empresa}")
        print(f"   Estilo: {estilo}")
        print(f"   Modelo: {self.model}")
        
        try:
            # Generar imagen con Hugging Face Inference Client
            # text_to_image devuelve directamente un PIL Image
            img = self.client.text_to_image(
                prompt,
                model=self.model
            )
            
            print(f"✅ Logo generado: {img.size}")
            return img
            
        except Exception as e:
            error_msg = str(e)
            print(f"❌ Error: {error_msg}")
            
            if "loading" in error_msg.lower():
                print("   → El modelo se está cargando...")
                print("   → Espera 20 segundos y vuelve a intentar")
            elif "token" in error_msg.lower():
                print("   → Problema con el token de Hugging Face")
            elif "rate" in error_msg.lower() or "limit" in error_msg.lower():
                print("   → Límite de API alcanzado. Espera unos minutos")
            
            return None


def generar_logo_simple(nombre_empresa, estilo="professional"):
    """
    Función simple para generar un logo
    
    Ejemplo:
        logo = generar_logo_simple("Constructora Atlas")
        logo.save("mi_logo.png")
    """
    load_dotenv()
    hf_token = os.getenv("HUGGINGFACE_TOKEN")
    
    if not hf_token:
        print("❌ No se encontró HUGGINGFACE_TOKEN en .env")
        return None
    
    generator = LogoGeneratorIA(hf_token)
    return generator.generar(nombre_empresa, estilo)


if __name__ == "__main__":
    load_dotenv()
    
    print("🚀 GENERADOR DE LOGOS CON IA")
    print("=" * 70)
    
    # Verificar token
    hf_token = os.getenv("HUGGINGFACE_TOKEN")
    if not hf_token:
        print("❌ No se encontró HUGGINGFACE_TOKEN")
        exit(1)
    
    print(f"✅ Token: {hf_token[:15]}...")
    print()
    
    # Generar logo
    try:
        logo = generar_logo_simple("Constructora Atlas", "professional")
        
        if logo:
            filename = "logo_ia_generado.png"
            logo.save(filename)
            print(f"\n{'=' * 70}")
            print(f"✅ ¡ÉXITO! Logo guardado")
            print(f"📁 Archivo: {filename}")
            print(f"📐 Tamaño: {logo.size}")
            print(f"{'=' * 70}")
            print()
            print("💡 Ahora puedes:")
            print(f"   1. Abrir '{filename}' para ver el resultado")
            print("   2. Generar más logos cambiando el nombre/estilo")
            print("   3. Integrar en tu app.py")
        else:
            print("\n❌ No se generó el logo")
            print("\n💡 Soluciones:")
            print("   1. Espera 30 segundos y ejecuta de nuevo")
            print("   2. Verifica tu token en https://huggingface.co/settings/tokens")
            print("   3. El modelo puede estar cargándose (es normal la primera vez)")
            
    except Exception as e:
        print(f"\n❌ Error fatal: {e}")
        print("\n💡 Verifica:")
        print("   1. Conexión a internet")
        print("   2. Token válido")
        print("   3. pip install huggingface-hub")
