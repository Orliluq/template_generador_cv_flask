# 🔎 Informe de Auditoría Lighthouse – Aplicación Web Generadora de CV

**📅 Fecha:** abril de 2025  
**🛠 Herramienta:** Google Lighthouse v12.4.0  
**🖥 Dispositivo:** Escritorio (emulado)  
**🌐 Navegador:** Chromium 135.0.0.0 con DevTools  
**🔄 Sesión:** Carga inicial de página, sesión de una sola página  
**🚦 Limitación de red personalizada:** Activada  

## 📊 Puntajes Generales

| Categoría            | Puntaje |
|----------------------|---------|
| **Rendimiento**      | 91      |
| **Accesibilidad**    | 96      |
| **Buenas Prácticas** | 100     |
| **SEO**              | 93      |

---

## 🚀 Métricas de Rendimiento

| Métrica                            | Valor   |
|------------------------------------|---------|
| 🖼 First Contentful Paint (FCP)    | 0.6 s   |
| 🖼 Largest Contentful Paint (LCP)  | 0.6 s   |
| ⏱ Tiempo Total de Bloqueo (TBT)   | 210 ms  |
| 📐 Cumulative Layout Shift (CLS)  | 0       |
| ⚡ Índice de Velocidad (SI)       | 0.7 s   |

> 📌 Estos valores son estimados y pueden variar. El puntaje de rendimiento se calcula en base a estas métricas. [Ver calculadora de puntuación](https://web.dev/performance-scoring/)

---

## 🛠️ Diagnóstico y Recomendaciones de Rendimiento

| Problema identificado                                       | Ahorro potencial  |
|-------------------------------------------------------------|-------------------|
| 🚫 Eliminar recursos que bloquean el renderizado            | 270 ms            |
| 📉 Minificar CSS                                            | 3 KiB             |
| 📉 Minificar JavaScript                                     | 64 KiB            |
| 🔄 Habilitar compresión de texto                            | 9 KiB             |
| 📦 Evitar JS heredado en navegadores modernos               | 9 KiB             |
| 🧹 Reducir CSS no utilizado                                 | 50 KiB            |
| 🧹 Reducir JS no utilizado                                  | 716 KiB           |
| 🧵 Evitar tareas largas en el hilo principal                | 4 tareas largas   |
| 🔗 Evitar cadenas críticas de solicitudes                   | 2 cadenas         |

---

## ♿ Accesibilidad

- **Puntaje:** 96  
- **Problema identificado:**
  - 🔄 Enlaces sin nombre discernible: se recomienda mejorar la semántica para tecnología asistiva.
  - ✅ Auditorías automáticas aprobadas: 10
  - 🧪 Elementos para revisión manual: 10
  - 🚫 No aplicables: 46

---

## ✅ Buenas Prácticas

- **Puntaje:** 100  
- 🔐 Seguridad:
  - Política de seguridad de contenido (CSP) contra XSS
  - Política HSTS fuerte
  - Aislamiento de origen (COOP)
  - Protección contra clickjacking (XFO o CSP)
- 📝 Sin errores críticos en consola
- ✅ Auditorías aprobadas: 13
- 🚫 No aplicables: 3

---

## 🔍 SEO

- **Puntaje:** 93  
- 📈 Mejores prácticas de optimización para motores de búsqueda aplicadas.
- ⚠️ **Observación:**
- ✅ Datos estructurados válidos
- ✅ Auditorías aprobadas: 7
- 🚫 No aplicables: 3