from flask import Flask, jsonify

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return jsonify({
        "message": "🚀 Cloud Native CI/CD Pipeline is Running!",
        "status": "success"
    })

# Health check route (VERY IMPORTANT)
@app.route('/health')
def health():
    return jsonify({
        "status": "healthy"
    })

# Entry point
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
