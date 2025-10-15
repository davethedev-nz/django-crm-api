#!/bin/bash

# Workflow Status Script
# Shows current branch, pending changes, and deployment status

set -e

echo "╔════════════════════════════════════════════════════════════╗"
echo "║           Django CRM API - Workflow Status                ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Current branch
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
echo "📍 Current Branch: $CURRENT_BRANCH"
echo ""

# Check git status
if [ -z "$(git status --porcelain)" ]; then
    echo "✅ Working directory clean - no uncommitted changes"
else
    echo "⚠️  Uncommitted changes detected:"
    echo ""
    git status --short
fi

echo ""
echo "────────────────────────────────────────────────────────────"
echo ""

# Show recent commits on current branch
echo "📝 Recent commits on $CURRENT_BRANCH:"
git log --oneline -5
echo ""

# Show commits ahead/behind
echo "────────────────────────────────────────────────────────────"
echo ""
echo "🔄 Branch Comparison:"
echo ""

# Fetch remote info
git fetch origin --quiet

# Check develop vs main
DEVELOP_AHEAD=$(git rev-list --count origin/main..origin/develop 2>/dev/null || echo "0")
DEVELOP_BEHIND=$(git rev-list --count origin/develop..origin/main 2>/dev/null || echo "0")

echo "develop vs main:"
echo "  • develop is $DEVELOP_AHEAD commit(s) ahead of main"
echo "  • develop is $DEVELOP_BEHIND commit(s) behind main"

if [ "$DEVELOP_AHEAD" -gt 0 ]; then
    echo "  ⚠️  You have $DEVELOP_AHEAD commit(s) on develop not yet deployed"
fi

if [ "$DEVELOP_BEHIND" -gt 0 ]; then
    echo "  ⚠️  main has $DEVELOP_BEHIND commit(s) not merged to develop"
fi

echo ""
echo "────────────────────────────────────────────────────────────"
echo ""

# Show available actions
echo "🚀 Available Actions:"
echo ""

if [ -n "$(git status --porcelain)" ]; then
    echo "  📦 Commit changes to $CURRENT_BRANCH:"
    echo "     ./scripts/auto_commit_develop.sh \"Your message\""
    echo ""
fi

if [ "$CURRENT_BRANCH" == "develop" ] && [ "$DEVELOP_AHEAD" -gt 0 ]; then
    echo "  🚢 Deploy to production (merge develop → main):"
    echo "     ./scripts/deploy_to_production.sh"
    echo ""
fi

if [ "$CURRENT_BRANCH" != "develop" ]; then
    echo "  🔀 Switch to develop branch:"
    echo "     git checkout develop"
    echo ""
fi

echo "  📊 View Railway deployment status:"
echo "     railway status"
echo ""
echo "  📜 View Railway logs:"
echo "     railway logs"
echo ""
echo "  🌐 Open Railway dashboard:"
echo "     railway open"
echo ""

echo "────────────────────────────────────────────────────────────"
echo ""
echo "📚 Documentation:"
echo "  • DEVELOP_WORKFLOW.md - Complete workflow guide"
echo "  • DEPLOY_GUIDE.md     - Deployment details"
echo "  • RAILWAY_STEPS.md    - Railway configuration"
echo ""
