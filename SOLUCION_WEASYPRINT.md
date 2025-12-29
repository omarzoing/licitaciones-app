# ⚠️ Solución para Error de WeasyPrint (libgobject)

## 🔍 Problema

```
OSError: cannot load library 'libgobject-2.0-0'
```

Este error ocurre porque Python no encuentra las librerías de Homebrew.

---

## ✅ Solución (Ya aplicada)

Ya he instalado las dependencias necesarias (`pango`, `cairo`, `glib`, etc.) usando Homebrew.
Ahora, para que Python las encuentre, DEBES usar el script de inicio proporcionado.

## 🚀 Cómo Iniciar la App

Simplemente ejecuta:

```bash
./iniciar_streamlit.sh
```

Esto:
1. ✅ Configura las rutas de librerías automáticamente
2. ✅ Activa el entorno virtual
3. ✅ Inicia Streamlit

---

## 🔧 Solución Manual (Si el script no funciona)

### Opción 1: Exportar variables cada vez

Ejecuta esto ANTES de `streamlit run app.py`:

```bash
export DYLD_LIBRARY_PATH="/opt/homebrew/lib:${DYLD_LIBRARY_PATH}"
export PKG_CONFIG_PATH="/opt/homebrew/lib/pkgconfig"
```

Luego:
```bash
source venv/bin/activate
streamlit run app.py
```

### Opción 2: Añadir al .zshrc (Permanente)

Añade estas líneas a tu `~/.zshrc`:

```bash
echo 'export DYLD_LIBRARY_PATH="/opt/homebrew/lib:${DYLD_LIBRARY_PATH}"' >> ~/.zshrc
echo 'export PKG_CONFIG_PATH="/opt/homebrew/lib/pkgconfig"' >> ~/.zshrc
source ~/.zshrc
```

Luego ejecuta normalmente:
```bash
streamlit run app.py
```

---

## 🎯 Solución Alternativa: Ignorar PDF por Ahora

Si solo quieres probar la generación de logos y no te importa el PDF por ahora:

### 1. Comentar la importación en app.py

Línea 19 de `app.py`:
```python
# from pdf_generator import PDFGenerator  # Comentado temporalmente
```

### 2. Comentar el uso en la función `generar_y_descargar_pdf`

Líneas 375-376:
```python
# pdf_bytes = PDFGenerator.html_to_pdf(html)  # Comentado
pdf_bytes = None  # Temporalmente deshabilitado
```

### 3. Ejecutar normalmente

```bash
streamlit run app.py
```

**Esto te permite:**
- ✅ Generar empresas
- ✅ Generar logos con IA
- ✅ Seleccionar logos
- ✅ Diseñar hojas
- ✅ Ver vista previa HTML
- ❌ NO descargar PDF (pero puedes copiar el HTML)

---

## 💡 ¿Qué Opción Usar?

### Si quieres probar AHORA los logos con IA:
**→ Solución Alternativa** (comentar PDF temporalmente)

### Si quieres el sistema completo con PDF:
**→ Solución Rápida** (usar `./iniciar_streamlit.sh`)

### Si ninguna funciona:
**→ Solución Manual Opción 2** (añadir a .zshrc)

---

## 🧪 Verificar que Funciona

Después de aplicar la solución, prueba:

```bash
python3 -c "from weasyprint import HTML; print('✅ WeasyPrint funciona')"
```

Si no da error, ¡está funcionando!

---

## 📋 Resumen de Comandos

### Para probar logos SIN PDF (más rápido):
```bash
# 1. Comentar línea 19 en app.py:
#    # from pdf_generator import PDFGenerator

# 2. Ejecutar
streamlit run app.py
```

### Para usar TODO el sistema:
```bash
# Opción A: Con el script
./iniciar_streamlit.sh

# Opción B: Manual
export DYLD_LIBRARY_PATH="/opt/homebrew/lib:${DYLD_LIBRARY_PATH}"
streamlit run app.py
```

---

## ✨ Recomendación

Te sugiero empezar con la **Solución Alternativa** (sin PDF) para que veas tu sistema de logos con IA funcionando YA.

Luego, cuando tengas tiempo, arreglas el PDF con una de las soluciones permanentes.

---

**¿Qué opción quieres probar?** 😊
