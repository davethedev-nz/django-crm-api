# 🚀 Complete AI-Powered Development Pipeline Setup

## 🎯 Overview

This is a **fully automated AI-powered development pipeline** that:

1. **Generates code** using AI (GitHub Copilot)
2. **Auto-commits** with AI-generated messages
3. **Auto-tests** via GitHub Actions CI/CD
4. **Auto-deploys** to production
5. **Monitors logs** for errors
6. **Auto-iterates** based on feedback

## 📋 Table of Contents

- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Pipeline Components](#pipeline-components)
- [Deployment Options](#deployment-options)
- [Monitoring Setup](#monitoring-setup)
- [Advanced Usage](#advanced-usage)

---

## ✅ Prerequisites

### Already Installed:
- ✅ Python 3.12
- ✅ Django & DRF
- ✅ Git
- ✅ GitHub CLI (`gh`)
- ✅ GitHub Copilot (in VS Code)

### To Configure:
- [ ] Deployment platform (Railway/Heroku/DigitalOcean)
- [ ] Monitoring service (optional)
- [ ] Notification service (optional)

---

## 🚀 Quick Start

### Option 1: Run the Full Pipeline (Recommended)

```bash
./scripts/ai_pipeline.sh
```

This single command runs the entire pipeline:
- Checks for changes
- Runs tests
- Commits with AI message
- Pushes to GitHub
- Monitors CI/CD
- Analyzes results
- Creates issues for problems

### Option 2: Run Individual Steps

```bash
# 1. Auto-commit changes
./scripts/ai_commit.sh "Add new feature description"

# 2. Run AI iteration analysis
python scripts/ai_iterate.py

# 3. Monitor logs
python scripts/monitor_logs.py --continuous

# 4. Monitor logs once
python scripts/monitor_logs.py
```

---

## 🔧 Pipeline Components

### 1. AI Code Generation (Active ✅)

**Using GitHub Copilot in VS Code:**

```
Ctrl+Shift+I  (or Cmd+Shift+I on Mac)
```

**Example prompts:**
```
- "Create a Task model with title, description, due_date, and priority"
- "Add email validation that checks for company domain"
- "Create an API endpoint to bulk import contacts from CSV"
- "Add filtering by date range for deals"
```

**Inline suggestions:**
Just type comments describing what you want:
```python
# Create a method to calculate total deal value for a company

# Copilot will suggest complete implementation!
```

### 2. Auto-Commit (Active ✅)

**Quick commit:**
```bash
./scripts/ai_commit.sh "Added email notifications for new deals"
```

**In VS Code:**
1. Stage changes (`Ctrl+Shift+G`)
2. Click ✨ sparkle icon
3. Review AI message
4. Commit & push

### 3. Auto-Test (GitHub Actions) (Active ✅)

**Automatic on every push to `main`:**
- Runs all Django tests
- Checks deployment settings
- Tests with Python 3.11 and 3.12

**View test results:**
```bash
gh run list                    # List all workflow runs
gh run watch                   # Watch current run
gh run view                    # View latest run details
gh run view --log             # View logs
```

### 4. Auto-Deploy (To Configure 📝)

**Choose a deployment platform:**

#### Option A: Railway (Recommended for Django)

1. **Sign up**: https://railway.app
2. **Get API token**: Settings → Tokens
3. **Add to GitHub Secrets:**
   ```bash
   gh secret set RAILWAY_TOKEN
   # Paste your token when prompted
   ```
4. **Enable deployment** in `.github/workflows/deploy.yml`:
   - Set `if: github.ref == 'refs/heads/main'` to true

#### Option B: Heroku

1. **Install Heroku CLI:**
   ```bash
   curl https://cli-assets.heroku.com/install.sh | sh
   ```

2. **Login:**
   ```bash
   heroku login
   ```

3. **Create app:**
   ```bash
   heroku create your-crm-api
   ```

4. **Add secrets:**
   ```bash
   gh secret set HEROKU_API_KEY
   gh secret set HEROKU_APP_NAME
   gh secret set HEROKU_EMAIL
   ```

5. **Enable Heroku deployment** in `.github/workflows/deploy.yml`

#### Option C: DigitalOcean App Platform

1. **Sign up**: https://www.digitalocean.com
2. **Create App** from GitHub repo
3. **Configure build settings**:
   - Build Command: `pip install -r requirements.txt`
   - Run Command: `gunicorn crm_project.wsgi`

### 5. Monitor Logs (Active ✅)

**Continuous monitoring:**
```bash
python scripts/monitor_logs.py --continuous --interval 30
```

**One-time check:**
```bash
python scripts/monitor_logs.py
```

**Features:**
- Detects error patterns
- Creates GitHub issues automatically
- Suggests AI-powered fixes
- Tracks error rates
- Alerts on threshold breaches

### 6. Auto-Iterate (Active ✅)

**Run analysis:**
```bash
python scripts/ai_iterate.py
```

**What it does:**
- Runs all tests
- Analyzes failures
- Generates AI suggestions
- Creates GitHub issues
- Provides fix recommendations

---

## 🌐 Deployment Options

### Railway (Recommended)

**Setup:**
1. Create `railway.json`:
```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "python manage.py migrate && gunicorn crm_project.wsgi",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

2. Create `Procfile`:
```
web: gunicorn crm_project.wsgi
release: python manage.py migrate
```

3. Add `gunicorn` to requirements.txt:
```bash
echo "gunicorn" >> requirements.txt
```

4. Deploy:
```bash
railway up
```

### Environment Variables

Add these to your deployment platform:

```bash
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=your-domain.com
DATABASE_URL=postgresql://...  # If using PostgreSQL
```

---

## 📊 Monitoring Setup

### Option 1: Sentry (Error Tracking)

1. **Install:**
```bash
pip install sentry-sdk
echo "sentry-sdk" >> requirements.txt
```

2. **Configure** in `settings.py`:
```python
import sentry_sdk

sentry_sdk.init(
    dsn="your-sentry-dsn",
    traces_sample_rate=1.0,
)
```

### Option 2: LogRocket (Session Replay)

For frontend applications.

### Option 3: DataDog (Full Observability)

Enterprise-grade monitoring.

---

## 🎮 Advanced Usage

### Custom Workflows

**Create feature branch workflow:**
```bash
git checkout -b feature/new-feature
# Make changes
./scripts/ai_commit.sh "Implement new feature"
gh pr create --title "Add new feature" --body "Description"
```

**Automated PR creation:**
```bash
# After committing to feature branch
gh pr create --fill  # Auto-fills from commits
```

### Scheduled Monitoring

**Add to crontab for automated monitoring:**
```bash
crontab -e

# Run iteration every hour
0 * * * * cd /home/dave/dev/ai_test_loop && python scripts/ai_iterate.py

# Monitor logs every 15 minutes
*/15 * * * * cd /home/dave/dev/ai_test_loop && python scripts/monitor_logs.py
```

### Webhooks & Notifications

**Slack notifications** (add to GitHub Actions):
```yaml
- name: Notify Slack
  uses: 8398a7/action-slack@v3
  with:
    status: ${{ job.status }}
    webhook_url: ${{ secrets.SLACK_WEBHOOK }}
```

### AI-Powered Code Reviews

**Enable GitHub Copilot for PR reviews:**
1. Install GitHub Copilot extension
2. Open PR in VS Code
3. Use Copilot to review changes

---

## 🎯 Complete Development Cycle Example

### Scenario: Add Task Management Feature

1. **Generate code with AI:**
   ```
   Copilot prompt: "Create a Task model with title, description, due_date, 
   priority (high/medium/low), assigned_to contact, related_to deal"
   ```

2. **Write tests:**
   ```
   Copilot prompt: "Generate tests for the Task model including validation tests"
   ```

3. **Create API endpoints:**
   ```
   Copilot prompt: "Create REST API endpoints for tasks with filtering by priority and status"
   ```

4. **Run the pipeline:**
   ```bash
   ./scripts/ai_pipeline.sh
   ```

5. **Monitor deployment:**
   ```bash
   gh run watch
   ```

6. **Check logs:**
   ```bash
   python scripts/monitor_logs.py
   ```

7. **Iterate on feedback:**
   - AI detects issues
   - Creates GitHub issues automatically
   - Suggests fixes
   - You implement fixes
   - Repeat!

---

## 🔥 Pro Tips

1. **Commit often** - Small commits are easier to manage
2. **Use descriptive prompts** - Better prompts = better AI code
3. **Review AI suggestions** - Always review before accepting
4. **Test locally first** - Catch issues early
5. **Monitor continuously** - Stay ahead of problems
6. **Iterate quickly** - Fast feedback loops improve quality

---

## 🆘 Troubleshooting

### Pipeline fails to start
```bash
# Check GitHub CLI auth
gh auth status

# Re-authenticate if needed
gh auth login
```

### Tests fail locally
```bash
# Run specific test
python manage.py test contacts.tests.TestContactModel

# Run with verbosity
python manage.py test --verbosity=2

# Check for migrations
python manage.py makemigrations
python manage.py migrate
```

### Deployment fails
```bash
# Check deployment logs
gh run view --log

# Check secrets are set
gh secret list

# Verify environment variables
railway variables
```

### Monitoring not working
```bash
# Check log file exists
ls -la logs/

# Create logs directory if needed
mkdir -p logs

# Test monitoring script
python scripts/monitor_logs.py
```

---

## 📚 Additional Resources

- **Django Docs**: https://docs.djangoproject.com
- **GitHub Actions**: https://docs.github.com/actions
- **Railway Docs**: https://docs.railway.app
- **GitHub CLI**: https://cli.github.com/manual

---

## 🎉 You're All Set!

Your AI-powered development pipeline is ready! Start with:

```bash
./scripts/ai_pipeline.sh
```

Happy coding! 🚀
