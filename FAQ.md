# ❓ Preguntas Frecuentes (FAQ)

## General

### ¿Qué hace esta aplicación?
Genera automáticamente hojas membretadas profesionales para empresas constructoras usando Inteligencia Artificial. Crea logos, genera datos realistas de empresas en Guadalajara, y produce PDFs de alta calidad listos para imprimir.

### ¿Es gratis?
Sí, completamente gratis si usas la API gratuita de Google Gemini y el tier gratuito de Streamlit Cloud. Los únicos costos potenciales son si excedes los límites gratuitos de las APIs.

### ¿Puedo usar las hojas membretadas comercialmente?
Sí, los documentos generados son para tu uso personal o comercial. Sin embargo, verifica los términos de servicio de Google Gemini para uso comercial de contenido generado por IA.

---

## Instalación

### ¿Qué necesito instalar?
- Python 3.10 o superior
- Dependencias de Python (automático con `pip install -r requirements.txt`)
- Dependencias del sistema para WeasyPrint (cairo, pango, etc.)

### ¿Cómo instalo en macOS?
```bash
# Instalar Homebrew si no lo tienes
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Ejecutar el instalador automático
./install.sh
```

### ¿Cómo instalo en Windows?
Windows requiere pasos adicionales para WeasyPrint. Recomendamos usar WSL (Windows Subsystem for Linux) o deployar directamente en Streamlit Cloud.

### Error: "command not found: streamlit"
```bash
# Instala streamlit
pip install streamlit

# O reinstala todas las dependencias
pip install -r requirements.txt
```

---

## API Keys

### ¿Dónde consigo la API key de Google Gemini?
1. Ve a https://makersuite.google.com/app/apikey
2. Inicia sesión con tu cuenta de Google
3. Haz clic en "Create API Key"
4. Copia la key y pégala en tu archivo `.env`

### ¿Mi suscripción de ChatGPT Plus me da acceso a la API?
No. ChatGPT Plus ($20/mes) es solo para la interfaz web. La API de OpenAI es un servicio separado con precios por uso.

### ¿La API de Google Gemini es gratuita?
Sí, Gemini Pro tiene un tier gratuito generoso:
- 60 requests por minuto
- 1,500 requests por día
- Gratis hasta cierto límite mensual

Para 1-2 hojas por semana, el tier gratuito es más que suficiente.

### ¿Puedo usar mi propia API key de OpenAI?
Sí, puedes modificar el código para usar OpenAI DALL-E. Edita `logo_image_generator.py` y configura el servicio a "dalle".

---

## Uso de la Aplicación

### ¿Cuánto tarda en generar los logos?
Aproximadamente 20-40 segundos para generar 5 opciones. La IA necesita tiempo para analizar tendencias y crear diseños profesionales.

### ¿Puedo usar mis propios logos?
Actualmente la app genera logos automáticamente. Para usar logos propios, necesitarías modificar el código. Esto está en el roadmap para futuras versiones.

### ¿Puedo editar el texto después de generarlo?
Sí, puedes editar el contenido en el Paso 3 tantas veces como quieras antes de descargar el PDF.

### ¿Los datos de las empresas son reales?
No, todos los datos (nombres, direcciones, teléfonos, RFC) son ficticios pero realistas. Están diseñados para parecer profesionales y están basados en ubicaciones reales de Guadalajara.

### ¿Puedo cambiar la ciudad de Guadalajara a otra?
Sí, puedes editar `empresa_generator.py` y modificar las listas de `CALLES` y `COLONIAS` con ubicaciones de tu ciudad preferida.

---

## Diseños

### ¿Cuántos estilos de diseño hay?
Tres estilos principales:
1. **Minimalista**: Limpio, moderno, líneas simples
2. **Tradicional**: Elegante, clásico, con detalles ornamentales
3. **Moderno**: Dinámico, con gradientes y elementos gráficos

### ¿Puedo crear mis propios diseños?
Sí, puedes añadir nuevos estilos editando `hoja_membretada_designer.py`. Solo necesitas crear un nuevo método con tu diseño HTML/CSS.

### ¿Se ajusta automáticamente a múltiples páginas?
Sí, WeasyPrint maneja automáticamente el contenido que excede una página y crea múltiples páginas si es necesario.

---

## PDFs

### ¿Qué tamaño tiene el PDF?
Tamaño carta estándar (8.5" x 11") compatible con impresoras normales.

### ¿Puedo cambiar a tamaño A4?
Sí, edita `hoja_membretada_designer.py` y cambia:
```css
@page {
    size: letter;  /* Cambia a 'A4' */
}
```

### ¿Qué calidad tiene el PDF?
Alta calidad, apto para impresión profesional. Los PDFs son vectoriales donde es posible, asegurando nitidez en cualquier tamaño.

---

