# 🚀 Inicio Rápido - Generador de Hojas Membretadas

## ⚡ Empezar en 5 Minutos

### Paso 1: Instalar Dependencias (2 minutos)

```bash
# Instalar dependencias de Python
pip install -r requirements.txt

# En macOS, si tienes problemas con WeasyPrint:
brew install python3 cairo pango gdk-pixbuf libffi
```

### Paso 2: Configurar API Key (1 minuto)

1. **Obtén tu API Key de Google Gemini:**
   - Ve a https://makersuite.google.com/app/apikey
   - Inicia sesión y crea una API key
   - Copia la key

2. **Configura el archivo `.env`:**

```bash
# Copia el ejemplo
cp .env.example .env

# Edita .env y pega tu API key
GOOGLE_API_KEY=tu_api_key_aqui
```

### Paso 3: Probar el Sistema (1 minuto)

```bash
# Ejecuta el script de prueba
python test_sistema.py
```

Deberías ver todos los checks ✅ en verde.

### Paso 4: Ejecutar la App (1 minuto)

```bash
streamlit run app.py
```

¡La aplicación se abrirá automáticamente en tu navegador! 🎉

---

## 📱 Usar la Aplicación

### Flujo de Trabajo:

1. **Generar Logos** 🎨
   - Haz clic en "Generar 5 Opciones de Logos"
   - Espera ~30 segundos mientras se generan
   - Revisa las opciones

2. **Seleccionar Logo** ✅
   - Haz clic en el botón "Seleccionar" del logo que te guste
   - Si no te convencen, genera nuevas opciones

3. **Elegir Diseño de Hoja** 📄
   - Elige entre Minimalista, Tradicional o Moderno
   - Puedes cambiar de diseño sin perder el logo

4. **Escribir Contenido** ✍️
   - Escribe o pega el texto de tu carta
   - Incluye el nombre del firmante al final

5. **Descargar PDF** 💾
   - Haz clic en "Descargar PDF"
   - Tu hoja membretada está lista

---

## 🌐 Deploy en Internet (Opcional)

### Opción A: Streamlit Cloud (Gratis, Recomendado)

1. **Sube a GitHub:**
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/TU_USUARIO/hojas-membretadas.git
git push -u origin main
```

2. **Deploy en Streamlit Cloud:**
   - Ve a https://streamlit.io/cloud
   - Conecta tu repo de GitHub
   - Configura los Secrets con tu `GOOGLE_API_KEY`
   - ¡Deploy!

**Sigue la guía completa en:** `GUIA_CONFIGURACION.md`

---

## 🛠️ Solución Rápida de Problemas

### ❌ "No module named 'streamlit'"
```bash
pip install -r requirements.txt
```

### ❌ "No module named 'weasyprint'"
```bash
# macOS
brew install cairo pango gdk-pixbuf libffi
pip install weasyprint

# Ubuntu/Debian
sudo apt-get install libpango-1.0-0 libpangoft2-1.0-0
pip install weasyprint
```

### ❌ "API key not found"
```bash
# Verifica que el archivo .env existe y tiene tu API key
cat .env

# Debe mostrar:
# GOOGLE_API_KEY=tu_api_key_aqui
```

### ⚠️ La generación de logos es lenta
- Es normal, la IA tarda ~20-30 segundos
- Reduce el número de logos generados a 3

### ⚠️ Error "Rate limit exceeded"
- Has excedido el límite de la API gratuita
- Espera unos minutos y vuelve a intentar

---

## 📁 Estructura del Proyecto

```
LICITACIONES/
├── app.py                          # Aplicación principal de Streamlit
├── empresa_generator.py            # Genera datos de empresas
├── logo_generator.py               # Genera conceptos de logos con IA
├── logo_image_generator.py         # Genera imágenes de logos
├── hoja_membretada_designer.py     # Diseños de hojas HTML/CSS
├── pdf_generator.py                # Convierte HTML a PDF
├── test_sistema.py                 # Script de pruebas
├── requirements.txt                # Dependencias Python
├── packages.txt                    # Dependencias del sistema (Streamlit Cloud)
├── .env                            # Variables de entorno (NO subir a Git)
├── .env.example                    # Ejemplo de .env
├── .gitignore                      # Archivos ignorados por Git
├── README.md                       # Documentación principal
├── GUIA_CONFIGURACION.md           # Guía completa de setup
├── INICIO_RAPIDO.md                # Esta guía
└── .streamlit/
    ├── config.toml                 # Configuración de Streamlit
    └── secrets.toml.example        # Ejemplo de secrets
```

---

## 🎯 Características del Sistema

✅ **Generación Automática:**
- Nombres de constructoras realistas
- Direcciones de Guadalajara, Jalisco
- Teléfonos en formato mexicano
- Emails corporativos
- RFC con formato válido
- Años de fundación 2000-2019

✅ **Diseños Profesionales:**
- Minimalista: Limpio y moderno
- Tradicional: Elegante y clásico
- Moderno: Dinámico y vanguardista

✅ **Calidad PDF:**
- Tamaño carta (8.5" x 11")
- Márgenes profesionales
- Ajuste automático de texto
- Alta resolución

✅ **Interfaz Intuitiva:**
- Flujo paso a paso
- Vista previa en tiempo real
- Fácil de usar

---

## 💡 Consejos de Uso

1. **Para logos más profesionales:** Describe bien lo que quieres en el prompt
2. **Para contenido largo:** Usa párrafos cortos y claros
3. **Para mejor diseño:** Revisa los 3 estilos antes de decidir
4. **Para compartir:** Deploy en Streamlit Cloud y comparte la URL

---

## 📞 Necesitas Ayuda?

1. **Revisa la documentación:** `GUIA_CONFIGURACION.md`
2. **Ejecuta las pruebas:** `python test_sistema.py`
3. **Verifica logs:** En Streamlit Cloud → App → Logs

---

## 🎉 ¡Ya Estás Listo!

Ejecuta:
```bash
streamlit run app.py
```

Y empieza a crear hojas membretadas profesionales en minutos. 🏗️✨

---

**Creado con ❤️ usando:**
- 🤖 Google Gemini AI
- 🎨 Streamlit
- 📄 WeasyPrint
- 🐍 Python
