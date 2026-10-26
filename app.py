import os
import socket
from flask import Flask, render_template_string, jsonify

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="hu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Felhőalapú Számítástechnika - Webalkalmazás</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            color: #333;
        }
        .card {
            background: white;
            padding: 2.5rem;
            border-radius: 15px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            max-width: 500px;
            width: 90%;
            text-align: center;
        }
        h1 { color: #4a5568; margin-bottom: 0.5rem; font-size: 1.8rem; }
        p.subtitle { color: #718096; margin-bottom: 1.5rem; }
        .info-box {
            background: #f7fafc;
            border-left: 4px solid #667eea;
            padding: 1rem;
            margin: 1rem 0;
            text-align: left;
            border-radius: 4px;
        }
        .info-box p { margin: 0.5rem 0; font-size: 0.95rem; }
        .btn {
            background: #667eea;
            color: white;
            border: none;
            padding: 0.75rem 1.5rem;
            font-size: 1rem;
            border-radius: 8px;
            cursor: pointer;
            transition: background 0.3s;
            margin-top: 1rem;
        }
        .btn:hover { background: #5a67d8; }
    </style>
</head>
<body>
    <div class="card">
        <h1>☁️ Felhőalapú Számítástechnika</h1>
        <p class="subtitle">Multi-stage Docker & Kubernetes Bemutató</p>
        
        <div class="info-box">
            <p><strong>Üzenet:</strong> {{ message }}</p>
            <p><strong>Konténer Hostnév (Pod ID):</strong> {{ hostname }}</p>
            <p><strong>Port:</strong> {{ port }}</p>
        </div>

        <button class="btn" onclick="location.reload()">Oldal frissítése</button>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    message = os.environ.get("APP_MESSAGE", "Üdvözöllek a felhőalapú webalkalmazásban!")
    port = os.environ.get("PORT", "8080")
    hostname = socket.gethostname()
    return render_template_string(HTML_TEMPLATE, message=message, port=port, hostname=hostname)

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
