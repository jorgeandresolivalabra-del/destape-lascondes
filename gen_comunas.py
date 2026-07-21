# -*- coding: utf-8 -*-
import os, urllib.parse

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "comunas")

# ---- Plantilla (mismo diseño que index.html / las-condes.html) ----
TPL = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
  <title>__META_TITLE__</title>
  <link rel="canonical" href="https://www.destapesantiago24h.cl/comunas/__SLUG__.html">
  <meta name="description" content="__META_DESC__">
  <meta name="keywords" content="__META_KW__">
  <meta property="og:title" content="__OG_TITLE__">
  <meta property="og:description" content="__OG_DESC__">
  <meta property="og:image" content="https://i.postimg.cc/4yxKLnCY/trabajador-y-su-camioneta.png">
  <meta property="og:url" content="https://www.destapesantiago24h.cl/comunas/__SLUG__.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "PlumbingService",
    "name": "Destapes __NOMBRE__ 24H",
    "image": "https://i.postimg.cc/4yxKLnCY/trabajador-y-su-camioneta.png",
    "telephone": "+56963571251",
    "url": "https://www.destapesantiago24h.cl/comunas/__SLUG__.html",
    "address": { "@type": "PostalAddress", "addressRegion": "Región Metropolitana", "addressCountry": "CL" },
    "geo": { "@type": "GeoCoordinates", "latitude": "__GEO_LAT__", "longitude": "__GEO_LONG__" },
    "openingHoursSpecification": { "@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"], "opens": "00:00", "closes": "23:59" },
    "priceRange": "$$",
    "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "__REVIEW_COUNT__" },
    "areaServed": { "@type": "City", "name": "__NOMBRE__" }
  }
  </script>
  <script>
    !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');fbq('init','1647071222974255');fbq('track','PageView');
  </script>
  <noscript><img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=1647071222974255&ev=PageView&noscript=1"/></noscript>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@700;800&family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root{--color-primary:#38bdf8;--color-primary-dark:#0ea5e9;--color-secondary:#fbbf24;--color-success:#34d399;--color-danger:#f87171;--color-dark:#060b14;--color-surface:#0d1626;--color-surface-2:#111d30;--color-surface-3:#162035;--color-border:rgba(56,189,248,0.12);--color-border-warm:rgba(251,191,36,0.18);--color-gray:#94a3b8;--color-gray-light:#64748b;--color-text:#e2e8f0;--color-text-muted:#94a3b8;--color-light:#0d1626;--glow-blue:0 0 24px rgba(56,189,248,0.25);--glow-amber:0 0 24px rgba(251,191,36,0.25);--glow-green:0 0 24px rgba(52,211,153,0.25);--shadow-sm:0 1px 3px rgba(0,0,0,0.4);--shadow-md:0 4px 16px rgba(0,0,0,0.5);--shadow-lg:0 10px 32px rgba(0,0,0,0.6);--shadow-xl:0 20px 48px rgba(0,0,0,0.7);--radius:14px;--radius-lg:20px;--transition:all 0.3s ease;}
    *{margin:0;padding:0;box-sizing:border-box;}
    html{scroll-behavior:smooth;}
    body{font-family:'DM Sans',-apple-system,BlinkMacSystemFont,sans-serif;line-height:1.6;color:var(--color-text);background:var(--color-dark);}
    img{max-width:100%;height:auto;display:block;}
    a{text-decoration:none;color:inherit;}
    ul{list-style:none;}
    .container{max-width:1280px;margin:0 auto;padding:0 20px;}
    .live-bar{position:sticky;top:0;z-index:1000;background:linear-gradient(90deg,#1a0a0a 0%,#200e0e 50%,#1a0a0a 100%);border-bottom:1px solid rgba(248,113,113,0.3);color:white;padding:10px 0;font-size:0.9rem;font-weight:500;text-align:center;box-shadow:0 2px 20px rgba(248,113,113,0.2);animation:slideDown 0.3s ease;}
    @keyframes slideDown{from{transform:translateY(-100%);opacity:0;}to{transform:translateY(0);opacity:1;}}
    .live-bar-content{display:flex;align-items:center;justify-content:center;gap:12px;flex-wrap:wrap;}
    .live-badge{display:inline-flex;align-items:center;gap:6px;background:rgba(255,255,255,0.2);padding:4px 12px;border-radius:20px;font-size:0.85rem;animation:pulse 2s infinite;}
    @keyframes pulse{0%,100%{opacity:1;}50%{opacity:0.7;}}
    .live-metrics{display:flex;gap:16px;flex-wrap:wrap;}
    .live-metric{display:flex;align-items:center;gap:4px;}
    .live-timestamp{font-size:0.8rem;opacity:0.9;}
    .site-header{background:rgba(6,11,20,0.95);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border-bottom:1px solid var(--color-border);position:sticky;top:48px;z-index:999;padding:12px 0;}
    .header-container{display:flex;justify-content:space-between;align-items:center;}
    .logo-area{display:flex;align-items:center;gap:10px;font-family:'Outfit',sans-serif;font-weight:800;font-size:1.2rem;color:white;}
    .logo-icon{font-size:1.8rem;}
    .logo-text span{color:var(--color-primary);}
    .nav-menu{display:flex;align-items:center;gap:20px;flex-wrap:wrap;}
    .nav-menu a{font-weight:500;font-size:0.9rem;padding:7px 12px;border-radius:8px;color:var(--color-text-muted);transition:var(--transition);}
    .nav-menu a:hover{background:rgba(56,189,248,0.08);color:var(--color-primary);}
    .btn-gasfiter-header{background:rgba(251,191,36,0.12);border:1px solid var(--color-border-warm);color:var(--color-secondary);padding:8px 18px;border-radius:40px;font-weight:700;transition:var(--transition);}
    .btn-gasfiter-header:hover{background:rgba(251,191,36,0.2);transform:scale(1.02);}
    .btn-ws-header{background:rgba(52,211,153,0.12);border:1px solid rgba(52,211,153,0.25);color:var(--color-success);padding:8px 18px;border-radius:40px;font-weight:600;transition:var(--transition);}
    .btn-ws-header:hover{background:rgba(52,211,153,0.2);transform:scale(1.02);}
    .hero-section{padding:56px 0 72px;background:var(--color-dark);color:white;position:relative;overflow:hidden;}
    .hero-section::before{content:'';position:absolute;top:-30%;right:-15%;width:700px;height:700px;background:radial-gradient(circle,rgba(56,189,248,0.07) 0%,transparent 65%);border-radius:50%;pointer-events:none;}
    .hero-section::after{content:'';position:absolute;bottom:-20%;left:-10%;width:500px;height:500px;background:radial-gradient(circle,rgba(251,191,36,0.05) 0%,transparent 65%);border-radius:50%;pointer-events:none;}
    .hero-grid{display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:center;position:relative;z-index:1;}
    .hero-title{font-family:'Outfit',sans-serif;font-size:clamp(2rem,4vw,3rem);font-weight:800;line-height:1.08;margin-bottom:20px;letter-spacing:-0.02em;}
    .hero-title span{color:var(--color-secondary);display:block;margin-top:8px;}
    .hero-subtitle{font-size:1.1rem;color:var(--color-text-muted);margin-bottom:28px;max-width:520px;line-height:1.7;}
    .hero-subtitle strong{color:var(--color-text);}
    .social-proof-badges{display:flex;align-items:center;gap:12px;margin-bottom:24px;flex-wrap:wrap;}
    .rating-badge{display:flex;align-items:center;gap:6px;background:rgba(251,191,36,0.1);border:1px solid rgba(251,191,36,0.2);padding:8px 16px;border-radius:50px;font-weight:600;font-size:0.9rem;color:white;}
    .rating-stars{color:var(--color-secondary);}
    .clients-counter{display:flex;align-items:center;gap:8px;background:rgba(52,211,153,0.1);border:1px solid rgba(52,211,153,0.2);padding:8px 16px;border-radius:50px;font-size:0.88rem;color:var(--color-text);}
    .client-avatars{display:flex;margin-left:-8px;}
    .client-avatars img{width:30px;height:30px;border-radius:50%;border:2px solid var(--color-surface);margin-left:-8px;object-fit:cover;}
    .client-avatars img:first-child{margin-left:0;}
    .hero-buttons{display:flex;gap:14px;margin-bottom:24px;flex-wrap:wrap;}
    .btn-llamar,.btn-whatsapp{display:inline-flex;align-items:center;justify-content:center;gap:10px;padding:17px 30px;border-radius:50px;font-weight:700;font-size:1.05rem;transition:var(--transition);text-align:center;min-width:215px;}
    .btn-llamar{background:linear-gradient(135deg,var(--color-primary),var(--color-primary-dark));color:var(--color-dark);box-shadow:0 4px 24px rgba(56,189,248,0.35);}
    .btn-llamar:hover{transform:translateY(-2px);box-shadow:0 8px 32px rgba(56,189,248,0.55);}
    .btn-whatsapp{background:linear-gradient(135deg,#34d399,#10b981);color:var(--color-dark);box-shadow:0 4px 24px rgba(52,211,153,0.3);}
    .btn-whatsapp:hover{transform:translateY(-2px);box-shadow:0 8px 32px rgba(52,211,153,0.5);}
    .trust-badges{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:20px;}
    .badge{display:inline-flex;align-items:center;gap:6px;background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.1);padding:6px 14px;border-radius:50px;font-size:0.88rem;font-weight:500;color:var(--color-text-muted);}
    .badge strong{color:var(--color-text);}
    .guarantee-seal{display:inline-flex;align-items:center;gap:8px;background:linear-gradient(135deg,rgba(52,211,153,0.12),rgba(52,211,153,0.06));border:1px solid rgba(52,211,153,0.25);padding:10px 20px;border-radius:50px;font-weight:600;font-size:0.9rem;color:var(--color-success);}
    .hero-image-wrapper{position:relative;text-align:center;}
    .hero-image-wrapper img{border-radius:var(--radius-lg);box-shadow:0 24px 64px rgba(0,0,0,0.7),0 0 0 1px rgba(56,189,248,0.1);max-width:100%;margin:0 auto;}
    .live-indicator{position:absolute;top:16px;right:16px;background:rgba(248,113,113,0.15);border:1px solid rgba(248,113,113,0.4);color:var(--color-danger);padding:6px 14px;border-radius:50px;font-size:0.82rem;font-weight:600;display:flex;align-items:center;gap:6px;animation:pulse 1.5s infinite;backdrop-filter:blur(8px);}
    .hero-stats{margin-top:20px;display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:var(--color-border);border:1px solid var(--color-border);border-radius:var(--radius);overflow:hidden;}
    .hero-stat{text-align:center;padding:14px 8px;background:var(--color-surface);}
    .hero-stat-value{font-family:'Outfit',sans-serif;font-size:1.4rem;font-weight:800;color:var(--color-secondary);}
    .hero-stat-label{font-size:0.78rem;color:var(--color-text-muted);margin-top:2px;}
    .section-problemas,.section-servicios,.section-proceso,.section-beneficios,.section-testimonios,.section-cobertura,.section-casos,.section-dashboard,.section-comunas,.section-faq,.section-urgency,.cta-final{padding:70px 0;}
    .section-title{text-align:center;font-family:'Outfit',sans-serif;font-size:clamp(1.7rem,3vw,2.4rem);font-weight:800;margin-bottom:16px;color:white;letter-spacing:-0.02em;}
    .section-subtitle{text-align:center;font-size:1.05rem;color:var(--color-text-muted);max-width:650px;margin:0 auto 40px;}
    .section-subtitle strong{color:var(--color-text);}
    .section-problemas{background:var(--color-surface);}
    .problemas-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px;margin-top:30px;}
    .problema-card{background:var(--color-surface-2);border:1px solid var(--color-border);padding:20px 24px;border-radius:var(--radius);display:flex;align-items:center;gap:14px;font-weight:500;color:var(--color-text);transition:var(--transition);}
    .problema-card:hover{transform:translateY(-3px);border-color:rgba(56,189,248,0.3);background:var(--color-surface-3);box-shadow:var(--glow-blue);}
    .problema-card span{font-size:1.8rem;}
    .section-servicios{background:var(--color-dark);}
    .servicios-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px;margin-top:30px;}
    .servicio-card{background:var(--color-surface);border-radius:var(--radius-lg);padding:28px;border:1px solid var(--color-border);transition:var(--transition);}
    .servicio-card:hover{transform:translateY(-5px);border-color:rgba(56,189,248,0.3);box-shadow:var(--glow-blue),var(--shadow-lg);}
    .servicio-icon{font-size:2.5rem;margin-bottom:16px;}
    .servicio-card h3{font-family:'Outfit',sans-serif;font-size:1.2rem;font-weight:700;margin-bottom:12px;color:white;}
    .servicio-card p{color:var(--color-text-muted);margin-bottom:16px;font-size:0.93rem;}
    .servicio-imagen{width:100%;height:180px;object-fit:cover;border-radius:var(--radius);margin:16px 0;opacity:0.9;}
    .servicio-features{margin:16px 0;}
    .servicio-features li{display:flex;align-items:center;gap:8px;font-size:0.88rem;color:var(--color-text-muted);margin-bottom:8px;}
    .servicio-features li::before{content:"✓";color:var(--color-success);font-weight:700;}
    .servicio-link{display:inline-flex;align-items:center;gap:6px;color:var(--color-primary);font-weight:600;margin-top:12px;transition:var(--transition);font-size:0.9rem;}
    .servicio-link:hover{gap:10px;}
    .servicio-note{font-size:0.82rem;color:var(--color-gray-light);margin-top:12px;font-style:italic;}
    .section-proceso{background:var(--color-surface);}
    .pasos-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:20px;margin-top:40px;}
    .paso-card{text-align:center;padding:28px 20px;background:var(--color-surface-2);border:1px solid var(--color-border);border-radius:var(--radius);position:relative;}
    .paso-numero{width:48px;height:48px;background:linear-gradient(135deg,var(--color-primary),var(--color-primary-dark));color:var(--color-dark);border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:'Outfit',sans-serif;font-weight:800;font-size:1.2rem;margin:0 auto 16px;box-shadow:var(--glow-blue);}
    .paso-card h3{font-weight:700;margin-bottom:10px;color:white;}
    .paso-card p{color:var(--color-text-muted);font-size:0.92rem;}
    .section-beneficios{background:var(--color-dark);}
    .beneficios-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:12px;margin-top:30px;}
    .beneficio-item{display:flex;align-items:center;gap:12px;padding:15px 20px;background:var(--color-surface);border:1px solid var(--color-border);border-radius:var(--radius);font-weight:500;color:var(--color-text);transition:var(--transition);}
    .beneficio-item:hover{transform:translateX(4px);border-color:rgba(56,189,248,0.3);}
    .beneficio-item::before{content:"✓";color:var(--color-success);font-weight:800;font-size:1.1rem;flex-shrink:0;}
    .section-casos{background:var(--color-surface);}
    .casos-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:24px;margin-top:40px;}
    .caso-card{background:var(--color-surface-2);border-radius:var(--radius-lg);padding:28px;border:1px solid var(--color-border);position:relative;overflow:hidden;transition:var(--transition);}
    .caso-card:hover{border-color:rgba(56,189,248,0.25);box-shadow:var(--glow-blue);}
    .caso-card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,var(--color-primary),var(--color-secondary));}
    .caso-header{display:flex;align-items:center;gap:16px;margin-bottom:20px;padding-bottom:16px;border-bottom:1px solid var(--color-border);}
    .caso-avatar{width:60px;height:60px;border-radius:50%;object-fit:cover;border:2px solid var(--color-success);}
    .caso-info h4{font-weight:700;font-size:1.05rem;margin-bottom:4px;color:white;}
    .caso-info p{color:var(--color-text-muted);font-size:0.88rem;}
    .verified-badge{display:inline-flex;align-items:center;gap:4px;background:rgba(52,211,153,0.12);border:1px solid rgba(52,211,153,0.2);color:var(--color-success);padding:3px 10px;border-radius:20px;font-size:0.8rem;font-weight:600;margin-top:6px;}
    .caso-metrics{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:20px 0;padding:16px;background:rgba(255,255,255,0.03);border:1px solid var(--color-border);border-radius:var(--radius);}
    .metric-item{text-align:center;}
    .metric-label{font-size:0.8rem;color:var(--color-text-muted);margin-bottom:4px;}
    .metric-value{font-family:'Outfit',sans-serif;font-weight:800;font-size:1.1rem;}
    .metric-value.before{color:var(--color-danger);}
    .metric-value.after{color:var(--color-success);}
    .caso-testimonio{font-style:italic;color:var(--color-text-muted);margin:16px 0;padding-left:14px;border-left:2px solid var(--color-primary);line-height:1.6;font-size:0.93rem;}
    .caso-verification{display:flex;gap:8px;margin-top:14px;flex-wrap:wrap;}
    .verification-tag{display:inline-flex;align-items:center;gap:4px;background:rgba(255,255,255,0.04);border:1px solid var(--color-border);padding:4px 10px;border-radius:20px;font-size:0.78rem;color:var(--color-text-muted);}
    .caso-timestamp{font-size:0.78rem;color:var(--color-gray-light);margin-top:12px;text-align:right;}
    .section-dashboard{background:var(--color-dark);position:relative;overflow:hidden;}
    .section-dashboard::before{content:'';position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:800px;height:800px;background:radial-gradient(circle,rgba(56,189,248,0.04) 0%,transparent 65%);pointer-events:none;}
    .dashboard-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:1px;background:var(--color-border);border:1px solid var(--color-border);border-radius:var(--radius-lg);overflow:hidden;margin-top:40px;}
    .dashboard-card{background:var(--color-surface);padding:28px 20px;text-align:center;transition:var(--transition);}
    .dashboard-card:hover{background:var(--color-surface-2);}
    .dashboard-value{font-family:'Outfit',sans-serif;font-size:2.2rem;font-weight:800;color:var(--color-secondary);margin:8px 0;line-height:1;}
    .dashboard-label{font-size:0.88rem;color:var(--color-text-muted);}
    .dashboard-update{text-align:center;margin-top:20px;font-size:0.85rem;color:var(--color-text-muted);}
    .section-testimonios{background:var(--color-surface);}
    .testimonios-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:20px;margin-top:40px;}
    .testimonio-card{background:var(--color-surface-2);padding:26px;border-radius:var(--radius-lg);border:1px solid var(--color-border);transition:var(--transition);}
    .testimonio-card:hover{border-color:rgba(251,191,36,0.2);box-shadow:var(--glow-amber);}
    .stars{color:var(--color-secondary);font-size:1.1rem;margin-bottom:12px;}
    .testimonio-card p{margin-bottom:16px;line-height:1.6;color:var(--color-text-muted);font-size:0.93rem;}
    .testimonio-card h4{font-weight:600;color:white;display:flex;align-items:center;gap:8px;}
    .testimonio-verified{color:var(--color-success);font-size:0.85rem;font-weight:500;}
    .video-testimonial{position:relative;border-radius:var(--radius);overflow:hidden;margin:16px 0;background:linear-gradient(135deg,#0d1626,#060b14);border:1px solid var(--color-border);aspect-ratio:16/9;display:flex;align-items:center;justify-content:center;cursor:pointer;}
    .video-play-btn{width:56px;height:56px;background:rgba(251,191,36,0.15);border:2px solid rgba(251,191,36,0.4);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:1.4rem;color:var(--color-secondary);transition:var(--transition);}
    .video-testimonial:hover .video-play-btn{transform:scale(1.1);background:rgba(251,191,36,0.25);}
    .video-caption{position:absolute;bottom:10px;left:10px;right:10px;background:rgba(0,0,0,0.75);padding:7px 12px;border-radius:8px;font-size:0.85rem;color:var(--color-text-muted);}
    .section-cobertura{background:var(--color-dark);}
    .section-comunas{background:var(--color-surface);}
    .cobertura-tags{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;margin-top:24px;}
    .tag{background:var(--color-surface);border:1px solid var(--color-border);padding:7px 16px;border-radius:50px;font-weight:500;font-size:0.9rem;color:var(--color-text-muted);transition:var(--transition);}
    .tag:hover{background:rgba(56,189,248,0.1);border-color:rgba(56,189,248,0.3);color:var(--color-primary);transform:translateY(-2px);}
    .comunas-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:16px;margin-top:30px;}
    .comuna-card{background:var(--color-surface-2);padding:24px;border-radius:var(--radius);border:1px solid var(--color-border);transition:var(--transition);display:block;color:var(--color-text);}
    .comuna-card:hover{transform:translateY(-4px);border-color:rgba(56,189,248,0.3);box-shadow:var(--glow-blue);}
    .comuna-card span{font-size:1.4rem;display:block;margin-bottom:10px;}
    .comuna-card h3{font-weight:700;margin-bottom:6px;font-size:1rem;color:white;}
    .comuna-card p{color:var(--color-text-muted);font-size:0.88rem;}
    .section-faq{background:var(--color-dark);}
    .faq-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:16px;margin-top:40px;}
    .faq-item{background:var(--color-surface);border-radius:var(--radius);padding:24px;border:1px solid var(--color-border);transition:var(--transition);}
    .faq-item:hover{transform:translateY(-3px);border-color:rgba(56,189,248,0.25);box-shadow:var(--glow-blue);}
    .faq-question{font-size:1rem;font-weight:700;color:white;margin-bottom:12px;display:flex;align-items:center;gap:10px;}
    .faq-question span{font-size:1.2rem;}
    .faq-answer{color:var(--color-text-muted);line-height:1.6;font-size:0.92rem;}
    .faq-answer a{color:var(--color-primary);}
    .faq-answer strong{color:var(--color-text);}
    .section-urgency{background:var(--color-surface);border-top:1px solid var(--color-border-warm);border-bottom:1px solid var(--color-border-warm);position:relative;overflow:hidden;}
    .section-urgency::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 50% 0%,rgba(251,191,36,0.06) 0%,transparent 60%);pointer-events:none;}
    .urgency-content{text-align:center;max-width:700px;margin:0 auto;position:relative;z-index:1;}
    .urgency-badge{display:inline-flex;align-items:center;gap:8px;background:rgba(248,113,113,0.1);border:1px solid rgba(248,113,113,0.25);color:var(--color-danger);padding:8px 20px;border-radius:50px;font-weight:700;font-size:0.9rem;margin-bottom:20px;animation:pulse 1.5s infinite;}
    .urgency-title{font-family:'Outfit',sans-serif;font-size:clamp(1.7rem,3vw,2.2rem);font-weight:800;margin-bottom:16px;color:white;letter-spacing:-0.02em;}
    .urgency-stats{display:flex;justify-content:center;gap:32px;margin:24px 0;flex-wrap:wrap;}
    .urgency-stat{text-align:center;}
    .urgency-stat-value{font-family:'Outfit',sans-serif;font-size:2rem;font-weight:800;color:var(--color-danger);}
    .urgency-stat-label{font-size:0.85rem;color:var(--color-text-muted);margin-top:2px;}
    .countdown{display:flex;justify-content:center;gap:10px;margin:24px 0;flex-wrap:wrap;}
    .countdown-item{background:var(--color-surface-2);border:1px solid var(--color-border-warm);padding:14px 20px;border-radius:var(--radius);min-width:72px;text-align:center;}
    .countdown-value{font-family:'Outfit',sans-serif;font-size:1.6rem;font-weight:800;color:var(--color-secondary);}
    .countdown-label{font-size:0.75rem;color:var(--color-text-muted);text-transform:uppercase;letter-spacing:0.05em;}
    .gasfiter-express-section{background:var(--color-surface);padding:80px 20px;margin:0 auto;text-align:center;border-top:1px solid var(--color-border-warm);border-bottom:1px solid var(--color-border-warm);position:relative;overflow:hidden;}
    .gasfiter-express-section::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 50% 100%,rgba(251,191,36,0.05) 0%,transparent 60%);pointer-events:none;}
