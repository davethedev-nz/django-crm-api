# 🚀 Complete Auto-Deploy Setup Guide

## ✅ Files Created

All necessary files have been created:
- ✅ `Procfile` - Railway startup commands
- ✅ `railway.json` - Railway configuration
- ✅ `runtime.txt` - Python version
- ✅ `requirements.txt` - Updated with production deps
- ✅ `settings.py` - Updated for production
- ✅ `scripts/deploy_railway.sh` - Automated setup script

---

## 🚂 Option 1: Railway (Easiest - Recommended)

### Step 1: Quick Setup (Automated)

```bash
./scripts/deploy_railway.sh
```

This script will:
1. Install Railway CLI
2. Login to Railway
3. Create project
4. Add PostgreSQL
5. Set environment variables
6. Deploy your app

**That's it!** 🎉

### Step 2: Manual Setup (If you prefer)

```bash
# 1. Install Railway CLI
npm install -g @railway/cli

# 2. Login
railway login

# 3. Initialize project
railway init

# 4. Add PostgreSQL
railway add --plugin postgresql

# 5. Deploy
railway up
```

### Step 3: Set GitHub Secret for Auto-Deploy

```bash
# Get your Railway token
railway whoami

# Add to GitHub secrets
gh secret set RAILWAY_TOKEN
# Paste your token when prompted
```

### Step 4: Verify Deployment

```bash
# Check status
railway status

# View logs
railway logs

# Get URL
railway domain

# Open in browser
railway open
```

---

## 🟣 Option 2: Heroku

### Setup

```bash
# 1. Install Heroku CLI
curl https://cli-assets.heroku.com/install.sh | sh

# 2. Login
heroku login

# 3. Create app
heroku create django-crm-api

# 4. Add PostgreSQL
heroku addons:create heroku-postgresql:mini

# 5. Set environment variables
heroku config:set DEBUG=False
heroku config:set SECRET_KEY=$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')

# 6. Deploy
git push heroku main

# 7. Run migrations
heroku run python manage.py migrate

# 8. Create superuser
heroku run python manage.py createsuperuser

# 9. Open app
heroku open
```

### Add GitHub Secrets

```bash
gh secret set HEROKU_API_KEY  # Get from: heroku auth:token
gh secret set HEROKU_APP_NAME  # Your app name
gh secret set HEROKU_EMAIL  # Your Heroku email
```

---

## 🌊 Option 3: DigitalOcean App Platform

### Setup (Web Interface)

1. Go to https://cloud.digitalocean.com/apps
2. Click "Create App"
3. Connect your GitHub repository
4. Configure:
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - **Run Command**: `gunicorn crm_project.wsgi`
5. Add PostgreSQL database
6. Set environment variables:
   ```
   SECRET_KEY=your-secret-key
   DEBUG=False
   ALLOWED_HOSTS=your-domain.ondigitalocean.app
   ```
7. Deploy!

---

## ⚙️ What Changed in Your Code

### 1. `settings.py` Updates

- ✅ Uses environment variables for configuration
- ✅ PostgreSQL support (production)
- ✅ SQLite (development)
- ✅ WhiteNoise for static files
- ✅ Security settings

### 2. New Files

- **`Procfile`**: Tells platform how to run your app
- **`railway.json`**: Railway-specific config
- **`runtime.txt`**: Python version specification

### 3. New Dependencies

```
gunicorn==21.2.0        # Production WSGI server
psycopg2-binary==2.9.9  # PostgreSQL adapter
whitenoise==6.6.0       # Static file serving
dj-database-url==2.1.0  # Database URL parsing
```

---

## 🔒 Environment Variables Needed

Set these in your deployment platform:

```bash
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-domain.com
DATABASE_URL=postgresql://...  # Auto-set by platform
```

---

## 🧪 Test Your Deployment

### After Deploying:

```bash
# Test API endpoints
curl https://your-app.railway.app/api/
curl https://your-app.railway.app/api/contacts/
curl https://your-app.railway.app/api/companies/
curl https://your-app.railway.app/api/deals/

# Test admin
curl https://your-app.railway.app/admin/
```

### Create Superuser on Production:

```bash
# Railway
railway run python manage.py createsuperuser

# Heroku
heroku run python manage.py createsuperuser

# DigitalOcean (via console)
python manage.py createsuperuser
```

### Load Sample Data:

```bash
# Railway
railway run python manage.py populate_sample_data

# Heroku
heroku run python manage.py populate_sample_data
```

