# ✅ Railway Dual Environment Setup - Complete!

## 🎉 Your Setup is Ready

Your Django CRM API now has a complete dual-environment Railway deployment pipeline:

```
┌─────────────────────────────────────────────────────────┐
│               DEVELOP BRANCH → DEV ENV                  │
│                                                          │
│  Push to develop                                        │
│       ↓                                                  │
│  Railway DEVELOPMENT 🔧                                 │
│  (Safe testing environment)                             │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│                MAIN BRANCH → PROD ENV                   │
│                                                          │
│  Push to main                                           │
│       ↓                                                  │
│  Railway PRODUCTION 🚀                                  │
│  (Live production site)                                 │
└─────────────────────────────────────────────────────────┘
```

## 🚀 Quick Start Guide

### Daily Development Workflow

```bash
# 1. Make sure you're on develop
git checkout develop

# 2. Make your changes
# Edit files...

# 3. Use AI pipeline (recommended)
./scripts/ai_pipeline.sh
```

**What happens:**
- ✅ Tests run locally
- ✅ AI generates commit message
- ✅ Code pushed to develop
- ✅ **Automatically deploys to Railway DEVELOPMENT** 🔧
- ✅ You can test on dev environment

### Test Your Changes

```bash
# View development site
railway open -e development

# Check development logs
railway logs -e development

# View status
railway status -e development
```

### Deploy to Production

When you're happy with changes on development:

```bash
./scripts/deploy_to_production.sh
```

**What happens:**
- ✅ Merges develop → main
- ✅ Pushes to main
- ✅ **Automatically deploys to Railway PRODUCTION** 🚀
- ✅ Live site updated

## 📊 Environment Overview

| Environment | Branch | Access | Purpose |
|-------------|--------|--------|---------|
| **Development** | `develop` | `railway open -e development` | Testing & debugging |
| **Production** | `main` | `railway open -e production` | Live site |

## 🛠️ Available Scripts

| Script | What It Does | Deploys To |
|--------|--------------|-----------|
| `./scripts/ai_pipeline.sh` | Full AI dev cycle | Railway DEV 🔧 |
| `./scripts/auto_commit_develop.sh` | Quick commit | Railway DEV 🔧 |
| `./scripts/ai_commit.sh` | AI commit | Railway DEV 🔧 |
| `./scripts/deploy_to_production.sh` | Deploy to prod | Railway PROD 🚀 |
| `./scripts/workflow_status.sh` | View status | N/A |

## 📖 Documentation

All guides are in the `guides/` directory:

### Essential Reads
- **[guides/DEVELOP_WORKFLOW.md](./guides/DEVELOP_WORKFLOW.md)** - Complete workflow guide
- **[guides/RAILWAY_ENVIRONMENTS.md](./guides/RAILWAY_ENVIRONMENTS.md)** - Environment details
- **[guides/AI_PIPELINE.md](./guides/AI_PIPELINE.md)** - AI automation

### Full Documentation
- **[guides/README.md](./guides/README.md)** - Complete documentation index

## 🎯 Common Tasks

### Develop New Feature
```bash
git checkout develop
# Make changes
./scripts/ai_pipeline.sh
# Test on Railway development
railway open -e development
```

### Deploy to Production
```bash
./scripts/deploy_to_production.sh
```

### Check Logs
```bash
# Development
railway logs -e development

# Production
railway logs -e production
```

### Rollback Production
```bash
git checkout main
git revert HEAD
git push origin main
# Automatically redeploys previous version
```

## 💡 Key Points

### ✅ What You Get

1. **Safe Development**
   - Develop on `develop` branch
   - Auto-deploys to Railway DEVELOPMENT
   - Test before production

2. **Controlled Production**
   - Manual merge to main
   - Auto-deploys to Railway PRODUCTION
   - No accidental prod deployments

3. **AI-Powered Workflow**
   - AI-generated commits
   - Automated testing
   - Continuous iteration

### 🎨 The Flow

```
1. Code on develop → Deploy to DEV → Test on DEV
                          ↓
                    Happy with it?
                          ↓
2. Merge to main → Deploy to PROD → Live!
```

## 🌐 Accessing Your Environments

### Development Environment
```bash
# Open dev site
railway open -e development

# View dev logs (live)
railway logs -e development --tail

# Check dev status
railway status -e development
```

### Production Environment
```bash
# Open prod site
railway open -e production

# View prod logs (live)
railway logs -e production --tail

# Check prod status
railway status -e production
```

## 🔄 Example Full Workflow

### Scenario: Add New Feature

```bash
# Step 1: Develop
git checkout develop
git pull origin develop

# Step 2: Code
# Edit contacts/models.py
# Add email validation

# Step 3: Test & Deploy to DEV
./scripts/ai_pipeline.sh
# Runs tests, commits, pushes to develop
# Automatically deploys to Railway DEVELOPMENT

# Step 4: Test on DEV
railway open -e development
# Test the feature on development site

# Step 5: Check DEV logs
railway logs -e development
# Verify no errors

# Step 6: Deploy to PRODUCTION
./scripts/deploy_to_production.sh
# Merges to main, deploys to Railway PRODUCTION

# Step 7: Verify PRODUCTION
railway open -e production
# Check live site

# Done! Feature is live! 🎉
```

## 📞 Troubleshooting

### Issue: Not deploying
```bash
# Check which environment you're viewing
railway status

# Switch if needed
railway environment
# Select: development or production
```

### Issue: Want to see deployment progress
```bash
# Watch logs in real-time
railway logs -e development --tail
```

### Issue: Need to check both environments
```bash
# Development
railway open -e development
railway logs -e development

# Production
railway open -e production
railway logs -e production
```

## 🎊 You're All Set!

Your complete AI-powered development pipeline with dual Railway environments is ready to use!

### Next Steps:
1. Start developing on `develop` branch
2. Use `./scripts/ai_pipeline.sh` for AI-powered commits
3. Test on Railway DEVELOPMENT automatically
4. Deploy to PRODUCTION with `./scripts/deploy_to_production.sh`

### Quick Commands:
```bash
# Develop & auto-deploy to DEV
./scripts/ai_pipeline.sh

# Deploy to PRODUCTION
./scripts/deploy_to_production.sh

# Check status
./scripts/workflow_status.sh
```

Happy coding! 🚀

---

**Environment Summary:**
- `develop` → Railway DEVELOPMENT 🔧
- `main` → Railway PRODUCTION 🚀
- Both auto-deploy on push
- Manual control over prod deployments
