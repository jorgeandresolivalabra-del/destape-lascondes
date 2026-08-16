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
# 3. FUNCIÓN: Actualizar páginas de comunas
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
    
    coordenadas = {
        'cerro-navia': '-33.4167,-70.7167',
        'conchali': '-33.3833,-70.6833',
        'huechuraba': '-33.3500,-70.6833',
        'independencia': '-33.4167,-70.6667',
        'la-dehesa': '-33.3667,-70.5667',
        'la-florida': '-33.5167,-70.6000',
        'las-condes': '-33.4145,-70.5785',
        'lo-barnechea': '-33.3500,-70.5500',
        'macul': '-33.4833,-70.6000',
        'maipu': '-33.5167,-70.7667',
        'nunoa': '-33.4667,-70.6000',
        'providencia': '-33.4333,-70.6167',
        'pudahuel': '-33.4333,-70.7500',
        'quilicura': '-33.3667,-70.7333',
        'recoleta': '-33.4167,-70.6500',
        'renca': '-33.4000,-70.7167',
        'san-miguel': '-33.5000,-70.6500',
        'santiago-centro': '-33.4500,-70.6667',
        'vitacura': '-33.3833,-70.5667'
    }
    
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
            
            coords = coordenadas.get(nombre_archivo, '-33.4500,-70.6667')
            lat, lng = coords.split(',')
            
            mapa_html = f'''
    <!-- ===== GOOGLE MAPS ===== -->
    <section class="section-mapa" style="padding:40px 0; background:var(--color-dark);">
      <div class="container">
        <h2 class="section-title">¿Dónde estamos en {comuna}?</h2>
        <p class="section-subtitle">Encuentranos fácilmente en {comuna}. ¡Llegamos en minutos!</p>
        <div style="border-radius:20px; overflow:hidden; box-shadow: 0 20px 50px rgba(0,0,0,0.5); border: 2px solid rgba(56,189,248,0.2);">
          <iframe 
            src="https://www.google.com/maps?q={lat},{lng}&z=13&output=embed"
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
            
            contenido = contenido.replace(
                '<section id="contacto" class="section-contacto">',
                mapa_html + '\n\n  <section id="contacto" class="section-contacto">'
            )
            
            with open(ruta, 'w', encoding='utf-8') as f:
                f.write(contenido)
            
            print(f"✅ {ruta} mapa agregado")
            
        except Exception as e:
            print(f"❌ Error en {ruta}: {e}")


# ============================================================
# 7. FUNCIÓN PRINCIPAL
# ============================================================

def main():
    print("=" * 50)
    print("🔧 ACTUALIZANDO SITIO COMPLETO")
    print("=" * 50)
    
    # PASO 1: Corregir enlaces en index.html
    print("\n📄 Corrigiendo enlaces en index.html...")
    corregir_todos_enlaces_index()
    
    # PASO 2: Corregir caracteres en todas las páginas
    print("\n🔤 Corrigiendo caracteres raros en todas las páginas...")
    corregir_caracteres_todas()
    
    # PASO 3: Agregar Google Maps
    print("\n🗺️ Agregando Google Maps a todas las comunas...")
    agregar_maps_todas()
    
    # PASO 4: Actualizar páginas de comunas
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
    print("\n🎯 ¡TODO LISTO! Sube los cambios a GitHub.")


# ============================================================
# 8. EJECUTAR
# ============================================================

if __name__ == "__main__":
    main()