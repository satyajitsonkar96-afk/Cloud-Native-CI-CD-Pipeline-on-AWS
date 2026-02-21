from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Cloud DevOps App - Version 1.0"