---

## 🔄 Enable Auto-Deploy from GitHub

### For Railway:

1. **Set GitHub secret:**
   ```bash
   gh secret set RAILWAY_TOKEN
   ```

2. **Already configured!** The workflow in `.github/workflows/deploy.yml` is ready.

3. **Test it:**
   ```bash
   # Make a change
   echo "# Test" >> README.md
   git add .
   git commit -m "Test auto-deploy"
   git push
   
   # Watch deployment
   gh run watch
   ```

### For Heroku:

1. **Set GitHub secrets:**
   ```bash
   gh secret set HEROKU_API_KEY
   gh secret set HEROKU_APP_NAME
   gh secret set HEROKU_EMAIL
   ```

2. **Enable Heroku deployment** in `.github/workflows/deploy.yml`:
   Change `if: false` to `if: github.ref == 'refs/heads/main'` in the Heroku section.

---

## 📊 Monitor Your Deployment

### Railway:

```bash
railway status         # Check deployment status
railway logs           # View application logs
railway logs --follow  # Follow logs in real-time
railway shell          # Access production shell
railway variables      # View environment variables
```

### Heroku:

```bash
heroku ps             # Check dyno status
heroku logs --tail    # View logs
heroku run bash       # Access production shell
heroku config         # View environment variables
```

---

## 🔥 Complete Workflow Now Active

### What Happens When You Push:

```
You: git push
   ↓
GitHub Actions: Runs tests
   ↓
Tests Pass: Deploys to Railway
   ↓
Railway: Builds app
   ↓
Railway: Runs migrations
   ↓
Railway: Starts app
   ↓
You: App is live! 🎉
```

### Auto-Deploy Cycle:

1. **Code** → Write code with Copilot
2. **Commit** → `./scripts/ai_pipeline.sh` or AI commit
3. **Push** → `git push` (automatic)
4. **Test** → GitHub Actions runs tests
5. **Deploy** → Railway auto-deploys
6. **Monitor** → Check logs automatically
7. **Iterate** → AI suggests improvements

---

## 🎯 Quick Commands Reference

### Development:
```bash
python manage.py runserver  # Local server
python manage.py test       # Run tests
python manage.py migrate    # Apply migrations
```

### Deployment:
```bash
railway up                  # Deploy to Railway
railway logs                # View logs
railway status              # Check status
railway open                # Open in browser
```

### CI/CD:
```bash
gh run watch                # Watch GitHub Actions
gh run view --log          # View test logs
gh workflow list           # List workflows
```

### Full Pipeline:
```bash
./scripts/ai_pipeline.sh   # Run everything!
```

---

## 🆘 Troubleshooting

### Deployment Fails:

```bash
# Check logs
railway logs

# Check environment variables
railway variables

# Rebuild
railway up --force

# Check database connection
railway run python manage.py check
```

### Static Files Not Loading:

```bash
# Collect static files
railway run python manage.py collectstatic --noinput

# Check STATIC_ROOT in settings
railway run python -c "from crm_project import settings; print(settings.STATIC_ROOT)"
```

### Database Issues:

```bash
# Run migrations
railway run python manage.py migrate

# Check database
railway run python manage.py dbshell
```

---

## ✅ Verification Checklist

Before you start:
- [x] All files created
- [x] Production dependencies installed
- [x] Settings updated for production
- [x] Scripts ready to run

To deploy:
- [ ] Run `./scripts/deploy_railway.sh`
- [ ] Set RAILWAY_TOKEN in GitHub secrets
- [ ] Push to GitHub
- [ ] Verify deployment

---

## 🎉 You're Ready!

### Quick Start:

```bash
# Run the automated setup
./scripts/deploy_railway.sh
```

That's literally it! The script handles everything.

### Then Enable Auto-Deploy:

```bash
# Get Railway token
railway whoami

# Add to GitHub
gh secret set RAILWAY_TOKEN
# Paste token when prompted

# Test auto-deploy
git push
gh run watch
```

---

## 📚 Next Steps

1. **Deploy now**: `./scripts/deploy_railway.sh`
2. **Set up auto-deploy**: Add RAILWAY_TOKEN to GitHub secrets
3. **Test your API**: Visit your Railway URL
4. **Load sample data**: `railway run python manage.py populate_sample_data`
5. **Create superuser**: `railway run python manage.py createsuperuser`

---

**Your auto-deploy pipeline is ready! 🚀**

Just run: `./scripts/deploy_railway.sh`
