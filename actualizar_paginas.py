import os
import re

CARPETA_COMUNAS = "comunas"

# ============================================================
# 1. CONFIGURACIÓN: Panel de enlaces legales
# ============================================================

NUEVO_PANEL = '''      <div class="footer-panel coverage-panel">
        <h4>Enlaces legales</h4>
        <ul style="list-style:none;padding:0;margin:0;display:grid;gap:12px;">
          <li><a href="/politica-de-privacidad.html" style="color:#0f172a;text-decoration:none;font-weight:600;">🔒 Política de Privacidad</a></li>
          <li><a href="/terminos-y-condiciones.html" style="color:#0f172a;text-decoration:none;font-weight:600;">📋 Términos y Condiciones</a></li>
          <li><a href="/index.html" style="color:#0f172a;text-decoration:none;font-weight:600;">🏠 Inicio</a></li>
        </ul>
      </div>'''

NUEVO_FOOTER = '''    <div class="container footer-bottom">
      <span>© 2026 Destapes Santiago 24H. Todos los derechos reservados.</span>
      <div class="footer-legal-links">
        <a href="/politica-de-privacidad.html">🔒 Política de Privacidad</a>
        <a href="/terminos-y-condiciones.html">📋 Términos de Servicio</a>
      </div>
    </div>'''


# ============================================================
# 2. FUNCIÓN: Leer archivos con diferentes codificaciones
# ============================================================

def leer_con_codificacion_fallback(ruta):
    """Intenta leer el archivo con diferentes codificaciones"""
    codificaciones = ['utf-8', 'windows-1252', 'latin-1', 'iso-8859-1', 'cp1252']
    
    for cod in codificaciones:
        try:
            with open(ruta, 'r', encoding=cod) as f:
                contenido = f.read()
                return contenido, cod
        except UnicodeDecodeError:
            continue
    
    # Último recurso: leer como bytes y reemplazar errores
    with open(ruta, 'rb') as f:
        raw = f.read()
        contenido = raw.decode('utf-8', errors='replace')
        return contenido, 'utf-8 (con reemplazo)'


# ============================================================
# 3. FUNCIÓN: Actualizar páginas de comunas (footer + caracteres)
# ============================================================

def actualizar_archivo(ruta):
    try:
        contenido, cod_usada = leer_con_codificacion_fallback(ruta)
        
        # Saltar si ya está actualizado
        if 'Enlaces legales' in contenido and '/politica-de-privacidad.html' in contenido:
            print(f"⏭️  {ruta} ya está actualizado")
            return False
        
        # Reemplazar panel de comunas por enlaces legales
        contenido = re.sub(
            r'<div class="footer-panel coverage-panel">.*?</div>\s*</div>\s*</div>\s*<div class="container footer-bottom">',
            NUEVO_PANEL + '\n\n    <div class="container footer-bottom">',
            contenido,
            flags=re.DOTALL
        )
        
        # Reemplazar footer-bottom
        contenido = re.sub(
            r'<div class="container footer-bottom">.*?</div>\s*</footer>',
            NUEVO_FOOTER + '\n  </footer>',
            contenido,
            flags=re.DOTALL
        )
        
        # CORREGIR CARACTERES RAROS
        contenido = contenido.replace('�', '')
        contenido = contenido.replace('??', '')
        contenido = contenido.replace('��', '')
        contenido = contenido.replace('?', '')
        
        # Guardar en UTF-8
        with open(ruta, 'w', encoding='utf-8') as f:
            f.write(contenido)
        
        print(f"✅ {ruta} actualizado (codificación: {cod_usada} → UTF-8)")
        return True
        
    except Exception as e:
        print(f"❌ Error en {ruta}: {e}")
        return False


# ============================================================
# 4. FUNCIÓN: Corregir TODOS los enlaces a comunas en index.html
# ============================================================

def corregir_todos_enlaces_index():
    """Corrige TODOS los enlaces a comunas en index.html"""
    ruta = "index.html"
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            contenido = f.read()
        
        comunas = [
            'las-condes', 'vitacura', 'lo-barnechea', 'recoleta', 
            'independencia', 'quilicura', 'conchali', 'huechuraba', 
            'renca', 'cerro-navia', 'pudahuel', 'maipu', 
            'san-miguel', 'la-florida', 'nunoa', 'santiago-centro', 
            'macul', 'la-dehesa', 'Santiago'
        ]
        
        for comuna in comunas:
            contenido = contenido.replace(
                f'href="{comuna}.html"',
                f'href="comunas/{comuna}.html"'
            )
        
        with open(ruta, 'w', encoding='utf-8') as f:
            f.write(contenido)
        
        print(f"✅ {ruta} actualizado (TODOS los enlaces a comunas corregidos)")
        return True
    except Exception as e:
        print(f"❌ Error en {ruta}: {e}")
        return False


