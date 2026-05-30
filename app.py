from flask import Flask, render_template
from datetime import datetime
import os

app = Flask(__name__)

with open("version.txt", "r") as f:
    VERSION = f.read().strip()

DEPLOYMENT_STATUS = "Healthy"

SUCCESSFUL_DEPLOYMENTS = 5
FAILED_DEPLOYMENTS = 1
ROLLBACKS = 1

@app.route('/')
def home():
    return render_template(
        'index.html',
        version=VERSION,
        status=DEPLOYMENT_STATUS,
        success=SUCCESSFUL_DEPLOYMENTS,
        failed=FAILED_DEPLOYMENTS,
        rollbacks=ROLLBACKS,
        last_deployment=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

@app.route('/health')
def health():
    return "healthy"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
