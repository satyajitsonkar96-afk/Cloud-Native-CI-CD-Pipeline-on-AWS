@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Cloud DevOps App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(to right, #4facfe, #00f2fe);
                margin: 0;
                padding: 0;
                text-align: center;
                color: white;
            }
            .container {
                margin-top: 100px;
            }
            h1 {
                font-size: 40px;
            }
            p {
                font-size: 18px;
            }
            .btn {
                display: inline-block;
                margin: 15px;
                padding: 12px 25px;
                font-size: 16px;
                color: white;
                background-color: #ff7b00;
                border: none;
                border-radius: 8px;
                text-decoration: none;
                transition: 0.3s;
            }
            .btn:hover {
                background-color: #ff5500;
                transform: scale(1.05);
            }
            .card {
                background: rgba(255,255,255,0.1);
                padding: 20px;
                border-radius: 10px;
                display: inline-block;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Cloud DevOps App</h1>
            <p>Deployed using Jenkins CI/CD on AWS</p>

            <div class="card">
                <p><strong>Version:</strong> 1.0</p>
                <p><strong>Author:</strong> Satyajit Sonkar</p>
            </div>

            <div>
                <a href="/health" class="btn">Health Check</a>
                <a href="/info" class="btn">App Info</a>
            </div>
        </div>
    </body>
    </html>
    """
