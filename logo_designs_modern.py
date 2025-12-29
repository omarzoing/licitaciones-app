"""
20 Diseños de logos modernos e innovadores para constructoras
Para usar en logo_image_generator.py
"""

def generar_diseños_modernos(draw, diseño, color_principal, color_acento, color_texto):
    """Genera 20 diseños completamente diferentes y modernos"""
    
    # 1. EDIFICIO MINIMALISTA - Línea ascendente simple
    if diseño == 'edificio_minimalista':
        for i in range(5):
            altura = 280 - i*40
            ancho = 25
            x = 80 + i*30
            draw.rectangle([x, altura, x+ancho, 280], fill=color_principal if i%2==0 else color_acento)
            # Línea superior diagonal
            if i < 4:
                draw.line([(x+ancho//2, altura), (x+30+ancho//2, 280-(i+1)*40)], 
                         fill=color_texto, width=3)
    
    # 2. SKYLINE URBANO - Silueta de ciudad
    elif diseño == 'skyline_urbano':
        alturas = [200, 150, 180, 120, 160, 140, 170]
        for i, altura in enumerate(alturas):
            x = 60 + i*25
            draw.rectangle([x, altura, x+22, 280], fill=color_principal, outline=color_acento, width=2)
            # Ventanas pequeñas
            for v in range(altura+10, 270, 20):
                draw.rectangle([x+5, v, x+8, v+8], fill=color_texto)
                draw.rectangle([x+14, v, x+17, v+8], fill=color_texto)
    
    # 3. MONOGRAMA GEOMÉTRICO - Iniciales entrelazadas
    elif diseño == 'monograma_geometrico':
        # Círculo exterior
        draw.ellipse([70, 120, 210, 260], outline=color_principal, width=8)
        # Formas interiores entrelazadas
        draw.polygon([(140, 140), (180, 190), (140, 240), (100, 190)], 
                    fill=color_acento, outline=color_principal, width=3)
        draw.rectangle([120, 160, 160, 220], fill=color_principal)
        draw.ellipse([110, 170, 170, 210], fill=color_texto)
    
    # 4. FLECHA DE PROGRESO - Movimiento ascendente
    elif diseño == 'flecha_progreso':
        # Barras ascendentes
        for i in range(5):
            altura = 240 - i*30
            x = 70 + i*30
            draw.rectangle([x, altura, x+25, 280], fill=color_acento)
        # Flecha grande
        draw.polygon([(200, 140), (240, 180), (200, 220), (180, 200), (200, 180), (180, 160)],
                    fill=color_principal, outline=color_acento, width=3)
    
    # 5. CÍRCULO DINÁMICO - Anillos en movimiento
    elif diseño == 'circulo_dinamico':
        # Anillos concéntricos con efecto de movimiento
        for i in range(4):
            radio = 40 + i*20
            draw.arc([140-radio, 190-radio, 140+radio, 190+radio], 
                    start=45*i, end=225+45*i, fill=color_principal, width=12)
        # Círculo central sólido
        draw.ellipse([110, 160, 170, 220], fill=color_acento, outline=color_principal, width=4)
    
    # 6. HEXÁGONO TECH - Diseño tecnológico
    elif diseño == 'hexagono_tech':
        # Hexágono principal
        hex_pts = [(140, 120), (180, 145), (180, 195), (140, 220), (100, 195), (100, 145)]
        draw.polygon(hex_pts, fill=color_principal, outline=color_acento, width=4)
        # Nodos y conexiones
        for pt in hex_pts:
            draw.ellipse([pt[0]-8, pt[1]-8, pt[0]+8, pt[1]+8], fill=color_acento)
        # Líneas internas
        draw.line([hex_pts[0], hex_pts[3]], fill=color_texto, width=3)
        draw.line([hex_pts[1], hex_pts[4]], fill=color_texto, width=3)
        draw.line([hex_pts[2], hex_pts[5]], fill=color_texto, width=3)
    
    # 7. ONDAS ARQUITECTURA - Curvas fluidas
    elif diseño == 'ondas_arquitectura':
        # Ondas horizontales con profundidad
        for i in range(4):
            y = 140 + i*30
            # Onda con curva
            points = []
            for x in range(60, 220, 5):
                wave_y = y + 15 * (i % 2 * 2 - 1) if (x // 20) % 2 == 0 else y
                points.append((x, wave_y))
            for j in range(len(points)-1):
                draw.line([points[j], points[j+1]], fill=color_principal if i%2==0 else color_acento, width=8)
    
    # 8. PUENTE MODERNO - Estructura de puente
    elif diseño == 'puente_moderno':
        # Torres del puente
        draw.rectangle([90, 120, 110, 280], fill=color_principal)
        draw.rectangle([170, 120, 190, 280], fill=color_principal)
        # Arcos de suspensión
        draw.arc([70, 100, 130, 180], start=0, end=180, fill=color_acento, width=6)
        draw.arc([150, 100, 210, 180], start=0, end=180, fill=color_acento, width=6)
        # Cables
        for x in range(95, 180, 15):
            draw.line([(x, 120), (x, 250)], fill=color_texto, width=2)
        # Plataforma
        draw.rectangle([70, 250, 210, 265], fill=color_principal)
    
    # 9. COLUMNAS CLÁSICAS - Estilo arquitectónico
    elif diseño == 'columnas_clasicas':
        # Tres columnas con estilo dórico
        for i, x in enumerate([80, 130, 180]):
            # Capitel (parte superior)
            draw.rectangle([x-5, 130, x+25, 150], fill=color_acento)
            draw.rectangle([x-8, 145, x+28, 155], fill=color_principal)
            # Fuste (columna)
            draw.polygon([(x, 155), (x+20, 155), (x+18, 260), (x+2, 260)], 
                        fill=color_principal, outline=color_acento, width=2)
            # Estrías verticales
            for s in range(x+4, x+18, 4):
                draw.line([(s, 160), (s+1, 255)], fill=color_acento, width=1)
            # Base
            draw.rectangle([x-5, 260, x+25, 275], fill=color_principal)
    
    # 10. ORIGAMI CONSTRUCCIÓN - Formas plegadas
    elif diseño == 'origami_construccion':
        # Forma de origami en 3D
        draw.polygon([(140, 120), (100, 160), (140, 200)], fill=color_principal)
        draw.polygon([(140, 120), (180, 160), (140, 200)], fill=color_acento)
        draw.polygon([(140, 200), (100, 240), (140, 280)], fill=color_acento)
        draw.polygon([(140, 200), (180, 240), (140, 280)], fill=color_principal)
        # Detalles de plegado
        draw.line([(100, 160), (180, 160)], fill=color_texto, width=3)
        draw.line([(100, 240), (180, 240)], fill=color_texto, width=3)
        draw.line([(140, 120), (140, 280)], fill=color_texto, width=3)
    
    # 11. CUBO 3D - Perspectiva isométrica
    elif diseño == 'cubo_3d':
        # Cubo en perspectiva isométrica
        draw.polygon([(140, 140), (190, 165), (190, 225), (140, 200)], fill=color_principal)
        draw.polygon([(90, 165), (140, 140), (140, 200), (90, 225)], fill=color_acento)
        draw.polygon([(90, 225), (140, 200), (190, 225), (140, 250)], fill=color_texto)
        # Líneas de estructura interna
        draw.line([(140, 140), (140, 250)], fill='white', width=2)
        draw.line([(90, 165), (190, 165)], fill='white', width=2)
        draw.line([(90, 225), (190, 225)], fill='white', width=2)
    
    # 12. ESPIRAL CRECIMIENTO - Movimiento circular ascendente
    elif diseño == 'espiral_crecimiento':
        # Espiral desde el centro
        import math
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
        # Triángulos en diferentes tamaños y colores
        triangulos = [
            ([(140, 120), (80, 260), (200, 260)], color_principal),
            ([(140, 140), (95, 245), (185, 245)], color_acento),
            ([(140, 160), (110, 230), (170, 230)], color_texto),
        ]
        for pts, color in triangulos:
            draw.polygon(pts, fill=color, outline='white', width=3)
    
    # 14. ARCO ELEGANTE - Arquitectura de arcos
    elif diseño == 'arco_elegante':
        # Arcos múltiples conectados
        for i in range(3):
            x_offset = i * 40
            draw.arc([70+x_offset, 140, 130+x_offset, 260], 
                    start=0, end=180, fill=color_principal, width=10)
            draw.line([(70+x_offset, 260), (130+x_offset, 260)], fill=color_principal, width=10)
        # Arco central más grande
        draw.arc([90, 120, 190, 280], start=0, end=180, fill=color_acento, width=8)
    
    # 15. GRID MODULAR - Sistema de módulos
    elif diseño == 'grid_modular':
        # Grid de cuadrados con patrón
        colores_pattern = [color_principal, color_acento, color_texto]
        import random
        for i in range(5):
            for j in range(4):
                x = 75 + j*30
                y = 130 + i*30
                color = random.choice(colores_pattern)
                draw.rectangle([x, y, x+28, y+28], fill=color, outline='white', width=2)
    
    # 16. LETRA ESTILIZADA - Monograma corporativo
    elif diseño == 'letra_estilizada':
        # Letra C estilizada para Constructora
        draw.arc([80, 130, 200, 250], start=45, end=315, fill=color_principal, width=20)
        # Líneas internas decorativas
        draw.arc([95, 145, 185, 235], start=45, end=315, fill=color_acento, width=10)
        # Barras horizontales
        draw.rectangle([180, 170, 220, 180], fill=color_principal)
        draw.rectangle([180, 200, 220, 210], fill=color_acento)
    
    # 17. BLUEPRINT TÉCNICO - Estilo plano técnico
    elif diseño == 'blueprint_tecnico':
        # Líneas de diseño técnico
        draw.rectangle([70, 150, 210, 230], fill=None, outline=color_principal, width=3)
        # Líneas de cota
        for y in [150, 190, 230]:
            draw.line([(60, y), (220, y)], fill=color_acento, width=2)
        for x in [70, 140, 210]:
            draw.line([(x, 140), (x, 240)], fill=color_acento, width=2)
        # Círculos en intersecciones
        for x in [70, 140, 210]:
            for y in [150, 190, 230]:
                draw.ellipse([x-5, y-5, x+5, y+5], fill=color_principal)
        # Líneas diagonales
        draw.line([(70, 150), (210, 230)], fill=color_texto, width=2)
        draw.line([(210, 150), (70, 230)], fill=color_texto, width=2)
    
    # 18. NODO CONEXIONES - Red conectada
    elif diseño == 'nodo_conexiones':
        # Nodos principales
        nodos = [(100, 160), (180, 160), (140, 220), (100, 250), (180, 250)]
        # Líneas de conexión
        conexiones = [(0,1), (0,2), (1,2), (2,3), (2,4), (3,4)]
        for i, j in conexiones:
            draw.line([nodos[i], nodos[j]], fill=color_acento, width=4)
        # Nodos circulares
        for x, y in nodos:
            draw.ellipse([x-12, y-12, x+12, y+12], fill=color_principal, outline=color_texto, width=3)
    
    # 19. CRISTAL FACETADO - Formas de cristal
    elif diseño == 'cristal_facetado':
        # Formas de cristal superpuestas
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
        # Montañas en capas
        # Montaña trasera
        draw.polygon([(70, 250), (120, 160), (170, 250)], fill=color_acento)
        # Montaña media
        draw.polygon([(100, 250), (140, 140), (180, 250)], fill=color_principal)
        # Montaña frontal
        draw.polygon([(140, 250), (180, 170), (220, 250)], fill=color_texto)
        # Sol/luna
        draw.ellipse([85, 145, 115, 175], fill=color_principal, outline=color_acento, width=3)
        # Línea de horizonte
        draw.line([(60, 250), (220, 250)], fill=color_acento, width=4)