# ============================================================
# 5. FUNCIÓN: Corregir caracteres en todas las páginas
# ============================================================

def corregir_caracteres_todas():
    """Corrige caracteres raros en todas las páginas de comunas"""
    archivos = [f for f in os.listdir(CARPETA_COMUNAS) if f.endswith('.html')]
    
    for archivo in archivos:
        ruta = os.path.join(CARPETA_COMUNAS, archivo)
        try:
            contenido, cod = leer_con_codificacion_fallback(ruta)
            
            contenido = contenido.replace('�', '')
            contenido = contenido.replace('??', '')
            contenido = contenido.replace('��', '')
            contenido = contenido.replace('��', '')
            contenido = contenido.replace('?', '')
            
            with open(ruta, 'w', encoding='utf-8') as f:
                f.write(contenido)
            
            print(f"✅ {ruta} caracteres corregidos")
        except Exception as e:
            print(f"❌ Error en {ruta}: {e}")


# ============================================================
# 6. FUNCIÓN: Agregar Google Maps a todas las páginas
# ============================================================

def agregar_maps_todas():
    """Agrega Google Maps a todas las páginas de comunas"""
    
    archivos = [f for f in os.listdir(CARPETA_COMUNAS) if f.endswith('.html')]
    
    for archivo in archivos:
        ruta = os.path.join(CARPETA_COMUNAS, archivo)
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                contenido = f.read()
            
            # Verificar si ya tiene mapa
            if 'google.com/maps' in contenido:
                print(f"⏭️  {ruta} ya tiene mapa")
                continue
            
            nombre_archivo = os.path.splitext(archivo)[0]
            comuna = nombre_archivo.replace('-', ' ').title()
            
            nombres_especiales = {
                'cerro-navia': 'Cerro Navia',
                'la-dehesa': 'La Dehesa',
                'la-florida': 'La Florida',
                'las-condes': 'Las Condes',
                'lo-barnechea': 'Lo Barnechea',
                'nunoa': 'Ñuñoa',
                'santiago-centro': 'Santiago Centro'
            }
            comuna = nombres_especiales.get(nombre_archivo, comuna)
            
            # MAPA CORREGIDO - Usando iframe con URL simple
            mapa_html = f'''
    <!-- ===== GOOGLE MAPS ===== -->
    <section class="section-mapa" style="padding:40px 0; background:var(--color-dark);">
      <div class="container">
        <h2 class="section-title">¿Dónde estamos en {comuna}?</h2>
        <p class="section-subtitle">Encuentranos fácilmente en {comuna}. ¡Llegamos en minutos!</p>
        <div style="border-radius:20px; overflow:hidden; box-shadow: 0 20px 50px rgba(0,0,0,0.5); border: 2px solid rgba(56,189,248,0.2);">
          <iframe 
            src="https://www.google.com/maps/embed/v1/place?key=AIzaSyBFw0Qbyq9zTFTd-tUY6dZWTgaQzuU17R8&q={comuna},+Santiago,+Chile"
            width="100%" 
            height="400" 
            style="border:0; display:block;"
            allowfullscreen="" 
            loading="lazy"
            referrerpolicy="no-referrer-when-downgrade"
            title="Mapa de {comuna}">
          </iframe>
        </div>
        <p style="text-align:center; color:var(--color-text-muted); margin-top:12px; font-size:0.9rem;">
          📍 Cobertura inmediata en todo {comuna} • Técnicos locales
        </p>
      </div>
    </section>
    '''
            
            # Buscar dónde insertar el mapa
            if 'section-contacto' in contenido:
                contenido = contenido.replace(
                    '<section id="contacto" class="section-contacto">',
                    mapa_html + '\n\n  <section id="contacto" class="section-contacto">'
                )
            else:
                contenido = contenido.replace(
                    '<footer',
                    mapa_html + '\n\n  <footer'
                )
            
            with open(ruta, 'w', encoding='utf-8') as f:
                f.write(contenido)
            
            print(f"✅ {ruta} mapa agregado")
            
        except Exception as e:
            print(f"❌ Error en {ruta}: {e}")


# ============================================================
# 7. FUNCIÓN: Actualizar WhatsApp flotante con mensaje dinámico
# ============================================================

