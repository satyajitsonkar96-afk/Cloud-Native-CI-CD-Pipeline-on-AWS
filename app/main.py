from flask import Flask, jsonify, render_template
import datetime
import platform
import os

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Health Check
@app.route("/health")
def health():
    return render_template("health.html")

# Application Info
@app.route("/info")
def info():
    return render_template("app_info.html")

# Metrics
@app.route("/metrics")
def metrics():
    return render_template("metrics.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
