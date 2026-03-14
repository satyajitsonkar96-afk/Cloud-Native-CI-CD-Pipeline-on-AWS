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
    return jsonify({
        "status": "healthy",
        "application": "Cloud DevOps App",
        "version": "1.0",
        "time": str(datetime.datetime.now())
    })

# Application Info
@app.route("/info")
def info():
    return jsonify({
        "project": "Cloud Native CI/CD Pipeline",
        "developer": "Satyajit Sonkar",
        "team": [
            "Uddhav Warule",
            "Harshal Subhedar",
            "Shree Dhadge",
            "Bhakti Ghodke",
            "Vaishnavi Dhanwat"
        ],
        "platform": "AWS EC2",
        "pipeline": "Jenkins CI/CD",
        "container": "Docker"
    })

# Metrics
@app.route("/metrics")
def metrics():
    return jsonify({
        "python_version": platform.python_version(),
        "server": platform.system(),
        "cpu_count": os.cpu_count(),
        "time": str(datetime.datetime.now())
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
