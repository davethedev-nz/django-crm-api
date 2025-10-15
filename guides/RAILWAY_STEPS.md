# 🚀 Railway Deployment - Step by Step

## ✅ Progress So Far:

- ✅ Railway CLI installed
- ✅ Logged in as: dave@davethedev.co.nz
- ✅ Project created: **New-app**
- ✅ Project URL: https://railway.com/project/ad63be2f-de2d-4999-92f3-aed0a21bd7ac

## 📋 Next Steps:

### Step 1: Add PostgreSQL Database (Via Web UI)

The easiest way is through Railway's web interface:

1. **Open your project:**
   ```bash
   railway open
   ```

2. **In the Railway dashboard:**
   - Click "+ New" button
   - Select "Database"
   - Choose "PostgreSQL"
   - Click "Add PostgreSQL"

That's it! Railway will automatically set the `DATABASE_URL` environment variable.

---

### Step 2: Set Environment Variables

Set the required variables:

```bash
# Generate and set SECRET_KEY
railway variables --set "SECRET_KEY=$(python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')"

# Set DEBUG to False
railway variables --set "DEBUG=False"

# Set ALLOWED_HOSTS (we'll update this after getting the domain)
railway variables --set "ALLOWED_HOSTS=*"
```

---

### Step 3: Deploy Your Application

Deploy your code to Railway:

```bash
railway up
```

This will:
- Upload your code
- Build your Docker container
- Install dependencies
- Run migrations (via `Procfile`)
- Start your server

**This takes 3-5 minutes. Watch the build logs!**

---

### Step 4: Generate a Public Domain

Once deployed, generate a public URL:

```bash
# Generate domain
railway domain

# Your app will get a URL like: your-app-production.up.railway.app
```

---

### Step 5: Update ALLOWED_HOSTS

After getting your domain, update ALLOWED_HOSTS:

```bash
# Replace <your-domain> with the actual domain from railway domain
railway variables --set "ALLOWED_HOSTS=<your-domain>.up.railway.app,*.up.railway.app"
```

---

### Step 6: Create Superuser

Create an admin user:

```bash
railway run python manage.py createsuperuser
```

Follow the prompts to set:
- Username
- Email
- Password

---

### Step 7: Load Sample Data (Optional)

```bash
railway run python manage.py populate_sample_data
```

---

## ✅ Verification

### Check Status:
```bash
railway status
```

### View Logs:
```bash
railway logs
```

### Open in Browser:
```bash
railway open
```

### Test Your API:
```bash
# Get your domain first
DOMAIN=$(railway domain 2>&1 | grep -o '[a-z0-9-]*\.up\.railway\.app' | head -1)

# Test API endpoints
curl https://$DOMAIN/api/
curl https://$DOMAIN/api/contacts/
curl https://$DOMAIN/admin/
```

---

## 🔄 Enable Auto-Deploy from GitHub

### Step 1: Connect GitHub Repository

In Railway dashboard:
1. Go to your service settings
2. Click "Settings"
3. Scroll to "Source"
4. Click "Connect GitHub"
5. Select your repository: `davethedev-nz/django-crm-api`
6. Select branch: `main`

Now every push to `main` automatically deploys!

### Step 2: (Alternative) Use Railway Token for GitHub Actions

```bash
# Get your Railway token
railway whoami

# Add to GitHub secrets
gh secret set RAILWAY_TOKEN
# Paste the token when prompted
```

---

## 📊 Useful Commands

```bash
# View all projects
railway list

# Check service status
railway status

# View live logs
railway logs

# Run Django commands
railway run python manage.py migrate
railway run python manage.py createsuperuser
railway run python manage.py shell

# Open project dashboard
railway open

# SSH into your container
railway ssh

# Redeploy
railway up

# Connect to PostgreSQL
railway connect postgres
```

---

## 🎯 Current Status

✅ **Ready for Step 1: Add PostgreSQL**

Run this command to open Railway dashboard:
```bash
railway open
```

Then add PostgreSQL database from the dashboard.

After that, continue with Step 2!

---

## 🆘 Troubleshooting

### Build Fails:
```bash
# Check logs
railway logs

# Redeploy
railway up
```

### Database Connection Issues:
```bash
# Verify DATABASE_URL is set
railway variables

# Check if PostgreSQL is running
railway status
```

### Static Files Not Loading:
```bash
# Collect static files
railway run python manage.py collectstatic --noinput
```

---

## 📚 Documentation

- Railway Docs: https://docs.railway.app
- Your Project: https://railway.com/project/ad63be2f-de2d-4999-92f3-aed0a21bd7ac

---

**Next:** Open Railway dashboard and add PostgreSQL!
```bash
railway open
```
