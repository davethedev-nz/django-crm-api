# Django CRM API - Documentation

Complete documentation for the Django CRM API project with AI-powered development pipeline.

## 📚 Table of Contents

### 🚀 Getting Started

1. **[QUICKSTART.md](./QUICKSTART.md)** - Quick project setup and first steps
2. **[DEVELOP_WORKFLOW.md](./DEVELOP_WORKFLOW.md)** - Development workflow with develop/main branches

### 🔧 Development

3. **[AI_PIPELINE.md](./AI_PIPELINE.md)** - AI-powered development automation
4. **[PIPELINE_SETUP.md](./PIPELINE_SETUP.md)** - Setting up the automation pipeline
5. **[QUICKSTART_PIPELINE.md](./QUICKSTART_PIPELINE.md)** - Quick pipeline setup

### 🚢 Deployment

6. **[DEPLOY_GUIDE.md](./DEPLOY_GUIDE.md)** - Complete deployment guide
7. **[DEPLOY_SETUP.md](./DEPLOY_SETUP.md)** - Detailed deployment setup
8. **[RAILWAY_STEPS.md](./RAILWAY_STEPS.md)** - Railway platform configuration
9. **[RAILWAY_STATUS.md](./RAILWAY_STATUS.md)** - Current Railway deployment status

### 🔗 Version Control

10. **[GIT_CHEATSHEET.md](./GIT_CHEATSHEET.md)** - Git commands reference
11. **[GITHUB_SETUP.md](./GITHUB_SETUP.md)** - GitHub setup and configuration

## 🎯 Quick Navigation

### For New Developers

Start here to get the project running:
1. [QUICKSTART.md](./QUICKSTART.md) - Get the project running locally
2. [DEVELOP_WORKFLOW.md](./DEVELOP_WORKFLOW.md) - Learn the development workflow

### For Daily Development

Use these scripts for daily work:
```bash
# Auto-commit to develop branch
./scripts/auto_commit_develop.sh "Your changes"

# AI-powered development pipeline
./scripts/ai_pipeline.sh

# Check workflow status
./scripts/workflow_status.sh

# Deploy to production
./scripts/deploy_to_production.sh
```

### For Deployment

Set up and manage deployment:
1. [RAILWAY_STEPS.md](./RAILWAY_STEPS.md) - Initial Railway setup
2. [DEPLOY_GUIDE.md](./DEPLOY_GUIDE.md) - Deployment configuration
3. [RAILWAY_STATUS.md](./RAILWAY_STATUS.md) - Current status

## 📖 Documentation by Topic

### Branch Strategy
- **develop** - Safe development branch (no auto-deploy)
- **main** - Production branch (auto-deploys to Railway)

See: [DEVELOP_WORKFLOW.md](./DEVELOP_WORKFLOW.md)

### Automation Scripts

| Script | Purpose | Branch |
|--------|---------|--------|
| `auto_commit_develop.sh` | Quick commit to develop | develop |
| `ai_commit.sh` | AI-powered commit to develop | develop |
| `ai_pipeline.sh` | Full AI development pipeline | develop |
| `deploy_to_production.sh` | Deploy to production | develop → main |
| `workflow_status.sh` | View current workflow status | any |

See: [AI_PIPELINE.md](./AI_PIPELINE.md)

### Environment Variables

Required for production deployment:
- `SECRET_KEY` - Django secret key
- `DEBUG` - Set to False
- `ALLOWED_HOSTS` - Railway domain
- `DATABASE_URL` - PostgreSQL connection

See: [DEPLOY_GUIDE.md](./DEPLOY_GUIDE.md)

### API Endpoints

- `/api/contacts/` - Contact management
- `/api/companies/` - Company management
- `/api/deals/` - Deal management
- `/admin/` - Django admin panel

See: [QUICKSTART.md](./QUICKSTART.md)

## 🆘 Common Tasks

### Start Development
```bash
git checkout develop
git pull origin develop
# Make changes
./scripts/auto_commit_develop.sh "Your changes"
```

### Run Tests
```bash
python manage.py test
```

### Deploy to Production
```bash
./scripts/deploy_to_production.sh
```

### Check Deployment Status
```bash
railway status
railway logs
./scripts/workflow_status.sh
```

### View Railway Dashboard
```bash
railway open
```

## 🔄 Workflow Summary

```
┌─────────────────────────────────────────────────────────┐
│                   DEVELOP BRANCH                        │
│  (Safe development - No auto-deploy)                    │
│                                                          │
│  1. Make changes                                         │
│  2. Run: ./scripts/auto_commit_develop.sh               │
│  3. Repeat steps 1-2 as needed                          │
└─────────────────────┬───────────────────────────────────┘
                      │
                      │ Manual merge when ready
                      │ ./scripts/deploy_to_production.sh
                      ↓
┌─────────────────────────────────────────────────────────┐
│                     MAIN BRANCH                         │
│  (Production - Auto-deploys to Railway)                 │
│                                                          │
│  1. Code merged from develop                            │
│  2. GitHub Actions runs tests                           │
│  3. Railway auto-deploys                                │
│  4. Production updated                                  │
└─────────────────────────────────────────────────────────┘
```

## 💡 Tips

1. **Always work on develop** - Keep main for production only
2. **Commit frequently** - Use auto-commit for quick iterations
3. **Test before deploying** - Run tests locally first
4. **Manual deployment** - You control when code goes to production
5. **Check logs** - Use `railway logs` to monitor production

## 📞 Support

For issues or questions:
1. Check relevant guide in this directory
2. View Railway logs: `railway logs`
3. Check GitHub Actions: `gh run list`
4. View workflow status: `./scripts/workflow_status.sh`

---

**Last Updated:** October 2025  
**Project:** Django CRM API  
**Repository:** github.com/davethedev-nz/django-crm-api
