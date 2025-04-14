# 🚀 Template Generador de CV en Flask
Este proyecto es una aplicación web construida con Flask que permite generar un CV dinámico en formatos DOCX y PDF. El CV incluye información personal, experiencia profesional, habilidades, proyectos, y más. Los usuarios pueden descargar el archivo generado directamente desde la interfaz web.

## 🛠️ Características del Proyecto
- ✨ Generación dinámica de CV en formatos DOCX y PDF.
- 🌟 Estilo personalizado para el contenido del CV (secciones, viñetas, encabezados, etc.).
- 📂 Conversión automática de documentos DOCX a PDF.
- 🌐 Interfaz de usuario minimalista creada con HTML, CSS y Flask.
- 📝 Contenido del CV altamente personalizable en el código fuente.
- 🖥️ Rutas adicionales para "Política de privacidad" y "Términos de uso".

## 📖 Requisitos previos
Antes de comenzar, asegúrate de que tu sistema cumpla con los siguientes requisitos:

1. Python 3.8 o superior instalado. Puedes verificar tu versión de Python con:
```
python.exe -m pip install --upgrade pip
python --version
```
2. Pip instalado para manejar las dependencias de Python.
3. Virtualenv (opcional, pero recomendado para aislar las dependencias del proyecto).
4. Microsoft Word o un visor de documentos DOCX para abrir el archivo generado.

## 💾 Instalación
Sigue estos pasos para configurar el proyecto:

1. Clona el repositorio del proyecto 📦:
```
git clone https://github.com/tuusuario/nombre-del-repo.git
cd nombre-del-repo
```
2. Crea un entorno virtual (opcional):
```
python -m venv venv
source venv/bin/activate  # En Linux/Mac
venv\Scripts\activate     # En Windows
```
3. Instala las dependencias del proyecto ⚙️:
```
pip install -r requirements.txt
```

4. Crea la estructura de carpetas necesarias: Si no existen, asegúrate de que las carpetas `src/static` y `src/templates` estén creadas.
5. Asegúrate de tener las siguientes herramientas instaladas:
- docx2pdf: Para convertir archivos DOCX a PDF.

Si no están instaladas, puedes hacerlo con:
```
pip install docx2pdf 
pip install flask
```
1. Configura las rutas necesarias:
Verifica que `generate_cv` crea y guarda los archivos DOCX y PDF en `src/static`.

## 🧩 Uso
1. Inicia el servidor Flask ▶️:
```
python main.py
```
2. Abre tu navegador y accede a la URL ✅:
```
http://127.0.0.1:5000/
```
3. Usa los enlaces en la interfaz para descargar tu CV en formato DOCX.

4. Si deseas probar el formato PDF, puedes modificar la ruta en el archivo principal (como se describe más adelante).

## 🗂️ Estructura del Proyecto
```
├── static/                       # Archivos estáticos públicos accesibles desde el navegador
│   ├── css/                      # Estilos globales adicionales (no procesados por Tailwind)
│   ├── js/                       # Scripts de JavaScript personalizados
│   ├── favicon.png              # Ícono de la página (favicon)
│   └── dist/
│       └── output.css           # Archivo CSS compilado por Tailwind (minificado para producción)

├── src/
│   ├── app/
│   │   ├── __init__.py          # Punto de inicio para inicializar la app Flask (create_app)
│   │   ├── routes.py            # Define las rutas y vistas principales de la aplicación
│   │   ├── utils.py             # Funciones auxiliares, como generación de archivos DOCX/PDF
│   ├── input.css                # Entrada personalizada para compilar Tailwind CSS
│   └── templates/               # Plantillas HTML renderizadas por Flask (Jinja2)

├── tests/
│   ├── test_routes.py           # Pruebas unitarias para las rutas HTTP de la aplicación
│   └── test_utils.py            # Pruebas para funciones auxiliares (como generación de CV)

├── requirements.txt             # Lista de dependencias del proyecto para instalación con pip
├── devserver.sh                 # Script de ayuda para levantar el servidor en desarrollo (opcional)
├── tailwind.config.js           # Configuración de Tailwind CSS (paths, colores, etc.)
├── postcss.config.js            # Configuración de PostCSS (usado junto con Tailwind)
├── LICENSE                      # Licencia de uso del proyecto
├── README.md                    # Documentación principal del proyecto
├── main.py                      # Archivo principal que inicia la app Flask (usado por Gunicorn)
├── Procfile                     # Comando de inicio usado por plataformas como Render
```

## 🔄 Rutas Principales
- `/`: Página principal que muestra la interfaz.
- `/tmp`: Genera y descarga el archivo DOCX del CV.
- `/politica-de-privacidad`: Página con la política de privacidad.
- `/terminos-de-uso`: Página con los términos de uso.

## 🆕 Dependencias
A continuación, se listan las principales dependencias utilizadas en este proyecto:
- Flask: Framework principal para la aplicación web.
- python-docx: Generación del documento DOCX.
- docx2pdf: Conversión de DOCX a PDF.

## 💡 Personalización
Si deseas personalizar el contenido del CV:
1. Abre el archivo `utils.py`.
2. Modifica las secciones de habilidades, experiencia, proyectos, etc., según tus necesidades.
3. Guarda los cambios y reinicia el servidor Flask.

[Ejemplo](CV.pdf)

## 🧪 Pruebas del Proyecto

Este directorio contiene los tests automatizados del generador de CV.

### Estructura

- `test_routes.py`: Verifica el comportamiento de las rutas Flask.
- `test_utils.py`: Prueba funciones utilitarias como generación de PDFs y DOCXs.

### Ejecutar las pruebas

```
pytest
```

## 📊 Optimización para ATS (Applicant Tracking System)

Este CV ha sido diseñado para pasar los filtros ATS, lo que mejora significativamente las posibilidades de ser considerado en el proceso de selección. A continuación se detallan las razones por las cuales este CV está optimizado para sistemas ATS:

- **Formato Estructurado**: Utiliza un formato claro y bien organizado, con encabezados que facilitan la lectura por parte de los sistemas automáticos.
- **Palabras Clave Relevantes**: El contenido incluye palabras clave específicas relacionadas con el puesto y la industria, lo que asegura que el CV sea detectado y clasificado correctamente.
- **Compatibilidad con Formatos Comunes**: El CV se genera en formatos estándar como Word (.docx) y PDF, que son ampliamente compatibles con la mayoría de los sistemas ATS.
- **Datos Claros y Accesibles**: Las secciones están bien separadas, y la información es fácil de extraer para los sistemas ATS, lo que mejora la puntuación en los filtros.

Con estas características, este CV tiene un alto nivel de compatibilidad con las herramientas automatizadas de reclutamiento y aumenta las probabilidades de superar la primera fase de selección.

## Próximos Pasos: [VER](Métricas_del_proyecto.md)
- **Optimización de JavaScript y CSS:** Reducir el código no utilizado y las dependencias de terceros podría mejorar significativamente la puntuación de rendimiento.

- **Mejorar la accesibilidad:** Hacer los controles más accesibles para los usuarios con discapacidades.

- **Ajustes en SEO:** Validar con herramientas externas para mejorar el SEO general.

# 🤝 Contribución
¡Aceptamos contribuciones! 💡 Por favor, abre un *pull request* o reporta un error 🐛.
Si deseas contribuir al proyecto:
- Realiza un fork del repositorio.
- Crea una nueva rama para tus cambios:
```
git checkout -b feature-nueva-funcionalidad
```
- Realiza un pull request con tus cambios.

# 📜 Licencia
Este proyecto está bajo la licencia MIT.
