from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Python Server</title>
        <style>
            body {
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #1d2671, #c33764);
                color: white;
                text-align: center;
            }
            .card {
                background: rgba(255,255,255,0.1);
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.3);
                backdrop-filter: blur(10px);
            }
            h1 {
                font-size: 36px;
                margin-bottom: 10px;
            }
            p {
                font-size: 18px;
                opacity: 0.9;
            }
            .btn {
                margin-top: 20px;
                padding: 10px 20px;
                background: white;
                color: #c33764;
                border-radius: 25px;
                text-decoration: none;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 My Python App is Live!</h1>
            <p>Successfully deployed on a cloud server.</p>
            <a class="btn" href="#">Explore More</a>
        </div>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

