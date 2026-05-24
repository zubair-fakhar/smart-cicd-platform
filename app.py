from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Smart CI/CD Platform"

@app.route('/health')
def health():
    return "healthy"

app.run(host='0.0.0.0', port=5000)