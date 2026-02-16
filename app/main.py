from flask import Flask, render_template_string

app = Flask(__name__)

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
    width: 360px;
    text-align: center;
    color: white;
    box-shadow: 0 10px 40px rgba(0,0,0,0.3);
}

h1 {
    font-size: 26px;
    margin-bottom: 10px;
}

p {
    font-size: 15px;
    opacity: 0.9;
}

.status {
    margin-top: 20px;
    padding: 12px;
    border-radius: 12px;
    background: #22c55e;
    color: black;
    font-weight: bold;
    display: inline-block;
    animation: pulse 1.5s infinite;
}

@keyframes pulse {
    0% { box-shadow: 0 0 0 0 rgba(34,197,94,0.6); }
    70% { box-shadow: 0 0 0 10px rgba(34,197,94,0); }
    100% { box-shadow: 0 0 0 0 rgba(34,197,94,0); }
}

.badge {
    margin-top: 15px;
    font-size: 13px;
    background: rgba(255,255,255,0.2);
    padding: 6px 12px;
    border-radius: 8px;
    display: inline-block;
}

.footer {
    margin-top: 20px;
    font-size: 12px;
    opacity: 0.7;
}
</style>
</head>

<body>

<div class="card">
    <h1>🚀 CI/CD Pipeline</h1>
    <p>Cloud-Native App Deployed Successfully</p>

    <div class="status">✅ Running</div>

    <div class="badge">Environment: Production</div>

    <div class="footer">
        Jenkins • Docker • AWS EC2 • Nginx
    </div>
</div>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

@app.route('/health')
def health():
    return {"status": "healthy"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
