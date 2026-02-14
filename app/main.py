from flask import Flask, jsonify
import os
import logging

app = Flask(__name__)

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Environment variables
APP_NAME = os.getenv("APP_NAME", "Cloud DevOps App")
VERSION = os.getenv("VERSION", "1.0")

@app.route("/")
def home():
    logger.info("Home endpoint accessed")
    return f"{APP_NAME} - Version {VERSION}"

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "app": APP_NAME,
        "version": VERSION
    })

@app.route("/info")
def info():
    return jsonify({
        "message": "This is a CI/CD deployed app",
        "author": "Satyajit Sonkar",
        "project": "Cloud Native DevOps Pipeline"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
