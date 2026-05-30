from flask import Flask, render_template, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)

with open("version.txt", "r") as f:
    VERSION = f.read().strip()

DEPLOYMENT_STATUS = "Healthy"

SUCCESSFUL_DEPLOYMENTS = 5
FAILED_DEPLOYMENTS = 1
ROLLBACKS = 1

@app.route('/history')
def history():

    with open("history.json") as f:
        history_data = json.load(f)

    return render_template(
        "history.html",
        history=history_data
    )

@app.route('/health')
def health():
    return "healthy"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
