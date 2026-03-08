# -*- coding: utf-8 -*-
import os
from datetime import datetime
from flask import Flask

app = Flask(__name__)

# =========================
# CONFIGURACIÓN
# =========================
CONFIG = {
    "titulo": "Feliz día de la mujer mamita",
    "nombre_receptor": "Mi mami hermosa",
    "nombre_emisor": "Tu hijo amado",
    "fecha": datetime.now().strftime("%d de %B de %Y"),
    "mensaje": """Mi mami bella 🥺💘

Feliz Día de la Mujer, mamá❤️🌹
Mi querida madre,
Te quiero recordar lo mucho que te amo mami enserio muchas gracias por todo mami gracias por estar en las buenas y en las malas mami enserio y quiero 
decirte que eres la mejor mama para mi mami espero y difrutes este dia mami te amo mucho mami en verdad no te olvides que siempre estare para ti mami 
porque al final del dia tu siempre estas conmigo mami gracias por trerme al mundo y gracias por ser mi mama en verdad mami tu sabes que no soy de expresarme bien
pero son palabras que sales de mi corazon mami y te las digo con total sinceridad mami
💌💖""",
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
    }}

    * {{ box-sizing: border-box; }}
    html, body {{
      height: 100%;
      margin: 0;
      font-family: "Segoe UI", Roboto, sans-serif;
      color: var(--ink);
      background: #fff5f8;
      overflow-x: hidden;
    }}

    .bg {{
      position: fixed;
      inset: 0;
      background: radial-gradient(circle at 10% 10%, rgba(255, 61, 110, .1), transparent 40%);
      z-index: 0;
    }}

    .wrap {{
      position: relative;
      z-index: 1;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }}

    .card {{
      width: min(900px, 95vw);
      background: white;
      border-radius: 20px;
      box-shadow: 0 15px 50px rgba(0,0,0,0.1);
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }}

    .header {{
      padding: 30px;
      text-align: center;
      background: linear-gradient(to bottom, var(--accent), white);
      border-bottom: 1px solid var(--secondary);
    }}

    .title {{ margin: 0; color: var(--primary); font-size: 2.2rem; }}
    .subtitle {{ margin: 10px 0 0; opacity: 0.7; }}

    .body-content {{
      padding: 30px;
      display: grid;
      grid-template-columns: 1.2fr 0.8fr;
      gap: 30px;
    }}

    @media (max-width: 768px) {{
      .body-content {{ grid-template-columns: 1fr; }}
    }}

    .letter-box {{
      background: #fff;
      border: 1px solid var(--secondary);
      border-radius: 15px;
      padding: 25px;
      min-height: 300px;
      position: relative;
    }}

    .message {{
      font-size: 1.1rem;
      line-height: 1.6;
      white-space: pre-wrap;
      margin-bottom: 20px;
    }}

    .envelope {{
      background: var(--accent);
      border: 2px dashed var(--primary);
      border-radius: 15px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      min-height: 200px;
      transition: 0.3s;
    }}

    .envelope:hover {{ transform: scale(1.02); background: white; }}

    .btn-group {{ display: flex; gap: 10px; margin-top: 20px; }}
    .btn {{
      padding: 10px 20px;
      border: none;
      border-radius: 25px;
      cursor: pointer;
      font-weight: bold;
      transition: 0.3s;
    }}
    .btn-primary {{ background: var(--primary); color: white; }}
    .btn-secondary {{ background: var(--secondary); color: var(--ink); }}

    .footer {{ padding: 15px; text-align: center; font-size: 0.9rem; opacity: 0.6; }}

    /* Cursor de escritura */
    .typing::after {{
      content: '|';
      animation: blink 0.7s infinite;
      color: var(--primary);
    }}
    @keyframes blink {{ 50% {{ opacity: 0; }} }}
  </style>
</head>
<body>
  <div class="bg"></div>
  <div class="wrap">
    <div class="card">
      <div class="header">
        <h1 class="title">{titulo}</h1>
        <p class="subtitle" id="status">Toca el sobre para leer ✉️</p>
      </div>

      <div class="body-content">
        <div class="letter-box">
          <p style="color:var(--primary); font-weight:bold;">Para: {nombre_receptor}</p>
          <div id="text-target" class="message"></div>
          <p id="sig-target" style="text-align:right; font-weight:bold;"></p>
          
          <div class="btn-group">
            <button class="btn btn-primary" onclick="startLetter()">Repetir</button>
            <button class="btn btn-secondary" onclick="location.reload()">Reiniciar</button>
          </div>
        </div>

        <div class="envelope" onclick="startLetter()">
          <div style="font-size: 5rem;">💌</div>
        </div>
      </div>
      <div class="footer">Hecho con ♥ para ti</div>
    </div>
  </div>

  <script>
    const msg = {mensaje_js};
    const emisor = {nombre_emisor_js};
    const fecha = {fecha_js};
    
    let isTyping = false;

    async function typewriter(element, text, speed = 30) {{
      element.innerHTML = "";
      element.classList.add("typing");
      
      // Convertimos el texto en un array para manejar correctamente los emojis (UTF-16)
      const characters = Array.from(text);
      
      for (const char of characters) {{
        element.textContent += char;
        await new Promise(r => setTimeout(r, speed));
      }}
      element.classList.remove("typing");
    }}

    async function startLetter() {{
      if (isTyping) return;
      isTyping = true;
      
      document.getElementById("status").textContent = "Leyendo con amor...";
      document.getElementById("sig-target").textContent = "";
      
      await typewriter(document.getElementById("text-target"), msg);
      
      document.getElementById("sig-target").textContent = `— ${{emisor}}, ${{fecha}}`;
      isTyping = false;
    }}
  </script>
</body>
</html>
"""

def _js_str(s: str) -> str:
    # Asegura que el string sea seguro para JS y use comillas invertidas
    if s is None: return "``"
    return "`" + s.replace("`", "\\`").replace("${", "\\${") + "`"

@app.route("/")
def home():
    return HTML_TEMPLATE.format(
        titulo=CONFIG["titulo"],
        nombre_receptor=CONFIG["nombre_receptor"],
        color_principal=CONFIG["color_principal"],
        color_secundario=CONFIG["color_secundario"],
        accent=CONFIG["accent"],
        mensaje_js=_js_str(CONFIG["mensaje"]),
        nombre_emisor_js=_js_str(CONFIG["nombre_emisor"]),
        fecha_js=_js_str(CONFIG["fecha"])
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
