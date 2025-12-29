# 🏗️ Generador de Hojas Membretadas para Constructoras

> Aplicación web en Streamlit que genera automáticamente logos profesionales de constructoras y hojas membretadas personalizadas usando Google Gemini AI.

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.29+-red.svg)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## ✨ Características Principales

- 🏗️ **Generación automática de empresas constructoras** con nombres realistas
- 🎨 **Creación de logos profesionales** usando IA (Google Gemini)
- 📄 **3 estilos de diseño** (minimalista, tradicional, moderno)
- 📍 **Datos realistas** de Guadalajara, Jalisco, México
- 📱 **Generación automática** de teléfonos, emails, RFC válidos
- 📝 **Ajuste inteligente de texto** respetando márgenes y saltos de página
- 💾 **Exportación a PDF** de alta calidad (tamaño carta)
- 🌐 **Deploy gratuito** en Streamlit Cloud
- 🎯 **Interfaz intuitiva** con flujo paso a paso

## 🎥 Demo

![Demo](https://via.placeholder.com/800x450/667eea/ffffff?text=Demo+Screenshot)

**Ejemplo de uso:**
1. Genera 5 opciones de logos con un clic
2. Selecciona tu favorito
3. Elige el estilo de diseño
4. Escribe tu contenido
5. Descarga el PDF listo para imprimir

## 🚀 Inicio Rápido

### Instalación Automática (Recomendado)

```bash
# Clonar o descargar el repositorio
cd LICITACIONES

# Ejecutar instalador automático
./install.sh
```

### Instalación Manual

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Configurar API key
cp .env.example .env
# Edita .env y añade tu GOOGLE_API_KEY

# 3. Ejecutar la app
streamlit run app.py
```

**📚 Documentación detallada:** Ver [INICIO_RAPIDO.md](INICIO_RAPIDO.md)

## 📋 Requisitos

- Python 3.10 o superior
- API Key de Google Gemini (gratis)
- Dependencias del sistema para WeasyPrint:
  - **macOS:** `brew install cairo pango gdk-pixbuf libffi`
  - **Linux:** `apt-get install libcairo2 libpango-1.0-0`

## 🎨 Características Detalladas

### Generación Automática de Empresas

El sistema genera datos completamente realistas:
- **Nombres:** "Constructora Atlas", "Edificaciones Minerva", etc.
- **Direcciones:** Ubicaciones reales de Guadalajara (Av. López Mateos, Providencia, etc.)
- **Teléfonos:** Formato mexicano válido (33-XXXX-XXXX)
- **Emails:** Corporativos (@nombreempresa.com.mx)
- **RFC:** Formato válido mexicano
- **Año fundación:** Entre 2000-2019

### Diseños de Hojas Membretadas

**1. Minimalista** ✨
- Diseño limpio y moderno
- Líneas simples
- Ideal para empresas tech-forward

**2. Tradicional** 🏛️
- Elegante y clásico
- Detalles ornamentales
- Perfecto para empresas establecidas

**3. Moderno** 🚀
- Dinámico y vanguardista
- Gradientes y elementos gráficos
- Para empresas innovadoras

### Generación de Logos con IA

- **Análisis de tendencias:** Estudia logos de constructoras exitosas
- **Múltiples opciones:** Genera 5 conceptos diferentes a la vez
- **Estilos variados:** Desde minimalista hasta elaborado
- **Elementos profesionales:** Formas geométricas, colores corporativos, tipografías claras

## 🌐 Deployment en Streamlit Cloud

### Opción 1: Deployment Gratuito (Recomendado)

```bash
# 1. Sube a GitHub
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/TU_USUARIO/hojas-membretadas.git
git push -u origin main

# 2. Conecta en Streamlit Cloud
# Ve a: https://streamlit.io/cloud
# Selecciona tu repo y configura los Secrets
```

**Configuración de Secrets:**
```toml
GOOGLE_API_KEY = "tu_api_key_aqui"
```

**📚 Guía completa:** Ver [GUIA_CONFIGURACION.md](GUIA_CONFIGURACION.md)

### Opción 2: Deployment Local

```bash
streamlit run app.py
```

La app se abrirá en `http://localhost:8501`

## 📖 Documentación

- 📘 [**INICIO_RAPIDO.md**](INICIO_RAPIDO.md) - Empezar en 5 minutos
- 📗 [**GUIA_CONFIGURACION.md**](GUIA_CONFIGURACION.md) - Configuración detallada y deployment
- 📕 [**FAQ.md**](FAQ.md) - Preguntas frecuentes

## 🛠️ Tecnologías Utilizadas

| Tecnología | Uso | Versión |
|------------|-----|---------|
| [Python](https://python.org) | Lenguaje base | 3.10+ |
| [Streamlit](https://streamlit.io) | Framework web | 1.29+ |
| [Google Gemini AI](https://ai.google.dev) | Generación de contenido IA | Latest |
| [WeasyPrint](https://weasyprint.org) | Generación de PDFs | 60.1+ |
| [Pillow](https://python-pillow.org) | Procesamiento de imágenes | 10.1+ |

## 📁 Estructura del Proyecto

```
LICITACIONES/
├── 📱 app.py                          # Aplicación principal Streamlit
├── 🏢 empresa_generator.py            # Generador de datos de empresas
├── 🎨 logo_generator.py               # Generador de conceptos de logos (IA)
├── 🖼️ logo_image_generator.py         # Generador de imágenes de logos
├── 📄 hoja_membretada_designer.py     # Sistema de diseños HTML/CSS
├── 📋 pdf_generator.py                # Convertidor HTML → PDF
├── 🧪 test_sistema.py                 # Suite de pruebas
├── ⚙️ install.sh                      # Instalador automático
├── 📦 requirements.txt                # Dependencias Python
├── 📦 packages.txt                    # Dependencias sistema (Streamlit Cloud)
├── 🔐 .env                            # Variables de entorno (local)
├── 📝 README.md                       # Este archivo
├── 📚 INICIO_RAPIDO.md                # Guía de inicio
├── 📚 GUIA_CONFIGURACION.md           # Guía completa
├── ❓ FAQ.md                          # Preguntas frecuentes
└── .streamlit/
    └── config.toml                    # Configuración de Streamlit
```

## 🎯 Casos de Uso

✅ **Empresas constructoras** que necesitan papelería corporativa
✅ **Freelancers** que ofrecen diseño de identidad corporativa
✅ **Startups** que necesitan branding rápido y profesional
✅ **Desarrolladores** que quieren aprender sobre IA generativa
✅ **Estudiantes** de diseño o desarrollo web

## 💡 Ejemplos de Uso

### Ejemplo 1: Carta de Recomendación

```
A quien corresponda:

Por medio de la presente, hago constar que [EMPRESA] ha mantenido
un desempeño ejemplar en todos sus proyectos de construcción...

Atentamente,
[Tu Nombre]
[Tu Cargo]
```

### Ejemplo 2: Cotización

```
Estimado Cliente:

Nos complace presentar nuestra cotización para el proyecto de
construcción solicitado...

[Detalles del proyecto]

Cordialmente,
[Tu Nombre]
[Tu Cargo]
```

## 🔧 Configuración Avanzada

### Personalizar Colores

Edita `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#TU_COLOR"
backgroundColor = "#ffffff"
```

### Añadir Nuevo Estilo de Diseño

Edita `hoja_membretada_designer.py`:
```python
@staticmethod
def diseño_personalizado(empresa, logo_base64, contenido):
    css = """
    /* Tu CSS aquí */
    """
    html = f"""
    <!-- Tu HTML aquí -->
    """
    return html
```

### Cambiar Ciudad

Edita `empresa_generator.py`:
```python
CALLES = [
    "Tu Calle 1", "Tu Calle 2", ...
]
COLONIAS = [
    "Tu Colonia 1", "Tu Colonia 2", ...
]
```

## 🧪 Testing

Ejecuta la suite de pruebas:
```bash
python test_sistema.py
```

Debería mostrar:
```
✅ PASS - Imports de dependencias
✅ PASS - Módulos propios
✅ PASS - Generador de empresas
✅ PASS - API Key
✅ PASS - Diseños de hojas
```

## 📊 Límites y Costos

### Google Gemini API (Tier Gratuito)
- ✅ **60 requests/minuto**
- ✅ **1,500 requests/día**
- ✅ **Gratis hasta límites**

### Streamlit Cloud (Tier Gratuito)
- ✅ **1 GB RAM**
- ✅ **Uptime 24/7**
- ✅ **Apps ilimitadas**

### Uso Estimado
- **1-2 hojas/semana:** ✅ 100% Gratis
- **10-20 hojas/semana:** ✅ 100% Gratis
- **100+ hojas/día:** ⚠️ Podrías necesitar plan de pago

**Costo total para uso moderado: $0/mes** 🎉
