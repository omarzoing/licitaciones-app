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
            
            # Tipos de diseños mucho más variados e innovadores
            diseños = [
                'edificio_minimalista', 'skyline_urbano', 'monograma_geometrico',
                'flecha_progreso', 'circulo_dinamico', 'hexagono_tech',
                'ondas_arquitectura', 'puente_moderno', 'columnas_clasicas',
                'origami_construccion', 'cubo_3d', 'espiral_crecimiento',
                'triangulos_superpuestos', 'arco_elegante', 'grid_modular',
                'letra_estilizada', 'blueprint_tecnico', 'nodo_conexiones',
                'cristal_facetado', 'mountain_landscape'
            ]
            diseño = random.choice(diseños)
            
            # ==================== 20 DISEÑOS MODERNOS E INNOVADORES ====================
            
            # 1. EDIFICIO MINIMALISTA - Línea ascendente simple
            if diseño == 'edificio_minimalista':
                for i in range(5):
                    altura = 280 - i*40
                    ancho = 25
                    x = 80 + i*30
                    draw.rectangle([x, altura, x+ancho, 280], fill=color_principal if i%2==0 else color_acento)
                    if i < 4:
                        draw.line([(x+ancho//2, altura), (x+30+ancho//2, 280-(i+1)*40)], 
                                fill=color_texto, width=3)
            
            # 2. SKYLINE URBANO - Silueta de ciudad
            elif diseño == 'skyline_urbano':
                alturas = [200, 150, 180, 120, 160, 140, 170]
                for i, altura in enumerate(alturas):
                    x = 60 + i*25
                    draw.rectangle([x, altura, x+22, 280], fill=color_principal, outline=color_acento, width=2)
                    for v in range(altura+10, 270, 20):
                        draw.rectangle([x+5, v, x+8, v+8], fill=color_texto)
                        draw.rectangle([x+14, v, x+17, v+8], fill=color_texto)
            
            # 3. MONOGRAMA GEOMÉTRICO - Iniciales entrelazadas
            elif diseño == 'monograma_geometrico':
                draw.ellipse([70, 120, 210, 260], outline=color_principal, width=8)
                draw.polygon([(140, 140), (180, 190), (140, 240), (100, 190)], 
                            fill=color_acento, outline=color_principal, width=3)
                draw.rectangle([120, 160, 160, 220], fill=color_principal)
                draw.ellipse([110, 170, 170, 210], fill=color_texto)
            
            # 4. FLECHA DE PROGRESO - Movimiento ascendente
            elif diseño == 'flecha_progreso':
                for i in range(5):
                    altura = 240 - i*30
                    x = 70 + i*30
                    draw.rectangle([x, altura, x+25, 280], fill=color_acento)
                draw.polygon([(200, 140), (240, 180), (200, 220), (180, 200), (200, 180), (180, 160)],
                            fill=color_principal, outline=color_acento, width=3)
            
            # 5. CÍRCULO DINÁMICO - Anillos en movimiento
            elif diseño == 'circulo_dinamico':
                for i in range(4):
                    radio = 40 + i*20
                    draw.arc([140-radio, 190-radio, 140+radio, 190+radio], 
                            start=45*i, end=225+45*i, fill=color_principal, width=12)
                draw.ellipse([110, 160, 170, 220], fill=color_acento, outline=color_principal, width=4)
            
            # 6. HEXÁGONO TECH - Diseño tecnológico
            elif diseño == 'hexagono_tech':
                hex_pts = [(140, 120), (180, 145), (180, 195), (140, 220), (100, 195), (100, 145)]
                draw.polygon(hex_pts, fill=color_principal, outline=color_acento, width=4)
                for pt in hex_pts:
                    draw.ellipse([pt[0]-8, pt[1]-8, pt[0]+8, pt[1]+8], fill=color_acento)
                draw.line([hex_pts[0], hex_pts[3]], fill=color_texto, width=3)
                draw.line([hex_pts[1], hex_pts[4]], fill=color_texto, width=3)
                draw.line([hex_pts[2], hex_pts[5]], fill=color_texto, width=3)
            
            # 7. ONDAS ARQUITECTURA - Curvas fluidas
            elif diseño == 'ondas_arquitectura':
                for i in range(4):
                    y = 140 + i*30
                    points = []
                    for x in range(60, 220, 5):
                        wave_y = y + 15 * (i % 2 * 2 - 1) if (x // 20) % 2 == 0 else y
                        points.append((x, wave_y))
                    for j in range(len(points)-1):
                        draw.line([points[j], points[j+1]], fill=color_principal if i%2==0 else color_acento, width=8)
            
            # 8. PUENTE MODERNO - Estructura de puente
            elif diseño == 'puente_moderno':
                draw.rectangle([90, 120, 110, 280], fill=color_principal)
                draw.rectangle([170, 120, 190, 280], fill=color_principal)
                draw.arc([70, 100, 130, 180], start=0, end=180, fill=color_acento, width=6)
                draw.arc([150, 100, 210, 180], start=0, end=180, fill=color_acento, width=6)
                for x in range(95, 180, 15):
                    draw.line([(x, 120), (x, 250)], fill=color_texto, width=2)
                draw.rectangle([70, 250, 210, 265], fill=color_principal)
            
            # 9. COLUMNAS CLÁSICAS - Estilo arquitectónico
            elif diseño == 'columnas_clasicas':
                for i, x in enumerate([80, 130, 180]):
                    draw.rectangle([x-5, 130, x+25, 150], fill=color_acento)
                    draw.rectangle([x-8, 145, x+28, 155], fill=color_principal)
                    draw.polygon([(x, 155), (x+20, 155), (x+18, 260), (x+2, 260)], 
                                fill=color_principal, outline=color_acento, width=2)
                    for s in range(x+4, x+18, 4):
                        draw.line([(s, 160), (s+1, 255)], fill=color_acento, width=1)
                    draw.rectangle([x-5, 260, x+25, 275], fill=color_principal)
            
            # 10. ORIGAMI CONSTRUCCIÓN - Formas plegadas
            elif diseño == 'origami_construccion':
                draw.polygon([(140, 120), (100, 160), (140, 200)], fill=color_principal)
                draw.polygon([(140, 120), (180, 160), (140, 200)], fill=color_acento)
                draw.polygon([(140, 200), (100, 240), (140, 280)], fill=color_acento)
                draw.polygon([(140, 200), (180, 240), (140, 280)], fill=color_principal)
                draw.line([(100, 160), (180, 160)], fill=color_texto, width=3)
                draw.line([(100, 240), (180, 240)], fill=color_texto, width=3)
                draw.line([(140, 120), (140, 280)], fill=color_texto, width=3)
            
            # 11. CUBO 3D - Perspectiva isométrica
            elif diseño == 'cubo_3d':
                draw.polygon([(140, 140), (190, 165), (190, 225), (140, 200)], fill=color_principal)
                draw.polygon([(90, 165), (140, 140), (140, 200), (90, 225)], fill=color_acento)
                draw.polygon([(90, 225), (140, 200), (190, 225), (140, 250)], fill=color_texto)
                draw.line([(140, 140), (140, 250)], fill='white', width=2)
                draw.line([(90, 165), (190, 165)], fill='white', width=2)
                draw.line([(90, 225), (190, 225)], fill='white', width=2)
            
            # 12. ESPIRAL CRECIMIENTO - Movimiento circular ascendente
            elif diseño == 'espiral_crecimiento':
                for angle in range(0, 720, 10):
                    rad = math.radians(angle)
                    r = 20 + angle/12
                    x1 = 140 + int(r * math.cos(rad))
                    y1 = 190 + int(r * math.sin(rad))
                    x2 = 140 + int((r+5) * math.cos(rad + 0.2))
                    y2 = 190 + int((r+5) * math.sin(rad + 0.2))
                    color = color_principal if angle % 60 < 30 else color_acento
                    draw.line([(x1, y1), (x2, y2)], fill=color, width=6)
            
            # 13. TRIÁNGULOS SUPERPUESTOS - Capas geométricas
            elif diseño == 'triangulos_superpuestos':
                triangulos = [
                    ([(140, 120), (80, 260), (200, 260)], color_principal),
                    ([(140, 140), (95, 245), (185, 245)], color_acento),
                    ([(140, 160), (110, 230), (170, 230)], color_texto),
                ]
                for pts, color in triangulos:
                    draw.polygon(pts, fill=color, outline='white', width=3)
            
            # 14. ARCO ELEGANTE - Arquitectura de arcos
            elif diseño == 'arco_elegante':
                for i in range(3):
                    x_offset = i * 40
                    draw.arc([70+x_offset, 140, 130+x_offset, 260], 
                            start=0, end=180, fill=color_principal, width=10)
                    draw.line([(70+x_offset, 260), (130+x_offset, 260)], fill=color_principal, width=10)
                draw.arc([90, 120, 190, 280], start=0, end=180, fill=color_acento, width=8)
            
            # 15. GRID MODULAR - Sistema de módulos
            elif diseño == 'grid_modular':
                colores_pattern = [color_principal, color_acento, color_texto]
                for i in range(5):
                    for j in range(4):
                        x = 75 + j*30
                        y = 130 + i*30
                        color = random.choice(colores_pattern)
                        draw.rectangle([x, y, x+28, y+28], fill=color, outline='white', width=2)
            
            # 16. LETRA ESTILIZADA - Monograma corporativo
            elif diseño == 'letra_estilizada':
                draw.arc([80, 130, 200, 250], start=45, end=315, fill=color_principal, width=20)
                draw.arc([95, 145, 185, 235], start=45, end=315, fill=color_acento, width=10)
                draw.rectangle([180, 170, 220, 180], fill=color_principal)
                draw.rectangle([180, 200, 220, 210], fill=color_acento)
            
            # 17. BLUEPRINT TÉCNICO - Estilo plano técnico
            elif diseño == 'blueprint_tecnico':
                draw.rectangle([70, 150, 210, 230], fill=None, outline=color_principal, width=3)
                for y in [150, 190, 230]:
                    draw.line([(60, y), (220, y)], fill=color_acento, width=2)
                for x in [70, 140, 210]:
                    draw.line([(x, 140), (x, 240)], fill=color_acento, width=2)
                for x in [70, 140, 210]:
                    for y in [150, 190, 230]:
                        draw.ellipse([x-5, y-5, x+5, y+5], fill=color_principal)
                draw.line([(70, 150), (210, 230)], fill=color_texto, width=2)
                draw.line([(210, 150), (70, 230)], fill=color_texto, width=2)
            
            # 18. NODO CONEXIONES - Red conectada
            elif diseño == 'nodo_conexiones':
                nodos = [(100, 160), (180, 160), (140, 220), (100, 250), (180, 250)]
                conexiones = [(0,1), (0,2), (1,2), (2,3), (2,4), (3,4)]
                for i, j in conexiones:
                    draw.line([nodos[i], nodos[j]], fill=color_acento, width=4)
                for x, y in nodos:
                    draw.ellipse([x-12, y-12, x+12, y+12], fill=color_principal, outline=color_texto, width=3)
            
            # 19. CRISTAL FACETADO - Formas de cristal
            elif diseño == 'cristal_facetado':
                facetas = [
                    [(140, 120), (110, 160), (140, 200)],
                    [(140, 120), (170, 160), (140, 200)],
                    [(140, 200), (110, 240), (140, 280)],
                    [(140, 200), (170, 240), (140, 280)],
                    [(110, 160), (90, 200), (110, 240)],
                    [(170, 160), (190, 200), (170, 240)]
                ]
                colores = [color_principal, color_acento, color_texto]
                for i, faceta in enumerate(facetas):
                    draw.polygon(faceta, fill=colores[i % 3], outline='white', width=2)
            
            # 20. MOUNTAIN LANDSCAPE - Paisaje de montañas
            elif diseño == 'mountain_landscape':
                draw.polygon([(70, 250), (120, 160), (170, 250)], fill=color_acento)
                draw.polygon([(100, 250), (140, 140), (180, 250)], fill=color_principal)
                draw.polygon([(140, 250), (180, 170), (220, 250)], fill=color_texto)
                draw.ellipse([85, 145, 115, 175], fill=color_principal, outline=color_acento, width=3)
                draw.line([(60, 250), (220, 250)], fill=color_acento, width=4)
            
            # Diseño por defecto (hexágono simple)
            else:
                hex_points = [(140, 120), (180, 145), (180, 195), (140, 220), (100, 195), (100, 145)]
                draw.polygon(hex_points, fill=color_principal, outline=color_acento, width=4)
                for pt in hex_pts:
                    draw.ellipse([pt[0]-6, pt[1]-6, pt[0]+6, pt[1]+6], fill=color_acento)
            
            
            # ==================================================================
                
                # Torre con estructura metálica (efecto celosía)
                for i in range(12):
                    y = 130 + i*10
                    draw.polygon([(110, y), (120, y+10), (130, y), (120, y-10)], 
                               outline=color_principal, fill=None, width=2)
                draw.rectangle([118, 130, 122, 250], fill=color_principal)
                
                # Brazo horizontal con estructura
                draw.rectangle([122, 125, 220, 135], fill=color_acento)
                for x in range(130, 220, 15):
                    draw.line([(x, 125), (x, 135)], fill=color_principal, width=2)
                
                # Cable con gancho
                draw.line([(190, 135), (190, 200)], fill=color_acento, width=4)
                draw.polygon([(185, 200), (195, 200), (190, 215)], fill=color_principal)
                
                # Contrapeso detallado
                draw.rectangle([60, 120, 118, 150], fill=color_acento, outline=color_principal, width=2)
                draw.line([(70, 130), (110, 130)], fill=color_principal, width=2)
                draw.line([(70, 140), (110, 140)], fill=color_principal, width=2)
                
                # Cabina del operador
                draw.rectangle([108, 240, 132, 255], fill=color_acento, outline=color_principal, width=2)
                draw.rectangle([112, 243, 128, 250], fill='#81D4FA')  # Ventana
            
            # DISEÑO 3: ESTRUCTURA DE VIGAS (ESTILO IPN)
            elif diseño == 'vigas':
                # Viga horizontal superior (tipo I con profundidad)
                draw.rectangle([55, 95, 225, 105], fill=color_principal)  # Ala superior
                draw.rectangle([135, 105, 145, 115], fill=color_principal)  # Alma
                draw.rectangle([55, 115, 225, 125], fill=color_acento)  # Ala inferior
                
                # Vigas verticales (perspectiva isométrica)
                # Viga izquierda
                draw.polygon([(55, 125), (70, 140), (70, 265), (55, 270)], fill=color_acento)
                draw.polygon([(70, 140), (85, 125), (85, 270), (70, 265)], fill=color_principal)
                
                # Viga derecha  
                draw.polygon([(195, 125), (210, 140), (210, 265), (195, 270)], fill=color_acento)
                draw.polygon([(210, 140), (225, 125), (225, 270), (210, 265)], fill=color_principal)
                
                # Viga horizontal inferior
                draw.rectangle([55, 255, 225, 265], fill=color_principal)  # Ala superior
                draw.rectangle([135, 265, 145, 275], fill=color_principal)  # Alma
                draw.rectangle([55, 275, 225, 285], fill=color_acento)  # Ala inferior
                
                # Remaches y detalles
                for i in range(5):
                    x = 70 + i*35
                    draw.ellipse([x-3, 108, x+3, 114], fill='#424242')
                    draw.ellipse([x-3, 268, x+3, 274], fill='#424242')
                
                # Líneas de soldadura
                draw.line([(85, 140), (195, 140)], fill=color_acento, width=2)
                draw.line([(70, 250), (210, 250)], fill=color_principal, width=2)
            
            # DISEÑO 4: CASA/RESIDENCIAL MODERNA
            elif diseño == 'casa':
                # Techo moderno (dos aguas con voladizo)
                draw.polygon([(140, 90), (60, 175), (75, 175), (140, 105), (205, 175), (220, 175)], 
                           fill=color_principal, outline=color_acento, width=3)
                # Línea de caballete
                draw.line([(140, 90), (140, 105)], fill=color_acento, width=4)
                
                # Estructura principal con profundidad
                draw.polygon([(75, 175), (205, 175), (210, 180), (70, 180)], fill=color_acento)
                draw.rectangle([75, 180, 205, 280], fill='#FFFFFF', outline=color_acento, width=3)
                
                # Puerta moderna (con vidrio)
                draw.rectangle([115, 220, 165, 280], fill=color_principal, outline=color_acento, width=2)
                draw.rectangle([120, 225, 160, 260], fill='#B3E5FC')  # Panel de vidrio
                draw.ellipse([155, 250, 160, 255], fill=color_acento)  # Manija
                
                # Ventanas grandes (estilo moderno)
                draw.rectangle([85, 190, 110, 210], fill='#E1F5FE', outline=color_principal, width=2)
                draw.line([(97, 190), (97, 210)], fill=color_principal, width=2)
                
                draw.rectangle([170, 190, 195, 210], fill='#E1F5FE', outline=color_principal, width=2)
                draw.line([(182, 190), (182, 210)], fill=color_principal, width=2)
                
                # Garaje
                draw.rectangle([75, 230, 110, 280], fill=color_acento, outline=color_principal, width=2)
                for i in range(4):
                    draw.line([(75, 240 + i*10), (110, 240 + i*10)], fill=color_principal, width=1)
                
                # Chimenea
                draw.rectangle([180, 120, 195, 175], fill=color_principal, outline=color_acento, width=2)
                draw.rectangle([177, 115, 198, 125], fill=color_acento)
            
            # DISEÑO 5: SKYLINE DE RASCACIELOS MODERNOS
            elif diseño == 'rascacielos':
                # Torre central (más alta, con ángulo)
                draw.polygon([(120, 60), (110, 280), (165, 280), (155, 60)], 
                           fill=color_principal, outline=color_acento, width=2)
                # Ventanas verticales continuas
                for col in range(3):
                    x = 122 + col * 13
                    for y in range(70, 270, 8):
                        draw.rectangle([x, y, x+8, y+6], fill='#64B5F6', outline=color_acento, width=1)
                
                # Torres laterales (diferentes alturas)
                draw.rectangle([70, 120, 105, 280], fill=color_acento, outline=color_principal, width=2)
                draw.rectangle([170, 100, 210, 280], fill=color_acento, outline=color_principal, width=2)
                
                # Ventanas para torres laterales
                for torre_x, inicio_y in [(70, 130), (170, 110)]:
                    for fila in range(6):
                        for col in range(2):
                            x = torre_x + 7 + col * 12
                            y = inicio_y + fila * 23
                            draw.rectangle([x, y, x+8, y+16], fill='#E3F2FD', outline=color_principal, width=1)
                
                # Detalles arquitectónicos (cornisas)
                draw.line([(110, 80), (165, 80)], fill=color_acento, width=4)
                draw.line([(70, 140), (105, 140)], fill=color_principal, width=3)
                draw.line([(170, 120), (210, 120)], fill=color_principal, width=3)
            
            # DISEÑO 6: CONSTRUCCIÓN EN PROCESO CON ANDAMIOS
            elif diseño == 'construccion':
                # Estructura del edificio (skeleton)
                for i in range(4):
                    y = 120 + i*40
                    draw.line([(75, y), (205, y)], fill=color_principal, width=6)
                
                # Columnas verticales
                for x in [75, 125, 175, 205]:
                    draw.line([(x, 120), (x, 280)], fill=color_principal, width=6)
                
                # Andamio frontal
                for nivel in range(4):
                    y = 140 + nivel*40
                    draw.rectangle([60, y, 70, y+30], fill=None, outline=color_acento, width=3)
                    draw.rectangle([210, y, 220, y+30], fill=None, outline=color_acento, width=3)
                    draw.line([(65, y+15), (215, y+15)], fill=color_acento, width=2)
                
                # Grúa pequeña en la parte superior
                draw.rectangle([135, 90, 145, 120], fill=color_acento)
                draw.line([(140, 90), (190, 100)], fill=color_acento, width=5)
                draw.line([(170, 105), (170, 130)], fill=color_principal, width=3)
                
                # Materiales de construcción en el suelo
                draw.rectangle([80, 265, 105, 280], fill=color_acento, outline=color_principal, width=2)
                draw.rectangle([110, 270, 135, 280], fill=color_principal, outline=color_acento, width=2)
                draw.rectangle([140, 268, 165, 280], fill=color_acento, outline=color_principal, width=2)
                
                # Casco de seguridad (icono)
                draw.arc([50, 100, 75, 125], 0, 180, fill=color_principal, width=4)
                draw.rectangle([50, 118, 75, 125], fill=color_principal)
            
            # DISEÑO 7: ABSTRACTO CORPORATIVO MODERNO
            else:
                # Forma principal - hexágono con profundidad
                hex_points = [(140, 90), (190, 120), (190, 180), (140, 210), (90, 180), (90, 120)]
                # Sombra
                shadow_points = [(p[0]+5, p[1]+5) for p in hex_points]
                draw.polygon(shadow_points, fill='#BBBBBB')
                # Hexágono principal
                draw.polygon(hex_points, fill=color_principal, outline=color_acento, width=4)
                
                # Barras dinámicas saliendo del hexágono
                draw.rectangle([140, 210, 160, 270], fill=color_acento)
                draw.polygon([(100, 230), (120, 210), (120, 270), (100, 280)], fill=color_principal)
                draw.polygon([(160, 210), (180, 230), (180, 280), (160, 270)], fill=color_principal)
                
                # Detalles interiores del hexágono
                inner_hex = [(140, 110), (175, 130), (175, 170), (140, 190), (105, 170), (105, 130)]
                draw.polygon(inner_hex, fill=color_acento)
                
                # Líneas de diseño
                draw.line([(90, 120), (70, 100)], fill=color_acento, width=5)
                draw.line([(190, 120), (210, 100)], fill=color_acento, width=5)
                draw.line([(140, 90), (140, 70)], fill=color_principal, width=5)
            
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
