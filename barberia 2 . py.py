from flask import Flask, request, redirect, url_for
import os

app = Flask(__name__)

# Usuario y contraseña de prueba
USUARIO_CORRECTO = "david"
CLAVE_CORRECTA = "1234"

# Datos de la barbería
servicios = {
    "corte": ("Corte de Cabello Clásico ✂️", 10.00),
    "barba": ("Arreglo de Barba Premium 🧔", 8.00),
    "peinado": ("Peinado con Estilo 💈", 6.00)
}

# Imágenes de internet para el catálogo
estilos_fotos = [
    {"nombre": "Corte Degradado / Fade", "url": "https://images.unsplash.com/photo-1621605815971-fbc98d665033?q=80&w=300&auto=format&fit=crop"},
    {"nombre": "Barba Perfilada", "url": "https://images.unsplash.com/photo-1599351431202-1e0f0137899a?q=80&w=300&auto=format&fit=crop"},
    {"nombre": "Estilo Clásico Pompadour", "url": "https://images.unsplash.com/photo-1605497746444-ac9da58d7d98?q=80&w=300&auto=format&fit=crop"}
]

ESTILOS_CSS = """
<style>
    body { font-family: 'Segoe UI', Arial, sans-serif; max-width: 800px; margin: 30px auto; padding: 20px; background-color: #111; color: #fff; }
    .contenedor { background: #1e1e1e; padding: 25px; border-radius: 12px; box-shadow: 0 10px 20px rgba(0,0,0,0.5); }
    h1, h2, h3 { color: #d4af37; text-align: center; text-transform: uppercase; }
    .seccion { background: #2a2a2a; padding: 20px; border-radius: 8px; margin-bottom: 25px; border-left: 4px solid #d4af37; }
    input[type="text"], input[type="password"] { width: 100%; padding: 10px; margin: 10px 0; border-radius: 5px; border: none; background: #333; color: white; }
    input[type="submit"] { background: #d4af37; color: #111; border: none; padding: 12px; border-radius: 6px; cursor: pointer; width: 100%; font-size: 16px; font-weight: bold; text-transform: uppercase; }
    input[type="submit"]:hover { background: #fff; }
    .galeria { display: flex; gap: 15px; justify-content: center; flex-wrap: wrap; margin-top: 15px; }
    .tarjeta-foto { background: #111; padding: 10px; border-radius: 8px; text-align: center; width: 200px; }
    .tarjeta-foto img { width: 100%; height: 150px; object-fit: cover; border-radius: 6px; }
    .error { color: #ff6b6b; text-align: center; font-weight: bold; }
</style>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    error = ""
    if request.method == "POST":
        usuario = request.form.get("txt_usuario")
        clave = request.form.get("txt_clave")
        if usuario == USUARIO_CORRECTO and clave == CLAVE_CORRECTA:
            return redirect(url_for("dashboard"))
        else:
            error = "❌ Usuario o contraseña incorrectos"

    html = f"""
    <html>
    <head><title>Login - Barberia Chopyn</title>{ESTILOS_CSS}</head>
    <body>
        <div class="contenedor" style="max-width: 400px; margin: 100px auto;">
            <h1>🔑 Iniciar Sesión</h1>
            <p style="text-align:center; color:#aaa;">Ingresa a tu cuenta de Barbería Chopyn</p>
            {f'<p class="error">{error}</p>' if error else ''}
            <form method="POST">
                <label>Usuario:</label>
                <input type="text" name="txt_usuario" placeholder="Ej: david" required>
                <label>Contraseña:</label>
                <input type="password" name="txt_clave" placeholder="Ej: 1234" required>
                <br><br>
                <input type="submit" value="Entrar al Sistema 🚀">
            </form>
        </div>
    </body>
    </html>
    """
    return html

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    total = 0.0
    elegidos = []
    if request.method == "POST":
        for clave, datos in servicios.items():
            if request.form.get(clave):
                elegidos.append(datos[0])
                total += datos[1]

    html_cuenta = f"""
    <div class="seccion">
        <h3>👤 Mi Cuenta PREMIUM</h3>
        <p><b>Cliente Especial:</b> David (Estudiante Técnico)</p>
        <p><b>Nivel de Miembro:</b> Platino 🌟 (10% descuento en tu próxima visita)</p>
    </div>
    """

    html_galeria = '<div class="seccion"><h3>✂️ Catálogo de Estilos</h3><div class="galeria">'
    for foto in estilos_fotos:
        html_galeria += f"""
        <div class="tarjeta-foto">
            <img src="{foto['url']}">
            <p style="font-size:14px; margin: 5px 0 0 0;">{foto['nombre']}</p>
        </div>
        """
    html_galeria += "</div></div>"

    html_cotizador = """
    <div class="seccion">
        <h3>🛒 Calculadora de Paquetes</h3>
        <form method="POST">
    """
    for clave, datos in servicios.items():
        html_cotizador += f'<p><input type="checkbox" name="{clave}"> {datos[0]} — <b style="color:#d4af37;">${datos[1]:.2f}</b></p>'
    
    html_cotizador += '<br><input type="submit" value="Calcular Mi Total"></form>'
    
    if total > 0:
        anticipo = total * 0.20
        html_cotizador += f"""
        <div style="background:#1b3a24; padding:15px; border-radius:8px; margin-top:15px;">
            <p><b>Total Neto:</b> ${total:.2f}</p>
            <p style="color:#2ecc71;"><b>💳 Anticipo (20%): ${anticipo:.2f}</b></p>
        </div>
        """
    html_cotizador += "</div>"

    html_final = f"""
    <html>
    <head><title>Panel - Barberia Chopyn</title>{ESTILOS_CSS}</head>
    <body>
        <h1>💈 Panel de Control - Barbería Chopyn</h1>
        <p style="text-align:center;"><a href="/" style="color:#ff6b6b;">Cerrar Sesión 🚪</a></p>
        {html_cuenta}
        {html_galeria}
        {html_cotizador}
    </body>
    </html>
    """
    return html_final

if __name__ == "__main__":
    # Este cambio es clave para que funcione en internet
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
