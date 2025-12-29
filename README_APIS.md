# 🎨 Configuración de APIs para Logos con IA

## Problema Actual
Los logos se están generando con **código** (Pillow) en lugar de IA, lo que resulta en diseños básicos y poco profesionales.

## Soluciones Disponibles

### ✅ OPCIÓN 1: Usar tu API de ChatGPT (DALL-E) - RECOMENDADO
Esta es la mejor opción para logos **PROFESIONALES Y REALES**.

#### Pasos:

1. **Obtén tu API Key de OpenAI:**
   - Ve a: https://platform.openai.com/api-keys
   - Inicia sesión con tu cuenta de ChatGPT
   - Haz clic en "Create new secret key"
   - Copia la key (empieza con `sk-...`)

2. **Configura la API Key:**
   
   Abre el archivo `api_config.py` y modifica estas líneas:
   ```python
   # Línea 15 - Pega tu API key aquí
   OPENAI_API_KEY = 'sk-tu-api-key-completa-aqui'
   
   # Línea 16 - Cambia a True
   USE_DALLE = True
   
   # Línea 10 - Cambia a False
   USE_GEMINI = False
   ```

3. **Instala la librería de OpenAI:**
   ```bash
   source venv/bin/activate
   pip install openai
   ```

4. **Reinicia la aplicación:**
   ```bash
   ./run.sh
   ```

5. **¡Listo!** Ahora los logos se generarán con DALL-E (IA de ChatGPT).

**NOTA:** DALL-E es de pago. Cada imagen cuesta aproximadamente $0.02 USD.
           Verifica que tengas créditos en tu cuenta de OpenAI.

---

### 📦 OPCIÓN 2: Usar Gemini (Google) - GRATIS
Ya está configurada, pero tiene límites mensuales gratuitos.

- **Ventajas:** Gratis, ya configurada
- **Desventajas:** No genera imágenes, solo texto para diseños

---

### 🖼️ OPCIÓN 3: Subir tus propios logos manualmente

Si prefieres usar logos que tú diseñes o descargues:

1. Crea una carpeta `logos_personalizados/` en el proyecto
2. Guarda tus logos en formato PNG (800x400 px recomendado)
3. Nombra los archivos: `logo_1.png`, `logo_2.png`, etc.
4. Modifica `app.py` línea 120 para cargar desde esa carpeta

---

## 🔍 Verificar Estado de APIs

Cuando inicies la aplicación, verás uno de estos mensajes:

- ✅ **"DALL-E (ChatGPT) configurado"** → Logos con IA funcionando
- ℹ️ **"Usando Gemini AI"** → Solo texto, logos gráficos
- ⚠️ **"No hay APIs configuradas"** → Solo logos gráficos básicos

---

## 💡 Recomendación Final

**Para logos PROFESIONALES y REALES:**
→ Usa tu API de ChatGPT (DALL-E) siguiendo la Opción 1

**Para ahorrar dinero:**
→ Diseña 10-15 logos profesionales en Canva o similar
→ Guárdalos y cárgalos manualmente (Opción 3)

**Para rapidez sin costo:**
→ Mantén Gemini + logos gráficos mejorados (Opción 2)

---

## 🆘 Problemas Comunes

### "Error: API key inválida"
- Verifica que copiaste la key completa (empieza con `sk-`)
- Asegúrate de tener créditos en tu cuenta de OpenAI

### "Error: Insufficient quota"
- Tu cuenta de OpenAI no tiene créditos
- Agrega fondos en: https://platform.openai.com/account/billing

### "Logos siguen siendo gráficos"
- Verifica que `USE_DALLE = True` en `api_config.py`
- Reinicia la aplicación completamente
- Revisa los mensajes de estado al inicio

---

## 📞 Contacto
Si tienes problemas, revisa el archivo `api_config.py` - tiene comentarios detallados.
