from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
    <title>My Live Python Server</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- Google Font -->
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600&display=swap" rel="stylesheet">

    <style>
        body {
13.205.60.123            margin: 0;
            padding: 0;
            height: 100vh;
            background: radial-gradient(circle at top, #0f2027, #203a43, #2c5364);
            font-family: 'Orbitron', sans-serif;
            color: #00ffe1;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
        }

        .container {
            text-align: center;
            z-index: 2;
        }

        h1 {
            font-size: 40px;
            margin-bottom: 10px;
        }

        .typing {
            font-size: 22px;
            border-right: 3px solid #00ffe1;
            white-space: nowrap;
            overflow: hidden;
            width: 0;
            animation: typing 4s steps(40, end) forwards, blink 0.8s infinite;
        }

        @keyframes typing {
            from { width: 0 }
            to { width: 100% }
        }

        @keyframes blink {
            50% { border-color: transparent }
        }

        .glow {
            margin-top: 20px;
            font-size: 16px;
            color: white;
            opacity: 0.8;
        }

        /* Floating particles */
        .particle {
            position: absolute;
            width: 4px;
            height: 4px;
            background: #00ffe1;
            border-radius: 50%;
            opacity: 0.5;
            animation: float 10s infinite linear;
        }

        @keyframes float {
            from {
                transform: translateY(100vh) scale(0.5);
            }
            to {
                transform: translateY(-10vh) scale(1);
            }
        }
    </style>
</head>
<body>

<div class="container">
    <h1>🚀 Server Status: ONLINE</h1>
    <div class="typing">My python application is running</div>
    <div class="glow">Deployed on Cloud • Powered by Flask</div>
</div>

<script>
    // Generate floating particles
    for (let i = 0; i < 40; i++) {
        let p = document.createElement("div");
        p.className = "particle";
        p.style.left = Math.random() * 100 + "vw";
        p.style.animationDuration = (5 + Math.random() * 10) + "s";
        p.style.opacity = Math.random();
        document.body.appendChild(p);
    }
</script>

</body>
</html>
""")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

