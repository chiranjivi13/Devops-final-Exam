# This script provides the exact commands you need to execute in a terminal where Git is installed.
# It fulfills Task #1 and #2 of your requirement: Branching, Committing, and Merging.

Write-Host "--- Git Operations Workflow ---" -ForegroundColor Cyan
Write-Host "Run these commands in a terminal where 'git' is installed (e.g., Git Bash or a properly configured PowerShell)."

$gitCommands = @"
# 1. Initialize repository and add files
git init
git add .
git commit -m "Initial commit: Added simple web application and CI pipeline"

# 2. Create a new branch
git checkout -b feature/update-ui

# Make a small change (Simulated by touching a file, or you can edit index.html)
echo "<!-- Git branch test -->" >> index.html

# 3. Perform a commit on the new branch
git add index.html
git commit -m "Feature: Updated UI component"

# 4. Merge the branch into the main branch
git checkout main
git merge feature/update-ui

# 5. (Optional) Connect to your GitHub repository and push
# git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
# git branch -M main
# git push -u origin main
"@

Write-Host $gitCommands -ForegroundColor Green

Write-Host "`nTo test your application via Docker locally, run:" -ForegroundColor Cyan
Write-Host "docker build -t simple-web-app ." -ForegroundColor Green
Write-Host "docker run -p 8080:80 -d simple-web-app" -ForegroundColor Green
Write-Host "Then open your browser to http://localhost:8080" -ForegroundColor Green
