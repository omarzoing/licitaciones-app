# 🏗️ Guía Completa de Configuración y Deployment

## 📋 Requisitos Previos

1. **Python 3.10 o superior** instalado
2. **Cuenta de GitHub** (para deployment)
3. **API Key de Google Gemini** (para generación con IA)

## 🔧 Paso 1: Configuración Local

### 1.1 Instalar Dependencias

Abre una terminal en la carpeta del proyecto y ejecuta:

```bash
pip install -r requirements.txt
```

**Nota sobre WeasyPrint en macOS:**
WeasyPrint requiere algunas dependencias del sistema. Si tienes problemas, instala:

```bash
brew install python3 cairo pango gdk-pixbuf libffi
```

### 1.2 Obtener API Key de Google Gemini

1. Ve a [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Inicia sesión con tu cuenta de Google (la que tiene Gemini Premium)
3. Haz clic en "Create API Key"
4. Copia la API key generada

### 1.3 Configurar Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto:

```bash
cp .env.example .env
```

Edita el archivo `.env` y añade tu API key:

```
GOOGLE_API_KEY=tu_api_key_aqui
```

**⚠️ IMPORTANTE:** Nunca subas el archivo `.env` a GitHub. Ya está en `.gitignore`.

### 1.4 Probar Localmente

Ejecuta la aplicación:

```bash
streamlit run app.py
```

La aplicación se abrirá en tu navegador en `http://localhost:8501`

## 🚀 Paso 2: Deployment en Streamlit Cloud

### 2.1 Preparar Repositorio de GitHub

1. **Inicializa Git** (si no lo has hecho):
```bash
git init
git add .
git commit -m "Initial commit: Generador de hojas membretadas"
```

2. **Crea un repositorio en GitHub:**
   - Ve a [github.com](https://github.com)
   - Haz clic en "New repository"
   - Nombre: `generador-hojas-membretadas`
   - Descripción: "Generador automático de hojas membretadas para constructoras"
   - **NO** marques "Initialize with README" (ya tienes uno)
   - Haz clic en "Create repository"

3. **Sube tu código a GitHub:**
```bash
git remote add origin https://github.com/TU_USUARIO/generador-hojas-membretadas.git
git branch -M main
git push -u origin main
```

### 2.2 Deploy en Streamlit Cloud

1. **Ve a [Streamlit Cloud](https://streamlit.io/cloud)**

2. **Inicia sesión** con tu cuenta de GitHub

3. **Haz clic en "New app"**

4. **Configura el deployment:**
   - **Repository:** Selecciona `generador-hojas-membretadas`
   - **Branch:** `main`
   - **Main file path:** `app.py`
   - **App URL:** Elige un nombre único (ej: `tu-usuario-hojas-membretadas`)

5. **Configura los Secrets (MUY IMPORTANTE):**
   - Antes de hacer clic en "Deploy", expande "Advanced settings"
   - En la sección "Secrets", pega esto:
   
   ```toml
   GOOGLE_API_KEY = "tu_api_key_de_google_gemini_aqui"
   ```
   
   - Reemplaza `tu_api_key_de_google_gemini_aqui` con tu API key real

6. **Haz clic en "Deploy"**

7. **Espera** unos 2-5 minutos mientras se instalan las dependencias y se despliega la app

8. **¡Listo!** Tu app estará disponible en una URL como:
   ```
   https://tu-usuario-hojas-membretadas.streamlit.app
   ```

### 2.3 Compartir con Otra Persona

Una vez deployada, simplemente comparte la URL. La app funcionará 24/7 sin necesidad de que tu computadora esté encendida.

**Límites del plan gratuito de Streamlit Cloud:**
- 1 app privada (solo tú puedes acceder)
- Apps públicas ilimitadas (cualquiera con el link puede acceder)
- Límites de recursos (suficiente para 1-2 hojas por semana)

## 🔐 Paso 3: Configurar Secrets (Explicación Detallada)

### ¿Qué son los Secrets?

Los "secrets" son variables de entorno seguras donde guardas información sensible como API keys. **NUNCA** debes subir tus API keys directamente en el código a GitHub.

### Cómo funcionan los Secrets en Streamlit Cloud:

1. **En desarrollo local:** Usa el archivo `.env` (Git lo ignora automáticamente)
2. **En producción (Streamlit Cloud):** Configura los secrets en la interfaz web

### Actualizar Secrets después del deployment:

1. Ve a tu app en Streamlit Cloud
2. Haz clic en "Settings" (⚙️)
3. Selecciona "Secrets" en el menú lateral
4. Edita el contenido del archivo `secrets.toml`
5. Guarda los cambios
6. La app se reiniciará automáticamente

## 🛠️ Paso 4: Mantenimiento y Actualizaciones

### Actualizar la App

Cada vez que hagas cambios en el código:

```bash
git add .
git commit -m "Descripción de los cambios"
git push
```

Streamlit Cloud detectará los cambios automáticamente y redesplegará la app.

### Ver Logs

Si algo falla, puedes ver los logs:
1. Ve a tu app en Streamlit Cloud
2. Haz clic en "Manage app"
3. Selecciona "Logs" para ver errores

## ❓ Solución de Problemas

### Error: "No module named 'weasyprint'"

**Causa:** WeasyPrint requiere dependencias del sistema.

**Solución en Streamlit Cloud:**
Crea un archivo `packages.txt` en la raíz:

```
libcairo2
libpango-1.0-0
libpangocairo-1.0-0
```

### Error: "API key not found"

**Causa:** No configuraste los secrets correctamente.

**Solución:**
1. Verifica que el nombre sea exactamente `GOOGLE_API_KEY`
2. Verifica que no haya espacios extra
3. Reinicia la app

### Error: "Rate limit exceeded"

**Causa:** Has excedido el límite de la API gratuita de Google Gemini.

**Solución:**
- Espera unas horas
- Considera actualizar a un plan de pago de Google AI
- Reduce la cantidad de logos generados a la vez

### La app está muy lenta

**Causa:** Generación de logos con IA puede tardar.

**Solución:**
- Genera solo 3 logos en vez de 5
- Usa cacheo de Streamlit (`@st.cache_data`)
- Considera usar APIs más rápidas

## 📊 Límites y Costos

### Google Gemini API (Gemini Pro):
- **Gratis:** 60 requests por minuto
- **Tu uso estimado:** 1-2 hojas por semana = ~10-20 requests/semana
- **Conclusión:** ✅ Plan gratuito es suficiente

### Streamlit Cloud (Free Tier):
- **Recursos:** 1 GB RAM
- **Uptime:** 24/7
- **Apps:** 1 privada + ilimitadas públicas
- **Tu uso:** ✅ Suficiente

### Total de costos: **$0 USD/mes** ✅

## 🎨 Personalización

### Cambiar colores

Edita `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#TU_COLOR_AQUI"
```

### Añadir más estilos de hojas

Edita `hoja_membretada_designer.py` y añade un nuevo método:

```python
@staticmethod
def diseño_personalizado(empresa, logo_base64, contenido):
    # Tu diseño aquí
    pass
```

## 📞 Soporte

Si tienes problemas:
1. Revisa los logs en Streamlit Cloud
2. Verifica que todos los secrets estén configurados
3. Asegúrate de que las dependencias estén instaladas

## 🎉 ¡Listo!

Tu aplicación está lista para usarse. Simplemente:
1. Abre la URL de tu app
2. Genera logos
3. Selecciona el que te guste
4. Elige el diseño de hoja
5. Escribe tu contenido
6. Descarga el PDF

**¡Disfruta tu generador automático de hojas membretadas! 🏗️✨**
