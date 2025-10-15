#!/bin/bash

# Auto-commit script for develop branch
# This script automatically commits and pushes changes to the develop branch

set -e

# Check if we're on develop branch
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
if [ "$CURRENT_BRANCH" != "develop" ]; then
    echo "⚠️  Warning: You're not on the develop branch (currently on $CURRENT_BRANCH)"
    echo "Switching to develop branch..."
    git checkout develop
fi

# Check if there are any changes
if [ -z "$(git status --porcelain)" ]; then
    echo "✅ No changes to commit"
    exit 0
fi

# Get current timestamp
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Stage all changes
echo "📦 Staging all changes..."
git add -A

# Generate commit message
if [ -n "$1" ]; then
    # Use custom message if provided
    COMMIT_MSG="$1"
else
    # Generate automatic commit message
    CHANGED_FILES=$(git diff --cached --name-only | wc -l)
    COMMIT_MSG="Auto-commit: $CHANGED_FILES file(s) updated at $TIMESTAMP"
fi

# Commit changes
echo "💾 Committing: $COMMIT_MSG"
git commit -m "$COMMIT_MSG"

# Push to develop branch
echo "🚀 Pushing to origin/develop..."
git push origin develop

echo "✅ Successfully pushed to develop branch!"
echo "🚀 Deploying to Railway DEVELOPMENT environment..."
echo ""
echo "📝 Next steps:"
echo "   • View dev logs: railway logs -e development"
echo "   • Open dev site: railway open -e development"
echo "   • Deploy to PRODUCTION: ./scripts/deploy_to_production.sh"
echo ""
echo "   git merge develop"
echo "   git push origin main"
