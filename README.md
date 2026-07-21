README.md actualizado con toda la estructura de archivos completa, incluyendo las páginas de comunas y las nuevas funcionalidades:

markdown
# Destapes Santiago 24H - Landing Page

Landing page profesional para servicio de destape de cañerías urgente en Santiago, Chile. Diseño moderno, responsive y optimizado para conversión (llamadas y WhatsApp).

## 🚀 Características

- Diseño 100% responsive (mobile first)
- Header sticky con navegación suave por secciones
- Botones destacados de llamada y WhatsApp (con números +56 9 6357 1251 y +56 9 7209 1242)
- Secciones: Hero, Problemas, Servicios, Cómo funciona, Beneficios, Testimonios, Cobertura, CTA final y Footer
- Animaciones CSS suaves (entradas, hovers, flotantes)
- Imágenes reales del servicio (técnico, camioneta, trabajos)
- Optimizado para SEO y Google My Business
- Código separado en HTML, CSS y JS para fácil mantenimiento
- **Banner flotante de oferta con botón de cierre (X)** que aparece al hacer scroll
- **Enlaces automáticos a WhatsApp con mensaje personalizado según la comuna**
- **Páginas individuales para 6 comunas de Santiago**

## 📁 Estructura de archivos
/
├── index.html # Página principal
├── styles.css # Estilos globales
├── script.js # Funcionalidades JavaScript
├── comunas/
│ ├── maipu.html # Página de Maipú
│ ├── providencia.html # Página de Providencia
│ ├── san-miguel.html # Página de San Miguel
│ ├── santiago-centro.html # Página de Santiago Centro
│ ├── las-dehesa.html # Página de La Dehesa
│ └── nunoa.html # Página de Ñuñoa
└── README.md # Este archivo

text

## 🗺️ Páginas de comunas

Cada comuna tiene su propia página optimizada con:

- **SEO local**: títulos, meta descripciones y keywords específicas
- **Contenido personalizado**: barrios, sectores y referencias locales
- **Testimonios de vecinos de la comuna**
- **Cobertura detallada** con nombres de sectores específicos
- **Tiempo de respuesta unificado**: 60 minutos en todas las comunas
- **Enlaces cruzados** entre todas las comunas en el footer

### Lista de comunas disponibles:

| Comuna | Archivo | Enlace |
|--------|---------|--------|
| Maipú | `maipu.html` | `/comunas/maipu.html` |
| Providencia | `providencia.html` | `/comunas/providencia.html` |
| San Miguel | `san-miguel.html` | `/comunas/san-miguel.html` |
| Santiago Centro | `santiago-centro.html` | `/comunas/santiago-centro.html` |
| La Dehesa | `las-dehesa.html` | `/comunas/las-dehesa.html` |
| Ñuñoa | `nunoa.html` | `/comunas/nunoa.html` |

## 🎨 Funcionalidades JavaScript

- **Animación de aparición** al hacer scroll (fade-in)
- **Smooth scroll** para navegación por anclas
- **Banner flotante de oferta** con botón de cierre (X) que se muestra al hacer scroll
- **Persistencia local** del banner cerrado en la misma sesión
- **Detección automática de comuna** para personalizar mensajes de WhatsApp
- **Actualización dinámica** de enlaces de WhatsApp con mensaje personalizado
- **Lazy loading** de imágenes con fade-in
- **Menú activo** que resalta la sección visible
- **Tracking de eventos** para Meta Pixel (Facebook Ads)
- **Efectos hover** en imágenes y tarjetas

## 📞 Números de contacto

| Servicio | Número |
|----------|--------|
| Llamadas | `+56 9 6357 1251` |
| WhatsApp | `+56 9 7209 1242` |

## 🔧 Tecnologías utilizadas

- HTML5
- CSS3 (Flexbox, Grid, Animaciones, Variables CSS)
- JavaScript (Vanilla, Intersection Observer)
- Meta Pixel (Facebook Ads)
- Google Fonts (Inter)

## 🌐 SEO y Meta tags

- Meta description optimizada por comuna
- Meta keywords relevantes para destapes
- Open Graph tags para compartir en redes sociales
- Twitter Card para mejor visualización
- URLs canónicas en cada página
- Estructura semántica HTML5

## 📱 Responsive

El sitio está optimizado para:

- 📱 Móviles (320px - 768px)
- 📟 Tablets (768px - 1024px)
- 💻 Escritorio (1024px+)

## 🔄 Enlaces entre comunas

Todas las páginas incluyen enlaces cruzados en el footer para mejorar la navegación y el SEO:
Otras comunas: Maipú | Providencia | San Miguel | Santiago Centro | La Dehesa | Ñuñoa

text

## 🎯 Conversión

Elementos optimizados para conversión:

- Botones flotantes de WhatsApp y llamada
- Banner de oferta temporal
- CTA en todas las secciones
- Badges de confianza y garantía
- Testimonios reales de clientes
- Tiempo de respuesta garantizado

## 📦 Instalación

1. Clona o descarga los archivos
2. Sube todos los archivos a tu servidor web
3. Asegúrate de mantener la estructura de carpetas:
   - `index.html` en la raíz
   - `styles.css` y `script.js` en la raíz
   - Carpeta `/comunas/` con todas las páginas de comunas
4. Configura los números de teléfono en los enlaces si es necesario
5. Configura el ID de Meta Pixel en `fbq('init', 'TU_ID')`

## 📝 Personalización

### Cambiar números de teléfono
Busca en todos los archivos HTML:
- `tel:+56963571251`
- `wa.me/56972091242`

### Cambiar Meta Pixel ID
En todos los archivos HTML, busca:
```javascript
fbq('init', '1647071222974255');
Cambia el ID por el tuyo.

Ajustar tiempo de respuesta
Busca en cada página:

60 minutos (todas las páginas están unificadas)

📄 Licencia
Todos los derechos reservados. © 2026 Destapes Santiago 24H

Desarrollado para servicios de destape urgente en Santiago, Región Metropolitana.

text

---

## ✅ **Principales actualizaciones del README:**

| Sección | Actualización |
|---------|---------------|
| **Características** | Añadido banner con X, enlaces automáticos a WhatsApp, páginas de comunas |
| **Estructura de archivos** | Lista completa de los 6 archivos de comunas |
| **Páginas de comunas** | Nueva sección detallando cada comuna y su archivo |
| **Funcionalidades JS** | Lista completa de todas las funciones del script |
| **Números de contacto** | Tabla con ambos números (llamada y WhatsApp) |
| **Enlaces entre comunas** | Ejemplo de enlaces cruzados en footer |
| **Conversión** | Añadidos elementos de conversión |
| **Instalación** | Instrucciones actualizadas con estructura de carpetas |
| **Personalización** | Guía para cambiar números y Meta Pixel ID |
