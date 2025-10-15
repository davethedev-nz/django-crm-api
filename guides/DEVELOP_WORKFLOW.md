# Development Workflow Guide

## Branch Strategy

This project uses a two-branch workflow for safe development and automated deployment:

- **`develop`** - Feature development branch (safe for experimentation)
- **`main`** - Production branch (auto-deploys to Railway)

## Daily Development Workflow

### 1. Start Working on Features

```bash
# Make sure you're on develop branch
git checkout develop

# Pull latest changes
git pull origin develop
```

### 2. Make Your Changes

- Edit files
- Add new features
- Fix bugs
- Test locally

### 3. Auto-Commit Changes (Develop Branch)

Use the auto-commit script to quickly commit and push to develop:

```bash
# Auto-commit with generated message
./scripts/auto_commit_develop.sh

# Or provide custom message
./scripts/auto_commit_develop.sh "Add user authentication feature"
```

**What this does:**
- ✅ Ensures you're on develop branch
- 📦 Stages all changes
- 💾 Commits with timestamp or custom message
- 🚀 Pushes to origin/develop
- ⚠️  Does NOT trigger production deployment

### 4. Deploy to Production

When you're ready to deploy your changes to production:

```bash
./scripts/deploy_to_production.sh
```

**What this does:**
1. Updates develop branch from remote
2. Switches to main branch
3. Merges develop into main
4. Pushes to main (triggers Railway auto-deploy)
5. Returns you to develop branch

## Quick Reference

| Command | Purpose | Auto-Deploy? |
|---------|---------|--------------|
| `./scripts/auto_commit_develop.sh` | Commit & push to develop | ❌ No |
| `./scripts/deploy_to_production.sh` | Deploy to production | ✅ Yes |
| `git push origin main` | Manual deploy trigger | ✅ Yes |

## Safety Features

### Develop Branch Safety
- ✅ Experiment freely - no production impact
- ✅ Multiple commits without deployment
- ✅ Easy rollback if needed
- ✅ Review changes before production

### Production Protection
- ✅ Only main branch deploys to Railway
- ✅ Explicit merge required (via script)
- ✅ CI/CD tests run before deploy
- ✅ Automatic health checks on Railway

## Example Workflows

### Scenario 1: Quick Feature Development

```bash
# Switch to develop
git checkout develop

# Make changes
nano crm_project/settings.py

# Auto-commit
./scripts/auto_commit_develop.sh "Update settings"

# Continue working...
nano contacts/models.py

# Another auto-commit
./scripts/auto_commit_develop.sh "Add contact validation"

# Deploy when ready
./scripts/deploy_to_production.sh
```

### Scenario 2: Multiple Features Before Deploy

```bash
# Work on feature 1
./scripts/auto_commit_develop.sh "Feature 1: Add email field"

# Work on feature 2
./scripts/auto_commit_develop.sh "Feature 2: Add phone validation"

# Work on feature 3
./scripts/auto_commit_develop.sh "Feature 3: Update API docs"

# Deploy all features at once
./scripts/deploy_to_production.sh
```

### Scenario 3: Emergency Hotfix

```bash
# Switch directly to main for urgent fixes
git checkout main

# Make the fix
nano crm_project/settings.py

# Commit and push (deploys immediately)
git add .
git commit -m "hotfix: Fix critical security issue"
git push origin main

# Merge back to develop
git checkout develop
git merge main
git push origin develop
```

## Auto-Commit Script Details

### Basic Usage

```bash
./scripts/auto_commit_develop.sh
```

Generates message like:
```
Auto-commit: 3 file(s) updated at 2024-01-15 14:30:00
```

### Custom Message

```bash
./scripts/auto_commit_develop.sh "Add user authentication"
```

Uses your custom message instead of auto-generated one.

### What It Checks

1. ✅ Current branch (switches to develop if needed)
2. ✅ Uncommitted changes (exits if none)
3. ✅ Stages all changes (git add -A)
4. ✅ Commits with message
5. ✅ Pushes to origin/develop

## CI/CD Pipeline

### On Push to Develop
- ❌ No deployment triggered
- ✅ Code is safely committed
- ✅ Available for testing

### On Push to Main
1. ✅ GitHub Actions runs tests
2. ✅ Railway detects push
3. ✅ Railway builds Docker image
4. ✅ Railway runs database migrations
5. ✅ Railway deploys new version
6. ✅ Health checks verify deployment

## Monitoring and Logs

### Check Deployment Status

```bash
# Railway dashboard
railway open

# View logs
railway logs

# Check running services
railway status
```

### Check Application Health

```bash
# Health check endpoint
curl https://django-crm-api-production.up.railway.app/health

# Admin panel
https://django-crm-api-production.up.railway.app/admin

# API root
https://django-crm-api-production.up.railway.app/api/
```

## Troubleshooting

### "Not on develop branch" Warning

The auto-commit script will automatically switch you to develop if needed.

### Push Rejected

```bash
# Pull latest changes first
git pull origin develop

# Then try auto-commit again
./scripts/auto_commit_develop.sh
```

### Deployment Failed

```bash
# Check Railway logs
railway logs

# Check GitHub Actions
# Go to: https://github.com/yourusername/django-crm-api/actions

# Rollback if needed
git checkout main
git revert HEAD
git push origin main
```

### Merge Conflicts

```bash
# When merging develop to main
git checkout main
git merge develop

# If conflicts occur
git status  # See conflicted files
# Edit and resolve conflicts
git add .
git commit
git push origin main
```

## Best Practices

### ✅ DO

- Use develop for all feature development
- Commit frequently with meaningful messages
- Test locally before deploying to production
- Use auto-commit script for quick iterations
- Deploy to production when features are complete

### ❌ DON'T

- Don't push directly to main (except emergencies)
- Don't skip testing before production deploy
- Don't leave develop branch uncommitted for days
- Don't deploy untested code

## Environment Variables

Both branches use the same Railway environment:

- **SECRET_KEY** - Django secret key
- **DEBUG** - Set to False in production
- **ALLOWED_HOSTS** - Your Railway domain
- **DATABASE_URL** - PostgreSQL connection string

Update via Railway CLI:

```bash
railway variables --set KEY=value
```

## Related Documentation

- [QUICKSTART.md](./QUICKSTART.md) - Project setup
- [DEPLOY_GUIDE.md](./DEPLOY_GUIDE.md) - Deployment details
- [RAILWAY_STEPS.md](./RAILWAY_STEPS.md) - Railway configuration
- [AI_PIPELINE.md](./AI_PIPELINE.md) - AI automation pipeline
- [GIT_CHEATSHEET.md](./GIT_CHEATSHEET.md) - Git commands

## Summary

🎯 **Key Takeaway**: Use `develop` for safe feature development with auto-commit, and `deploy_to_production.sh` to deploy to main when ready.

```bash
# Daily workflow
git checkout develop                           # Work on develop
./scripts/auto_commit_develop.sh "My changes" # Commit frequently
./scripts/deploy_to_production.sh             # Deploy when ready
```

Happy coding! 🚀
