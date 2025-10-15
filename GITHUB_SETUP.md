# GitHub Setup Guide

This guide will help you connect your Django CRM API project to GitHub and enable AI commit capabilities.

## Step 1: Create a GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the "+" icon in the top right corner
3. Select "New repository"
4. Fill in the details:
   - **Repository name**: `django-crm-api` (or your preferred name)
   - **Description**: Django REST Framework CRM API for managing contacts, companies, and deals
   - **Visibility**: Choose Public or Private
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
5. Click "Create repository"

## Step 2: Connect Your Local Repository to GitHub

After creating the repository, GitHub will show you commands. Use these commands in your terminal:

```bash
# Add the remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/django-crm-api.git

# Verify the remote was added
git remote -v

# Push your code to GitHub
git push -u origin main
```

**Alternative with SSH (if you have SSH keys set up):**
```bash
git remote add origin git@github.com:YOUR_USERNAME/django-crm-api.git
git push -u origin main
```

## Step 3: Enable GitHub Copilot (AI Commit Capability)

### Prerequisites
- GitHub Copilot subscription (Individual, Business, or Enterprise)
- VS Code with GitHub Copilot extension installed

### Enable AI Commit Messages

1. **Install GitHub Copilot Extension** (if not already installed):
   - Open VS Code
   - Go to Extensions (Ctrl+Shift+X)
   - Search for "GitHub Copilot"
   - Click Install

2. **Enable Copilot for Git Commit Messages**:
   - Open VS Code Settings (Ctrl+,)
   - Search for "copilot git"
   - Enable these settings:
     - ✅ `GitHub Copilot: Enable` (General)
     - ✅ `Git: Enable Smart Commit` (for AI suggestions)
   
3. **Use AI-Powered Commits in VS Code**:
   - Open Source Control panel (Ctrl+Shift+G)
   - Stage your changes
   - Click the sparkle ✨ icon in the commit message box
   - Copilot will suggest a commit message based on your changes
   - Review and edit if needed
   - Commit!

## Step 4: Alternative - GitHub CLI

You can also use GitHub CLI for easier repository creation:

```bash
# Install GitHub CLI (if not installed)
# Ubuntu/Debian:
sudo apt install gh

# Authenticate
gh auth login

# Create repository and push
gh repo create django-crm-api --public --source=. --remote=origin --push
```

## Step 5: Verify Your Setup

```bash
# Check remote configuration
git remote -v

# View commit history
git log --oneline

# Check current branch
git branch
```

## Regular Git Workflow

### Making Changes

```bash
# Check status
git status

# Stage specific files
git add path/to/file.py

# Stage all changes
git add .

# Commit with message
git commit -m "Add new feature"

# Push to GitHub
git push
```

### Using AI Commit Messages

In VS Code:
1. Make your changes
2. Open Source Control (Ctrl+Shift+G)
3. Stage changes
4. Click the sparkle ✨ icon for AI-generated commit message
5. Commit and push

### Working with Branches

```bash
# Create and switch to a new branch
git checkout -b feature/new-feature

# Switch back to main
git checkout main

# Merge feature branch
git merge feature/new-feature

# Delete feature branch
git branch -d feature/new-feature
```

## Additional GitHub Features

### Setting Up GitHub Actions (CI/CD)

Create `.github/workflows/django.yml` for automated testing:

```yaml
name: Django CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: 3.12
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run tests
      run: |
        python manage.py test
```

### Repository Settings for AI Development

1. **Enable Issues**: For tracking features and bugs
2. **Enable Projects**: For project management
3. **Branch Protection**: Protect the main branch
   - Go to Settings → Branches → Add rule
   - Require pull request reviews
   - Enable status checks

## Troubleshooting

### Authentication Issues

If you encounter authentication problems:

```bash
# Use GitHub CLI for easier auth
gh auth login

# Or configure Git credential helper
git config --global credential.helper cache
```

### Push Rejected

If your push is rejected:

```bash
# Pull latest changes first
git pull origin main --rebase

# Then push
git push origin main
```

### Merge Conflicts

If you encounter conflicts:

```bash
# Pull with rebase
git pull origin main --rebase

# Fix conflicts in files
# Then continue
git add .
git rebase --continue
git push
```

## Best Practices

1. **Commit Often**: Make small, focused commits
2. **Write Clear Messages**: Use AI suggestions but review them
3. **Use Branches**: Create feature branches for new work
4. **Pull Regularly**: Stay up to date with remote changes
5. **Review Before Push**: Always review your commits before pushing

## Next Steps

✅ Repository initialized locally
✅ Initial commit created
⬜ Create GitHub repository
⬜ Connect to remote
⬜ Push to GitHub
⬜ Enable GitHub Copilot
⬜ Make your first AI-assisted commit

Your project is now version-controlled and ready for GitHub! 🚀