## Deployment

### ¿Puedo usar la app sin internet?
Necesitas internet para:
- Generar logos con la API de Google Gemini
- Buscar tendencias de diseño

Pero una vez generado, el PDF se crea localmente.

### ¿Cómo comparto la app con mi equipo?
La mejor opción es deployar en Streamlit Cloud (gratis). Todos podrán acceder desde cualquier dispositivo con la URL.

### ¿La app funciona en móviles?
Sí, la interfaz de Streamlit es responsive y funciona en móviles, pero recomendamos usar desktop para una mejor experiencia.

### ¿Puedo deployar en mi propio servidor?
Sí, puedes deployar en cualquier servidor que soporte Python y Streamlit. Opciones:
- Streamlit Cloud (gratis, recomendado)
- Heroku
- AWS
- Google Cloud
- Tu propio servidor VPS

---

## Problemas Comunes

### Error: "No module named 'weasyprint'"
WeasyPrint requiere dependencias del sistema:

**macOS:**
```bash
brew install cairo pango gdk-pixbuf libffi
pip install weasyprint
```

**Ubuntu/Debian:**
```bash
sudo apt-get install libcairo2 libpango-1.0-0 libgdk-pixbuf2.0-0
pip install weasyprint
```

### Error: "API key not found"
Verifica que:
1. Tienes un archivo `.env` en la raíz del proyecto
2. El archivo contiene: `GOOGLE_API_KEY=tu_api_key_aqui`
3. La API key es válida (sin espacios extra)

### Error: "Rate limit exceeded"
Has excedido el límite de la API gratuita. Soluciones:
- Espera unos minutos
- Genera menos logos a la vez (3 en vez de 5)
- Considera actualizar a un plan de pago

### Los logos no se ven profesionales
La calidad depende de la API usada:
- **Google Gemini + Imagen API**: Calidad profesional
- **Placeholder (sin API)**: Solo para pruebas

Asegúrate de tener configurada una API key válida.

### El texto se sale de la página
El sistema debería ajustar automáticamente. Si no lo hace:
1. Reduce el tamaño del texto
2. Usa párrafos más cortos
3. Verifica que WeasyPrint esté instalado correctamente

---

## Personalización

### ¿Puedo cambiar los colores del diseño?
Sí, edita `.streamlit/config.toml` para colores de la interfaz, o `hoja_membretada_designer.py` para colores de las hojas membretadas.

### ¿Puedo añadir mi logo corporativo?
Sí, requiere modificar el código. En una futura versión se podrá hacer desde la interfaz.

### ¿Puedo cambiar las fuentes?
Sí, edita los estilos CSS en `hoja_membretada_designer.py`:
```css
font-family: 'Tu Fuente', 'Arial', sans-serif;
```

---

## Costos

### ¿Cuánto cuesta usar la app?
- **Desarrollo local**: Gratis
- **Google Gemini API (tier gratuito)**: Gratis hasta 1,500 requests/día
- **Streamlit Cloud (tier gratuito)**: Gratis
- **Total para uso moderado**: $0/mes ✅

### ¿Cuándo necesitaría pagar?
Solo si:
- Generas más de 1,500 documentos por día (excede tier gratuito de Gemini)
- Quieres más recursos en Streamlit Cloud
- Decides usar APIs premium (OpenAI DALL-E, etc.)

---

## Seguridad

### ¿Es seguro usar mi API key?
Sí, si sigues las buenas prácticas:
- ✅ Nunca subas tu `.env` a GitHub (ya está en `.gitignore`)
- ✅ Usa Streamlit Secrets para deployment
- ✅ No compartas tu API key públicamente
- ✅ Regenera tu API key si crees que fue comprometida

### ¿Los datos generados se guardan?
No, la aplicación no guarda ningún dato. Todo se genera en tiempo real y se descarta después de descargar el PDF.

---

## Soporte

### ¿Dónde reporto bugs?
Abre un issue en el repositorio de GitHub o contacta al desarrollador.

### ¿Puedo contribuir al proyecto?
¡Sí! El proyecto es open source. Pull requests son bienvenidos.

### ¿Hay un roadmap de futuras funcionalidades?
Funcionalidades planeadas:
- [ ] Subir logos personalizados
- [ ] Más estilos de diseño
- [ ] Plantillas predefinidas
- [ ] Guardar borradores
- [ ] Exportar en otros formatos (Word, PNG)
- [ ] Soporte multiidioma
- [ ] Editor visual de diseños

---

## ¿Más preguntas?

Revisa la documentación completa en:
- `README.md` - Visión general
- `INICIO_RAPIDO.md` - Guía de inicio
- `GUIA_CONFIGURACION.md` - Configuración detallada

O ejecuta el script de pruebas para diagnóstico:
```bash
python test_sistema.py
```
