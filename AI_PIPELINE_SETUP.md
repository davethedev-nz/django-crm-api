# AI Pipeline - Develop Branch Workflow

## ✅ Completed Setup

Your AI-powered development pipeline is now fully configured to work with the **develop branch workflow**.

## 🔄 Key Changes

### 1. Branch Strategy
- **develop** - Safe development (auto-deploys to Railway DEVELOPMENT)
- **main** - Production (auto-deploys to Railway PRODUCTION)

### 2. Updated Scripts

| Script | Purpose | Deployment |
|--------|---------|-----------|
| `./scripts/ai_commit.sh` | AI-powered commit to develop | 🔧 Development |
| `./scripts/auto_commit_develop.sh` | Quick commit to develop | 🔧 Development |
| `./scripts/ai_pipeline.sh` | Full AI development pipeline | 🔧 Development |
| `./scripts/deploy_to_production.sh` | Merge develop → main | 🚀 Production |
| `./scripts/workflow_status.sh` | View current status | N/A |

### 3. Documentation Organization

All guides moved to `guides/` directory:
```
guides/
├── README.md                 # Documentation index
├── QUICKSTART.md            # Getting started
├── DEVELOP_WORKFLOW.md      # Development workflow
├── AI_PIPELINE.md           # AI automation
├── DEPLOY_GUIDE.md          # Deployment guide
├── RAILWAY_STEPS.md         # Railway setup
└── ... (more guides)
```

## 🚀 Daily Workflow

### Option 1: Quick Auto-Commit
```bash
# Make your changes
./scripts/auto_commit_develop.sh "Description of changes"
```

### Option 2: AI-Powered Pipeline
```bash
# Run full AI pipeline (tests + commit + iterate)
./scripts/ai_pipeline.sh
```

**What the AI pipeline does:**
1. ✅ Ensures you're on develop branch
2. ✅ Checks for changes
3. ✅ Runs tests locally
4. ✅ Creates AI-generated commit message
5. ✅ Pushes to develop (deploys to Railway DEVELOPMENT)
6. ✅ Monitors deployment
7. ✅ Offers to run AI iteration for improvements

### Option 3: Deploy to Production
```bash
# When ready to deploy
./scripts/deploy_to_production.sh
```

**What this does:**
1. Updates develop from remote
2. Switches to main
3. Merges develop → main
4. Pushes to main (triggers Railway auto-deploy)
5. Returns you to develop

## 🎯 Workflow Summary

```
┌──────────────────────────────────────────────────────┐
│                  DEVELOP BRANCH                      │
│          Safe Iterative Development                  │
└──────────────────────────────────────────────────────┘

1. Make changes
   ↓
2. ./scripts/ai_pipeline.sh (or auto_commit_develop.sh)
   ↓
3. Repeat as needed
   ↓
4. When ready: ./scripts/deploy_to_production.sh

┌──────────────────────────────────────────────────────┐
│                    MAIN BRANCH                       │
│              Production Deployment                   │
└──────────────────────────────────────────────────────┘

Auto-deploys to Railway ✅
```

## 💡 Key Benefits

### Safe Development
- ✅ Experiment freely on develop
- ✅ Multiple commits without deployment
- ✅ Test before production
- ✅ Easy rollback

### Manual Deployment Control
- ✅ You decide when to deploy
- ✅ No accidental production pushes
- ✅ Review changes before merge
- ✅ Controlled releases

### AI-Powered Iteration
- ✅ AI-generated commit messages
- ✅ Automated testing
- ✅ Code quality suggestions
- ✅ Continuous improvement loop

## 📊 Check Status Anytime

```bash
./scripts/workflow_status.sh
```

Shows:
- Current branch
- Uncommitted changes
- Recent commits
- Commits ahead/behind
- Available actions
- Railway status

## 📚 Documentation

Main documentation index: **[guides/README.md](./guides/README.md)**

Quick links:
- [Development Workflow](./guides/DEVELOP_WORKFLOW.md)
- [AI Pipeline Details](./guides/AI_PIPELINE.md)
- [Deployment Guide](./guides/DEPLOY_GUIDE.md)

## ⚡ Quick Reference

### Start Working
```bash
git checkout develop
git pull origin develop
```

### Auto-Commit (Quick)
```bash
./scripts/auto_commit_develop.sh "Your changes"
```

### AI Pipeline (Full)
```bash
./scripts/ai_pipeline.sh
```

### Deploy Production
```bash
./scripts/deploy_to_production.sh
```

### Check Status
```bash
./scripts/workflow_status.sh
railway status
railway logs
```

## 🎉 You're All Set!

Your AI-powered development pipeline is ready to use with the develop branch workflow.

**Next steps:**
1. Start making changes on develop
2. Use `./scripts/ai_pipeline.sh` for AI-powered commits
3. Deploy to production when ready with `./scripts/deploy_to_production.sh`

Happy coding! 🚀
