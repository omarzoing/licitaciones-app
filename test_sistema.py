"""
Script de prueba rápida para verificar que todos los módulos funcionan
Ejecuta: python test_sistema.py
"""

import sys

def test_imports():
    """Verifica que todas las dependencias se puedan importar"""
    print("🔍 Verificando imports...")
    
    try:
        import streamlit
        print("✅ Streamlit instalado")
    except ImportError:
        print("❌ Streamlit NO instalado - ejecuta: pip install streamlit")
        return False
    
    try:
        from PIL import Image
        print("✅ Pillow instalado")
    except ImportError:
        print("❌ Pillow NO instalado - ejecuta: pip install Pillow")
        return False
    
    try:
        import google.generativeai
        print("✅ Google Generative AI instalado")
    except ImportError:
        print("❌ Google Generative AI NO instalado - ejecuta: pip install google-generativeai")
        return False
    
    try:
        from weasyprint import HTML
        print("✅ WeasyPrint instalado")
    except ImportError:
        print("❌ WeasyPrint NO instalado")
        print("   En macOS, ejecuta:")
        print("   brew install python3 cairo pango gdk-pixbuf libffi")
        print("   pip install weasyprint")
        return False
    
    try:
        from dotenv import load_dotenv
        print("✅ Python-dotenv instalado")
    except ImportError:
        print("❌ Python-dotenv NO instalado - ejecuta: pip install python-dotenv")
        return False
    
    return True


def test_modulos_propios():
    """Verifica que los módulos propios se puedan importar"""
    print("\n🔍 Verificando módulos propios...")
    
    try:
        from empresa_generator import EmpresaGenerator
        print("✅ empresa_generator.py")
    except Exception as e:
        print(f"❌ Error en empresa_generator.py: {e}")
        return False
    
    try:
        from logo_generator import LogoGenerator
        print("✅ logo_generator.py")
    except Exception as e:
        print(f"❌ Error en logo_generator.py: {e}")
        return False
    
    try:
        from logo_image_generator import LogoImageGenerator
        print("✅ logo_image_generator.py")
    except Exception as e:
        print(f"❌ Error en logo_image_generator.py: {e}")
        return False
    
    try:
        from hoja_membretada_designer import HojaMembretadaDesigner
        print("✅ hoja_membretada_designer.py")
    except Exception as e:
        print(f"❌ Error en hoja_membretada_designer.py: {e}")
        return False
    
    try:
        from pdf_generator import PDFGenerator
        print("✅ pdf_generator.py")
    except Exception as e:
        print(f"❌ Error en pdf_generator.py: {e}")
        return False
    
    return True


def test_generador_empresas():
    """Prueba el generador de empresas"""
    print("\n🏗️ Probando generador de empresas...")
    
    try:
        from empresa_generator import EmpresaGenerator
        
        empresa = EmpresaGenerator.generar_empresa_completa()
        
        print(f"✅ Empresa generada: {empresa['nombre_completo']}")
        print(f"   Dirección: {empresa['direccion']['completa']}")
        print(f"   Teléfono: {empresa['telefono']}")
        print(f"   Email: {empresa['email']}")
        print(f"   RFC: {empresa['rfc']}")
        
        return True
    except Exception as e:
        print(f"❌ Error generando empresa: {e}")
        return False


def test_api_key():
    """Verifica si hay una API key configurada"""
    print("\n🔑 Verificando API Key...")
    
    import os
    from dotenv import load_dotenv
    
    load_dotenv()
    
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if api_key:
        print(f"✅ API Key encontrada (primeros 10 caracteres): {api_key[:10]}...")
        return True
    else:
        print("⚠️ No se encontró GOOGLE_API_KEY en .env")
        print("   El sistema funcionará en modo de prueba con placeholders")
        return True  # No es crítico para la prueba


def test_diseño_hoja():
    """Prueba el generador de diseños"""
    print("\n📄 Probando generador de diseños...")
    
    try:
        from hoja_membretada_designer import HojaMembretadaDesigner
        from empresa_generator import EmpresaGenerator
        import base64
        
        empresa = EmpresaGenerator.generar_empresa_completa()
        logo_base64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg=="
        contenido = "Contenido de prueba para la hoja membretada."
        
        for estilo in ['minimalista', 'tradicional', 'moderno']:
            html = HojaMembretadaDesigner.generar_diseño(estilo, empresa, logo_base64, contenido)
            if html and len(html) > 100:
                print(f"✅ Diseño {estilo} generado correctamente")
            else:
                print(f"❌ Error generando diseño {estilo}")
                return False
        
        return True
    except Exception as e:
        print(f"❌ Error generando diseños: {e}")
        return False


def main():
    """Ejecuta todas las pruebas"""
    print("="*60)
    print("🧪 PRUEBA DEL SISTEMA - Generador de Hojas Membretadas")
    print("="*60)
    
    tests = [
        ("Imports de dependencias", test_imports),
        ("Módulos propios", test_modulos_propios),
        ("Generador de empresas", test_generador_empresas),
        ("API Key", test_api_key),
        ("Diseños de hojas", test_diseño_hoja)
    ]
    
    resultados = []
    
    for nombre, test_func in tests:
        try:
            resultado = test_func()
            resultados.append((nombre, resultado))
        except Exception as e:
            print(f"\n❌ Error ejecutando {nombre}: {e}")
            resultados.append((nombre, False))
    
    print("\n" + "="*60)
    print("📊 RESUMEN DE PRUEBAS")
    print("="*60)
    
    for nombre, resultado in resultados:
        estado = "✅ PASS" if resultado else "❌ FAIL"
        print(f"{estado} - {nombre}")
    
    total = len(resultados)
    exitosas = sum(1 for _, r in resultados if r)
    
    print("\n" + "="*60)
    print(f"Resultado: {exitosas}/{total} pruebas exitosas")
    
    if exitosas == total:
        print("\n🎉 ¡TODO FUNCIONA CORRECTAMENTE!")
        print("\nPuedes ejecutar la aplicación con:")
        print("   streamlit run app.py")
    else:
        print("\n⚠️ Hay problemas que necesitan ser resueltos")
        print("Revisa los errores arriba y sigue las instrucciones de instalación")
    
    print("="*60)
    
    return exitosas == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
