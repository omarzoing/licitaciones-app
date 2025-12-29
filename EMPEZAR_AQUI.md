# 🚀 EMPEZAR EN 3 PASOS

## Paso 1: Instalar (2 minutos)

Abre una terminal en esta carpeta y ejecuta:

```bash
./install.sh
```

Si tienes problemas, ejecuta manualmente:

```bash
pip install -r requirements.txt
```

---

## Paso 2: Configurar API Key (1 minuto)

1. **Obtén tu API Key gratis:**
   - Ve a: https://makersuite.google.com/app/apikey
   - Inicia sesión con tu cuenta de Google
   - Haz clic en "Create API Key"
   - Copia la key

2. **Configura el archivo `.env`:**
   - Abre el archivo `.env` en esta carpeta
   - Pega tu API key:
   ```
   GOOGLE_API_KEY=tu_api_key_aqui
   ```
   - Guarda el archivo

---

## Paso 3: Ejecutar (30 segundos)

```bash
streamlit run app.py
```

¡La aplicación se abrirá automáticamente en tu navegador! 🎉

---

## ¿Cómo Usar?

1. **Genera logos** → Haz clic en "Generar 5 Opciones"
2. **Selecciona** → Elige el logo que más te guste
3. **Diseño** → Selecciona estilo (Minimalista, Tradicional, Moderno)
4. **Contenido** → Escribe tu texto
5. **Descarga** → ¡Listo tu PDF!

---

## ❌ ¿Problemas?

### "No module named 'streamlit'"
```bash
pip install -r requirements.txt
```

### "No module named 'weasyprint'"
```bash
# macOS
brew install cairo pango gdk-pixbuf libffi
pip install weasyprint
```

### "API key not found"
Verifica que el archivo `.env` tiene tu API key correcta.

---

## 📚 Más Información

- **Guía rápida:** `INICIO_RAPIDO.md`
- **Guía completa:** `GUIA_CONFIGURACION.md`
- **Preguntas:** `FAQ.md`
- **Ejemplos de texto:** `EJEMPLOS_CONTENIDO.md`

---

## 🌐 Subir a Internet (Opcional)

Para que funcione 24/7 sin tu computadora:

1. **Sube a GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/TU_USUARIO/hojas-membretadas.git
   git push -u origin main
   ```

2. **Deploy en Streamlit Cloud:**
   - Ve a: https://streamlit.io/cloud
   - Conecta tu repositorio
   - Añade tu API key en Secrets:
   ```
   GOOGLE_API_KEY = "tu_api_key"
   ```
   - ¡Deploy!

**Guía completa:** `GUIA_CONFIGURACION.md`

---

## ✅ Verificar Instalación

Ejecuta el script de pruebas:

```bash
python test_sistema.py
```

Si ves todos los ✅, ¡está listo!

---

## 🎯 ¿Qué Hace Esta App?

- 🏗️ Genera nombres de constructoras automáticamente
- 🎨 Crea logos profesionales con IA
- 📄 Diseña hojas membretadas elegantes
- 📍 Usa datos realistas de Guadalajara, Jalisco
- 💾 Exporta a PDF de alta calidad
- 🆓 ¡Completamente gratis!

---

## 📞 ¿Necesitas Ayuda?

1. Lee el `FAQ.md`
2. Ejecuta `python test_sistema.py`
3. Revisa los ejemplos en `EJEMPLOS_CONTENIDO.md`

---

**¡Listo! Ahora ejecuta:**

```bash
streamlit run app.py
```

**¡Y empieza a crear hojas membretadas profesionales! 🏗️✨**
