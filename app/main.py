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
            background: linear-gradient(135deg, #4facfe, #00f2fe);
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(15px);
            border-radius: 20px;
            padding: 40px;
            width: 350px;
            text-align: center;
            color: white;
            box-shadow: 0 8px 32px rgba(0,0,0,0.2);
        }

        h1 {
            font-size: 28px;
            margin-bottom: 15px;
        }

        p {
            font-size: 16px;
            opacity: 0.9;
        }

        .status {
            margin-top: 25px;
            padding: 12px;
            border-radius: 10px;
            background: #22c55e;
            color: black;
            font-weight: bold;
            font-size: 16px;
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
        <p>Your Cloud-Native App is Live on AWS</p>

        <div class="status">✅ Status: Running</div>

        <div class="footer">
            Powered by Jenkins • Docker • AWS
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

