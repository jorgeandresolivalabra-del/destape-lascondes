(function() {
  console.log('Destapes Santiago 24H - Versión optimizada con enlaces entre comunas');

  // Definir animación pulse para el timer (si no existe)
  if (!document.querySelector('style#pulse-animation')) {
    const style = document.createElement('style');
    style.id = 'pulse-animation';
    style.textContent = `
      @keyframes pulse {
        0% { opacity: 0.9; transform: scale(1); }
        50% { opacity: 1; transform: scale(1.02); background: #d32f2f; }
        100% { opacity: 0.9; transform: scale(1); }
      }
    `;
    document.head.appendChild(style);
  }

  // Efecto de aparición suave para elementos al hacer scroll
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  // Seleccionamos todos los elementos que queremos que aparezcan gradualmente
  const elementosAnimados = document.querySelectorAll('.servicio-card, .problema-card, .paso-card, .beneficio-item, .testimonio-card, .tag, .comuna-card');
  
  elementosAnimados.forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(el);
  });

  // Efecto hover en la imagen del proceso
  const procesoImg = document.querySelector('.section-proceso img');
  if (procesoImg) {
    procesoImg.addEventListener('mouseenter', () => {
      procesoImg.style.transform = 'scale(1.02)';
      procesoImg.style.transition = 'transform 0.3s ease';
    });
    procesoImg.addEventListener('mouseleave', () => {
      procesoImg.style.transform = 'scale(1)';
    });
  }

  // Agregar contador de oferta con botón de cierre (X) - SIN localStorage
  const createOfferTimer = () => {
    // Verificar si ya existe para no duplicar
    if (document.querySelector('.offer-timer')) return;
    
    const timerDiv = document.createElement('div');
    timerDiv.className = 'offer-timer';
    timerDiv.style.cssText = `
      background: #d32f2f;
      color: white;
      text-align: center;
      padding: 12px 40px 12px 16px;
      font-weight: bold;
      font-size: 0.9rem;
      position: fixed;
      bottom: 100px;
      left: 0;
      right: 0;
      width: 100%;
      z-index: 999;
      box-shadow: 0 -2px 10px rgba(0,0,0,0.2);
      display: none;
      cursor: pointer;
      transition: all 0.3s;
      letter-spacing: 0.5px;
    `;
    timerDiv.innerHTML = `
      ⏳ OFERTA ESPECIAL: 15% OFF si llamas en los próximos 30 minutos ⏳
      <span style="position: absolute; right: 15px; top: 50%; transform: translateY(-50%); 
                   cursor: pointer; font-size: 1.2rem; font-weight: bold; 
                   background: rgba(0,0,0,0.3); width: 24px; height: 24px; 
                   border-radius: 50%; display: inline-flex; align-items: center; 
                   justify-content: center; transition: background 0.3s;" 
            class="close-timer">✕</span>
    `;
    document.body.appendChild(timerDiv);

    // Lógica de cierre (X) - NO guarda en localStorage
    const closeBtn = timerDiv.querySelector('.close-timer');
    closeBtn.addEventListener('click', (e) => {
      e.stopPropagation(); // Evitar que se active el click del banner
      timerDiv.style.display = 'none';
      console.log('✅ Banner de oferta cerrado, aparecerá al recargar la página');
    });

    // Mostrar el timer solo después de scroll
    let scrollTimer;
    window.addEventListener('scroll', () => {
      clearTimeout(scrollTimer);
      scrollTimer = setTimeout(() => {
        if (window.scrollY > 300) {
          timerDiv.style.display = 'block';
          timerDiv.style.animation = 'pulse 1s ease-in-out infinite';
        } else {
          timerDiv.style.display = 'none';
          timerDiv.style.animation = 'none';
        }
      }, 100);
    });

    // Click en el banner (no en la X) redirige a teléfono
    timerDiv.addEventListener('click', (e) => {
      // Si el clic fue en la X o en sus hijos, no redirigir
      if (e.target === closeBtn || closeBtn.contains(e.target)) return;
      window.location.href = 'tel:+56963571251';
    });
  };

  createOfferTimer();

  // Smooth scroll para enlaces internos
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const href = this.getAttribute('href');
      if (href !== '#' && href !== '' && href !== '/') {
        const target = document.querySelector(href);
        if (target) {
          e.preventDefault();
          target.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
          });
        }
      }
    });
  });

  // Detectar la comuna actual para personalizar mensaje de WhatsApp
  const detectarComuna = () => {
    const url = window.location.pathname;
    let comuna = 'Santiago';
    
    if (url.includes('maipu') || url.includes('maipú')) comuna = 'Maipú';
    else if (url.includes('providencia')) comuna = 'Providencia';
    else if (url.includes('sanmiguel') || url.includes('san-miguel')) comuna = 'San Miguel';
    else if (url.includes('santiagocentro') || url.includes('santiago-centro')) comuna = 'Santiago Centro';
    else if (url.includes('ladehesa') || url.includes('la-dehesa')) comuna = 'La Dehesa';
    else if (url.includes('nunoa') || url.includes('ñuñoa')) comuna = 'Ñuñoa';
    
    return comuna;
  };

  // Actualizar enlaces de WhatsApp con mensaje personalizado
  const actualizarWhatsAppLinks = () => {
    const comuna = detectarComuna();
    const mensajePersonalizado = `Hola, necesito un destape urgente en ${comuna}`;
    const mensajeCodificado = encodeURIComponent(mensajePersonalizado);
    
    const whatsappLinks = document.querySelectorAll('a[href*="wa.me"], a[href*="api.whatsapp.com"]');
    whatsappLinks.forEach(link => {
      const href = link.getAttribute('href');
      if (href && !href.includes('text=')) {
        if (href.includes('?')) {
          link.setAttribute('href', href + `&text=${mensajeCodificado}`);
        } else {
          link.setAttribute('href', href + `?text=${mensajeCodificado}`);
        }
      }
    });
  };

  actualizarWhatsAppLinks();

  // Efecto de carga de imágenes lazy con fade-in
  const imagenes = document.querySelectorAll('img[loading="lazy"]');
  const imageObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;
        img.style.opacity = '0';
        img.style.transition = 'opacity 0.5s ease';
        
        if (img.complete) {
          img.style.opacity = '1';
        } else {
          img.addEventListener('load', () => {
            img.style.opacity = '1';
          });
          img.addEventListener('error', () => {
            img.style.opacity = '1';
          });
        }
        imageObserver.unobserve(img);
      }
    });
  }, { threshold: 0.1 });

  imagenes.forEach(img => imageObserver.observe(img));

  // Agregar clase active al menú según sección visible
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-menu a[href^="#"]');

  if (sections.length > 0 && navLinks.length > 0) {
    window.addEventListener('scroll', () => {
      let current = '';
      const scrollPosition = window.scrollY + 120;

      sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionBottom = sectionTop + section.offsetHeight;
        if (scrollPosition >= sectionTop && scrollPosition < sectionBottom) {
          current = section.getAttribute('id');
        }
      });

      navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href && href.startsWith('#') && href !== '#') {
          const linkId = href.substring(1);
          if (linkId === current) {
            link.classList.add('active');
            link.style.color = '#F2B705';
          } else {
            link.classList.remove('active');
            link.style.color = '';
          }
        }
      });
    });
  }

  // Efecto de conteo para estadísticas (opcional)
  const animarNumeros = () => {
    const numeros = document.querySelectorAll('.numero-stats');
    if (numeros.length === 0) return;
    
    numeros.forEach(num => {
      const target = parseInt(num.getAttribute('data-target'), 10);
      if (target && !isNaN(target)) {
        let current = 0;
        const increment = target / 50;
        const updateNumber = () => {
          current += increment;
          if (current < target) {
            num.textContent = Math.floor(current);
            requestAnimationFrame(updateNumber);
          } else {
            num.textContent = target;
          }
        };
        updateNumber();
      }
    });
  };

  // Ejecutar cuando los números sean visibles
  const statsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animarNumeros();
        statsObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.3 });

  const statsSection = document.querySelector('.section-beneficios');
  if (statsSection) {
    statsObserver.observe(statsSection);
  }

  // Agregar soporte para clics en botones de teléfono (tracking)
  document.querySelectorAll('a[href^="tel:"]').forEach(btn => {
    btn.addEventListener('click', () => {
      if (typeof fbq !== 'undefined') {
        fbq('track', 'Contact');
        fbq('track', 'Lead');
        console.log('✅ Contact + Lead enviados desde botón de llamada');
      }
    });
  });

  console.log('✅ Scripts cargados correctamente - Banner aparece cada vez que se hace scroll');
})();
