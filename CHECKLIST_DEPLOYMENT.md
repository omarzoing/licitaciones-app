# ✅ Checklist de Deployment

Usa esta lista para verificar que todo está configurado correctamente antes de deployar.

## 📋 Pre-Deployment (Desarrollo Local)

### Instalación y Configuración

- [ ] Python 3.10+ instalado
  ```bash
  python3 --version
  ```

- [ ] Dependencias de Python instaladas
  ```bash
  pip install -r requirements.txt
  ```

- [ ] Dependencias del sistema instaladas (macOS)
  ```bash
  brew install cairo pango gdk-pixbuf libffi
  ```

- [ ] Archivo `.env` creado y configurado
  ```bash
  # Debe contener:
  GOOGLE_API_KEY=tu_api_key_aqui
  ```

- [ ] API Key de Google Gemini obtenida
  - Ir a: https://makersuite.google.com/app/apikey
  - Crear API key
  - Copiar y pegar en `.env`

### Testing

- [ ] Script de pruebas ejecutado exitosamente
  ```bash
  python test_sistema.py
  # Debe mostrar: ✅ TODO FUNCIONA CORRECTAMENTE!
  ```

- [ ] App ejecutada localmente sin errores
  ```bash
  streamlit run app.py
  # Debe abrir en http://localhost:8501
  ```

- [ ] Generación de empresas funciona
  - Genera 5 opciones de empresas
  - Verifica que se muestran correctamente

- [ ] Selección de logo funciona
  - Selecciona un logo
  - Verifica que pasa al paso 2

- [ ] Diseños de hojas funcionan
  - Prueba los 3 estilos (minimalista, tradicional, moderno)
  - Verifica que se visualizan correctamente

- [ ] Generación de PDF funciona
  - Ingresa contenido de prueba
  - Descarga el PDF
  - Abre y verifica que se ve bien

### Control de Versiones

- [ ] Git inicializado
  ```bash
  git init
  ```

- [ ] Archivo `.gitignore` configurado
  ```bash
  # Debe incluir:
  # .env
  # .streamlit/secrets.toml
  # __pycache__/
  # *.pyc
  ```

- [ ] Verificar que `.env` NO está en Git
  ```bash
  git status
  # NO debe aparecer .env en la lista
  ```

- [ ] Primer commit realizado
  ```bash
  git add .
  git commit -m "Initial commit: Generador de hojas membretadas"
  ```

---

## 🚀 Deployment en Streamlit Cloud

### Preparación de GitHub

- [ ] Repositorio creado en GitHub
  - Ir a: https://github.com/new
  - Nombre: `generador-hojas-membretadas`
  - Visibilidad: Privado (recomendado)

- [ ] Código subido a GitHub
  ```bash
  git remote add origin https://github.com/TU_USUARIO/generador-hojas-membretadas.git
  git branch -M main
  git push -u origin main
  ```

- [ ] Verificar que `.env` NO está en GitHub
  - Ve al repositorio en GitHub
  - Confirma que NO ves el archivo `.env`

### Configuración en Streamlit Cloud

- [ ] Cuenta de Streamlit Cloud creada
  - Ir a: https://streamlit.io/cloud
  - Iniciar sesión con GitHub

- [ ] Nueva app creada
  - Click en "New app"
  - Seleccionar repositorio
  - Branch: `main`
  - Main file: `app.py`

- [ ] Secrets configurados
  - Expandir "Advanced settings"
  - En "Secrets", pegar:
  ```toml
  GOOGLE_API_KEY = "tu_api_key_real_aqui"
  ```
  - **IMPORTANTE:** Usar tu API key real, no el placeholder

- [ ] App deployada
  - Click en "Deploy"
  - Esperar 2-5 minutos

### Verificación Post-Deployment

- [ ] App se carga sin errores
  - Abrir la URL de tu app
  - Verificar que no hay errores en pantalla

- [ ] Generación de logos funciona en producción
  - Generar 5 opciones
  - Verificar que se generan correctamente

- [ ] Flujo completo funciona
  - Generar logos → Seleccionar → Diseño → Contenido → PDF
  - Descargar PDF y verificar

