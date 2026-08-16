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
        
        # Lista de todas las comunas
        comunas = [
            'las-condes', 'vitacura', 'lo-barnechea', 'recoleta', 
            'independencia', 'quilicura', 'conchali', 'huechuraba', 
            'renca', 'cerro-navia', 'pudahuel', 'maipu', 
            'san-miguel', 'la-florida', 'nunoa', 'santiago-centro', 
            'macul', 'la-dehesa', 'Santiago'
        ]
        
        for comuna in comunas:
            # Reemplazar href="comuna.html" por href="comunas/comuna.html"
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
# 5. FUNCIÓN PRINCIPAL
# ============================================================

def main():
    print("=" * 50)
    print("🔧 ACTUALIZANDO SITIO COMPLETO")
    print("=" * 50)
    
    # PASO 1: Corregir enlaces en index.html
    print("\n📄 Corrigiendo enlaces en index.html...")
    corregir_todos_enlaces_index()
    
    # PASO 2: Actualizar páginas de comunas
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
    print("\n🎯 ¡TODO LISTO! Sube los cambios a GitHub.")


# ============================================================
# 6. EJECUTAR
# ============================================================

if __name__ == "__main__":
    main()