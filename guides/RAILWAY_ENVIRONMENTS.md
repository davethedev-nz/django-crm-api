# Railway Environments Setup

## 🌍 Environment Overview

Your Django CRM API has **two Railway environments**:

| Environment | Branch | Purpose | Auto-Deploy |
|-------------|--------|---------|-------------|
| **development** | `develop` | Testing & development | ✅ Yes |
| **production** | `main` | Live production | ✅ Yes |

## 🔄 Workflow

```
┌─────────────────────────────────────────────────────────┐
│                   DEVELOP BRANCH                        │
│                                                          │
│  git push origin develop                                │
│         ↓                                                │
│  Railway DEVELOPMENT Environment                        │
│  🔧 Safe testing environment                            │
└─────────────────────────────────────────────────────────┘

                         ↓ (Manual merge when ready)
                         ↓ ./scripts/deploy_to_production.sh

┌─────────────────────────────────────────────────────────┐
│                     MAIN BRANCH                         │
│                                                          │
│  git push origin main                                   │
│         ↓                                                │
│  Railway PRODUCTION Environment                         │
│  🚀 Live production site                                │
└─────────────────────────────────────────────────────────┘
```

## 🚀 Using Environments

### View Current Environment

```bash
railway status
```

### Switch Between Environments

```bash
# Switch to development
railway environment
# Select: development

# Switch to production
railway environment
# Select: production
```

### View Logs

```bash
# Development logs
railway logs -e development

# Production logs
railway logs -e production

# Live tail (follow)
railway logs -e development --tail
```

### Open Dashboards

```bash
# Open development site
railway open -e development

# Open production site
railway open -e production
```

### Check Service Status

```bash
# Development status
railway status -e development

# Production status
railway status -e production
```

## 🔧 Development Environment

### Purpose
- Test new features before production
- Experiment safely
- Debug issues
- Review changes

### Auto-Deploy Triggers
- Push to `develop` branch
- Manual Railway deployment
- Pull request deployments (if configured)

### Access
```bash
# View development URL
railway open -e development

# View logs
railway logs -e development

# Check status
railway status -e development
```

### Development Workflow
```bash
# 1. Make changes on develop branch
git checkout develop

# 2. Auto-commit and deploy to development
./scripts/auto_commit_develop.sh "Your changes"

# 3. Test on development environment
railway open -e development

# 4. Check logs if needed
railway logs -e development

# 5. Repeat until satisfied
```

## 🚀 Production Environment

### Purpose
- Live production site
- Stable, tested code only
- Customer-facing

### Auto-Deploy Triggers
- Push to `main` branch
- Merge from develop (via deploy_to_production.sh)

### Access
```bash
# View production URL
railway open -e production

# View logs
railway logs -e production

# Check status
railway status -e production
```

### Production Deployment
```bash
# When ready to deploy to production
./scripts/deploy_to_production.sh
```

This script:
1. Updates develop from remote
2. Switches to main
3. Merges develop → main
4. Pushes to main (triggers production deploy)
5. Returns you to develop

## 📊 Environment Variables

Both environments should have the same variables (with different values if needed):

### Required Variables
```bash
SECRET_KEY=<your-secret-key>
DEBUG=False
ALLOWED_HOSTS=<your-railway-domains>
DATABASE_URL=<postgres-connection-string>
```

### Set Variables for Specific Environment

```bash
# Development
railway environment
# Select: development
railway variables --set DEBUG=True

# Production
railway environment
# Select: production
railway variables --set DEBUG=False
```

### View All Variables

```bash
# Development
railway variables -e development

# Production
railway variables -e production
```

## 🔍 Monitoring

### Real-time Logs

```bash
# Development (live tail)
railway logs -e development --tail

# Production (live tail)
railway logs -e production --tail
```

### Health Checks

```bash
# Development health
curl https://your-dev-domain.railway.app/health

# Production health
curl https://your-prod-domain.railway.app/health
```

### Railway Dashboard

```bash
# Open Railway web dashboard
railway open
```

## 🛠️ Common Tasks

### Deploy to Development

```bash
git checkout develop
# Make changes
./scripts/auto_commit_develop.sh "Feature: Add validation"
# Automatically deploys to development
```

### Deploy to Production

```bash
# From develop branch
./scripts/deploy_to_production.sh
```

### Rollback Production

```bash
git checkout main
git revert HEAD
git push origin main
# Production automatically redeploys previous version
```

### Compare Environments

```bash
# Check what's different between develop and main
git log main..develop --oneline

# See commits ahead on develop
git log origin/main..origin/develop --oneline
```

### Test on Development Before Production

```bash
# 1. Commit to develop
./scripts/auto_commit_develop.sh "New feature"

# 2. Wait for deployment
sleep 10

# 3. Test development site
railway open -e development

# 4. Check logs
railway logs -e development

# 5. If good, deploy to production
./scripts/deploy_to_production.sh
```

## 📝 Environment URLs

### Get Environment URLs

```bash
# Development domain
railway domain -e development

# Production domain
railway domain -e production
```

### Custom Domains (Optional)

```bash
# Add custom domain to production
railway domain add yourdomain.com -e production

# Add custom domain to development
railway domain add dev.yourdomain.com -e development
```

## 🔐 Database Per Environment

Each environment should have its own database:

### Development Database
- Safe for testing
- Can reset/migrate freely
- Test data only

### Production Database
- Live customer data
- Careful with migrations
- Regular backups

### View Database Info

```bash
# Development database
railway variables -e development | grep DATABASE_URL

# Production database
railway variables -e production | grep DATABASE_URL
```

## 💡 Best Practices

### Development Environment
✅ DO:
- Test all changes here first
- Experiment freely
- Use for debugging
- Reset database when needed

❌ DON'T:
- Use production data
- Skip testing
- Deploy untested code

### Production Environment
✅ DO:
- Only deploy tested code
- Monitor logs regularly
- Have rollback plan
- Use production-ready settings

❌ DON'T:
- Test experimental features
- Deploy without testing
- Make database changes without backups
- Debug live issues (use development)

## 🎯 Quick Reference

| Task | Command |
|------|---------|
| Deploy to development | `./scripts/auto_commit_develop.sh "changes"` |
| Deploy to production | `./scripts/deploy_to_production.sh` |
| Switch environment | `railway environment` |
| View dev logs | `railway logs -e development` |
| View prod logs | `railway logs -e production` |
| Open dev site | `railway open -e development` |
| Open prod site | `railway open -e production` |
| Check dev status | `railway status -e development` |
| Check prod status | `railway status -e production` |

## 🔗 Related Documentation

- [guides/DEVELOP_WORKFLOW.md](./DEVELOP_WORKFLOW.md) - Development workflow
- [guides/RAILWAY_STEPS.md](./RAILWAY_STEPS.md) - Railway setup
- [guides/DEPLOY_GUIDE.md](./DEPLOY_GUIDE.md) - Deployment guide
- [guides/AI_PIPELINE.md](./AI_PIPELINE.md) - AI automation

---

**Remember:** 
- `develop` branch → Railway DEVELOPMENT environment 🔧
- `main` branch → Railway PRODUCTION environment 🚀