- [ ] Logs revisados
  - En Streamlit Cloud: App → Manage app → Logs
  - Verificar que no hay errores críticos

---

## 🔐 Seguridad

### Variables de Entorno

- [ ] API key NO está hardcodeada en el código
  ```python
  # ❌ MAL
  api_key = "sk-..."
  
  # ✅ BIEN
  api_key = os.getenv("GOOGLE_API_KEY")
  ```

- [ ] Archivo `.env` en `.gitignore`
  ```bash
  cat .gitignore | grep .env
  # Debe mostrar: .env
  ```

- [ ] Secrets configurados en Streamlit Cloud
  - Verificar en App settings → Secrets

### Control de Acceso

- [ ] Decidir visibilidad de la app
  - [ ] Pública (cualquiera con el link)
  - [ ] Privada (solo usuarios autorizados)
  - Configurar en Streamlit Cloud → App settings

---

## 📊 Monitoreo

### Después del Deployment

- [ ] URL de la app guardada
  ```
  https://TU_USUARIO-hojas-membretadas.streamlit.app
  ```

- [ ] URL compartida con usuarios
  - Enviar por email
  - Documentar en Wiki/Notion/Confluence

- [ ] Límites de API monitoreados
  - Revisar uso en Google AI Studio
  - Configurar alertas si es necesario

- [ ] Feedback de usuarios recopilado
  - ¿La app funciona bien?
  - ¿Hay errores?
  - ¿Necesita mejoras?

---

## 🔄 Actualizaciones Futuras

### Proceso de Actualización

- [ ] Cambios realizados localmente
  ```bash
  # Hacer cambios en el código
  # Probar localmente
  streamlit run app.py
  ```

- [ ] Cambios testeados
  ```bash
  python test_sistema.py
  ```

- [ ] Cambios commiteados
  ```bash
  git add .
  git commit -m "Descripción de los cambios"
  ```

- [ ] Cambios pusheados
  ```bash
  git push
  ```

- [ ] App redesplegada automáticamente
  - Streamlit Cloud detecta los cambios
  - Redespliega automáticamente
  - Verificar que funciona

---

## 🆘 Troubleshooting Checklist

Si algo no funciona, verifica:

### Error: "No module named..."

- [ ] `requirements.txt` tiene todas las dependencias
- [ ] `packages.txt` tiene dependencias del sistema
- [ ] Reiniciar la app en Streamlit Cloud

### Error: "API key not found"

- [ ] Secrets están configurados en Streamlit Cloud
- [ ] Nombre es exactamente `GOOGLE_API_KEY`
- [ ] No hay espacios extra en el secret
- [ ] App reiniciada después de añadir secrets

### Error: "Rate limit exceeded"

- [ ] Esperado - límite de API alcanzado
- [ ] Esperar unos minutos
- [ ] Reducir cantidad de generaciones
- [ ] Considerar plan de pago

### App muy lenta

- [ ] Normal para generación de IA (20-30 segundos)
- [ ] Reducir cantidad de logos generados (3 en vez de 5)
- [ ] Verificar que no hay loops infinitos en el código

### PDF no se genera

- [ ] `packages.txt` configurado correctamente
- [ ] Revisar logs en Streamlit Cloud
- [ ] Verificar que WeasyPrint se instaló
- [ ] Reiniciar app

---

## 📝 Documentación

- [ ] README.md actualizado
- [ ] INICIO_RAPIDO.md revisado
- [ ] GUIA_CONFIGURACION.md completa
- [ ] FAQ.md con preguntas comunes
- [ ] EJEMPLOS_CONTENIDO.md disponible

---

## 🎉 ¡Listo para Producción!

Si todos los checks están ✅, tu app está lista para usarse en producción.

**URL de tu app:** _______________________________________

**Fecha de deployment:** _______________________________________

**Notas adicionales:**
_______________________________________________
_______________________________________________
_______________________________________________

---

## 📞 Soporte

Si necesitas ayuda:

1. ✅ Revisa esta checklist completamente
2. ✅ Consulta FAQ.md
3. ✅ Revisa logs en Streamlit Cloud
4. ✅ Ejecuta `python test_sistema.py`
5. ✅ Verifica que API key es válida

**¡Éxito con tu deployment! 🚀**
