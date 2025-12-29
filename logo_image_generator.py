"""
Generador de imágenes de logos usando API gratuita de generación de imágenes
Compatible con múltiples servicios
"""

import os
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import base64
import random
import math

class LogoImageGenerator:
    """
    Genera imágenes de logos usando servicios de IA
    
    Opciones:
    1. Hugging Face (Stable Diffusion) - Gratuito con límites
    2. Replicate - Créditos gratuitos limitados  
    3. Generación con Pillow (fallback básico)
    """
    
    def __init__(self, api_key=None, service="huggingface"):
        self.api_key = api_key
        self.service = service
    
    def generar_logo_dalle(self, prompt, nombre_empresa):
        """
        Genera logo usando DALL-E de OpenAI (requiere API key)
        """
        if not self.api_key:
            return None
        
        try:
            import openai
            openai.api_key = self.api_key
            
            # Prompt optimizado para logos
            prompt_completo = f"""Professional construction company logo design for '{nombre_empresa}'. 
{prompt}
Corporate, clean, minimalist, vector style, white background, 
professional construction business logo, high quality."""
            
            response = openai.Image.create(
                prompt=prompt_completo,
                n=1,
                size="1024x1024"
            )
            
            image_url = response['data'][0]['url']
            response = requests.get(image_url)
            img = Image.open(BytesIO(response.content))
            
            return img
            
        except Exception as e:
            print(f"Error generando con DALL-E: {e}")
            return None
    
    def generar_logo_huggingface(self, prompt, nombre_empresa):
        """
        Genera logo usando Stable Diffusion en Hugging Face (gratuito con límites)
        """
        API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
        
        if not self.api_key:
            # Intenta sin API key (puede funcionar con límites)
            headers = {}
        else:
            headers = {"Authorization": f"Bearer {self.api_key}"}
        
        # Prompt optimizado
        prompt_completo = f"""professional construction company logo, {nombre_empresa}, 
{prompt}, corporate design, minimalist, vector style, clean, 
construction business, architectural elements, white background, 
high quality, professional branding"""
        
        payload = {
            "inputs": prompt_completo,
            "parameters": {
                "negative_prompt": "text, letters, words, watermark, signature, blurry, low quality, amateur",
                "num_inference_steps": 50
            }
        }
        
        try:
            response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
            
            if response.status_code == 200:
                img = Image.open(BytesIO(response.content))
                return img
            else:
                print(f"Error de Hugging Face: {response.status_code} - {response.text}")
                return None
                
        except Exception as e:
            print(f"Error conectando con Hugging Face: {e}")
            return None
    
    def generar_logo_placeholder(self, nombre_empresa, concepto_visual):
        """
        Genera un logo profesional usando Pillow (sin IA)
        Diseños variados inspirados en constructoras reales
        """
        try:
            # Crear imagen base
            width, height = 800, 400
            img = Image.new('RGB', (width, height), color='white')
            draw = ImageDraw.Draw(img)
            
            # Paletas de colores profesionales más amplias y modernas
            colores = [
                ('#003366', '#0066CC', '#00BCD4'),  # Azul corporativo con cyan
                ('#1B5E20', '#4CAF50', '#8BC34A'),  # Verde construcción con lima
                ('#E65100', '#FF6F00', '#FF9800'),  # Naranja industrial con ámbar
                ('#1A1A1A', '#424242', '#FFC107'),  # Gris con dorado
                ('#01579B', '#0277BD', '#4FC3F7'),  # Azul cielo degradado
                ('#BF360C', '#D84315', '#FF5722'),  # Terracota con naranja
                ('#4A148C', '#7B1FA2', '#9C27B0'),  # Púrpura corporativo
                ('#006064', '#00838F', '#00ACC1'),  # Cyan profundo
                ('#F57F17', '#FBC02D', '#FFEB3B'),  # Amarillo construcción
                ('#263238', '#455A64', '#607D8B'),  # Gris azulado moderno
                ('#1B5E20', '#388E3C', '#66BB6A'),  # Verde ecológico
                ('#B71C1C', '#C62828', '#E53935'),  # Rojo corporativo
            ]
            
            color_principal, color_acento, color_texto = random.choice(colores)
            
            # LOGOS CORPORATIVOS PROFESIONALES - Estilo minimalista y moderno
            diseños = [
                'monograma_cuadrado', 'letra_estilizada_c', 'triangulo_minimalista',
                'circulo_dividido', 'hexagono_simple', 'rectangulos_superpuestos',
                'lineas_paralelas', 'forma_l_geometrica', 'cuadrados_conectados',
                'semicirculos_espejo', 'trapecio_moderno', 'cruz_arquitectonica',
                'rombo_elegante', 'arco_minimalista', 'angulo_recto',
                'barras_verticales', 'circulo_abierto', 'triangulo_invertido',
                'forma_h_estilizada', 'cuadrado_en_cuadrado'
            ]
            diseño = random.choice(diseños)
            
            # ==================== 20 LOGOS PROFESIONALES DE CONSTRUCTORA ====================
            
            # 1. MONOGRAMA EN CUADRADO - Badge profesional
            if diseño == 'monograma_cuadrado':
                # Cuadrado exterior con esquinas redondeadas
                draw.rounded_rectangle([90, 130, 190, 230], radius=15, fill=None, outline=color_principal, width=8)
                # Letra C grande y minimalista
                draw.arc([110, 150, 170, 210], start=45, end=315, fill=color_acento, width=25)
            
            # 2. LETRA C ESTILIZADA - Tipografía corporativa
            elif diseño == 'letra_estilizada_c':
                # C grande y moderna con grosor variable
                draw.arc([85, 130, 195, 240], start=40, end=320, fill=color_principal, width=35)
                # Detalle interior
                draw.arc([105, 150, 175, 220], start=40, end=320, fill=color_acento, width=15)
            
            # 3. TRIÁNGULO MINIMALISTA - Forma geométrica pura
            elif diseño == 'triangulo_minimalista':
                # Triángulo equilátero perfecto
                draw.polygon([(140, 120), (200, 230), (80, 230)], fill=None, outline=color_principal, width=12)
                # Línea interior horizontal
                draw.line([(105, 195), (175, 195)], fill=color_acento, width=8)
            
            # 4. CÍRCULO DIVIDIDO - Diseño minimalista moderno
            elif diseño == 'circulo_dividido':
                # Círculo completo
                draw.ellipse([90, 140, 190, 240], fill=None, outline=color_principal, width=10)
                # Línea divisoria vertical
                draw.line([(140, 145), (140, 235)], fill=color_acento, width=12)
                # Semicírculos de relleno
                draw.chord([95, 145, 135, 235], start=90, end=270, fill=color_acento)
            
            # 5. HEXÁGONO SIMPLE - Geometría perfecta
            elif diseño == 'hexagono_simple':
                # Hexágono regular
                hex_pts = [(140, 125), (175, 145), (175, 205), (140, 225), (105, 205), (105, 145)]
                draw.polygon(hex_pts, fill=None, outline=color_principal, width=10)
                # Hexágono interior más pequeño
                hex_inner = [(140, 155), (160, 167), (160, 193), (140, 205), (120, 193), (120, 167)]
                draw.polygon(hex_inner, fill=color_acento)
            
            # 6. RECTÁNGULOS SUPERPUESTOS - Capas arquitectónicas
            elif diseño == 'rectangulos_superpuestos':
                # Rectángulo grande
                draw.rectangle([95, 145, 165, 225], fill=None, outline=color_principal, width=8)
                # Rectángulo mediano superpuesto
                draw.rectangle([115, 160, 185, 210], fill=color_acento, outline=color_principal, width=6)
            
            # 7. LÍNEAS PARALELAS - Diseño ultra minimalista
            elif diseño == 'lineas_paralelas':
                # Cinco líneas verticales paralelas de diferentes alturas
                alturas = [80, 50, 100, 70, 60]
                for i, h in enumerate(alturas):
                    x = 95 + i*20
                    y_start = 180 - h//2
                    draw.line([(x, y_start), (x, y_start + h)], fill=color_principal if i%2==0 else color_acento, width=10)
            
            # 8. FORMA L GEOMÉTRICA - Angulo recto estilizado
            elif diseño == 'forma_l_geometrica':
                # Forma L gruesa y moderna
                draw.rectangle([95, 130, 125, 230], fill=color_principal)  # Vertical
                draw.rectangle([95, 200, 185, 230], fill=color_acento)  # Horizontal
                # Detalle esquina
                draw.rectangle([125, 200, 155, 230], fill=color_principal)
            
            # 9. CUADRADOS CONECTADOS - Red modular
            elif diseño == 'cuadrados_conectados':
                # Tres cuadrados en diagonal
                posiciones = [(95, 145), (125, 165), (155, 185)]
                for i, (x, y) in enumerate(posiciones):
                    color = color_principal if i%2==0 else color_acento
                    draw.rectangle([x, y, x+30, y+30], fill=None, outline=color, width=8)
                # Líneas conectoras
                draw.line([(125, 160), (140, 175)], fill=color_acento, width=6)
                draw.line([(155, 180), (170, 195)], fill=color_principal, width=6)
            
            # 10. SEMICÍRCULOS ESPEJO - Simetría perfecta
            elif diseño == 'semicirculos_espejo':
                # Semicírculo superior
                draw.chord([90, 140, 190, 240], start=0, end=180, fill=None, outline=color_principal, width=10)
                # Semicírculo inferior invertido
                draw.chord([90, 140, 190, 240], start=180, end=360, fill=color_acento)
            
            # 11. TRAPECIO MODERNO - Forma geométrica dinámica
            elif diseño == 'trapecio_moderno':
                # Trapecio principal
                draw.polygon([(110, 130), (170, 130), (185, 230), (95, 230)], fill=None, outline=color_principal, width=10)
                # Línea horizontal interior
                draw.line([(120, 180), (165, 180)], fill=color_acento, width=8)
            
            # 12. CRUZ ARQUITECTÓNICA - Forma de más estilizada
            elif diseño == 'cruz_arquitectonica':
                # Barra vertical
                draw.rectangle([125, 130, 155, 230], fill=color_principal)
                # Barra horizontal
                draw.rectangle([90, 165, 190, 195], fill=color_acento)
            
            # 13. ROMBO ELEGANTE - Diamante corporativo
            elif diseño == 'rombo_elegante':
                # Rombo exterior
                draw.polygon([(140, 120), (200, 180), (140, 240), (80, 180)], fill=None, outline=color_principal, width=10)
                # Rombo interior más pequeño
                draw.polygon([(140, 150), (170, 180), (140, 210), (110, 180)], fill=color_acento)
            
            # 14. ARCO MINIMALISTA - Curva elegante
            elif diseño == 'arco_minimalista':
                # Arco principal grande
                draw.arc([80, 130, 200, 250], start=0, end=180, fill=color_principal, width=15)
                # Arco interior más pequeño
                draw.arc([100, 150, 180, 230], start=0, end=180, fill=color_acento, width=10)
            
            # 15. ÁNGULO RECTO - Esquina perfecta
            elif diseño == 'angulo_recto':
                # Línea vertical gruesa
                draw.line([(110, 130), (110, 230)], fill=color_principal, width=18)
                # Línea horizontal gruesa
                draw.line([(110, 230), (190, 230)], fill=color_acento, width=18)
                # Punto de unión reforzado
                draw.rectangle([100, 220, 120, 240], fill=color_principal)
            
            # 16. BARRAS VERTICALES - Ritmo ascendente
            elif diseño == 'barras_verticales':
                # Cinco barras de alturas crecientes
                alturas = [50, 65, 80, 95, 110]
                for i, h in enumerate(alturas):
                    x = 90 + i*20
                    y = 230 - h
                    color = color_principal if i%2==0 else color_acento
                    draw.rectangle([x, y, x+15, 230], fill=color)
            
            # 17. CÍRCULO ABIERTO - Forma incompleta moderna
            elif diseño == 'circulo_abierto':
                # Círculo casi completo con abertura
                draw.arc([85, 135, 195, 245], start=45, end=315, fill=color_principal, width=18)
                # Detalle en la abertura
                draw.ellipse([165, 205, 180, 220], fill=color_acento)
            
            # 18. TRIÁNGULO INVERTIDO - Forma v invertida
            elif diseño == 'triangulo_invertido':
                # Triángulo apuntando hacia abajo
                draw.polygon([(90, 130), (190, 130), (140, 230)], fill=None, outline=color_principal, width=12)
                # Triángulo interior relleno
                draw.polygon([(115, 155), (165, 155), (140, 205)], fill=color_acento)
            
            # 19. FORMA H ESTILIZADA - Letra corporativa minimalista
            elif diseño == 'forma_h_estilizada':
                # Pilar izquierdo
                draw.rectangle([95, 130, 120, 230], fill=color_principal)
                # Pilar derecho
                draw.rectangle([160, 130, 185, 230], fill=color_principal)
                # Puente central con degradado simulado
                draw.rectangle([120, 170, 160, 190], fill=color_acento)
            
            # 20. CUADRADO EN CUADRADO - Marcos concéntricos
            elif diseño == 'cuadrado_en_cuadrado':
                # Cuadrado exterior
                draw.rectangle([85, 135, 195, 245], fill=None, outline=color_principal, width=10)
                # Cuadrado interior rotado 45 grados simulado
                draw.rectangle([110, 160, 170, 220], fill=color_acento, outline=color_principal, width=6)
            
            # Diseño por defecto (hexágono simple)
            else:
                hex_points = [(140, 120), (180, 145), (180, 195), (140, 220), (100, 195), (100, 145)]
                draw.polygon(hex_points, fill=color_principal, outline=color_acento, width=4)
                for pt in hex_points:
                    draw.ellipse([pt[0]-6, pt[1]-6, pt[0]+6, pt[1]+6], fill=color_acento)
            
            # Añadir texto del nombre de empresa
            try:
                font_grande = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 50)
                font_pequeña = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 24)
            except:
                try:
                    font_grande = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 50)
                    font_pequeña = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 24)
                except:
                    font_grande = ImageFont.load_default()
                    font_pequeña = ImageFont.load_default()
            
            # Extraer nombre corto
            nombre_corto = nombre_empresa.replace('Constructora', '').replace('Construcciones', '')
            nombre_corto = nombre_corto.replace('Edificaciones', '').replace('Desarrollos', '')
            nombre_corto = nombre_corto.replace('Proyectos', '').replace('Grupo', '')
            nombre_corto = nombre_corto.replace('Ingeniería', '').replace('Obras', '').strip()
            
            # Si el nombre es muy largo, solo usar la primera palabra
            if len(nombre_corto) > 15:
                nombre_corto = nombre_corto.split()[0]
            
            # Posicionar texto a la derecha del logo
            text_x = 280
            
            # Nombre principal (más grande)
            draw.text((text_x, 150), nombre_corto.upper(), fill=color_principal, font=font_grande)
            
            # Subtítulo
            draw.text((text_x, 210), "CONSTRUCTORA", fill=color_acento, font=font_pequeña)
            
            return img
            
        except Exception as e:
            print(f"Error generando logo profesional: {e}")
            import traceback
            traceback.print_exc()
            return None
    
    def generar_logo(self, descripcion_concepto, nombre_empresa):
        """
        Método principal que intenta diferentes servicios
        """
        # Extraer información clave de la descripción
        prompt = f"construction company logo, {nombre_empresa}, professional, corporate"
        
        # Intentar con el servicio configurado
        if self.service == "dalle" and self.api_key:
            img = self.generar_logo_dalle(prompt, nombre_empresa)
            if img:
                return img
        
        if self.service == "huggingface":
            img = self.generar_logo_huggingface(prompt, nombre_empresa)
            if img:
                return img
        
        # Fallback: generar placeholder
        print("Usando generador placeholder...")
        return self.generar_logo_placeholder(nombre_empresa, descripcion_concepto)


if __name__ == "__main__":
    # Prueba del generador
    generator = LogoImageGenerator(service="huggingface")
    
    print("Generando logo de prueba...")
    logo = generator.generar_logo(
        "Logo moderno con elementos geométricos",
        "Constructora Atlas"
    )
    
    if logo:
        logo.save("logo_prueba.png")
        print("Logo guardado como 'logo_prueba.png'")
    else:
        print("No se pudo generar el logo")