def actualizar_whatsapp_flotante():
    """Actualiza el botón flotante de WhatsApp con mensaje dinámico por comuna"""
    
    archivos = [f for f in os.listdir(CARPETA_COMUNAS) if f.endswith('.html')]
    
    for archivo in archivos:
        ruta = os.path.join(CARPETA_COMUNAS, archivo)
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                contenido = f.read()
            
            # Extraer nombre de comuna
            nombre_base = os.path.splitext(archivo)[0]
            comuna = nombre_base.replace('-', ' ').title()
            
            nombres_especiales = {
                'cerro-navia': 'Cerro Navia',
                'la-dehesa': 'La Dehesa',
                'la-florida': 'La Florida',
                'las-condes': 'Las Condes',
                'lo-barnechea': 'Lo Barnechea',
                'nunoa': 'Ñuñoa',
                'santiago-centro': 'Santiago Centro'
            }
            comuna = nombres_especiales.get(nombre_base, comuna)
            
            # Mensaje dinámico
            mensaje = f"Hola%2C%20necesito%20un%20destape%20urgente%20en%20{comuna}"
            url_whatsapp = f"https://wa.me/56972091242?text={mensaje}"
            
            # Botón flotante con estilos incluidos
            nuevo_boton = f'''
    <!-- WhatsApp Float -->
    <a href="{url_whatsapp}" class="whatsapp-float" target="_blank" rel="noopener noreferrer" aria-label="WhatsApp urgente" style="position:fixed;bottom:24px;right:24px;width:60px;height:60px;background:linear-gradient(135deg,#34d399,#10b981);color:white;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:1.8rem;box-shadow:0 4px 24px rgba(52,211,153,0.35);z-index:1000;transition:all 0.3s ease;animation:pulse-whatsapp 1.8s infinite;text-decoration:none;">💬</a>
    <style>
    .whatsapp-float:hover {{ transform:scale(1.1); box-shadow:0 6px 32px rgba(52,211,153,0.55); }}
    @keyframes pulse-whatsapp {{ 0% {{ box-shadow:0 0 0 0 rgba(52,211,153,0.5); }} 70% {{ box-shadow:0 0 0 14px rgba(52,211,153,0); }} 100% {{ box-shadow:0 0 0 0 rgba(52,211,153,0); }} }}
    </style>
    '''
            
            # Reemplazar o agregar botón
            if 'whatsapp-float' in contenido:
                contenido = re.sub(
                    r'<a href="https://wa\.me/[^"]*" class="whatsapp-float"[^>]*>.*?</a>',
                    nuevo_boton,
                    contenido,
                    flags=re.DOTALL
                )
            else:
                contenido = contenido.replace('</body>', nuevo_boton + '\n</body>')
            
            with open(ruta, 'w', encoding='utf-8') as f:
                f.write(contenido)
            
            print(f"✅ {ruta} WhatsApp dinámico actualizado → {comuna}")
            
        except Exception as e:
            print(f"❌ Error en {ruta}: {e}")


# ============================================================
# 8. FUNCIÓN: Regenerar páginas con diseño de Vitacura
# ============================================================

