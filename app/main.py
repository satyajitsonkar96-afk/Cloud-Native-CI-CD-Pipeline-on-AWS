from flask import Flask, render_template_string
from datetime import datetime
import random

app = Flask(__name__)

def get_pipeline_data():
    # Simulated data (replace with Jenkins API later)
    statuses = ["Running", "Failed", "Building"]
    status = random.choice(statuses)

    return {
        "status": status,
        "version": "v1.2.3",
        "build": "#42",
        "last_deploy": datetime.now().strftime("%d %b %Y, %I:%M %p")
    }

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Cloud CI/CD Dashboard</title>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    height: 100vh;
    font-family: 'Segoe UI', sans-serif;
    background: linear-gradient(135deg, #667eea, #764ba2);
    display: flex;
    justify-content: center;
    align-items: center;
}

.card {
    background: rgba(255, 255, 255, 0.12);
    backdrop-filter: blur(18px);
    border-radius: 20px;
    padding: 40px;
    width: 380px;
    text-align: center;
    color: white;
    box-shadow: 0 10px 40px rgba(0,0,0,0.3);
    animation: fadeIn 1s ease;
}

h1 {
    font-size: 26px;
    margin-bottom: 8px;
}

.subtitle {
    font-size: 14px;
    opacity: 0.85;
}

.status {
    margin-top: 20px;
    padding: 12px 18px;
    border-radius: 12px;
    font-weight: bold;
    display: inline-block;
    animation: pulse 1.5s infinite;
}

.running { background: #22c55e; color: black; }
.failed { background: #ef4444; color: white; }
.building { background: #facc15; color: black; }

.badge {
    margin-top: 15px;
    font-size: 13px;
    background: rgba(255,255,255,0.2);
    padding: 6px 12px;
    border-radius: 8px;
    display: inline-block;
}

.info {
    margin-top: 20px;
    font-size: 13px;
    opacity: 0.9;
    line-height: 1.6;
}

.buttons {
    margin-top: 20px;
}

button {
    padding: 10px 14px;
    border: none;
    border-radius: 8px;
    margin: 5px;
    cursor: pointer;
    font-weight: bold;
}

.logs { background: #3b82f6; color: white; }
.deploy { background: #10b981; color: white; }

.footer {
    margin-top: 20px;
    font-size: 12px;
    opacity: 0.7;
}

@keyframes pulse {
    0% { box-shadow: 0 0 0 0 rgba(255,255,255,0.4); }
    70% { box-shadow: 0 0 0 10px rgba(255,255,255,0); }
    100% { box-shadow: 0 0 0 0 rgba(255,255,255,0); }
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px);}
    to { opacity: 1; transform: translateY(0);}
}
</style>
</head>

<body>

<div class="card">
    <h1>🚀 CI/CD Pipeline</h1>
    <div class="subtitle">Cloud-Native Deployment Dashboard</div>

    <div class="status {{ status_class }}">
        {{ status_icon }} {{ status }}
    </div>

    <div class="badge">Environment: Production</div>

    <div class="info">
        <div>Version: {{ version }}</div>
        <div>Build: {{ build }}</div>
        <div>Last Deploy: {{ last_deploy }}</div>
    </div>

    <div class="buttons">
        <button class="logs">📄 View Logs</button>
        <button class="deploy">🔄 Redeploy</button>
    </div>

    <div class="footer">
        Jenkins 🧩 • Docker 🐳 • AWS ☁️ • Nginx 🌐
    </div>
</div>

</body>
</html>
"""

@app.route('/')
def home():
    data = get_pipeline_data()

    status_map = {
        "Running": ("running", "✅"),
        "Failed": ("failed", "❌"),
        "Building": ("building", "⚙️")
    }

    status_class, status_icon = status_map[data["status"]]

    return render_template_string(
        HTML_PAGE,
        status=data["status"],
        status_class=status_class,
        status_icon=status_icon,
        version=data["version"],
        build=data["build"],
        last_deploy=data["last_deploy"]
    )

@app.route('/health')
def health():
    return {"status": "healthy"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
