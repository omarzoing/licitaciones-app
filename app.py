"""
Aplicación Streamlit para generación de hojas membretadas de constructoras
Autor: Sistema automatizado
"""

import streamlit as st
import os
from dotenv import load_dotenv
import base64
from io import BytesIO
from PIL import Image
import random

# Importar módulos propios
from empresa_generator import EmpresaGenerator
from logo_generator import LogoGenerator
from logo_image_generator import LogoImageGenerator
from logo_generator_hf import generar_logo_simple  # Generador de logos con IA
from hoja_membretada_designer import HojaMembretadaDesigner
from pdf_generator import PDFGenerator
from api_config import get_api_config, is_dalle_configured, is_gemini_configured

# Configuración de la página
st.set_page_config(
    page_title="Generador de Hojas Membretadas",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Cargar variables de entorno
load_dotenv()

# CSS personalizado
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 30px;
    }
    .logo-option {
        border: 2px solid #ddd;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        cursor: pointer;
        transition: all 0.3s;
    }
    .logo-option:hover {
        border-color: #667eea;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .logo-selected {
        border-color: #667eea;
        background-color: #f0f4ff;
    }
    .info-box {
        background-color: #f8f9fa;
        color: #333333 !important;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #667eea;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)


def inicializar_session_state():
    """Inicializa las variables de sesión"""
    if 'paso' not in st.session_state:
        st.session_state.paso = 1
    if 'empresas_generadas' not in st.session_state:
        st.session_state.empresas_generadas = []
    if 'logos_generados' not in st.session_state:
        st.session_state.logos_generados = []
    if 'empresa_seleccionada' not in st.session_state:
        st.session_state.empresa_seleccionada = None
    if 'logo_seleccionado' not in st.session_state:
        st.session_state.logo_seleccionado = None
    if 'diseño_seleccionado' not in st.session_state:
        st.session_state.diseño_seleccionado = None
    if 'contenido_texto' not in st.session_state:
        st.session_state.contenido_texto = ""


def imagen_a_base64(imagen):
    """Convierte imagen PIL a base64"""
    buffered = BytesIO()
    imagen.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()


def generar_empresas_y_logos(cantidad=5):
    """Genera empresas y sus logos usando IA de Hugging Face (con fallback)"""
    with st.spinner(f"🏗️ Generando {cantidad} opciones de constructoras con logos de IA..."):
        # Verificar si Hugging Face está disponible
        import os
        hf_token = os.getenv("HUGGINGFACE_TOKEN")
        
        if hf_token:
            st.success("✅ Hugging Face IA configurado - Generando logos con IA (FLUX.1)")
            usar_ia = True
        else:
            st.info("ℹ️ Usando sistema clásico - Logos con diseño gráfico")
            st.caption("💡 Configura HUGGINGFACE_TOKEN en .env para logos con IA (gratis)")
            usar_ia = False
        
        # Obtener configuración de APIs (para fallback)
        api_config = get_api_config()
        logo_img_gen = LogoImageGenerator(service="placeholder")
        
        empresas = []
        logos = []
        logos_ia_count = 0
        logos_codigo_count = 0
        
        for i in range(cantidad):
            # Generar datos de empresa
            empresa = EmpresaGenerator.generar_empresa_completa()
            
            logo_img = None
            concepto = ""
            metodo = "codigo"
            
            # Intentar generar con IA de Hugging Face
            if usar_ia:
                try:
                    with st.spinner(f"🎨 Generando logo {i+1}/{cantidad} con IA..."):
                        logo_img = generar_logo_simple(empresa['nombre'], 'professional')
                        
                        if logo_img:
                            concepto = "✨ Logo generado con IA (Hugging Face FLUX.1)"
                            metodo = "ia"
                            logos_ia_count += 1
                        else:
                            raise Exception("IA no disponible")
                            
                except Exception as e:
                    # Fallback al sistema clásico
                    st.warning(f"⚠️ IA no disponible para logo {i+1}, usando sistema clásico")
                    logo_img = None
            
            # Fallback: Sistema clásico si IA falló o no está configurada
            if not logo_img:
                concepto = f"Logo corporativo para {empresa['nombre']}"
                logo_img = logo_img_gen.generar_logo_placeholder(empresa['nombre'], concepto)
                metodo = "codigo"
                logos_codigo_count += 1
            
            empresas.append(empresa)
            logos.append({
                'empresa': empresa,
                'concepto': concepto,
                'imagen': logo_img,
                'metodo': metodo  # Para estadísticas
            })
            
            # Mostrar progreso
            emoji = "✨" if metodo == "ia" else "🔧"
            st.progress((i + 1) / cantidad, text=f"{emoji} Logo {i + 1}/{cantidad} - {metodo.upper()}")
        
        # Mostrar estadísticas
        if logos_ia_count > 0 or logos_codigo_count > 0:
            col1, col2 = st.columns(2)
            with col1:
                if logos_ia_count > 0:
                    st.metric("✨ Con IA", logos_ia_count)
            with col2:
                if logos_codigo_count > 0:
                    st.metric("🔧 Clásicos", logos_codigo_count)
        
        return empresas, logos


def mostrar_paso_1_generacion_logos():
    """Paso 1: Generar y seleccionar logo"""
    st.markdown('<div class="main-header"><h1>🏗️ Paso 1: Genera y Selecciona tu Logo</h1></div>', 
                unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col2:
        st.markdown("""
        <div class="info-box">
            <strong>Instrucciones:</strong>
            <ol style="margin-top: 10px; margin-bottom: 0px; padding-left: 20px;">
                <li>Genera 5 opciones de logos</li>
                <li>Revisa cada opción</li>
                <li>Si no te convencen, genera nuevas opciones</li>
                <li>Selecciona tu favorito</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
    
    with col1:
        if st.button("🎨 Generar 5 Opciones de Logos", type="primary", use_container_width=True):
            empresas, logos = generar_empresas_y_logos(5)
            st.session_state.empresas_generadas = empresas
            st.session_state.logos_generados = logos
            st.success("✅ ¡Logos generados exitosamente!")
            st.rerun()
    
    # Mostrar logos generados
    if st.session_state.logos_generados:
        st.subheader("Selecciona el logo que más te guste:")
        
        # Mostrar en grid
        cols = st.columns(2)
        
        for idx, logo_data in enumerate(st.session_state.logos_generados):
            with cols[idx % 2]:
                with st.container():
                    st.markdown(f"### Opción {idx + 1}")
                    st.write(f"**{logo_data['empresa']['nombre_completo']}**")
                    
                    # Mostrar logo
                    if logo_data['imagen']:
                        st.image(logo_data['imagen'], width=400)
                    else:
                        st.info("Vista previa del logo")
                    
                    # Mostrar concepto
                    with st.expander("Ver concepto del diseño"):
                        st.write(logo_data['concepto'])
                    
                    # Botón de selección
                    if st.button(f"✅ Seleccionar Opción {idx + 1}", key=f"select_logo_{idx}", use_container_width=True):
                        st.session_state.empresa_seleccionada = logo_data['empresa']
                        st.session_state.logo_seleccionado = logo_data['imagen']
                        st.session_state.paso = 2
                        st.success(f"✅ ¡Logo seleccionado! Pasando al diseño de la hoja...")
                        st.rerun()
                
                st.markdown("---")
    else:
        st.info("👆 Haz clic en el botón para generar opciones de logos")


def mostrar_paso_2_diseño_hoja():
    """Paso 2: Seleccionar diseño de hoja membretada con vista previa"""
    st.markdown('<div class="main-header"><h1>📄 Paso 2: Selecciona el Diseño de tu Hoja</h1></div>', 
                unsafe_allow_html=True)
    
    # Empresa seleccionada en la parte superior
    col_header1, col_header2 = st.columns([3, 1])
    
    with col_header1:
    with col_header1:
        logo_html = ""
        if st.session_state.logo_seleccionado:
            # Convertir imagen para incrustar en HTML
            buffered = BytesIO()
            st.session_state.logo_seleccionado.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            logo_html = f'<div style="margin-top: 10px;"><img src="data:image/png;base64,{img_str}" width="120"></div>'
            
        st.markdown(f"""
        <div class="info-box">
            <strong>Empresa:</strong> {st.session_state.empresa_seleccionada['nombre_completo']}
            {logo_html}
        </div>
        """, unsafe_allow_html=True)
    
    with col_header2:
        if st.button("⬅️ Cambiar Logo", use_container_width=True):
            st.session_state.paso = 1
            st.rerun()
    
    st.markdown("---")
    st.subheader("🎨 Selecciona uno de los 18 diseños profesionales:")
    
    # Lista de diseños con descripciones
    diseños_info = [
        ('azul_amarillo_bold', '💙💛 Azul Amarillo Bold', 'Corporativo atrevido con azul marino y amarillo'),
        ('verde_minimalista', '💚 Verde Minimalista', 'Limpio y ecológico con líneas verdes'),
        ('negro_naranja', '🖤🧡 Negro Naranja', 'Industrial moderno con barra lateral naranja'),
        ('azul_rosa_isometrico', '💙💗 Azul Rosa Isométrico', 'Diseño 3D con perspectiva isométrica'),
        ('marron_simple', '🟤 Marrón Simple', 'Profesional y elegante en tonos tierra'),
        ('negro_rojo', '🖤❤️ Negro Rojo', 'Potente y dinámico con franja roja'),
        ('blanco_naranja_clean', '🤍🧡 Blanco Naranja Clean', 'Minimalista limpio con detalles naranjas'),
        ('blanco_negro_simple', '⬜⬛ Blanco Negro Simple', 'Elegancia atemporal monocromática'),
        ('morado_minimalista', '💜 Morado Minimalista', 'Sofisticado con degradado morado'),
        ('negro_amarillo_industrial', '🖤💛 Negro Amarillo Industrial', 'Estilo construcción con rayas de precaución'),
        ('barra_lateral_naranja', '🟠 Barra Lateral Naranja', 'Sidebar naranja con footer oscuro'),
        ('diagonal_moderno', '📐 Diagonal Moderno', 'Diseño diagonal negro y amarillo'),
        ('franja_superior_roja', '🔴 Franja Superior Roja', 'Banda roja superior llamativa'),
        ('geometrico_purpura', '🟣 Geométrico Púrpura', 'Formas geométricas modernas moradas'),
        ('azul_corporativo', '🔵 Azul Corporativo', 'Profesional con elementos isométricos azules'),
        ('verde_ecologico', '🟢 Verde Ecológico', 'Diseño sustentable verde limpio'),
        ('gris_elegante', '⚫ Gris Elegante', 'Sofisticación en blanco y negro'),
        ('terracota_profesional', '🟤 Terracota Profesional', 'Tonos tierra profesionales')
    ]
    
    # Mostrar diseños en grid de 3 columnas
    num_cols = 3
    for i in range(0, len(diseños_info), num_cols):
        cols = st.columns(num_cols)
        
        for j in range(num_cols):
            idx = i + j
            if idx < len(diseños_info):
                estilo_id, nombre, descripcion = diseños_info[idx]
                
                with cols[j]:
                    st.markdown(f"""
                    <div style='padding: 15px; border: 2px solid #ddd; border-radius: 10px; 
                                background: white; height: 100%; text-align: center;'>
                        <h4 style='color: #1E88E5; margin-bottom: 10px;'>{nombre}</h4>
                        <p style='font-size: 12px; color: #666; margin-bottom: 15px;'>{descripcion}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if st.button("✅ Seleccionar", key=f"diseño_{estilo_id}", use_container_width=True):
                        st.session_state.diseño_seleccionado = estilo_id
                        st.session_state.paso = 3
                        st.success(f"✅ Diseño seleccionado: {nombre}")
                        st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)


def mostrar_paso_3_contenido():
    """Paso 3: Ingresar contenido y generar PDF"""
    st.markdown('<div class="main-header"><h1>✍️ Paso 3: Ingresa el Contenido</h1></div>', 
                unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col2:
    with col2:
        logo_html = ""
        if st.session_state.logo_seleccionado:
            buffered = BytesIO()
            st.session_state.logo_seleccionado.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            logo_html = f'<div style="margin: 10px 0;"><img src="data:image/png;base64,{img_str}" width="150"></div>'

        st.markdown(f"""
        <div class="info-box">
            <p><strong>Resumen:</strong></p>
            <p><strong>Empresa:</strong> {st.session_state.empresa_seleccionada['nombre']}</p>
            {logo_html}
            <p><strong>Diseño:</strong> {st.session_state.diseño_seleccionado.title()}</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("⬅️ Cambiar Diseño", use_container_width=True):
            st.session_state.paso = 2
            st.rerun()
    
    with col1:
        st.subheader("Escribe el contenido de tu carta:")
        
        # Texto de ejemplo
        ejemplo = """A quien corresponda:

Por medio de la presente, hago constar que la empresa ha mantenido un desempeño ejemplar en materia de responsabilidad ambiental.

A lo largo de nuestra relación profesional, hemos podido observar un compromiso constante con la calidad y la excelencia.

Atentamente,
[Tu Nombre]
[Tu Cargo]"""
        
        contenido = st.text_area(
            "Contenido de la carta:",
            value=st.session_state.contenido_texto or ejemplo,
            height=400,
            help="Escribe el contenido completo de tu carta. Incluye el nombre del firmante al final."
        )
        
        st.session_state.contenido_texto = contenido
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            if st.button("👁️ Vista Previa", type="secondary", use_container_width=True):
                with st.spinner("📄 Generando vista previa..."):
                    try:
                        # Convertir logo a base64
                        logo_base64 = imagen_a_base64(st.session_state.logo_seleccionado)
                        
                        # Generar HTML
                        html = HojaMembretadaDesigner.generar_diseño(
                            st.session_state.diseño_seleccionado,
                            st.session_state.empresa_seleccionada,
                            logo_base64,
                            contenido
                        )
                        
                        # Mostrar preview HTML
                        st.markdown("---")
                        st.subheader("📄 Vista Previa de tu Hoja Membretada")
                        st.components.v1.html(html, height=800, scrolling=True)
                        
                    except Exception as e:
                        st.error(f"❌ Error generando vista previa: {str(e)}")
        
        with col_b:
            if st.button("📥 Descargar PDF", type="primary", use_container_width=True):
                generar_y_descargar_pdf(contenido)


def generar_y_descargar_pdf(contenido):
    """Genera el PDF final y permite descargarlo"""
    with st.spinner("📄 Generando tu hoja membretada..."):
        try:
            # Convertir logo a base64
            logo_base64 = imagen_a_base64(st.session_state.logo_seleccionado)
            
            # Generar HTML
            html = HojaMembretadaDesigner.generar_diseño(
                st.session_state.diseño_seleccionado,
                st.session_state.empresa_seleccionada,
                logo_base64,
                contenido
            )
            
            # Generar PDF
            pdf_bytes = PDFGenerator.html_to_pdf(html)
            
            if pdf_bytes:
                # Nombre del archivo
                nombre_archivo = f"{st.session_state.empresa_seleccionada['nombre'].replace(' ', '_')}_membrete.pdf"
                
                st.success("✅ ¡PDF generado exitosamente!")
                
                # Botón de descarga
                st.download_button(
                    label="📥 Descargar PDF",
                    data=pdf_bytes,
                    file_name=nombre_archivo,
                    mime="application/pdf",
                    type="primary",
                    use_container_width=True
                )
            else:
                st.error("❌ Error al generar el PDF")
                
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.info("Verifica que todas las dependencias estén instaladas correctamente.")


def main():
    """Función principal de la aplicación"""
    # Inicializar estado
    inicializar_session_state()
    
    # Sidebar
    with st.sidebar:
        st.image("constructor_ai_logo.png", width=200)
        st.title("Generador de Hojas Membretadas")
        st.markdown("---")
        
        st.write("**Progreso:**")
        pasos = [
            ("1️⃣ Generar Logo", 1),
            ("2️⃣ Diseño de Hoja", 2),
            ("3️⃣ Contenido y PDF", 3)
        ]
        
        for nombre, numero in pasos:
            if st.session_state.paso > numero:
                st.success(f"✅ {nombre}")
            elif st.session_state.paso == numero:
                st.info(f"▶️ {nombre}")
            else:
                st.write(f"⚪ {nombre}")
        
        st.markdown("---")
        
        # Botón de reinicio
        if st.button("🔄 Comenzar de Nuevo", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
        
        st.markdown("---")
        st.caption("🏗️ Powered by Google Gemini AI")
    
    # Contenido principal según el paso
    if st.session_state.paso == 1:
        mostrar_paso_1_generacion_logos()
    elif st.session_state.paso == 2:
        mostrar_paso_2_diseño_hoja()
    elif st.session_state.paso == 3:
        mostrar_paso_3_contenido()


if __name__ == "__main__":
    main()