def regenerar_paginas_problema():
    """Regenera TODAS las páginas con el diseño de Vitacura"""
    
    plantilla_ruta = os.path.join(CARPETA_COMUNAS, 'vitacura.html')
    
    if not os.path.exists(plantilla_ruta):
        print("❌ Plantilla 'vitacura.html' no encontrada")
        return
    
    comunas_a_regenerar = [
        'cerro-navia', 'conchali', 'huechuraba', 'independencia',
        'la-dehesa', 'la-florida', 'las-condes', 'lo-barnechea',
        'macul', 'maipu', 'nunoa', 'providencia', 'pudahuel',
        'quilicura', 'recoleta', 'renca', 'san-miguel',
        'santiago-centro'
    ]
    
    nombres_especiales = {
        'nunoa': 'Ñuñoa',
        'santiago-centro': 'Santiago Centro',
        'cerro-navia': 'Cerro Navia',
        'la-dehesa': 'La Dehesa',
        'la-florida': 'La Florida',
        'las-condes': 'Las Condes',
        'lo-barnechea': 'Lo Barnechea'
    }
    
    try:
        with open(plantilla_ruta, 'r', encoding='utf-8') as f:
            plantilla = f.read()
        
        for comuna in comunas_a_regenerar:
            ruta = os.path.join(CARPETA_COMUNAS, f'{comuna}.html')
            
            nombre_comuna = nombres_especiales.get(comuna, comuna.replace('-', ' ').title())
            
            if os.path.exists(ruta):
                with open(ruta, 'r', encoding='utf-8') as f:
                    contenido_actual = f.read()
                
                match = re.search(r'<title>(.*?)</title>', contenido_actual)
                titulo = match.group(1) if match else f'Destape en {nombre_comuna}'
                
                match_h1 = re.search(r'<h1 class="hero-title">(.*?)</h1>', contenido_actual)
                hero_text = match_h1.group(1) if match_h1 else f'Destape urgente en {nombre_comuna}'
                
                match_desc = re.search(r'<meta name="description" content="(.*?)">', contenido_actual)
                meta_desc = match_desc.group(1) if match_desc else f'Destape urgente en {nombre_comuna}. Técnicos 24/7.'
            else:
                titulo = f'Destape en {nombre_comuna}'
                hero_text = f'Destape urgente en {nombre_comuna}'
                meta_desc = f'Destape urgente en {nombre_comuna}. Técnicos 24/7.'
            
            nuevo_contenido = plantilla
            
            nuevo_contenido = re.sub(r'<title>.*?</title>', f'<title>{titulo}</title>', nuevo_contenido)
            nuevo_contenido = re.sub(r'<h1 class="hero-title">.*?</h1>', f'<h1 class="hero-title">{hero_text}</h1>', nuevo_contenido)
            nuevo_contenido = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{meta_desc}">', nuevo_contenido)
            
            nuevo_contenido = nuevo_contenido.replace(
                'Destapes <span>Vitacura 24H</span>',
                f'Destapes <span>{nombre_comuna} 24H</span>'
            )
            nuevo_contenido = nuevo_contenido.replace(
                'Destapes Vitacura 24H',
                f'Destapes {nombre_comuna} 24H'
            )
            nuevo_contenido = nuevo_contenido.replace(
                'Destape urgente en Vitacura',
                f'Destape urgente en {nombre_comuna}'
            )
            nuevo_contenido = nuevo_contenido.replace(
                'Nuestros servicios en Vitacura',
                f'Nuestros servicios en {nombre_comuna}'
            )
            
            with open(ruta, 'w', encoding='utf-8') as f:
                f.write(nuevo_contenido)
            
            print(f"✅ {ruta} regenerado con diseño de Vitacura")
            
    except Exception as e:
        print(f"❌ Error regenerando páginas: {e}")


# ============================================================
# 9. FUNCIÓN PRINCIPAL
# ============================================================

def main():
    print("=" * 50)
    print("🔧 ACTUALIZANDO SITIO COMPLETO")
    print("=" * 50)
    
    # PASO 1: Regenerar páginas con diseño de Vitacura
    print("\n🔄 Regenerando páginas con diseño de Vitacura...")
    regenerar_paginas_problema()
    
    # PASO 2: Corregir enlaces en index.html
    print("\n📄 Corrigiendo enlaces en index.html...")
    corregir_todos_enlaces_index()
    
    # PASO 3: Corregir caracteres en todas las páginas
    print("\n🔤 Corrigiendo caracteres raros en todas las páginas...")
    corregir_caracteres_todas()
    
    # PASO 4: Agregar Google Maps
    print("\n🗺️ Agregando Google Maps a todas las comunas...")
    agregar_maps_todas()
    
    # PASO 5: Actualizar WhatsApp flotante
    print("\n💬 Actualizando WhatsApp flotante con mensaje dinámico...")
    actualizar_whatsapp_flotante()
    
    # PASO 6: Actualizar páginas de comunas (footer)
    if not os.path.exists(CARPETA_COMUNAS):
        print(f"\n❌ Carpeta '{CARPETA_COMUNAS}' no encontrada")
        return
    
    archivos = [f for f in os.listdir(CARPETA_COMUNAS) if f.endswith('.html')]
    
    if not archivos:
        print(f"❌ No se encontraron archivos HTML en '{CARPETA_COMUNAS}'")
        return
    
    print(f"\n📂 Encontrados {len(archivos)} archivos en '{CARPETA_COMUNAS}'")
    print("=" * 50)
    
    actualizados = 0
    for archivo in archivos:
        ruta = os.path.join(CARPETA_COMUNAS, archivo)
        if actualizar_archivo(ruta):
            actualizados += 1
    
    print("=" * 50)
    print(f"\n✅ {actualizados} páginas de comunas actualizadas correctamente")
    print("✅ index.html con enlaces corregidos")
    print("✅ Caracteres raros eliminados")
    print("✅ Google Maps agregado a todas las comunas")
    print("✅ WhatsApp flotante con mensaje dinámico")
    print("✅ Todas las páginas con diseño de Vitacura")
    print("\n🎯 ¡TODO LISTO! Sube los cambios a GitHub.")


# ============================================================
# 10. EJECUTAR
# ============================================================

if __name__ == "__main__":
    main()