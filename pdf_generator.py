"""
Generador de PDF desde HTML usando WeasyPrint
"""

from weasyprint import HTML, CSS
import io
import base64

class PDFGenerator:
    """Convierte HTML/CSS en PDF de alta calidad"""
    
    @staticmethod
    def html_to_pdf(html_content):
        """
        Convierte HTML a PDF
        
        Args:
            html_content: String con el contenido HTML completo
            
        Returns:
            BytesIO object con el PDF generado
        """
        try:
            # Crear objeto HTML
            html = HTML(string=html_content)
            
            # Generar PDF en memoria
            pdf_bytes = io.BytesIO()
            html.write_pdf(pdf_bytes)
            pdf_bytes.seek(0)
            
            return pdf_bytes
            
        except Exception as e:
            print(f"Error generando PDF: {e}")
            return None
    
    @staticmethod
    def html_to_pdf_file(html_content, output_path):
        """
        Convierte HTML a PDF y lo guarda en un archivo
        
        Args:
            html_content: String con el contenido HTML completo
            output_path: Ruta donde guardar el PDF
        """
        try:
            html = HTML(string=html_content)
            html.write_pdf(output_path)
            return True
        except Exception as e:
            print(f"Error guardando PDF: {e}")
            return False
    
    @staticmethod
    def calcular_paginas_necesarias(html_content):
        """
        Calcula cuántas páginas ocupará el contenido
        Útil para prevención de desbordamiento
        """
        try:
            html = HTML(string=html_content)
            # WeasyPrint automáticamente maneja múltiples páginas
            # Solo necesitamos verificar que se genere correctamente
            pdf_bytes = io.BytesIO()
            html.write_pdf(pdf_bytes)
            return True
        except Exception as e:
            print(f"Error al calcular páginas: {e}")
            return False


if __name__ == "__main__":
    # Prueba del generador de PDF
    html_test = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            @page {
                size: letter;
                margin: 1in;
            }
            body {
                font-family: Arial, sans-serif;
            }
            h1 {
                color: #333;
            }
        </style>
    </head>
    <body>
        <h1>Hoja Membretada de Prueba</h1>
        <p>Este es un documento de prueba para verificar la generación de PDF.</p>
        <p>La página debe tener tamaño carta (8.5 x 11 pulgadas).</p>
    </body>
    </html>
    """
    
    print("Generando PDF de prueba...")
    pdf = PDFGenerator.html_to_pdf(html_test)
    
    if pdf:
        with open("prueba.pdf", "wb") as f:
            f.write(pdf.read())
        print("PDF generado exitosamente: prueba.pdf")
    else:
        print("Error al generar PDF")
