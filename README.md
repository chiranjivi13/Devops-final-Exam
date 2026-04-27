# DevOps CI Pipeline Final Exam Project

This repository contains the solution for the DevOps CI pipeline task.

## Contents
1. **Web Application**: `index.html`, `style.css`, `app.js` make up a simple, interactive web application.
2. **Docker**: `Dockerfile` uses Nginx to containerize the web application.
3. **Selenium Test**: `test.py` is a Python script using Selenium to test the UI functionality of the web app.
4. **CI/CD Pipeline**: `.github/workflows/ci.yml` defines the GitHub Actions pipeline that automatically tests the code and builds the Docker image on push/PR.
5. **Git Operations**: `git_workflow.ps1` contains the Git commands you need to run to demonstrate branching, committing, and merging.

## How to execute

### 1. Git branching and merging
Since your current terminal doesn't have Git installed, please open a terminal that has Git (like Git Bash) and run the commands printed by:
```powershell
.\git_workflow.ps1
```

### 2. Docker Deployment
You can build and deploy the application locally using Docker:
```powershell
docker build -t devops-demo-app .
docker run -d -p 8080:80 --name demo-app devops-demo-app
```
Then visit `http://localhost:8080` in your web browser.

### 3. Selenium Testing
If you have Python installed elsewhere, you can run the Selenium test:
```powershell
pip install -r requirements.txt
python test.py
```
*(Note: the CI pipeline will also run this automatically when you push the code to GitHub).*
