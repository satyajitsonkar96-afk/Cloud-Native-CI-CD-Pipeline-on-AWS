@app.route('/')
def home():
    return """
z<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>CI/CD Dashboard - Animated</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Segoe UI', sans-serif;
}

body {
    height: 100vh;
    background: linear-gradient(270deg, #0f2027, #203a43, #2c5364);
    background-size: 600% 600%;
    animation: bgMove 12s ease infinite;
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
    overflow: hidden; /* prevent scroll from bubbles */
    position: relative;
}

/* Background animation */
@keyframes bgMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Card - enhanced with pulse animation on hover */
.card {
    width: 380px;
    padding: 30px;
    border-radius: 20px;
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(15px);
    box-shadow: 0 20px 50px rgba(0,0,0,0.5);
    text-align: center;
    animation: fadeIn 1.2s ease;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    position: relative;
    z-index: 10;
    border: 1px solid rgba(255,255,255,0.1);
}

.card:hover {
    transform: scale(1.02) translateY(-5px);
    box-shadow: 0 30px 60px rgba(0, 255, 200, 0.3);
    border-color: rgba(0, 255, 200, 0.3);
}

/* Fade animation */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}

.title {
    font-size: 22px;
    margin-bottom: 10px;
    text-shadow: 0 0 5px rgba(0,255,255,0.5);
}

/* Status with spinning ring */
.status {
    font-size: 26px;
    font-weight: bold;
    margin: 10px 0;
    color: #00ffcc;
    animation: glow 2s infinite alternate;
    position: relative;
    display: inline-block;
    padding-left: 40px; /* make space for ring */
}

.status::before {
    content: "";
    position: absolute;
    left: 0;
    top: 50%;
    transform: translateY(-50%);
    width: 24px;
    height: 24px;
    border: 3px solid rgba(0, 255, 200, 0.3);
    border-top-color: #00ffcc;
    border-radius: 50%;
    animation: spin 1.5s linear infinite;
}

@keyframes glow {
    from { text-shadow: 0 0 10px #00ffcc; }
    to { text-shadow: 0 0 25px #00ffcc, 0 0 35px #00ffaa; }
}

@keyframes spin {
    0% { transform: translateY(-50%) rotate(0deg); }
    100% { transform: translateY(-50%) rotate(360deg); }
}

.info {
    margin: 8px 0;
    font-size: 15px;
    opacity: 0.9;
}

/* Progress bar with shimmer effect */
.progress-container {
    width: 100%;
    height: 8px;
    background: rgba(255,255,255,0.2);
    border-radius: 10px;
    overflow: hidden;
    margin-top: 20px;
    position: relative;
}

.progress {
    height: 100%;
    width: 0;
    background: linear-gradient(90deg, #00ffcc, #00ff88);
    animation: load 3s forwards;
    position: relative;
}

.progress::after {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
    animation: shimmer 2s infinite;
}

@keyframes load {
    to { width: 100%; }
}

@keyframes shimmer {
    0% { transform: translateX(-100%); }
    100% { transform: translateX(100%); }
}

/* Badge with pulse and shimmer */
.badge {
    margin-top: 15px;
    display: inline-block;
    padding: 8px 18px;
    border-radius: 25px;
    background: #00ff88;
    color: black;
    font-weight: bold;
    animation: pop 0.5s ease, badgePulse 2s infinite 0.5s;
    position: relative;
    overflow: hidden;
}

.badge::after {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.6), transparent);
    transform: translateX(-100%);
    animation: badgeShimmer 2s infinite 1s;
}

@keyframes pop {
    from { transform: scale(0); }
    to { transform: scale(1); }
}

@keyframes badgePulse {
    0% { box-shadow: 0 0 0 0 rgba(0, 255, 136, 0.7); }
    70% { box-shadow: 0 0 0 10px rgba(0, 255, 136, 0); }
    100% { box-shadow: 0 0 0 0 rgba(0, 255, 136, 0); }
}

@keyframes badgeShimmer {
    100% { transform: translateX(100%); }
}

/* Footer */
.footer {
    margin-top: 20px;
    font-size: 12px;
    opacity: 0.6;
    letter-spacing: 1px;
}

/* Floating bubbles - more dynamic */
.bubble {
    position: absolute;
    border-radius: 50%;
    background: rgba(255,255,255,0.1);
    pointer-events: none;
    z-index: 0;
}

.bubble:nth-child(1) {
    width: 80px;
    height: 80px;
    top: 10%;
    left: 15%;
    animation: float 8s infinite alternate ease-in-out;
}

.bubble:nth-child(2) {
    width: 60px;
    height: 60px;
    bottom: 15%;
    right: 10%;
    animation: float 12s infinite alternate-reverse ease-in-out;
}

.bubble:nth-child(3) {
    width: 100px;
    height: 100px;
    top: 60%;
    left: 5%;
    animation: float 10s infinite alternate ease-in-out;
}

.bubble:nth-child(4) {
    width: 40px;
    height: 40px;
    top: 30%;
    right: 20%;
    animation: float 7s infinite alternate ease-in-out;
    background: rgba(255,255,255,0.15);
}

.bubble:nth-child(5) {
    width: 120px;
    height: 120px;
    bottom: 5%;
    left: 20%;
    animation: float 15s infinite alternate-reverse ease-in-out;
    background: rgba(255,255,255,0.05);
}

@keyframes float {
    0% { transform: translate(0, 0) scale(1); }
    100% { transform: translate(30px, -30px) scale(1.1); }
}

/* Additional subtle animation on the title */
.title {
    animation: titleGlow 3s infinite alternate;
}

@keyframes titleGlow {
    0% { text-shadow: 0 0 5px cyan; }
    100% { text-shadow: 0 0 20px cyan, 0 0 30px #00ffaa; }
}
</style>

</head>
<body>

<!-- More bubbles for extra movement -->
<div class="bubble"></div>
<div class="bubble"></div>
<div class="bubble"></div>
<div class="bubble"></div>
<div class="bubble"></div>

<div class="card">
    <div class="title">🚀 CI/CD Dashboard</div>
    <div class="status">✔ Deployment Successful</div>
    <div class="info">Build: <b>#1</b></div>
    <div class="info">Environment: <b>Production</b></div>
    <div class="info">Server: <b>AWS EC2</b></div>
    <div class="info">Container: <b>Docker</b></div>
    <div class="progress-container">
        <div class="progress"></div>
    </div>
    <div class="badge">SUCCESS</div>
    <div class="footer">Jenkins • GitHub • Docker</div>
</div>

</body>
</html>
