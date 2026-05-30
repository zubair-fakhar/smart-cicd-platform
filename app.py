from flask import Flask, render_template
import os

app = Flask(__name__)

with open("version.txt", "r") as f:
    VERSION = f.read().strip()

DEPLOYMENT_STATUS = "Successful"

@app.route('/')
def home():
    return render_template(
        'index.html',
        version=VERSION,
        status=DEPLOYMENT_STATUS
    )

@app.route('/health')
def health():
    return "healthy"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
