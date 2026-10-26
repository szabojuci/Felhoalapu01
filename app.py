import os
import socket
from datetime import datetime
from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

# Kezdeti mintaadatok (In-memory adatok a REST API-hoz)
ITEMS = [
    {"id": 1, "name": "Felhoalapu Szamitastechnika", "status": "Aktiv"},
    {"id": 2, "name": "Docker Multi-stage Build", "status": "Kesz"},
    {"id": 3, "name": "Kubernetes Deployment", "status": "Folyamatban"}
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="hu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>REST API & Webapp - Felhőalapú Számítástechnika</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #0f172a; color: #f8fafc; margin: 0; padding: 2rem; }
        .container { max-width: 800px; margin: 0 auto; background: #1e293b; padding: 2rem; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); }
        h1 { color: #38bdf8; border-bottom: 2px solid #334155; padding-bottom: 0.5rem; }
        .badge { background: #0284c7; color: white; padding: 0.3rem 0.6rem; border-radius: 4px; font-size: 0.85rem; }
        .endpoint { background: #0f172a; padding: 1rem; border-radius: 8px; margin: 1rem 0; border-left: 4px solid #38bdf8; }
        code { color: #f43f5e; background: #334155; padding: 0.2rem 0.4rem; border-radius: 4px; }
        .btn { background: #38bdf8; color: #0f172a; border: none; padding: 0.5rem 1rem; font-weight: bold; border-radius: 6px; cursor: pointer; }
        .btn:hover { background: #7dd3fc; }
        pre { background: #0f172a; padding: 1rem; border-radius: 6px; overflow-x: auto; color: #4ade80; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Felhőalapú REST API Microservice</h1>
        <p><strong>Konténer ID / Pod Név:</strong> <code>{{ hostname }}</code></p>
        <p><strong>Konfigurált Üzenet:</strong> <span class="badge">{{ message }}</span></p>

        <h2>Elérhető REST API Végpontok:</h2>
        
        <div class="endpoint">
            <h3>1. GET <code>/api/v1/info</code></h3>
            <p>Rendszer- és konténerinformációk lekérése JSON-ban.</p>
            <button class="btn" onclick="fetchApi('/api/v1/info')">Tesztelés</button>
        </div>

        <div class="endpoint">
            <h3>2. GET <code>/api/v1/items</code></h3>
            <p>Adatlista lekérése JSON formátumban.</p>
            <button class="btn" onclick="fetchApi('/api/v1/items')">Tesztelés</button>
        </div>

        <div class="endpoint">
            <h3>3. GET <code>/health</code></h3>
            <p>Kubernetes Health Check végpont.</p>
            <button class="btn" onclick="fetchApi('/health')">Tesztelés</button>
        </div>

        <h2>API Válasz (JSON):</h2>
        <pre id="json-response">Kattints valamelyik "Tesztelés" gombra az API válasz megtekintéséhez...</pre>
    </div>

    <script>
        async function fetchApi(endpoint) {
            const res = await fetch(endpoint);
            const data = await res.json();
            document.getElementById('json-response').innerText = JSON.stringify(data, null, 2);
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    message = os.environ.get("APP_MESSAGE", "REST API Működik")
    hostname = socket.gethostname()
    return render_template_string(HTML_TEMPLATE, message=message, hostname=hostname)

@app.route("/api/v1/info", methods=["GET"])
def get_info():
    return jsonify({
        "status": "success",
        "app_name": "Cloud REST API Service",
        "hostname": socket.gethostname(),
        "timestamp": datetime.now().isoformat(),
        "env_message": os.environ.get("APP_MESSAGE", "Nincs beállítva"),
        "port": os.environ.get("PORT", "8080")
    })

@app.route("/api/v1/items", methods=["GET"])
def get_items():
    return jsonify({
        "status": "success",
        "count": len(ITEMS),
        "data": ITEMS
    })

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "UP", "service": "Healthy"}), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
