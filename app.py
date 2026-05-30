from flask import Flask, render_template, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)

# Version Tracking
with open("version.txt", "r") as f:
    VERSION = f.read().strip()

# Analytics
with open("analytics.json", "r") as f:
    stats = json.load(f)

SUCCESSFUL_DEPLOYMENTS = stats["success"]
FAILED_DEPLOYMENTS = stats["failed"]
ROLLBACKS = stats["rollbacks"]

DEPLOYMENT_STATUS = "Healthy"


# Main Dashboard
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


# Deployment History Page
@app.route('/history')
def history():

    with open("history.json") as f:
        history_data = json.load(f)

    return render_template(
        "history.html",
        history=history_data
    )


# Health Check
@app.route('/health')
def health():
    return "healthy"


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
