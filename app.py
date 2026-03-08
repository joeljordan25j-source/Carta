# -*- coding: utf-8 -*-
"""
Servidor web en Flask que genera una carta romántica con animaciones en HTML.
Listo para desplegar en Render.
"""

import os
from datetime import datetime
from flask import Flask

app = Flask(__name__)

# =========================
# CONFIGURACIÓN (EDITA AQUÍ)
# =========================
CONFIG = {
    "titulo": "Feliz dia de la mujer mi amor",
    "nombre_receptor": "Mi niña hermosa",
    "nombre_emisor": "Tu eterno enamorado",
    "fecha": datetime.now().strftime("%d de %B de %Y"),
    "mensaje": """Mi niña hermosa 🥺💘💍

Quiero que sepas que lo que siento por ti no es algo pequeño ni pasajero. Te amo con una intensidad que a veces ni yo mismo logro explicar. Desde que llegaste a mi vida, todo cambió: mis pensamientos, mis prioridades y hasta la forma en la que veo el mundo.

Eres esa persona que con una sola palabra logra calmarme, la que puede sacarme una sonrisa incluso en los días más pesados. Te amo por quien eres, por tu forma tan especial de ser, por tu manera de amar y por cada pequeño detalle que te hace única. No hay nadie que se compare contigo, ni nadie que pueda ocupar el lugar que tienes en mi corazón. 🥺🫂💗

A tu lado he aprendido que amar también significa cuidar, respetar, escuchar y crecer juntos. Y aunque no soy perfecto, mi amor por ti es real, sincero y está lleno de ganas de seguir mejorando cada día por nosotros. Te amo en tus mejores momentos, pero también en los días difíciles, porque todo lo que eres forma parte de lo que amo. 🫂💘🫶🏻

Quiero seguir construyendo recuerdos contigo, compartir sueños, apoyarte en cada paso que des y ser ese lugar seguro al que siempre puedas volver. Mi amor por ti no tiene límites ni condiciones; es puro, fuerte y verdadero. 🥺🫶🏻💗

Te amo hoy, mañana y todos los días que la vida me permita caminar a tu lado. 🥺🫂🤍""",
    "color_principal": "#ff3d6e",
    "color_secundario": "#ffc2d1",
    "accent": "#fff4f7",
}

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>{titulo}</title>
  <style>
    :root {{
      --primary: {color_principal};
      --secondary: {color_secundario};
      --accent: {accent};
      --ink: #521b2a;
      --glow: rgba(255, 61, 110, .6);
    }}

    * {{ box-sizing: border-box; }}
    html, body {{
      height: 100%;
      margin: 0;
      font-family: "Segoe UI", system-ui, -apple-system, Roboto, Arial, "Noto Sans", sans-serif;
      color: var(--ink);
      background: radial-gradient(1500px 800px at 20% 10%, #ffe6ee 0%, #ffeef3 40%, #fff 70%) fixed,
                  linear-gradient(120deg, #fff 0%, #fff 40%, #fff7fa 100%) fixed;
      overflow-x: hidden;
    }}

    .bg {{
      position: fixed;
      inset: 0;
      pointer-events: none;
      background:
        radial-gradient(circle at 10% 10%, rgba(255, 61, 110, .12), transparent 35%),
        radial-gradient(circle at 90% 20%, rgba(255, 182, 193, .15), transparent 35%),
        radial-gradient(circle at 20% 85%, rgba(255, 61, 110, .08), transparent 45%);
      filter: blur(10px) saturate(1.1);
      animation: breathe 10s ease-in-out infinite;
      z-index: 0;
    }}
    @keyframes breathe {{
      0%, 100% {{ transform: scale(1); opacity: .9; }}
      50%      {{ transform: scale(1.03); opacity: 1; }}
    }}

    .wrap {{
      position: relative;
      z-index: 1;
      min-height: 100%;
      display: grid;
      place-items: center;
      padding: 24px;
    }}

    .card {{
      width: min(920px, 92vw);
      background: linear-gradient(180deg, white 0%, #fff9fb 100%);
      border-radius: 22px;
      box-shadow:
        0 20px 60px rgba(82, 27, 42, .15),
        0 0 0 1px rgba(255, 61, 110, .10) inset;
      overflow: hidden;
      transform-style: preserve-3d;
      transform: perspective(1200px) rotateX(0deg);
      transition: transform .8s cubic-bezier(.2,.8,.2,1), box-shadow .4s ease;
      position: relative;
    }}
    .card:hover {{
      transform: perspective(1200px) rotateX(0deg) translateY(-2px);
      box-shadow:
        0 28px 70px rgba(82, 27, 42, .18),
        0 0 0 1px rgba(255, 61, 110, .12) inset;
    }}

    .header {{
      position: relative;
      padding: 28px 24px;
      text-align: center;
      background:
        linear-gradient(135deg, rgba(255, 182, 193, .2) 0%, rgba(255, 61, 110, .12) 100%);
      border-bottom: 1px solid rgba(255, 61, 110, .12);
    }}
    .title {{
      margin: 0;
      font-size: clamp(28px, 4.6vw, 44px);
      line-height: 1.1;
      letter-spacing: .4px;
      color: var(--primary);
      text-shadow: 0 2px 10px rgba(255, 61, 110, .15);
      filter: drop-shadow(0 3px 6px rgba(255, 61, 110, .12));
      position: relative;
    }}
    .subtitle {{
      margin: 8px 0 0 0;
      font-size: clamp(14px, 2.4vw, 18px);
      opacity: .8;
      color: #7a3448;
    }}

    .body {{
      padding: clamp(20px, 4vw, 36px);
      display: grid;
      grid-template-columns: 1.3fr .9fr;
      gap: clamp(16px, 3vw, 28px);
    }}
    @media (max-width: 860px) {{
      .body {{ grid-template-columns: 1fr; }}
    }}

    .envelope {{
      position: relative;
      background: linear-gradient(180deg, #fff, #fff5f7);
      border-radius: 18px;
      border: 1px solid rgba(255, 61, 110, .16);
      padding: 18px;
      display: grid;
      place-items: center;
      cursor: pointer;
      transition: transform .5s ease, box-shadow .4s ease;
      box-shadow: 0 10px 28px rgba(255, 61, 110, .12);
      isolation: isolate;
    }}
    .envelope:hover {{
      transform: translateY(-3px);
      box-shadow: 0 18px 40px rgba(255, 61, 110, .18);
    }}
    .envelope .flap {{
      width: 160px; height: 100px;
      background: linear-gradient(135deg, var(--secondary), #ffd6e1);
      clip-path: polygon(0 0, 100% 0, 50% 60%);
      border-radius: 12px 12px 4px 4px;
      position: relative;
      box-shadow: 0 8px 22px rgba(255, 61, 110, .22);
      animation: heartbeat 1.6s ease-in-out infinite;
    }}
    @keyframes heartbeat {{
      0%, 100% {{ transform: scale(1); }}
      20% {{ transform: scale(1.04); }}
      40% {{ transform: scale(1); }}
      60% {{ transform: scale(1.04); }}
      80% {{ transform: scale(1); }}
    }}
    .envelope .seal {{
      position: absolute;
      top: 58%;
      left: 50%;
      transform: translate(-50%, -50%);
      width: 52px; height: 52px;
      border-radius: 50%;
      background: radial-gradient(circle at 30% 30%, #fff, #ffd2dd 60%, #ff94af 100%);
      box-shadow: 0 10px 18px rgba(255, 61, 110, .28);
      display: grid;
      place-items: center;
      color: var(--ink);
      font-weight: 700;
      letter-spacing: .4px;
      border: 1px solid rgba(82, 27, 42, .08);
    }}

    .letter {{
      position: relative;
      background: #fff;
      border-radius: 16px;
      border: 1px solid rgba(255, 61, 110, .16);
      box-shadow: 0 10px 24px rgba(82, 27, 42, .12);
      padding: clamp(16px, 2.8vw, 24px);
      overflow: hidden;
    }}

    .to {{
      font-weight: 700;
      color: var(--primary);
      margin: 0 0 8px 0;
      letter-spacing: .3px;
    }}
    .message {{
      font-size: clamp(16px, 2.6vw, 19px);
      line-height: 1.7;
      opacity: .95;
      white-space: pre-wrap;
      min-height: 110px;
    }}
    .signature {{
      margin-top: 18px;
      text-align: right;
      font-weight: 600;
      color: #7a3448;
    }}

    .actions {{
      margin-top: 14px;
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
    }}
    .btn {{
      appearance: none;
      border: none;
      border-radius: 999px;
      padding: 10px 16px;
      font-weight: 700;
      letter-spacing: .3px;
      background: linear-gradient(180deg, var(--primary), #ff527c);
      color: white;
      box-shadow: 0 10px 24px rgba(255, 61, 110, .35);
      cursor: pointer;
      transition: transform .2s ease, box-shadow .2s ease, filter .2s ease;
    }}
    .btn:hover {{ transform: translateY(-1px); filter: brightness(1.05); }}
    .btn:active {{ transform: translateY(0); box-shadow: 0 8px 18px rgba(255, 61, 110, .35); }}
    .btn.secondary {{
      background: linear-gradient(180deg, #ffd1dd, #ffabc2);
      color: #521b2a;
      box-shadow: 0 10px 24px rgba(255, 193, 208, .6);
    }}

    .hearts {{
      pointer-events: none;
      position: absolute;
      inset: 0;
      overflow: hidden;
      z-index: 0;
      opacity: .9;
    }}
    .heart {{
      position: absolute;
      width: var(--s, 18px);
      height: var(--s, 18px);
      transform: translate(-50%, -50%);
      background: radial-gradient(circle at 30% 30%, #fff, var(--primary) 40%, #ff275e 60%);
      clip-path: path("M12.5,3 C12.5,1.62 11.38,0.5 10,0.5 C8.88,0.5 7.92,1.19 7.5,2.18 C7.08,1.19 6.12,0.5 5,0.5 C3.62,0.5 2.5,1.62 2.5,3 C2.5,6.28 7.5,9.5 7.5,9.5 C7.5,9.5 12.5,6.28 12.5,3 Z");
      opacity: 0;
      animation: floatUp var(--dur, 4s) ease-in forwards;
      filter: drop-shadow(0 6px 10px rgba(255, 61, 110, .35));
    }}
    @keyframes floatUp {{
      0%   {{ transform: translate(var(--x, 0), var(--y, 0)) scale(.8) rotate(0deg); opacity: 0; }}
      10%  {{ opacity: .9; }}
      100% {{ transform: translate(var(--xEnd, 0), -120vh) scale(1.35) rotate(28deg); opacity: 0; }}
    }}

    .typewriter {{
      border-right: 2px solid var(--primary);
      white-space: pre-wrap;
      overflow: hidden;
      animation: caret .9s steps(1) infinite;
    }}
    @keyframes caret {{
      50% {{ border-color: transparent; }}
    }}

    .twinkle {{
      position: absolute;
      width: 6px; height: 6px;
      border-radius: 50%;
      background: radial-gradient(circle, #fff, rgba(255,255,255,.2));
      box-shadow: 0 0 18px 4px rgba(255,255,255,.7);
      opacity: 0;
      animation: twinkle 1.2s ease-out forwards;
    }}
    @keyframes twinkle {{
      0% {{ transform: scale(.4); opacity: 0; }}
      40% {{ opacity: 1; }}
      100% {{ transform: scale(1.8); opacity: 0; }}
    }}

    .footer {{
      padding: 14px 18px 24px;
      text-align: center;
      color: #a05569;
      font-size: 14px;
      opacity: .9;
    }}
  </style>
</head>
<body>
  <div class="bg" aria-hidden="true"></div>

  <div class="wrap">
    <div class="card" id="card">
      <div class="header">
        <h1 class="title" id="mainTitle">{titulo}</h1>
        <p class="subtitle" id="subtitle">Toca el sobre para abrir tu carta ✉️</p>
      </div>

      <div class="body">
        <section class="letter" aria-live="polite">
          <p class="to" id="toText">Para: <span></span></p>
          <div class="message typewriter" id="message"></div>
          <p class="signature" id="signature"></p>
          <div class="actions">
            <button class="btn" id="replayBtn">Repetir animación</button>
            <button class="btn secondary" id="themeBtn">Cambiar colores</button>
          </div>
          <div class="hearts" id="hearts" aria-hidden="true"></div>
        </section>

        <aside class="envelope" id="envelope" role="button" aria-label="Abrir carta">
          <div class="flap"></div>
          <div class="seal" id="seal">♥</div>
        </aside>
      </div>

      <div class="footer" id="footerNote"></div>
    </div>
  </div>

  <script>
    const CONFIG = {{
      titulo: {titulo_js},
      nombreReceptor: {nombre_receptor_js},
      nombreEmisor: {nombre_emisor_js},
      fecha: {fecha_js},
      mensaje: {mensaje_js},
      colorPrincipal: "{color_principal}",
      colorSecundario: "{color_secundario}",
      accent: "{accent}"
    }};

    const root = document.documentElement;
    const el = {{
      title: document.getElementById("mainTitle"),
      subtitle: document.getElementById("subtitle"),
      to: document.getElementById("toText").querySelector("span"),
      msg: document.getElementById("message"),
      sign: document.getElementById("signature"),
      env: document.getElementById("envelope"),
      seal: document.getElementById("seal"),
      hearts: document.getElementById("hearts"),
      replay: document.getElementById("replayBtn"),
      theme: document.getElementById("themeBtn"),
      footer: document.getElementById("footerNote"),
      card: document.getElementById("card")
    }};

    function applyTheme({{ colorPrincipal, colorSecundario, accent }}) {{
      root.style.setProperty("--primary", colorPrincipal);
      root.style.setProperty("--secondary", colorSecundario);
      root.style.setProperty("--accent", accent || "#fff4f7");
      el.card.animate([{{ filter: "brightness(1.02)" }}, {{ filter: "brightness(1)" }}], {{ duration: 600, easing: "ease-out" }});
    }}

    function typewriter(node, text, speed = 22) {{
      node.classList.add("typewriter");
      node.textContent = "";
      return new Promise(resolve => {{
        let i = 0;
        const timer = setInterval(() => {{
          node.textContent += text.charAt(i++);
          if (i >= text.length) {{
            clearInterval(timer);
            node.classList.remove("typewriter");
            resolve();
          }}
        }}, speed);
      }});
    }}

    function floatHeart(x, y) {{
      const h = document.createElement("div");
      h.className = "heart";
      const size = 12 + Math.random() * 22;
      const dur = 3.5 + Math.random() * 2.2;
      const xEnd = (Math.random() * 120 - 60) + "vw";

      h.style.setProperty("--s", size + "px");
      h.style.setProperty("--dur", dur + "s");
      h.style.setProperty("--x", x + "px");
      h.style.setProperty("--y", y + "px");
      h.style.setProperty("--xEnd", xEnd);

      el.hearts.appendChild(h);
      h.addEventListener("animationend", () => h.remove(), {{ once: true }});
    }}

    function sparkle(x, y) {{
      const s = document.createElement("div");
      s.className = "twinkle";
      s.style.left = x + "px";
      s.style.top = y + "px";
      s.style.background = "radial-gradient(circle, #fff, rgba(255,255,255,.3))";
      el.hearts.appendChild(s);
      setTimeout(() => s.remove(), 1200);
    }}

    function burst(x, y, n = 12) {{
      for (let i = 0; i < n; i++) {{
        setTimeout(() => floatHeart(x + (Math.random()*80 - 40), y + (Math.random()*60 - 30)), i * 40);
      }}
      sparkle(x, y);
    }}

    function autoHearts() {{
      const {{ width, height }} = el.hearts.getBoundingClientRect();
      const x = Math.random() * width;
      const y = height + 40;
      floatHeart(x, y);
    }}

    function openLetter() {{
      el.env.animate([
        {{ transform: "translateY(0) scale(1)" }},
        {{ transform: "translateY(-8px) scale(1.02)" }},
        {{ transform: "translateY(0) scale(1)" }}
      ], {{ duration: 600, easing: "cubic-bezier(.2,.8,.2,1)" }});

      el.seal.animate([
        {{ boxShadow: "0 0 0 rgba(255,61,110,0)", transform: "scale(1)" }},
        {{ boxShadow: "0 0 26px rgba(255,61,110,.65)", transform: "scale(1.06)" }},
        {{ boxShadow: "0 0 0 rgba(255,61,110,0)", transform: "scale(1)" }}
      ], {{ duration: 900, easing: "ease-out" }});

      playSequence(true);
    }}

    async function playSequence(fromEnvelope = false) {{
      el.msg.textContent = "";
      el.msg.classList.remove("typewriter");
      el.subtitle.textContent = "Con todo mi corazón…";

      if (fromEnvelope) burst(window.innerWidth * 0.75, el.env.getBoundingClientRect().top);

      await typewriter(el.msg, CONFIG.mensaje, 22);

      el.sign.textContent = `Con amor, ${{CONFIG.nombreEmisor}} — ${{CONFIG.fecha}}`;
      el.sign.animate([{{ opacity: 0, transform: "translateY(6px)" }}, {{ opacity: 1, transform: "translateY(0)" }}],
        {{ duration: 500, easing: "ease-out" }});

      for (let i = 0; i < 10; i++) {{
        setTimeout(() => floatHeart(Math.random() * window.innerWidth, window.innerHeight - 20), 120 * i);
      }}
    }}

    function setTexts() {{
      el.title.textContent = CONFIG.titulo;
      el.to.textContent = CONFIG.nombreReceptor;
      el.footer.textContent = "Hecho con ♥ para ti";
    }}

    function cycleTheme() {{
      const palettes = [
        {{ colorPrincipal: "#ff3d6e", colorSecundario: "#ffc2d1", accent: "#fff4f7" }},
        {{ colorPrincipal: "#c850c0", colorSecundario: "#ffb3d1", accent: "#fff0ff" }},
        {{ colorPrincipal: "#ff6f61", colorSecundario: "#ffd1c1", accent: "#fff5f1" }},
        {{ colorPrincipal: "#e83e8c", colorSecundario: "#ffc9de", accent: "#fff2f8" }}
      ];
      cycleTheme.idx = (cycleTheme.idx ?? 0) + 1;
      applyTheme(palettes[cycleTheme.idx % palettes.length]);
    }}

    (function init() {{
      setTexts();
      applyTheme(CONFIG);
      el.env.addEventListener("click", openLetter);
      el.replay.addEventListener("click", () => playSequence(false));
      el.theme.addEventListener("click", cycleTheme);
      setInterval(autoHearts, 700);
      document.addEventListener("pointerdown", (e) => {{
        if (e.target.closest('.btn') || e.target.closest('.envelope')) return;
        burst(e.clientX, e.clientY, 10 + Math.floor(Math.random()*8));
      }});
      const mx = 18;
      document.addEventListener("mousemove", (e) => {{
        const {{ innerWidth: w, innerHeight: h }} = window;
        const rx = ((e.clientY / h) - 0.5) * -mx;
        const ry = ((e.clientX / w) - 0.5) * mx;
        el.card.style.transform = `perspective(1200px) rotateX(${{rx}}deg) rotateY(${{ry}}deg)`;
      }});
      document.addEventListener("mouseleave", () => {{
        el.card.style.transform = "perspective(1200px) rotateX(0deg) rotateY(0deg)";
      }});
      el.subtitle.textContent = "Toca el sobre para abrir tu carta ✉️";
    }})();
  </script>
</body>
</html>
"""

def _js_str(s: str) -> str:
    """Escapa el texto para incrustarlo como string literal JS entre backticks."""
    if s is None:
        return "``"
    s = s.replace("`", "\\`")
    return f"`{s}`"

def generar_html(cfg: dict) -> str:
    html = HTML_TEMPLATE.format(
        titulo=cfg["titulo"],
        color_principal=cfg["color_principal"],
        color_secundario=cfg["color_secundario"],
        accent=cfg["accent"],
        titulo_js=_js_str(cfg["titulo"]),
        nombre_receptor_js=_js_str(cfg["nombre_receptor"]),
        nombre_emisor_js=_js_str(cfg["nombre_emisor"]),
        fecha_js=_js_str(cfg["fecha"]),
        mensaje_js=_js_str(cfg["mensaje"]),
    )
    return html

# Ruta principal del servidor
@app.route("/")
def home():
    return generar_html(CONFIG)

if __name__ == "__main__":
    # Render asigna dinámicamente el puerto en la variable de entorno PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
