Smart CI/CD Platform 🚀
Intelligent CI/CD Deployment & Auto Rollback Platform using AWS

📌 Project Overview
Smart CI/CD Platform is a cloud-based deployment automation system built using Flask, GitHub Actions, and AWS EC2.

It automates the complete software delivery pipeline including:
Continuous Integration (CI)
Continuous Deployment (CD)
Automated server deployment
Health monitoring
Deployment history tracking
Automatic rollback on failure

This project demonstrates real-world DevOps and Cloud Computing concepts.

⚙️ Features
🔄 Automated CI/CD pipeline using GitHub Actions
☁️ AWS EC2 deployment integration
🧠 Auto rollback on deployment failure
📊 Deployment dashboard (Flask web UI)
📜 Deployment history tracking
❤️ Health check endpoint for monitoring
📦 Backup of previous stable version before deployment
🚀 Zero-downtime deployment simulation
🏗️ System Architecture
Developer
   │
   ▼
GitHub Repository
   │
   ▼
GitHub Actions (CI/CD Pipeline)
   │
   ├── Backup Current Version
   ├── Deploy New Code to EC2
   ├── Run Health Check
   └── Auto Rollback if Failed
   │
   ▼
AWS EC2 Server
   │
   ▼
Flask Application (Dashboard + API)
🧰 Tech Stack
Python (Flask)
GitHub Actions
AWS EC2
Gunicorn
Bash Scripting
HTML/CSS (Dashboard UI)
🔄 CI/CD Workflow
Developer pushes code to main branch
GitHub Actions pipeline is triggered
Current application is backed up
New code is deployed to AWS EC2
Health check is executed (/health)
If successful → deployment completes
If failed → automatic rollback to previous version
🚀 Setup Instructions
1. Clone Repository
git clone https://github.com/your-username/smart-cicd-platform.git
cd smart-cicd-platform
2. Install Dependencies
pip install -r requirements.txt
3. Run Locally
python app.py

Open:

http://127.0.0.1:5000
☁️ AWS Deployment Setup
Required GitHub Secrets:

You must configure these in:

GitHub Repository → Settings → Secrets and Variables → Actions

Add:

EC2_HOST → Your AWS EC2 public IP
EC2_USER → Usually ubuntu
EC2_SSH_KEY → Your private SSH key (.pem content)
🔐 Security Note

All sensitive data (SSH keys, IPs, credentials) are stored securely using GitHub Secrets and are NOT exposed publicly.

📊 Health Check Endpoint
/health

Returns:

healthy

Used by CI/CD pipeline to verify successful deployment.

📁 Project Structure
smart-cicd-platform/
│
├── app.py
├── requirements.txt
├── appspec.yml
├── version.txt
├── analytics.json
├── history.json
│
├── scripts/
│   ├── start_server.sh
│   ├── stop_server.sh
│   └── health_check.sh
│
├── templates/
│   ├── index.html
│   └── history.html
│
└── .github/workflows/
    └── deploy.yml
📸 Screenshots

Add screenshots of dashboard and deployment history here.

Example:

Dashboard view
Deployment history page
CI/CD pipeline success logs
🔮 Future Improvements
Integration with AWS CloudWatch
Real-time monitoring dashboard
Docker containerization
Multi-environment deployment (dev/staging/prod)
Slack/email notifications for deployment status
👨‍💻 Author

Zubair

Cloud Computing Project – Smart CI/CD Platform
GitHub: https://github.com/zubair-fakhar

⭐ Conclusion

This project demonstrates a complete real-world DevOps pipeline with automated deployment, monitoring, and rollback using modern cloud tools.
