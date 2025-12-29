"""
Sistema de diseño de hojas membretadas
Genera diferentes estilos de plantillas HTML/CSS
"""

from datetime import datetime

class HojaMembretadaDesigner:
    """Genera diseños de hojas membretadas en HTML/CSS"""
    
    # 18 Estilos inspirados en diseños profesionales de construcción
    ESTILOS = [
        'azul_amarillo_bold', 'verde_minimalista', 'negro_naranja', 
        'azul_rosa_isometrico', 'marron_simple', 'negro_rojo',
        'blanco_naranja_clean', 'blanco_negro_simple', 'morado_minimalista',
        'negro_amarillo_industrial', 'barra_lateral_naranja', 'diagonal_moderno',
        'franja_superior_roja', 'geometrico_purpura', 'azul_corporativo',
        'verde_ecologico', 'gris_elegante', 'terracota_profesional'
    ]
    
    @staticmethod
    def get_css_base():
        """CSS base para todas las hojas membretadas (tamaño carta)"""
        return """
        @page {
            size: letter;
            margin: 1.2in 1in 0.75in 1in;
            @top-center {
                content: element(header);
                margin-top: 0.3in;
            }
        }
        
        body {
            margin: 0;
            padding: 0;
            font-family: 'Helvetica', 'Arial', sans-serif;
            color: #333;
            line-height: 1.6;
        }
        
        .page {
            background: white;
        }
        
        .header {
            margin-bottom: 30px;
            padding-bottom: 15px;
            border-bottom: 2px solid #ddd;
        }
        
        .header-fixed {
            position: running(header);
            display: flex;
            align-items: center;
            padding-top: 15px;
            padding-bottom: 15px;
            border-bottom: 1px solid #ddd;
            margin-bottom: 25px;
        }
        
        .logo {
            max-width: 180px;
            max-height: 90px;
            display: block;
            margin-right: 20px;
        }
        
        .empresa-header {
            font-size: 10pt;
            font-weight: bold;
            color: #333;
        }
        
        .content {
            font-size: 11pt;
            text-align: justify;
            margin-bottom: 40px;
            margin-top: 80px;
        }
        
        .content p {
            margin-bottom: 12pt;
        }
        
        .footer {
            margin-top: 40px;
            padding-top: 15px;
            border-top: 1px solid #ccc;
            font-size: 9pt;
            color: #666;
        }
        
        .firma {
            margin-top: 40px;
            text-align: center;
        }
        
        .linea-firma {
            border-top: 1px solid #333;
            width: 300px;
            margin: 0 auto;
            margin-bottom: 5px;
        }
        """
    
    @staticmethod
    def diseño_minimalista(empresa, logo_base64, contenido):
        """Diseño minimalista y limpio"""
        css = HojaMembretadaDesigner.get_css_base() + """
        .header {
            display: flex;
            align-items: center;
            padding-bottom: 20px;
            border-bottom: 2px solid #000;
        }
        
        .logo {
            margin-right: 20px;
        }
        
        .empresa-info {
            font-size: 9pt;
            color: #555;
        }
        
        .empresa-nombre {
            font-size: 14pt;
            font-weight: bold;
            color: #000;
            margin-bottom: 5px;
        }
        
        .content {
            margin-top: 40px;
        }
        
        .footer {
            margin-top: 40px;
            padding-top: 15px;
            border-top: 2px solid #000;
            font-size: 8pt;
        }
        """
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>{css}</style>
        </head>
        <body>
            <div class="header-fixed">
                <img src="data:image/png;base64,{logo_base64}" class="logo" alt="Logo">
                <div class="empresa-header">{empresa['nombre_completo']}</div>
            </div>
            
            <div class="page">
                <div class="content">
                    {HojaMembretadaDesigner._formatear_contenido(contenido)}
                </div>
                
                <div class="footer">
                    <strong>{empresa['nombre_completo']}</strong><br>
                    {empresa['direccion']['completa']}, {empresa['direccion']['ciudad']}<br>
                    Tel: {empresa['telefono']} | Email: {empresa['email']} | RFC: {empresa['rfc']}
                </div>
            </div>
        </body>
        </html>
        """
        return html
    
    @staticmethod
    def diseño_tradicional(empresa, logo_base64, contenido):
        """Diseño tradicional y elegante"""
        css = HojaMembretadaDesigner.get_css_base() + """
        .header {
            text-align: center;
            padding-bottom: 25px;
            border-bottom: 3px double #333;
        }
        
        .logo {
            margin: 0 auto 15px;
        }
        
        .empresa-nombre {
            font-size: 16pt;
            font-weight: bold;
            color: #1a1a1a;
            margin-bottom: 8px;
            letter-spacing: 1px;
        }
        
        .empresa-slogan {
            font-size: 10pt;
            color: #666;
            font-style: italic;
        }
        
        .content {
            margin-top: 35px;
            font-family: 'Georgia', 'Times New Roman', serif;
        }
        
        .footer {
            border-top: 3px double #333;
            text-align: center;
            font-size: 8pt;
        }
        """
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>{css}</style>
        </head>
        <body>
            <div class="header-fixed">
                <img src="data:image/png;base64,{logo_base64}" class="logo" alt="Logo">
                <div class="empresa-header">{empresa['nombre_completo']}</div>
            </div>
            
            <div class="page">
                <div class="content">
                    {HojaMembretadaDesigner._formatear_contenido(contenido)}
                </div>
                
                <div class="footer">
                    <strong>{empresa['nombre_completo']}</strong><br>
                    {empresa['direccion']['completa']}<br>
                    {empresa['direccion']['ciudad']}<br>
                    Tel: {empresa['telefono']} | {empresa['email']}<br>
                    RFC: {empresa['rfc']}
                </div>
            </div>
        </body>
        </html>
        """
        return html
    
    @staticmethod
    def diseño_moderno(empresa, logo_base64, contenido):
        """Diseño moderno con elementos gráficos"""
        css = HojaMembretadaDesigner.get_css_base() + """
        .header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: -0.75in -1in 30px -1in;
            padding: 25px 1in;
        }
        
        .logo {
            background: white;
            padding: 10px;
            border-radius: 8px;
        }
        
        .empresa-info {
            color: white;
            text-align: right;
        }
        
        .empresa-nombre {
            font-size: 15pt;
            font-weight: bold;
            margin-bottom: 5px;
        }
        
        .empresa-datos {
            font-size: 8pt;
        }
        
        .content {
            margin-top: 20px;
        }
        
        .footer {
            border-top: none;
            background: #f8f9fa;
            padding: 15px;
            margin: 40px -1in 0 -1in;
            font-size: 8pt;
            text-align: center;
        }
        
        .footer-highlight {
            color: #667eea;
            font-weight: bold;
        }
        """
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>{css}</style>
        </head>
        <body>
            <div class="header-fixed">
                <img src="data:image/png;base64,{logo_base64}" class="logo" alt="Logo">
                <div class="empresa-header">{empresa['nombre_completo']}</div>
            </div>
            
            <div class="page">
                <div class="content">
                    {HojaMembretadaDesigner._formatear_contenido(contenido)}
                </div>
                
                <div class="footer">
                    <span class="footer-highlight">{empresa['nombre_completo']}</span><br>
                    {empresa['direccion']['completa']}, {empresa['direccion']['ciudad']}<br>
                    Tel: {empresa['telefono']} | Email: {empresa['email']}
                </div>
            </div>
        </body>
        </html>
        """
        return html
    
    @staticmethod
    def diseño_barra_lateral(empresa, logo_base64, contenido):
        """Diseño con barra lateral de color (estilo Venngage)"""
        css = HojaMembretadaDesigner.get_css_base() + """
        .barra-lateral {
            position: absolute;
            left: 0;
            top: 0;
            bottom: 0;
            width: 0.6in;
            background: linear-gradient(180deg, #FF6B00 0%, #FF8C00 100%);
        }
        
        .header-fixed {
            border-bottom: 3px solid #FF6B00;
        }
        
        .content {
            margin-left: 0.3in;
        }
        
        .footer {
            background: #2C3E50;
            color: white;
            padding: 20px;
            margin: 40px -1in 0 -1in;
            font-size: 8pt;
        }
        
        .footer strong {
            color: #FF6B00;
        }
        """
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>{css}</style>
        </head>
        <body>
            <div class="barra-lateral"></div>
            
            <div class="header-fixed">
                <img src="data:image/png;base64,{logo_base64}" class="logo" alt="Logo">
                <div class="empresa-header">{empresa['nombre_completo']}</div>
            </div>
            
            <div class="page">
                <div class="content">
                    {HojaMembretadaDesigner._formatear_contenido(contenido)}
                </div>
                
                <div class="footer">
                    <strong>{empresa['nombre_completo']}</strong><br>
                    {empresa['direccion']['completa']} • {empresa['direccion']['ciudad']}<br>
                    Tel: {empresa['telefono']} • Email: {empresa['email']}
                </div>
            </div>
        </body>
        </html>
        """
        return html
    
    @staticmethod
    def diseño_diagonal_bold(empresa, logo_base64, contenido):
        """Diseño con líneas diagonales atrevidas (estilo construcción moderno)"""
        css = HojaMembretadaDesigner.get_css_base() + """
        .header-diagonal {
            position: relative;
            background: linear-gradient(135deg, #1A1A1A 0%, #1A1A1A 60%, #FFC107 60%, #FFC107 100%);
            padding: 30px 1in;
            margin: -1.2in -1in 30px -1in;
            color: white;
            min-height: 120px;
            display: flex;
            align-items: center;
        }
        
        .header-diagonal .logo {
            background: white;
            padding: 10px;
            border-radius: 5px;
        }
        
        .header-fixed {
            border-bottom: 4px solid #FFC107;
            background: #1A1A1A;
            color: white;
            padding: 10px 0;
        }
        
        .footer {
            border-top: 4px solid #FFC107;
            font-weight: bold;
        }
        """
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>{css}</style>
        </head>
        <body>
            <div class="header-fixed">
                <img src="data:image/png;base64,{logo_base64}" class="logo" alt="Logo">
                <div class="empresa-header" style="color: white;">{empresa['nombre_completo']}</div>
            </div>
            
            <div class="page">
                <div class="content">
                    {HojaMembretadaDesigner._formatear_contenido(contenido)}
                </div>
                
                <div class="footer">
                    {empresa['nombre_completo']}<br>
                    {empresa['direccion']['completa']}, {empresa['direccion']['ciudad']}<br>
                    {empresa['telefono']} | {empresa['email']}
                </div>
            </div>
        </body>
        </html>
        """
        return html
    
    @staticmethod
    def diseño_isometrico(empresa, logo_base64, contenido):
        """Diseño con elementos isométricos 3D (estilo técnico/arquitectónico)"""
        css = HojaMembretadaDesigner.get_css_base() + """
        .header-iso {
            position: relative;
            overflow: hidden;
            padding-bottom: 20px;
        }
        
        .iso-shape {
            position: absolute;
            top: -20px;
            right: 0;
            width: 200px;
            height: 150px;
            background: linear-gradient(45deg, #0066CC 0%, #00BCD4 100%);
            transform: skewY(-5deg);
            opacity: 0.1;
        }
        
        .header-fixed {
            border-bottom: 2px solid #0066CC;
        }
        
        .content {
            position: relative;
        }
        
        .content::before {
            content: '';
            position: absolute;
            right: -0.5in;
            top: 100px;
            width: 150px;
            height: 150px;
            background: linear-gradient(135deg, #0066CC 0%, #00BCD4 100%);
            transform: rotate(45deg);
            opacity: 0.05;
        }
        
        .footer {
            background: linear-gradient(90deg, #0066CC 0%, #00BCD4 100%);
            color: white;
            padding: 15px;
            margin: 40px -1in 0 -1in;
            font-size: 8pt;
        }
        """
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>{css}</style>
        </head>
        <body>
            <div class="header-fixed">
                <img src="data:image/png;base64,{logo_base64}" class="logo" alt="Logo">
                <div class="empresa-header">{empresa['nombre_completo']}</div>
            </div>
            
            <div class="page">
                <div class="header-iso">
                    <div class="iso-shape"></div>
                </div>
                
                <div class="content">
                    {HojaMembretadaDesigner._formatear_contenido(contenido)}
                </div>
                
                <div class="footer">
                    {empresa['nombre_completo']} • {empresa['direccion']['ciudad']}<br>
                    {empresa['telefono']} • {empresa['email']} • RFC: {empresa['rfc']}
                </div>
            </div>
        </body>
        </html>
        """
        return html
    
    @staticmethod
    def diseño_franja_superior(empresa, logo_base64, contenido):
        """Diseño con franja de color superior llamativa"""
        css = HojaMembretadaDesigner.get_css_base() + """
        .franja-superior {
            background: linear-gradient(90deg, #D32F2F 0%, #F44336 50%, #FF5722 100%);
            height: 0.4in;
            margin: -1.2in -1in 0 -1in;
        }
        
        .header-fixed {
            border-bottom: 3px solid #D32F2F;
        }
        
        .empresa-header {
            color: #D32F2F;
        }
        
        .footer {
            border-top: 3px solid #D32F2F;
            padding-top: 20px;
        }
        
        .footer-highlight {
            color: #D32F2F;
            font-weight: bold;
        }
        """
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>{css}</style>
        </head>
        <body>
            <div class="franja-superior"></div>
            
            <div class="header-fixed">
                <img src="data:image/png;base64,{logo_base64}" class="logo" alt="Logo">
                <div class="empresa-header">{empresa['nombre_completo']}</div>
            </div>
            
            <div class="page">
                <div class="content">
                    {HojaMembretadaDesigner._formatear_contenido(contenido)}
                </div>
                
                <div class="footer">
                    <span class="footer-highlight">{empresa['nombre_completo']}</span><br>
                    {empresa['direccion']['completa']}<br>
                    {empresa['direccion']['ciudad']} • Tel: {empresa['telefono']}<br>
                    {empresa['email']} • RFC: {empresa['rfc']}
                </div>
            </div>
        </body>
        </html>
        """
        return html
    
    @staticmethod
    def diseño_geometrico(empresa, logo_base64, contenido):
        """Diseño con formas geométricas modernas"""
        css = HojaMembretadaDesigner.get_css_base() + """
        .header-geo {
            position: relative;
            margin-bottom: 30px;
        }
        
        .geo-box {
            position: absolute;
            top: -10px;
            right: 0;
            width: 100px;
            height: 100px;
            background: #7B1FA2;
            opacity: 0.15;
        }
        
        .geo-circle {
            position: absolute;
            top: 30px;
            right: 80px;
            width: 60px;
            height: 60px;
            border: 8px solid #9C27B0;
            border-radius: 50%;
            opacity: 0.2;
        }
        
        .header-fixed {
            border-bottom: 4px solid #7B1FA2;
        }
        
        .content {
            position: relative;
        }
        
        .footer {
            background: linear-gradient(135deg, #7B1FA2 0%, #9C27B0 100%);
            color: white;
            padding: 20px;
            margin: 40px -1in 0 -1in;
            font-size: 8pt;
            text-align: center;
        }
        """
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>{css}</style>
        </head>
        <body>
            <div class="header-fixed">
                <img src="data:image/png;base64,{logo_base64}" class="logo" alt="Logo">
                <div class="empresa-header">{empresa['nombre_completo']}</div>
            </div>
            
            <div class="page">
                <div class="header-geo">
                    <div class="geo-box"></div>
                    <div class="geo-circle"></div>
                </div>
                
                <div class="content">
                    {HojaMembretadaDesigner._formatear_contenido(contenido)}
                </div>
                
                <div class="footer">
                    <strong>{empresa['nombre_completo']}</strong><br>
                    {empresa['direccion']['completa']}, {empresa['direccion']['ciudad']}<br>
                    {empresa['telefono']} • {empresa['email']} • RFC: {empresa['rfc']}
                </div>
            </div>
        </body>
        </html>
        """
        return html
    
    @staticmethod
    def diseño_azul_amarillo_bold(empresa, logo_base64, contenido):
        """Azul marino y amarillo - Estilo corporativo atrevido"""
        css = HojaMembretadaDesigner.get_css_base() + """
        .header-fixed {
            background: #003D82;
            color: white;
            padding: 20px 0;
            border-bottom: 8px solid #FFD700;
        }
        
        .empresa-header { color: white; }
        
        .content {
            margin-top: 50px;
        }
        
        .footer {
            background: linear-gradient(90deg, #003D82 0%, #0056B3 100%);
            color: white;
            padding: 20px;
            margin: 40px -1in 0 -1in;
            border-top: 8px solid #FFD700;
            font-size: 8pt;
        }
        """
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>{css}</style>
        </head>
        <body>
            <div class="header-fixed">
                <img src="data:image/png;base64,{logo_base64}" class="logo" alt="Logo">
                <div class="empresa-header">{empresa['nombre_completo']}</div>
            </div>
            
            <div class="page">
                <div class="content">
                    {HojaMembretadaDesigner._formatear_contenido(contenido)}
                </div>
                
                <div class="footer">
                    <strong>{empresa['nombre_completo']}</strong> • {empresa['direccion']['ciudad']}<br>
                    {empresa['telefono']} • {empresa['email']} • RFC: {empresa['rfc']}
                </div>
            </div>
        </body>
        </html>
        """
        return html
    
    @staticmethod
    def diseño_verde_minimalista(empresa, logo_base64, contenido):
        """Verde limpio y minimalista"""
        css = HojaMembretadaDesigner.get_css_base() + """
        .header-fixed {
            border-bottom: 4px solid #4CAF50;
            padding-bottom: 15px;
        }
        
        .empresa-header {
            color: #2E7D32;
        }
        
        .content {
            margin-top: 60px;
        }
        
        .footer {
            border-top: 4px solid #4CAF50;
            color: #2E7D32;
            font-weight: 500;
            padding-top: 20px;
        }
        """
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>{css}</style>
        </head>
        <body>
            <div class="header-fixed">
                <img src="data:image/png;base64,{logo_base64}" class="logo" alt="Logo">
                <div class="empresa-header">{empresa['nombre_completo']}</div>
            </div>
            
            <div class="page">
                <div class="content">
                    {HojaMembretadaDesigner._formatear_contenido(contenido)}
                </div>
                
                <div class="footer">
                    {empresa['nombre_completo']}<br>
                    {empresa['direccion']['completa']}, {empresa['direccion']['ciudad']}<br>
                    Tel: {empresa['telefono']} • {empresa['email']}
                </div>
            </div>
        </body>
        </html>
        """
        return html
    
    @staticmethod
    def diseño_negro_naranja(empresa, logo_base64, contenido):
        """Negro y naranja - Industrial moderno SIN línea lateral"""
        css = HojaMembretadaDesigner.get_css_base() + """
        .header-fixed {
            background: #1A1A1A;
            color: white;
            padding: 20px 0;
            border-bottom: 6px solid #FF6B00;
        }
        
        .empresa-header { color: white; }
        
        .content {
            margin-top: 40px;
        }
        
        .footer {
            background: #1A1A1A;
            color: white;
            padding: 20px;
            margin: 40px -1in 0 -1in;
            font-size: 8pt;
        }
        """
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>{css}</style>
        </head>
        <body>
            <div class="header-fixed">
                <img src="data:image/png;base64,{logo_base64}" class="logo" alt="Logo">
                <div class="empresa-header">{empresa['nombre_completo']}</div>
            </div>
            
            <div class="page">
                <div class="content">
                    {HojaMembretadaDesigner._formatear_contenido(contenido)}
                </div>
                
                <div class="footer">
                    {empresa['nombre_completo']} • {empresa['direccion']['ciudad']}<br>
                    {empresa['telefono']} • {empresa['email']} • RFC: {empresa['rfc']}
                </div>
            </div>
        </body>
        </html>
        """
        return html
    
    @staticmethod
    def diseño_azul_rosa_isometrico(empresa, logo_base64, contenido):
        """Azul oscuro y rosa - Diseño isométrico 3D"""
        css = HojaMembretadaDesigner.get_css_base() + """
        .header-iso {
            position: relative;
            padding-bottom: 30px;
        }
        
        .iso-element {
            position: absolute;
            right: -0.3in;
            top: 20px;
            width: 150px;
            height: 150px;
            background: linear-gradient(135deg, #1E3A8A 0%, #EC4899 100%);
            transform: rotate(45deg) skewY(20deg);
            opacity: 0.15;
        }
        
        .header-fixed {
            border-bottom: 3px solid #1E3A8A;
        }
        
        .empresa-header {
            color: #1E3A8A;
        }
        
        .footer {
            background: linear-gradient(90deg, #1E3A8A 0%, #EC4899 100%);
            color: white;
            padding: 20px;
            margin: 40px -1in 0 -1in;
            font-size: 8pt;
        }
        """
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>{css}</style>
        </head>
        <body>
            <div class="header-fixed">
                <img src="data:image/png;base64,{logo_base64}" class="logo" alt="Logo">
                <div class="empresa-header">{empresa['nombre_completo']}</div>
            </div>
            
            <div class="page">
                <div class="header-iso">
                    <div class="iso-element"></div>
                </div>
                
                <div class="content">
                    {HojaMembretadaDesigner._formatear_contenido(contenido)}
                </div>
                
                <div class="footer">
                    <strong>{empresa['nombre_completo']}</strong><br>
                    {empresa['direccion']['completa']}, {empresa['direccion']['ciudad']}<br>
                    Tel: {empresa['telefono']} • {empresa['email']} • RFC: {empresa['rfc']}
                </div>
            </div>
        </body>
        </html>
        """
        return html
    
    @staticmethod
    def diseño_marron_simple(empresa, logo_base64, contenido):
        """Marrón simple y profesional"""
        css = HojaMembretadaDesigner.get_css_base() + """
        .header-fixed {
            border-bottom: 3px solid #8B4513;
            padding-bottom: 15px;
        }
        
        .empresa-header {
            color: #8B4513;
            font-weight: 600;
        }
        
        .content {
            margin-top: 60px;
        }
        
        .footer {
            border-top: 3px solid #8B4513;
            color: #654321;
            padding-top: 20px;
            font-weight: 500;
        }
        """
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>{css}</style>
        </head>
        <body>
            <div class="header-fixed">
                <img src="data:image/png;base64,{logo_base64}" class="logo" alt="Logo">
                <div class="empresa-header">{empresa['nombre_completo']}</div>
            </div>
            
            <div class="page">
                <div class="content">
                    {HojaMembretadaDesigner._formatear_contenido(contenido)}
                </div>
                
                <div class="footer">
                    <strong>{empresa['nombre_completo']}</strong><br>
                    {empresa['direccion']['completa']}<br>
                    {empresa['direccion']['ciudad']} • Tel: {empresa['telefono']}<br>
                    Email: {empresa['email']} • RFC: {empresa['rfc']}
                </div>
            </div>
        </body>
        </html>
        """
        return html
    
    @staticmethod
    def diseño_negro_rojo(empresa, logo_base64, contenido):
        """Negro y rojo - Potente y dinámico"""
        css = HojaMembretadaDesigner.get_css_base() + """
        .franja-roja {
            height: 0.3in;
            background: linear-gradient(90deg, #DC2626 0%, #B91C1C 100%);
            margin: -1.2in -1in 30px -1in;
        }
        
        .header-fixed {
            border-bottom: 4px solid #DC2626;
        }
        
        .empresa-header {
            color: #DC2626;
        }
        
        .footer {
            background: #1F2937;
            color: white;
            padding: 20px;
            margin: 40px -1in 0 -1in;
            border-top: 4px solid #DC2626;
            font-size: 8pt;
        }
        """
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>{css}</style>
        </head>
        <body>
            <div class="franja-roja"></div>
            
            <div class="header-fixed">
                <img src="data:image/png;base64,{logo_base64}" class="logo" alt="Logo">
                <div class="empresa-header">{empresa['nombre_completo']}</div>
            </div>
            
            <div class="page">
                <div class="content">
                    {HojaMembretadaDesigner._formatear_contenido(contenido)}
                </div>
                
                <div class="footer">
                    <strong>{empresa['nombre_completo']}</strong> • {empresa['direccion']['ciudad']}<br>
                    Tel: {empresa['telefono']} • {empresa['email']} • RFC: {empresa['rfc']}
                </div>
            </div>
        </body>
        </html>
        """
        return html
    
    @staticmethod
    def diseño_blanco_naranja_clean(empresa, logo_base64, contenido):
        """Blanco y naranja - Limpio y moderno"""
        css = HojaMembretadaDesigner.get_css_base() + """
        .header-fixed {
            border-bottom: 2px solid #F97316;
            padding-bottom: 20px;
        }
        
        .empresa-header {
            color: #EA580C;
        }
        
        .content {
            margin-top: 50px;
            position: relative;
        }
        
        .content::after {
            content: '';
            position: absolute;
            right: -0.5in;
            top: 50px;
            width: 120px;
            height: 120px;
            border: 15px solid #F97316;
            border-radius: 50%;
            opacity: 0.1;
        }
        
        .footer {
            border-top: 2px solid #F97316;
            padding-top: 15px;
        }
        
        .footer strong {
            color: #F97316;
        }
        """
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>{css}</style>
        </head>
        <body>
            <div class="header-fixed">
                <img src="data:image/png;base64,{logo_base64}" class="logo" alt="Logo">
                <div class="empresa-header">{empresa['nombre_completo']}</div>
            </div>
            
            <div class="page">
                <div class="content">
                    {HojaMembretadaDesigner._formatear_contenido(contenido)}
                </div>
                
                <div class="footer">
                    <strong>{empresa['nombre_completo']}</strong><br>
                    {empresa['direccion']['completa']}, {empresa['direccion']['ciudad']}<br>
                    Tel: {empresa['telefono']} • Email: {empresa['email']}
                </div>
            </div>
        </body>
        </html>
        """
        return html
    
    @staticmethod
    def diseño_blanco_negro_simple(empresa, logo_base64, contenido):
        """Blanco y negro - Elegancia atemporal"""
        css = HojaMembretadaDesigner.get_css_base() + """
        .header-fixed {
            border-bottom: 4px solid #000;
            padding-bottom: 15px;
        }
        
        .empresa-header {
            color: #000;
            font-weight: 700;
            letter-spacing: 2px;
        }
        
        .content {
            margin-top: 60px;
        }
        
        .footer {
            border-top: 4px solid #000;
            padding-top: 20px;
            font-weight: 600;
        }
        """
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>{css}</style>
        </head>
        <body>
            <div class="header-fixed">
                <img src="data:image/png;base64,{logo_base64}" class="logo" alt="Logo">
                <div class="empresa-header">{empresa['nombre_completo']}</div>
            </div>
            
            <div class="page">
                <div class="content">
                    {HojaMembretadaDesigner._formatear_contenido(contenido)}
                </div>
                
                <div class="footer">
                    <strong>{empresa['nombre_completo']}</strong><br>
                    {empresa['direccion']['completa']}<br>
                    {empresa['direccion']['ciudad']}, Jalisco<br>
                    Tel: {empresa['telefono']} • {empresa['email']} • RFC: {empresa['rfc']}
                </div>
            </div>
        </body>
        </html>
        """
        return html
    
    @staticmethod
    def diseño_morado_minimalista(empresa, logo_base64, contenido):
        """Morado minimalista - Elegante y sofisticado"""
        css = HojaMembretadaDesigner.get_css_base() + """
        .header-fixed {
            border-bottom: 3px solid #7C3AED;
            padding-bottom: 15px;
        }
        
        .empresa-header {
            color: #7C3AED;
        }
        
        .content {
            margin-top: 60px;
        }
        
        .footer {
            background: linear-gradient(135deg, #7C3AED 0%, #A78BFA 100%);
            color: white;
            padding: 20px;
            margin: 40px -1in 0 -1in;
            text-align: center;
            font-size: 8pt;
        }
        """
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>{css}</style>
        </head>
        <body>
            <div class="header-fixed">
                <img src="data:image/png;base64,{logo_base64}" class="logo" alt="Logo">
                <div class="empresa-header">{empresa['nombre_completo']}</div>
            </div>
            
            <div class="page">
                <div class="content">
                    {HojaMembretadaDesigner._formatear_contenido(contenido)}
                </div>
                
                <div class="footer">
                    <strong>{empresa['nombre_completo']}</strong><br>
                    {empresa['direccion']['completa']}, {empresa['direccion']['ciudad']}<br>
                    {empresa['telefono']} • {empresa['email']} • RFC: {empresa['rfc']}
                </div>
            </div>
        </body>
        </html>
        """
        return html
    
    @staticmethod
    def diseño_negro_amarillo_industrial(empresa, logo_base64, contenido):
        """Negro y amarillo - Estilo industrial de construcción"""
        css = HojaMembretadaDesigner.get_css_base() + """
        .diagonal-strip {
            position: absolute;
            top: 0;
            right: 0;
            width: 200px;
            height: 150px;
            background: repeating-linear-gradient(
                45deg,
                #1F2937 0px,
                #1F2937 20px,
                #FCD34D 20px,
                #FCD34D 40px
            );
            transform: skewY(-5deg);
            opacity: 0.2;
        }
        
        .header-fixed {
            background: #1F2937;
            color: white;
            padding: 20px 0;
            border-bottom: 6px solid #FCD34D;
        }
        
        .empresa-header { color: white; }
        
        .page {
            position: relative;
        }
        
        .content {
            margin-top: 50px;
        }
        
        .footer {
            background: #1F2937;
            color: white;
            padding: 20px;
            margin: 40px -1in 0 -1in;
            border-top: 6px solid #FCD34D;
            font-size: 8pt;
        }
        """
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>{css}</style>
        </head>
        <body>
            <div class="header-fixed">
                <img src="data:image/png;base64,{logo_base64}" class="logo" alt="Logo">
                <div class="empresa-header">{empresa['nombre_completo']}</div>
            </div>
            
            <div class="page">
                <div class="diagonal-strip"></div>
                
                <div class="content">
                    {HojaMembretadaDesigner._formatear_contenido(contenido)}
                </div>
                
                <div class="footer">
                    <strong>{empresa['nombre_completo']}</strong> • {empresa['direccion']['ciudad']}<br>
                    Tel: {empresa['telefono']} • {empresa['email']} • RFC: {empresa['rfc']}
                </div>
            </div>
        </body>
        </html>
        """
        return html
    
    @staticmethod
    def _formatear_contenido(contenido):
        """Formatea el contenido respetando párrafos y saltos de línea"""
        if not contenido:
            return ""
        
        # Dividir por líneas vacías (párrafos)
        parrafos = contenido.split('\n\n')
        html_parrafos = []
        
        for parrafo in parrafos:
            # Reemplazar saltos de línea simples por <br>
            parrafo_limpio = parrafo.strip()
            if parrafo_limpio:
                parrafo_html = parrafo_limpio.replace('\n', '<br>')
                html_parrafos.append(f'<p>{parrafo_html}</p>')
        
        return '\n'.join(html_parrafos)
    
    @staticmethod
    def generar_diseño(estilo, empresa, logo_base64, contenido):
        """
        Genera un diseño de hoja membretada según el estilo especificado
        
        Args:
            estilo: Uno de los 18 estilos disponibles
            empresa: Diccionario con datos de la empresa
            logo_base64: Logo en formato base64
            contenido: Texto del contenido de la carta
        """
        if estilo == 'azul_amarillo_bold':
            return HojaMembretadaDesigner.diseño_azul_amarillo_bold(empresa, logo_base64, contenido)
        elif estilo == 'verde_minimalista':
            return HojaMembretadaDesigner.diseño_verde_minimalista(empresa, logo_base64, contenido)
        elif estilo == 'negro_naranja':
            return HojaMembretadaDesigner.diseño_negro_naranja(empresa, logo_base64, contenido)
        elif estilo == 'azul_rosa_isometrico':
            return HojaMembretadaDesigner.diseño_azul_rosa_isometrico(empresa, logo_base64, contenido)
        elif estilo == 'marron_simple':
            return HojaMembretadaDesigner.diseño_marron_simple(empresa, logo_base64, contenido)
        elif estilo == 'negro_rojo':
            return HojaMembretadaDesigner.diseño_negro_rojo(empresa, logo_base64, contenido)
        elif estilo == 'blanco_naranja_clean':
            return HojaMembretadaDesigner.diseño_blanco_naranja_clean(empresa, logo_base64, contenido)
        elif estilo == 'blanco_negro_simple':
            return HojaMembretadaDesigner.diseño_blanco_negro_simple(empresa, logo_base64, contenido)
        elif estilo == 'morado_minimalista':
            return HojaMembretadaDesigner.diseño_morado_minimalista(empresa, logo_base64, contenido)
        elif estilo == 'negro_amarillo_industrial':
            return HojaMembretadaDesigner.diseño_negro_amarillo_industrial(empresa, logo_base64, contenido)
        elif estilo == 'barra_lateral_naranja':
            return HojaMembretadaDesigner.diseño_barra_lateral(empresa, logo_base64, contenido)
        elif estilo == 'diagonal_moderno':
            return HojaMembretadaDesigner.diseño_diagonal_bold(empresa, logo_base64, contenido)
        elif estilo == 'franja_superior_roja':
            return HojaMembretadaDesigner.diseño_franja_superior(empresa, logo_base64, contenido)
        elif estilo == 'geometrico_purpura':
            return HojaMembretadaDesigner.diseño_geometrico(empresa, logo_base64, contenido)
        elif estilo == 'azul_corporativo':
            return HojaMembretadaDesigner.diseño_isometrico(empresa, logo_base64, contenido)
        elif estilo == 'verde_ecologico':
            return HojaMembretadaDesigner.diseño_verde_minimalista(empresa, logo_base64, contenido)
        elif estilo == 'gris_elegante':
            return HojaMembretadaDesigner.diseño_blanco_negro_simple(empresa, logo_base64, contenido)
        elif estilo == 'terracota_profesional':
            return HojaMembretadaDesigner.diseño_marron_simple(empresa, logo_base64, contenido)
        else:
            # Default: azul amarillo bold
            return HojaMembretadaDesigner.diseño_azul_amarillo_bold(empresa, logo_base64, contenido)


if __name__ == "__main__":
    # Prueba del diseñador
    empresa_test = {
        'nombre': 'Constructora Atlas',
        'nombre_completo': 'Constructora Atlas S.A. de C.V.',
        'direccion': {
            'completa': 'Av. López Mateos 2375',
            'ciudad': 'Guadalajara, Jalisco',
            'cp': 44500
        },
        'telefono': '33-1234-5678',
        'email': 'contacto@atlas.com.mx',
        'rfc': 'CAT150501ABC',
        'año_fundacion': 2015
    }
    
    contenido_test = """A quien corresponda:

Por medio de la presente, hacemos constar que Constructora Atlas ha mantenido un desempeño ejemplar en todos sus proyectos.

Atentamente,
Director General"""
    
    # Logo de prueba (imagen vacía en base64)
    import base64
    logo_base64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg=="
    
    print("Generando diseños de prueba...")
    for estilo in HojaMembretadaDesigner.ESTILOS:
        html = HojaMembretadaDesigner.generar_diseño(estilo, empresa_test, logo_base64, contenido_test)
        filename = f"test_{estilo}.html"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Diseño {estilo} guardado en {filename}")
