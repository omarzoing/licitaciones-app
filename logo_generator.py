"""
Generador de logos profesionales usando Google Gemini AI
"""

import os
import google.generativeai as genai
from PIL import Image
import requests
from io import BytesIO
import base64
import time

class LogoGenerator:
    """Genera logos profesionales de constructoras usando Gemini"""
    
    def __init__(self, api_key):
        """Inicializa el generador con la API key de Google"""
        genai.configure(api_key=api_key)
        # Usar gemini-2.5-flash (modelo estable con mejor cuota gratuita)
        self.model = genai.GenerativeModel('gemini-2.5-flash')
    
    def generar_prompt_logo(self, nombre_empresa, estilo_analizado):
        """
        Genera un prompt profesional para crear logos de constructoras
        
        Args:
            nombre_empresa: Nombre de la constructora
            estilo_analizado: Análisis de tendencias de logos (opcional)
        """
        
        prompt = f"""Crea un diseño profesional de logotipo para una constructora mexicana llamada "{nombre_empresa}".

REQUISITOS DEL DISEÑO:
- Estilo profesional y corporativo
- Colores sólidos y elegantes (evita degradados excesivos)
- Debe transmitir confianza, solidez y experiencia
- Puede incluir elementos arquitectónicos sutiles (edificios, estructuras, líneas geométricas)
- Tipografía clara y legible
- Diseño limpio que funcione en papelería

INSPIRACIÓN:
Analiza los estilos comunes en logos de constructoras exitosas:
- Uso de formas geométricas (triángulos, cuadrados, hexágonos)
- Colores corporativos: azul oscuro, gris, naranja, verde, negro
- Elementos: vigas, edificios estilizados, flechas ascendentes
- Balance entre modernidad y tradición

ESPECIFICACIONES TÉCNICAS:
- Formato vectorial mentalizado
- Fondo transparente o blanco
- Proporciones adecuadas para uso horizontal
- Escalable sin perder calidad

Describe el diseño del logo de manera detallada y profesional."""

        return prompt
    
    def analizar_tendencias_constructoras(self):
        """
        Usa Gemini para analizar tendencias de logos de constructoras
        """
        prompt = """Analiza las tendencias actuales en diseño de logos para empresas constructoras profesionales en México.

Incluye:
1. Paletas de colores más utilizadas
2. Elementos gráficos comunes
3. Estilos tipográficos
4. Formas geométricas frecuentes
5. Conceptos visuales que transmiten confianza y profesionalismo

Dame un análisis conciso de 200 palabras máximo."""

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Error al analizar tendencias: {e}")
            return "Análisis de tendencias no disponible"
    
    def generar_descripcion_logo(self, nombre_empresa):
        """
        Genera una descripción detallada del logo usando Gemini
        """
        # Primero analizamos tendencias
        tendencias = self.analizar_tendencias_constructoras()
        
        # Generamos el prompt con las tendencias
        prompt = self.generar_prompt_logo(nombre_empresa, tendencias)
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Error al generar descripción de logo: {e}")
            return None
    
    def generar_logo_texto_arte(self, nombre_empresa):
        """
        Genera una representación en texto ASCII art del logo
        (Gemini Pro no genera imágenes directamente, necesitaríamos Imagen API)
        """
        prompt = f"""Crea un diseño conceptual en texto para el logo de "{nombre_empresa}".

Describe:
1. FORMA PRINCIPAL: Qué forma geométrica o símbolo usar
2. COLORES: Paleta de colores específica (códigos hex)
3. TIPOGRAFÍA: Estilo de letra para el nombre
4. COMPOSICIÓN: Cómo se organizan los elementos
5. SIGNIFICADO: Qué representa cada elemento del diseño

Sé muy específico y profesional."""

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Error al generar concepto de logo: {e}")
            return None
    
    def generar_multiples_conceptos(self, nombre_empresa, cantidad=5):
        """
        Genera múltiples conceptos de logos para que el usuario elija
        """
        conceptos = []
        
        for i in range(cantidad):
            print(f"Generando concepto {i+1}/{cantidad}...")
            
            # Variamos el estilo en cada iteración
            estilos = [
                "minimalista y moderno",
                "tradicional y elegante",
                "geométrico y futurista",
                "clásico corporativo",
                "contemporáneo con elementos arquitectónicos"
            ]
            
            estilo = estilos[i % len(estilos)]
            
            prompt = f"""Diseña un logo {estilo} para la constructora "{nombre_empresa}".

ESPECIFICACIONES:
- Estilo: {estilo}
- Debe ser único y memorable
- Adecuado para papelería corporativa
- Transmite profesionalismo

Describe el diseño detalladamente incluyendo:
1. Forma/símbolo principal
2. Colores (códigos hex)
3. Tipografía
4. Elementos adicionales

Sé conciso pero específico (150 palabras máximo)."""

            try:
                response = self.model.generate_content(prompt)
                conceptos.append({
                    'numero': i + 1,
                    'estilo': estilo,
                    'descripcion': response.text,
                    'nombre_empresa': nombre_empresa
                })
                
                # Pequeña pausa para no saturar la API
                time.sleep(1)
                
            except Exception as e:
                print(f"Error generando concepto {i+1}: {e}")
                continue
        
        return conceptos


# Nota: Para generar imágenes reales, necesitarías usar una API de generación de imágenes
# como DALL-E, Stable Diffusion, o Imagen de Google
# Gemini Pro (texto) + descripción detallada puede usarse para luego generar con otra API

if __name__ == "__main__":
    # Prueba del generador (necesitas API key)
    api_key = os.getenv("GOOGLE_API_KEY")
    if api_key:
        generator = LogoGenerator(api_key)
        
        print("=== ANÁLISIS DE TENDENCIAS ===")
        tendencias = generator.analizar_tendencias_constructoras()
        print(tendencias)
        print("\n" + "="*50 + "\n")
        
        print("=== GENERANDO CONCEPTOS DE LOGOS ===")
        conceptos = generator.generar_multiples_conceptos("Constructora Atlas", 3)
        
        for concepto in conceptos:
            print(f"\nCONCEPTO #{concepto['numero']} - {concepto['estilo']}")
            print("-" * 50)
            print(concepto['descripcion'])
            print()
    else:
        print("No se encontró GOOGLE_API_KEY en las variables de entorno")
